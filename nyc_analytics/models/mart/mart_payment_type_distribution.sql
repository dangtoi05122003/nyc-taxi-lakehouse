SELECT
    payment_type,
    SUM(trips) AS value
FROM (
    SELECT
        'yellow' AS trip_type,
        COALESCE(p.description, 'Missing') AS payment_type,
        COUNT(*) AS trips
    FROM {{ ref('fact_yellow_trip') }} f
    LEFT JOIN hive.gold.dim_payment_type p
        ON f.payment_type = p.payment_type
    GROUP BY 1,2

    UNION ALL

    SELECT
        'green' AS trip_type,
        COALESCE(p.description, 'Missing') AS payment_type,
        COUNT(*) AS trips
    FROM {{ ref('fact_green_trip') }} f
    LEFT JOIN hive.gold.dim_payment_type p
        ON f.payment_type = p.payment_type
    GROUP BY 1,2
) t
GROUP BY payment_type
ORDER BY value DESC;