with base as (
    select 1 as RatecodeID, 'Standard rate' as rate_code_name union all
    select 2 as RatecodeID, 'JFK' as rate_code_name union all
    select 3 as RatecodeID, 'Neward' as rate_code_name union all
    select 4 as RatecodeID, 'Nassau or Westchester' as rate_code_name union all
    select 5 as RatecodeID, 'Negotiated fare' as rate_code_name union all
    select 6 as RatecodeID, 'Group ride' as rate_code_name union all
    select 99 as RatecodeID, 'Unknown' as  rate_code_name
)
select
    RatecodeID as rate_code_id,
    rate_code_name
from base