# first-repo
# reference documentation:
# https://nasapy.readthedocs.io/en/latest/api.html?highlight=get_asteroids#near-earth-objects
# https://www.educative.io/blog/how-to-use-api-nasa-daily-image
# https://medium.com/daily-python/consuming-nasa-api-using-python-part-1-daily-python-17-4ce104fa47ab
# https://codelabs.developers.google.com/codelabs/cloud-bigquery-python#6
# https://ssd-api.jpl.nasa.gov/doc/cad.html

#json sample of asteroid

{'links': 
	{'self': 'http://api.nasa.gov/neo/rest/v1/neo/3542519?api_key=xxxxxxxxxxxxxxx'},
	'id': '3542519',
	'neo_reference_id': '3542519',
	'name': '(2010 PK9)',
	 'designation': '2010 PK9',
	 'nasa_jpl_url': 'http://ssd.jpl.nasa.gov/sbdb.cgi?sstr=3542519',
	 'absolute_magnitude_h': 21.8,
	 'estimated_diameter': {
		'kilometers': {
			'estimated_diameter_min': 0.1160259082,
			'estimated_diameter_max': 0.2594418179},
		'meters': {
			'estimated_diameter_min': 116.0259082094,
			'estimated_diameter_max': 259.4418179074},
		'miles': {
			'estimated_diameter_min': 0.0720951346,
			'estimated_diameter_max': 0.1612096218},
		'feet': {
		'estimated_diameter_min': 380.6624406898,
		'estimated_diameter_max': 851.1870938635}
		},
	 'is_potentially_hazardous_asteroid': True,
	 'close_approach_data': [],
	 'orbital_data': {
		'orbit_id': '26',
		'orbit_determination_date': '2023-03-01 06:01:11',
		'first_observation_date': '2010-07-18',
		'last_observation_date': '2019-08-04',
		'data_arc_in_days': 3304,
		'observations_used': 106,
		'orbit_uncertainty': '0',
		'minimum_orbit_intersection': '.0156523',
		'jupiter_tisserand_invariant': '8.150',
		'epoch_osculation': '2460000.5',
		'eccentricity': '.6758397835550958',
		'semi_major_axis': '.6820488566033581',
		'inclination': '12.59219906149941',
		'ascending_node_longitude': '306.5280898357266',
		'orbital_period': '205.7413829181466',
		'perihelion_distance': '.221093104982544',
		'perihelion_argument': '195.6367907331395',
		'aphelion_distance': '1.143004608224172',
		'perihelion_time': '2460066.437374223272',
		'mean_anomaly': '244.6247926221936',
		'mean_motion': '1.749769515952095',
		'equinox': 'J2000',
		'orbit_class': {
			'orbit_class_type': 'ATE',
			'orbit_class_description': 'Near-Earth asteroid orbits similar to that of 2062 Aten',
			'orbit_class_range': 'a (semi-major axis) < 1.0 AU; q (perihelion) > 0.983 AU'}
	 },
	 'is_sentry_object': False}
