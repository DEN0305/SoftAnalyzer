# Reporte de Análisis de Rendimiento

## Información General
- **Fecha de Análisis:** 2025-10-17 22:09:39
- **Archivo Analizado:** logs_ejemplo.txt
- **Total de Líneas Procesadas:** 50
- **Período de Tiempo:** 2024-10-17 10:23:45 - 2024-10-17 10:24:34

## Estadísticas Generales
- **Total de solicitudes procesadas:** 50
- **Tiempo promedio de respuesta:** 254.56 ms
- **Tiempo máximo:** 1234.0 ms
- **Tiempo mínimo:** 11.0 ms
- **Desviación estándar:** 307.685 ms

## Análisis por Código de Estado
| Código | Cantidad | Porcentaje | Tiempo Promedio |
|--------|----------|------------|-----------------|
| 200    | 44      | 88.0%        | 228.773 ms       |
| 201    | 3      | 6.0%        | 171.0 ms       |
| 404    | 1      | 2.0%        | 23.0 ms       |
| 413    | 1      | 2.0%        | 1234.0 ms       |
| 500    | 1      | 2.0%        | 892.0 ms       |

## Análisis por Endpoint
| Endpoint | Solicitudes | Tiempo Promedio | Tiempo Max | Tiempo Min |
|----------|-------------|-----------------|------------|------------|
| /api/backup | 1 | 1234.0 ms | 1234.0 ms | 1234.0 ms |
| /api/cache | 1 | 12.0 ms | 12.0 ms | 12.0 ms |
| /api/cart | 1 | 345.0 ms | 345.0 ms | 345.0 ms |
| /api/categories | 1 | 89.0 ms | 89.0 ms | 89.0 ms |
| /api/comments | 1 | 123.0 ms | 123.0 ms | 123.0 ms |
| /api/config | 1 | 67.0 ms | 67.0 ms | 67.0 ms |
| /api/dashboard | 1 | 456.0 ms | 456.0 ms | 456.0 ms |
| /api/drafts | 1 | 23.0 ms | 23.0 ms | 23.0 ms |
| /api/expired | 1 | 67.0 ms | 67.0 ms | 67.0 ms |
| /api/export | 1 | 890.0 ms | 890.0 ms | 890.0 ms |
| /api/feedback | 1 | 156.0 ms | 156.0 ms | 156.0 ms |
| /api/health | 1 | 12.0 ms | 12.0 ms | 12.0 ms |
| /api/history | 1 | 234.0 ms | 234.0 ms | 234.0 ms |
| /api/import | 1 | 456.0 ms | 456.0 ms | 456.0 ms |
| /api/inventory | 1 | 123.0 ms | 123.0 ms | 123.0 ms |
| /api/login | 1 | 123.0 ms | 123.0 ms | 123.0 ms |
| /api/logout | 1 | 12.0 ms | 12.0 ms | 12.0 ms |
| /api/logs | 1 | 34.0 ms | 34.0 ms | 34.0 ms |
| /api/metrics | 1 | 234.0 ms | 234.0 ms | 234.0 ms |
| /api/notifications | 1 | 56.0 ms | 56.0 ms | 56.0 ms |
| /api/orders | 1 | 892.0 ms | 892.0 ms | 892.0 ms |
| /api/payment | 1 | 567.0 ms | 567.0 ms | 567.0 ms |
| /api/preferences | 1 | 178.0 ms | 178.0 ms | 178.0 ms |
| /api/process | 1 | 567.0 ms | 567.0 ms | 567.0 ms |
| /api/products | 2 | 150.5 ms | 234.0 ms | 67.0 ms |
| /api/profile | 1 | 234.0 ms | 234.0 ms | 234.0 ms |
| /api/queue | 1 | 234.0 ms | 234.0 ms | 234.0 ms |
| /api/refresh | 1 | 123.0 ms | 123.0 ms | 123.0 ms |
| /api/reports | 1 | 789.0 ms | 789.0 ms | 789.0 ms |
| /api/results | 1 | 345.0 ms | 345.0 ms | 345.0 ms |
| /api/search | 1 | 456.0 ms | 456.0 ms | 456.0 ms |
| /api/sessions | 1 | 34.0 ms | 34.0 ms | 34.0 ms |
| /api/settings | 1 | 167.0 ms | 167.0 ms | 167.0 ms |
| /api/shipping | 1 | 89.0 ms | 89.0 ms | 89.0 ms |
| /api/stats | 1 | 678.0 ms | 678.0 ms | 678.0 ms |
| /api/status | 1 | 89.0 ms | 89.0 ms | 89.0 ms |
| /api/sync | 1 | 345.0 ms | 345.0 ms | 345.0 ms |
| /api/temp | 1 | 11.0 ms | 11.0 ms | 11.0 ms |
| /api/upload | 1 | 1234.0 ms | 1234.0 ms | 1234.0 ms |
| /api/users | 6 | 48.667 ms | 52.0 ms | 45.0 ms |
| /api/users/123 | 1 | 234.0 ms | 234.0 ms | 234.0 ms |
| /api/users/456 | 1 | 23.0 ms | 23.0 ms | 23.0 ms |
| /api/validate | 1 | 89.0 ms | 89.0 ms | 89.0 ms |
| /api/version | 1 | 11.0 ms | 11.0 ms | 11.0 ms |

## Endpoints Más Lentos
1. **/api/upload** - Promedio: 1234.0 ms
   - Solicitudes: 1
   - Tiempo máximo: 1234.0 ms

2. **/api/backup** - Promedio: 1234.0 ms
   - Solicitudes: 1
   - Tiempo máximo: 1234.0 ms

3. **/api/orders** - Promedio: 1234.0 ms
   - Solicitudes: 1
   - Tiempo máximo: 1234.0 ms

## Análisis de Errores
- **Total de errores (4xx, 5xx):** 3
- **Tasa de error:** 6.0%
- **Endpoint con más errores:** /api/upload
- **Tipo de error más común:** 413 - 1 ocurrencias

## Patrones Identificados
[DESCRIBIR PATRONES OBSERVADOS]
- Ejemplo: Se observa un incremento en los tiempos de respuesta para el endpoint /api/reports
- Ejemplo: Los errores 500 están concentrados en el endpoint /api/orders

## Recomendaciones de Optimización
1. **Revisar y corregir errores 4xx/5xx frecuentes**
   - Impacto esperado: Mejora significativa en rendimiento
   - Prioridad: Alta

2. **Implementar caching para reducir tiempos de respuesta**
   - Impacto esperado: Mejora significativa en rendimiento
   - Prioridad: Alta

3. **Investigar picos de latencia en endpoints críticos**
   - Impacto esperado: Mejora significativa en rendimiento
   - Prioridad: Alta

## Conclusiones
El análisis de 50 requests muestra un rendimiento promedio de 254.56 ms con una tasa de error del 6.0%. 
    Se identificaron 0 alertas por tiempo de respuesta excesivo y 3 errores HTTP. 
    Los endpoints más críticos requieren optimización inmediata.

---
*Reporte generado usando Python - Análisis de Logs de Rendimiento*
*Asignatura: Diseño Funcional - FESC*
*Tema: Subalgoritmos, Funciones y Procedimientos*