select id,
    name,
    absolute_magnitude_h,
    est_dim_min_km,
    est_dim_max_km,
    is_potentially_hazardous_asteroid,
    orbital_period,
    perihelion_distance,
    aphelion_distance,
    orbit_class_type,
    is_sentry_object
from {{ ref('stg_nasa__asteroids') }}
