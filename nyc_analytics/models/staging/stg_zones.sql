select *
from {{ source('nyc_taxi', 'zones') }}