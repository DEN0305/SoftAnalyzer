import re
import statistics
import functools
import datetime
from collections import Counter


UMBRALES = {'rapido': 0.5, 'normal': 1.0, 'lento': 2.0}

def parsear_log(linea):
    """
    Extrae información de una línea del log.
    Retorna un diccionario con timestamp, endpoint, tiempo_respuesta y código_estado.
    """
    linea = linea.strip()
    if not linea:
        return None
    m = re.match(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\s+(\S+)\s+(\S+)\s+(\d{3})\s+([\d.]+)', linea)
    if not m:
        return None
    ts_str, metodo, endpoint, codigo, tiempo = m.groups()
    timestamp = datetime.datetime.strptime(ts_str, "%Y-%m-%d %H:%M:%S")
    return {
        'timestamp': timestamp,
        'metodo': metodo,
        'endpoint': endpoint,
        'codigo': int(codigo),
        'tiempo': float(tiempo)
    }

def calcular_percentiles(tiempos, percentiles=[50, 90, 95, 99]):
    """
    Calcula los percentiles solicitados (por defecto 50, 90, 95, 99).
    Retorna un diccionario con los valores en milisegundos.
    """
    if not tiempos:
        return {p: None for p in percentiles}
    tiempos_ordenados = sorted(tiempos)
    n = len(tiempos_ordenados)
    resultado = {}
    for p in percentiles:
        k = (p / 100) * (n - 1)
        f = int(k)
        c = min(f + 1, n - 1)
        if f == c:
            val = tiempos_ordenados[int(k)]
        else:
            d0 = tiempos_ordenados[f] * (c - k)
            d1 = tiempos_ordenados[c] * (k - f)
            val = d0 + d1
        resultado[p] = round(val * 1000, 3)
    return resultado

def clasificar_rendimiento(tiempo):
    """
    Clasifica el rendimiento del endpoint según su tiempo de respuesta.
    """
    if tiempo < UMBRALES['rapido']:
        return 'rápida'
    elif tiempo < UMBRALES['normal']:
        return 'normal'
    elif tiempo < UMBRALES['lento']:
        return 'lenta'
    else:
        return 'crítica'

def contador_alertas():
    """
    Closure que mantiene el conteo de alertas cuando el tiempo supera el umbral lento.
    """
    contador = 0
    
    def contar(endpoint, tiempo):
        nonlocal contador
        if tiempo >= UMBRALES['lento']:
            contador += 1
        return contador
    
    return contar

def procesar_logs(ruta_logs):
    """
    Procesa el archivo de logs y retorna las estadísticas requeridas.
    """
    with open(ruta_logs, 'r', encoding='utf-8') as f:
        lineas = [parsear_log(l) for l in f if parsear_log(l)]

    tiempos = [l['tiempo'] for l in lineas]
    total = len(tiempos)
    promedio = round(statistics.mean(tiempos) * 1000, 3)
    maximo = round(max(tiempos) * 1000, 3)
    minimo = round(min(tiempos) * 1000, 3)

    errores = list(filter(lambda x: x['codigo'] >= 400, lineas))
    ordenados = sorted(lineas, key=lambda x: x['tiempo'], reverse=True)
    timestamps = list(map(lambda x: x['timestamp'].isoformat(), lineas))
    endpoints = list(map(lambda x: x['endpoint'], lineas))
    categorias = list(map(lambda x: clasificar_rendimiento(x['tiempo']), lineas))

    percentiles = calcular_percentiles(tiempos)
    distribucion = Counter(map(lambda x: x['codigo'] // 100 * 100, lineas))

    contar = contador_alertas()
    for l in lineas:
        contar(l['endpoint'], l['tiempo'])

    resultados = {
        'total': total,
        'promedio': promedio,
        'max': maximo,
        'min': minimo,
        'percentiles': percentiles,
        'distribucion': distribucion,
        'alertas': contar('', 0),
        'errores': len(errores),
        'ordenados': ordenados,
        'timestamps': timestamps,
        'endpoints': endpoints,
        'categorias': categorias
    }
    return resultados

def generar_reporte(resultados, plantilla, salida):
    """
    Genera el archivo reporte_rendimiento.md usando la plantilla.
    """
    with open(plantilla, 'r', encoding='utf-8') as f:
        contenido = f.read()
    
    tiempos = [l['tiempo'] for l in resultados['ordenados']]
    desviacion = round(statistics.stdev(tiempos) * 1000, 3) if len(tiempos) > 1 else 0
    tasa_error = round((resultados['errores'] / resultados['total']) * 100, 2) if resultados['total'] > 0 else 0
    
    timestamps = [l['timestamp'] for l in resultados['ordenados']]
    fecha_inicio = min(timestamps).strftime("%Y-%m-%d %H:%M:%S")
    fecha_fin = max(timestamps).strftime("%Y-%m-%d %H:%M:%S")
    fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    codigos_estado = {}
    for linea in resultados['ordenados']:
        codigo = linea['codigo']
        if codigo not in codigos_estado:
            codigos_estado[codigo] = {'cantidad': 0, 'tiempos': []}
        codigos_estado[codigo]['cantidad'] += 1
        codigos_estado[codigo]['tiempos'].append(linea['tiempo'])
    
    tabla_codigos = ""
    for codigo in sorted(codigos_estado.keys()):
        datos = codigos_estado[codigo]
        cantidad = datos['cantidad']
        porcentaje = round((cantidad / resultados['total']) * 100, 1)
        tiempo_promedio = round(statistics.mean(datos['tiempos']) * 1000, 3)
        tabla_codigos += f"| {codigo}    | {cantidad}      | {porcentaje}%        | {tiempo_promedio} ms       |\n"
    
    endpoint_stats = {}
    for linea in resultados['ordenados']:
        endpoint = linea['endpoint']
        if endpoint not in endpoint_stats:
            endpoint_stats[endpoint] = {'cantidad': 0, 'tiempos': []}
        endpoint_stats[endpoint]['cantidad'] += 1
        endpoint_stats[endpoint]['tiempos'].append(linea['tiempo'])
    
    endpoint_promedios = {}
    for endpoint, datos in endpoint_stats.items():
        tiempos_endpoint = datos['tiempos']
        promedio = round(statistics.mean(tiempos_endpoint) * 1000, 3)
        maximo = round(max(tiempos_endpoint) * 1000, 3)
        minimo = round(min(tiempos_endpoint) * 1000, 3)
        endpoint_promedios[endpoint] = {
            'cantidad': datos['cantidad'],
            'promedio': promedio,
            'maximo': maximo,
            'minimo': minimo
        }
    
    top_3_endpoints = sorted(endpoint_promedios.items(), key=lambda x: x[1]['promedio'], reverse=True)[:3]
    
    errores_por_endpoint = {}
    for linea in resultados['ordenados']:
        if linea['codigo'] >= 400:
            endpoint = linea['endpoint']
            if endpoint not in errores_por_endpoint:
                errores_por_endpoint[endpoint] = 0
            errores_por_endpoint[endpoint] += 1
    
    endpoint_mas_errores = max(errores_por_endpoint.items(), key=lambda x: x[1]) if errores_por_endpoint else ("N/A", 0)
    
    errores_por_codigo = {}
    for linea in resultados['ordenados']:
        if linea['codigo'] >= 400:
            codigo = linea['codigo']
            errores_por_codigo[codigo] = errores_por_codigo.get(codigo, 0) + 1
    
    error_mas_comun = max(errores_por_codigo.items(), key=lambda x: x[1]) if errores_por_codigo else (0, 0)
    
    reemplazos = {
        '[FECHA]': fecha_actual,
        '[TOTAL_LINEAS]': str(resultados['total']),
        '[INICIO]': fecha_inicio,
        '[FIN]': fecha_fin,
        '[TOTAL]': str(resultados['total']),
        '[PROMEDIO]': str(resultados['promedio']),
        '[MAX]': str(resultados['max']),
        '[MIN]': str(resultados['min']),
        '[DESVIACION]': str(desviacion),
        '[TOTAL_ERRORES]': str(resultados['errores']),
        '[PORCENTAJE]': str(tasa_error),
        '[ENDPOINT]': endpoint_mas_errores[0],
        '[CODIGO]': str(error_mas_comun[0]),
        '[CANTIDAD]': str(error_mas_comun[1])
    }
    
    contenido = contenido.replace('| 200    | [N]      | [%]        | [TIME] ms       |\n| 201    | [N]      | [%]        | [TIME] ms       |\n| 404    | [N]      | [%]        | [TIME] ms       |\n| 500    | [N]      | [%]        | [TIME] ms       |\n| Otros  | [N]      | [%]        | [TIME] ms       |', tabla_codigos.rstrip())
    
    tabla_endpoints = ""
    for endpoint, stats in sorted(endpoint_promedios.items()):
        tabla_endpoints += f"| {endpoint} | {stats['cantidad']} | {stats['promedio']} ms | {stats['maximo']} ms | {stats['minimo']} ms |\n"
    
    contenido = contenido.replace('| /api/users | [N] | [AVG] ms | [MAX] ms | [MIN] ms |\n| /api/products | [N] | [AVG] ms | [MAX] ms | [MIN] ms |\n| /api/login | [N] | [AVG] ms | [MAX] ms | [MIN] ms |\n| [OTROS ENDPOINTS] | ... | ... | ... | ... |', tabla_endpoints.rstrip())
    
    for i, (endpoint, stats) in enumerate(top_3_endpoints, 1):
        contenido = contenido.replace(f'[ENDPOINT_{i}]', endpoint)
        contenido = contenido.replace(f'[TIME]', str(stats['promedio']))
        contenido = contenido.replace(f'[N]', str(stats['cantidad']))
        contenido = contenido.replace(f'[MAX]', str(stats['maximo']))
    
    for placeholder, valor in reemplazos.items():
        contenido = contenido.replace(placeholder, valor)
    
    recomendaciones = []
    if resultados['alertas'] > 0:
        recomendaciones.append("Optimizar endpoints con tiempo de respuesta > 2 segundos")
    if tasa_error > 5:
        recomendaciones.append("Revisar y corregir errores 4xx/5xx frecuentes")
    if resultados['promedio'] > 200:
        recomendaciones.append("Implementar caching para reducir tiempos de respuesta")
    if resultados['max'] > 1000:
        recomendaciones.append("Investigar picos de latencia en endpoints críticos")
    if len(recomendaciones) < 3:
        recomendaciones.append("Monitorear continuamente el rendimiento de la API")
    
    for i, rec in enumerate(recomendaciones[:3], 1):
        contenido = contenido.replace(f'[RECOMENDACION_{i}]', rec)
    
    contenido = contenido.replace('[DESCRIPCION]', 'Mejora significativa en rendimiento')
    contenido = contenido.replace('[Alta/Media/Baja]', 'Alta')
    
    conclusiones = f"""El análisis de {resultados['total']} requests muestra un rendimiento promedio de {resultados['promedio']} ms con una tasa de error del {tasa_error}%. 
    Se identificaron {resultados['alertas']} alertas por tiempo de respuesta excesivo y {resultados['errores']} errores HTTP. 
    Los endpoints más críticos requieren optimización inmediata."""
    
    contenido = contenido.replace('[TUS CONCLUSIONES SOBRE EL ANÁLISIS]', conclusiones)
    
    with open(salida, 'w', encoding='utf-8') as f:
        f.write(contenido)

def main():
    """
    Función principal: procesa el log y genera el reporte.
    """
    resultados = procesar_logs('Logs_ejemplo.txt')
    generar_reporte(resultados, 'plantilla_reporte.md', 'reporte_rendimiento.md')
    print("Reporte generado correctamente: reporte_rendimiento.md")

if __name__ == '__main__':
    main()
