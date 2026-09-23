with base as (
    select 'HV0003' as hvfhs_license_num, 'Uber' as company_name union all
    select 'HV0005' as hvfhs_license_num, 'Lyft' as company_name
)
select
    hvfhs_license_num,
    company_name
from base