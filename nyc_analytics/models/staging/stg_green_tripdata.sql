select
    *,
    vendorid as vendor_id,
    pulocationid as pickup_location_id,
    dolocationid as dropoff_location_id
from {{ source('nyc_taxi', 'green_tripdata') }}