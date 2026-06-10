CREATE OR REPLACE VIEW smart_support.priority_tickets AS
SELECT
date AS fecha_origen,
content AS contenido,
user_email AS email,
phone AS telefono,
area,
sentiment AS sentimiento,
sentiment_score AS sentimiento_sc,
processed_date AS fecha_analisis,
CASE
    WHEN sentiment = 'negativo' THEN 1
    WHEN sentiment = 'neutral' THEN 2
    WHEN sentiment = 'positivo' THEN 3
END AS prioridad_sentimiento,
CASE
    WHEN area LIKE 'T%cnico' THEN 1
    WHEN area LIKE 'Ventas' THEN 2
    WHEN area LIKE 'Facturaci%n' THEN 3
END AS prioridad_area
FROM smart_support.processed_tickets
ORDER BY 
prioridad_sentimiento ASC,
prioridad_area ASC,
date