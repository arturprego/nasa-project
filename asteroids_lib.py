#Process all asteroids in json file
import json
import pandas as pd

def process_asteroids_deprecated(asteroids):
    df = pd.DataFrame()
    df_new = pd.DataFrame()
    for asteroid in asteroids["near_earth_objects"]:
        print(asteroid["links"])
        df = pd.DataFrame.from_dict(pd.json_normalize(asteroid), orient='columns')
        df_new = pd.concat([df,df_new])
        #asteroid_array = json.dumps(asteroid)
    print("******** page number = " + str(asteroids["page"]["number"]) + "**********")
    print(df)
    df2 = pd.DataFrame.from_dict(pd.json_normalize(asteroids["near_earth_objects"]), orient='columns')
    print(df2)
    print(df2.loc[3])
    print(df2.loc[3,"id"])
    print(df_new)

    return df2


def process_asteroids(asteroids):
    return pd.DataFrame.from_dict(pd.json_normalize(asteroids["near_earth_objects"]), orient='columns')



def column_definition():
    return [
      'id'
    , 'neo_reference_id'
    , 'name'
    , 'name_limited'
    , 'designation'
    , 'nasa_jpl_url'
    , 'absolute_magnitude_h'
    , 'is_potentially_hazardous'
    , 'close_approach_data'
    , 'is_sentry_object'
    , 'url'
    , 'est_dim_min_km'
    , 'est_dim_max_km'
    , 'est_dim_min_m'
    , 'est_dim_max_m'
    , 'est_dim_min_ml'
    , 'est_dim_max_ml'
    , 'est_dim_min_ft'
    , 'est_dim_max_ft'
    , 'orbit_id'
    , 'orbit_determination_date'
    , 'first_observation_date'
    , 'last_observation_date'
    , 'data_arc_in_days'
    , 'observations_used'
    , 'orbit_uncertainty'
    , 'minimum_orbit_intersection'
    , 'jupiter_tisserand_invariant'
    , 'epoch_osculation'
    , 'eccentricity'
    , 'semi_major_axis'
    , 'inclination'
    , 'ascending_node_longitude'
    , 'orbital_period'
    , 'perihelion_distance'
    , 'perihelion_argument'
    , 'aphelion_distance'
    , 'perihelion_time'
    , 'mean_anomaly'
    , 'mean_motion'
    , 'equinox'
    , 'orbit_class_type'
    , 'orbit_class_description'
    , 'orbit_class_range'
]
