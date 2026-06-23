WITH trips as (
    select
        tpep_pickup_datetime as pickup_datetime,
        'yellow' as trip_type,
        total_amount,
        tip_amount
    from {{ ref('fact_yellow_trip') }}

    union all

    select
        lpep_pickup_datetime as pickup_datetime,
        'green' as trip_type,
        total_amount,
        tip_amount
    from {{ ref('fact_green_trip') }}
)

select
    date(pickup_datetime) as trip_date,
    trip_type,
    count(*) as total_trips,
    sum(coalesce(total_amount, 0)) as total_revenue,
    sum(coalesce(tip_amount, 0)) as total_tips
from trips
group by 1, 2
order by 1, 2;