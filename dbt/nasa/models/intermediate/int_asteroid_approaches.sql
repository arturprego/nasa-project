select *
from {{ ref('stg_nasa__close_approaches') }} t
