select
    cast(date_format(pickup_datetime, '%Y%m%d') as integer) as date_key,
    coalesce(pickup_location_id, 264) as pickup_location_id,
    coalesce(dropoff_location_id, 264) as dropoff_location_id,
    trim(dispatching_base_num) as dispatching_base_num,
    trim(affiliated_base_number) as affiliated_base_number,
    pickup_datetime,
    dropoff_datetime,
    duration_seconds
from {{ ref('stg_fhv_tripdata') }}