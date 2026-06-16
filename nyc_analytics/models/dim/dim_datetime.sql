select distinct
    tpep_pickup_datetime
from {{ ref('stg_yellow_tripdata') }}

union

select distinct
    lpep_pickup_datetime
from {{ ref('stg_green_tripdata') }}