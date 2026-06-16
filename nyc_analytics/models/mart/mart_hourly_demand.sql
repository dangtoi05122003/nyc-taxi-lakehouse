select
    extract(hour from tpep_pickup_datetime) as hour,
    count(*) as trip_count
from {{ ref('fact_yellow_trip') }}
group by 1