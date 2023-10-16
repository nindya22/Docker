import requests
import pandas as pd

url = 'https://api.opencagedata.com/geocode/v1/json'
api_key = 'a34768ccd55d49cfa29fb5753e2d1486'

countries = population_df['country'].to_list()

countries_list = []
for country in countries:
    params = {'q': country, 'key': api_key} 
    response = requests.get(url,params=params)
    
    json_data = response.json()
    
    components = json_data['results'][0]['components']
    geometry = json_data['results'][0]['geometry']
    
    country_components = {
        'country': country,
        'country_code': components.get('country_code',''),
        'latitude': geometry.get('lat'),
        'longitude': geometry.get('Ing')
    }
    
    countries_list.append(country components)

    component_df = pd.DataFrame(countries_list)



