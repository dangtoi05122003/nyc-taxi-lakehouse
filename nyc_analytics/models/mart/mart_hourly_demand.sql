with trips AS (
    select
        tpep_pickup_datetime as pickup_datetime,
        'yellow' as trip_type
    from {{ ref('fact_yellow_trip') }}
    
    union all
    
    select
        lpep_pickup_datetime as pickup_datetime,
        'green' as trip_type
    from {{ref('fact_green_trip')}}

    union all

    select
        pickup_datetime,
        'fhvhv' as trip_type
    from {{ref('fact_fhvhv_trip')}}

    union all

    select
        pickup_datetime,
        'fhv' as trip_type
    from {{ref('fact_fhv_trip')}}
)
select
    extract(hour from pickup_datetime) as hour,
    trip_type,
    count(*) as trip_count
from trips
group by 1, 2