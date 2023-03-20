select t.id, 
    cast(unnested.close_approach_date as date) as close_approach_date,
    unnested.epoch_date_close_approach,
    cast(unnested.miss_distance.kilometers as numeric) as miss_distance_km,
    cast(unnested.miss_distance.lunar as numeric) as miss_distance_lunar,
    unnested.orbiting_body,
    cast(unnested.relative_velocity.kilometers_per_hour as numeric) as relative_velocity_km_per_hour
from {{ ref('stg_nasa__asteroids_raw') }} t
join unnest(t.close_approach_data) as unnested