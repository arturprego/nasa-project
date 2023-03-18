{{
  config(
    materialized='table'
  )
}}

select t.id, unnested.*
from {{ ref('stg_asteroids_raw') }} t
join unnest(t.close_approach_data) as unnested
