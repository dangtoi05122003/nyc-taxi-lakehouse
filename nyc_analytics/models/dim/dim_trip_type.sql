with base as (
    select 1 as trip_id, 'Street-hall' as trip_name union all
    select 2 as trip_id, 'Dispatch' as trip_name
)
select
    trip_id,
    trip_name
from base