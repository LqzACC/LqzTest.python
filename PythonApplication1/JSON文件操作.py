import json
from pygal_maps_world.i18n import COUNTRIES

def get_country_code(country_name):
    for code,name in COUNTRIES.items():
        if country_name in name:
            return code


filepath='D:\\代码\\python块包\\pcc-master\\chapter_16\\population_data.json'
file=open(filepath)
json_data=json.load(file)
#print(json_data)

world_population,w_p1,w_p2,w_p3={},{},{},{}
for Json_data in json_data:
    if Json_data['Year']=='2010':
        country_name=Json_data['Country Name']
        country_code=get_country_code(country_name)
        country_population=int(float(Json_data['Value']))
        print('The country code is: '+str(country_code)+
              '\nThe country name is: '+country_name+
              '\nThe country population is: '+str(country_population)+
              '\n')
        if country_code:
            world_population[country_code]=country_population
        if country_population<10000000:
            w_p1[country_code]=country_population
        elif country_population>10000000 and country_population<1000000000:
            w_p2[country_code]=country_population
        else:
            w_p3[country_code]=country_population
    