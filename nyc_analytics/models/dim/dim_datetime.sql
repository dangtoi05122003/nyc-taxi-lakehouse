with base as (
    select cast(d as date) as date_day
    from unnest(sequence(date '2022-01-01', date '2026-12-31', interval '1' day)) as t(d)
)
select
    cast(date_format(date_day, '%Y%m%d') as integer) as date_id,
    date_day as date,
    year(date_day) as year,
    month(date_day) as month,
    date_format(date_day, '%Y-%m') as year_month
from base