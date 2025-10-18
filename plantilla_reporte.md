# Reporte de Análisis de Rendimiento

## Información General
- **Fecha de Análisis:** [FECHA]
- **Archivo Analizado:** logs_ejemplo.txt
- **Total de Líneas Procesadas:** [TOTAL_LINEAS]
- **Período de Tiempo:** [INICIO] - [FIN]

## Estadísticas Generales
- **Total de solicitudes procesadas:** [TOTAL]
- **Tiempo promedio de respuesta:** [PROMEDIO] ms
- **Tiempo máximo:** [MAX] ms
- **Tiempo mínimo:** [MIN] ms
- **Desviación estándar:** [DESVIACION] ms

## Análisis por Código de Estado
| Código | Cantidad | Porcentaje | Tiempo Promedio |
|--------|----------|------------|-----------------|
| 200    | [N]      | [%]        | [TIME] ms       |
| 201    | [N]      | [%]        | [TIME] ms       |
| 404    | [N]      | [%]        | [TIME] ms       |
| 500    | [N]      | [%]        | [TIME] ms       |
| Otros  | [N]      | [%]        | [TIME] ms       |

## Análisis por Endpoint
| Endpoint | Solicitudes | Tiempo Promedio | Tiempo Max | Tiempo Min |
|----------|-------------|-----------------|------------|------------|
| /api/users | [N] | [AVG] ms | [MAX] ms | [MIN] ms |
| /api/products | [N] | [AVG] ms | [MAX] ms | [MIN] ms |
| /api/login | [N] | [AVG] ms | [MAX] ms | [MIN] ms |
| [OTROS ENDPOINTS] | ... | ... | ... | ... |

## Endpoints Más Lentos
1. **[ENDPOINT_1]** - Promedio: [TIME] ms
   - Solicitudes: [N]
   - Tiempo máximo: [MAX] ms

2. **[ENDPOINT_2]** - Promedio: [TIME] ms
   - Solicitudes: [N]
   - Tiempo máximo: [MAX] ms

3. **[ENDPOINT_3]** - Promedio: [TIME] ms
   - Solicitudes: [N]
   - Tiempo máximo: [MAX] ms

## Análisis de Errores
- **Total de errores (4xx, 5xx):** [TOTAL_ERRORES]
- **Tasa de error:** [PORCENTAJE]%
- **Endpoint con más errores:** [ENDPOINT]
- **Tipo de error más común:** [CODIGO] - [CANTIDAD] ocurrencias

## Patrones Identificados
[DESCRIBIR PATRONES OBSERVADOS]
- Ejemplo: Se observa un incremento en los tiempos de respuesta para el endpoint /api/reports
- Ejemplo: Los errores 500 están concentrados en el endpoint /api/orders

## Recomendaciones de Optimización
1. **[RECOMENDACION_1]**
   - Impacto esperado: [DESCRIPCION]
   - Prioridad: [Alta/Media/Baja]

2. **[RECOMENDACION_2]**
   - Impacto esperado: [DESCRIPCION]
   - Prioridad: [Alta/Media/Baja]

3. **[RECOMENDACION_3]**
   - Impacto esperado: [DESCRIPCION]
   - Prioridad: [Alta/Media/Baja]

## Conclusiones
[TUS CONCLUSIONES SOBRE EL ANÁLISIS]

---
*Reporte generado usando Python - Análisis de Logs de Rendimiento*
*Asignatura: Diseño Funcional - FESC*
*Tema: Subalgoritmos, Funciones y Procedimientos*