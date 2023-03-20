select id,
    name,
    cast(absolute_magnitude_h as numeric) as absolute_magnitude_h,
    cast(est_dim_min_km as numeric) as est_dim_min_km,
    cast(est_dim_max_km as numeric) as est_dim_max_km,
    is_potentially_hazardous_asteroid,
    cast(orbital_period as numeric) as orbital_period,
    cast(perihelion_distance as numeric) as perihelion_distance,
    cast(aphelion_distance as numeric) as aphelion_distance,
    orbit_class_type,
    is_sentry_object
from {{ ref('stg_nasa__asteroids_raw') }}
