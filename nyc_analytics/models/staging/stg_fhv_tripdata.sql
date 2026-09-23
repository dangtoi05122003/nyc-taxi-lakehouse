select
    dispatching_base_num,
    pickup_datetime,
    dropOff_datetime as dropoff_datetime,
    PUlocationID as pickup_location_id,
    DOlocationID as dropoff_location_id,
    Affiliated_base_number,
    duration_seconds
from {{ source('nyc_taxi', 'fhv_tripdata') }}