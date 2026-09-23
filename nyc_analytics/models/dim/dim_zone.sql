select
    location_id,
    Borough,
    Zone,
    service_zone
from {{ ref('stg_zones') }}