select
    dispatching_base_num,
    count(*) as total_trips
from {{ ref('fact_fhv_trip') }}
group by 1