{{
  config(
    materialized='view'
  )
}}

select *
from nasa_asteroids.asteroids_raw
