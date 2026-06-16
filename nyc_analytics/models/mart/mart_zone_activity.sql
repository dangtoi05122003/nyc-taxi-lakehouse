select
    pickup_location_id,
    count(*) as pickup_trips
from {{ ref('fact_yellow_trip') }}
group by 1