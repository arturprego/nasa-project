with mapped_distance as (
    select orbiting_body, 
        {{ date_trunc("month", "close_approach_date") }} as close_approach_date,
        case when miss_distance_lunar <  1 then 'Less than moon'
             when miss_distance_lunar >= 1 and miss_distance_lunar < 2 then 'Up to 2 moons'
             when miss_distance_lunar >  2 then 'Over 2 moons'
             else 'unknown' end as miss_distance_moon_ref
    from {{ ref('int_asteroid_approaches') }}
)
select count(1) as num_approaches, 
    orbiting_body, 
    cast(close_approach_date as date) as close_approach_date,
    miss_distance_moon_ref
from mapped_distance
group by orbiting_body, close_approach_date, miss_distance_moon_ref