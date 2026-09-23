with base as (
    SELECT 1 AS vendor_id, 'Creative Mobile Technologies, LLC' AS vendor_name UNION ALL
    SELECT 2 as vendor_id, 'Curb Mobility, LLC' as vendor_name UNION ALL
    SELECT 6 as vendor_id, 'Myle Technologies Inc' as vendor_name
)
select
    vendor_id,
    vendor_name
from base