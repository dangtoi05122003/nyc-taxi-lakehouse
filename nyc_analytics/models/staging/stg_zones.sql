select 
    LocationID as location_id,
    Borough,
    Zone,
    service_zone
from {{ source('nyc_taxi', 'zones') }}