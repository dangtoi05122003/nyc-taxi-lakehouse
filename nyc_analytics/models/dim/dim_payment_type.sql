with base as (
    SELECT 0 AS payment_type, 'Flex Fare trip' as payment_type_name UNION ALL
    SELECT 1 AS payment_type, 'Credit Card' AS payment_type_name UNION ALL
    SELECT 2 AS payment_type, 'Cash' AS payment_type_name UNION ALL
    SELECT 3 AS payment_type, 'No Charge' AS payment_type_name UNION ALL
    SELECT 4 AS payment_type, 'Dispute' AS payment_type_name UNION ALL
    SELECT 5 AS payment_type, 'Unknown' AS payment_type_name
)
select
    payment_type as payment_type_id,
    payment_type_name
from base