from flask import Flask
from flask_restful import Resource, Api
import re

app = Flask(__name__)
app.config['RESTFUL_JSON'] = {'ensure_ascii': False}
api = Api(app)


def get_info(file_name):
    info = dict()
    keys = ['geonameid', 'name', 'asciiname', 'alternatenames',
            'latitude', 'longitude', 'feature class', 'feature code',
            'country code', 'cc2', 'admin1 code', 'admin2 code',
            'admin3 code', 'admin4 code', 'population', 'elevation',
            'dem', 'timezone', 'modification date']
    with open(file_name, 'r') as file:
        text = file.readlines()
        for line in text:
            if '\tP' in line:
                city_info = line.replace('\n', '').split('\t')
                info[city_info[0]] = dict(list(zip(keys[1:], city_info[1:])))
    return info


def find_city(city_name: str):
    city_info = []
    population = 0
    for id, info in data.items():
        if city_name in info['alternatenames']:
            if not city_info:
                city_info.append({id: info})
                population = info['population']
            if int(info['population']) > int(population):
                city_info.insert(0, {id: info})
    if not city_info:
        return city_name, 'Not found'
    else:
        return city_info[0]


class GeoNameId(Resource):
    def get(self, geonameid: str):
        return {geonameid: data[geonameid]}


class Pages(Resource):
    def get(self, page: int, count: int):
        return dict(list(data.items())[count*(page-1):count*page])


class City(Resource):
    def get(self, city1_name: str, city2_name: str):
        city1 = find_city(city1_name)
        city2 = find_city(city2_name)
        city1_id = list(city1.keys())[0]
        city2_id = list(city2.keys())[0]
        if city1[city1_id] == 'Not found' or city2[city2_id] == 'Not found':
            return city1, city2
        if float(city1[city1_id]['latitude']) > float(city2[city2_id]['latitude']):
            return {city1_id: city1[city1_id], city2_id: city2[city2_id]}
        else:
            return {city2_id: city2[city2_id], city1_id: city1[city1_id]}


class Help(Resource):
    def get(self, name: str):
        result = []
        for city in data.values():
            str = re.findall(r'[^,\t]*'+name+r'[^,\t]*', city['alternatenames'])
            for city_name in str:
                if city_name not in result:
                    result.append(city_name)
        return {name: result}


data = get_info('RU.txt')
api.add_resource(GeoNameId, '/api/v1.0/<string:geonameid>')
api.add_resource(Pages, '/api/v1.0/pages/<int:page>/<int:count>')
api.add_resource(City, '/api/v1.0/city/<string:city1_name>/<string:city2_name>')
api.add_resource(Help, '/api/v1.0/help/<string:name>')

if __name__ == '__main__':
    app.run(port=8000)
