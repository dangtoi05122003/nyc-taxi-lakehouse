with trips as (
    select
        PULocationID as pickup_location_id, 
        'yellow' as trip_type
    from {{ ref('fact_yellow_trip') }}

    union all

    select 
        PULocationID as pickup_location_id,
        'green' as trip_type
    from {{ ref('fact_green_trip') }}

)
select
    z.Zone as pickup_zone,
    t.trip_type,
    count(*) as pickup_trips
from trips t
left join {{ref('dim_zone')}} z
    on t.pickup_location_id = cast(z.LocationID as integer)
group by 1, 2