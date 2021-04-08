#!/usr/bin/python3


from nation_day import NationDay
from region_day import RegionDay
from province_day import ProvinceDay
import requests
import sys

_DATA_REPO_ALL_NATION_URL = 'https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-json/dpc-covid19-ita-andamento-nazionale.json'
_DATA_REPO_LATEST_NATION_URL = 'https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-json/dpc-covid19-ita-andamento-nazionale-latest.json'
_DATA_REPO_ALL_REGION_URL = 'https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-json/dpc-covid19-ita-regioni.json'
_DATA_REPO_LATEST_REGION_URL = 'https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-json/dpc-covid19-ita-regioni-latest.json'
_DATA_REPO_ALL_PROVINCE_URL = 'https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-json/dpc-covid19-ita-province.json'
_DATA_REPO_LATEST_PROVINCE_URL = 'https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-json/dpc-covid19-ita-province-latest.json'

mode = 'latest'
if len(sys.argv) > 1:
    if sys.argv[1] != 'latest':
        mode = 'all'

if mode == 'latest':
    # LATEST NATION DATA
    r = requests.get(_DATA_REPO_LATEST_NATION_URL)
    parsed_json = r.json()
    nation_day = NationDay(parsed_json[0])
    nation_day.writeData()
    # LATEST REGION DATA
    r = requests.get(_DATA_REPO_LATEST_REGION_URL)
    parsed_json = r.json()
    for j in parsed_json:
        region_day = RegionDay(j)
        region_day.writeData()
    # LATEST PROVINCE DATA
    r = requests.get(_DATA_REPO_LATEST_PROVINCE_URL)
    parsed_json = r.json()
    for j in parsed_json:
        region_day = ProvinceDay(j)
        region_day.writeData()
else:
    # ALL NATION DATAS
    r = requests.get(_DATA_REPO_ALL_NATION_URL)
    parsed_json = r.json()
    for j in parsed_json:
        nation_day = NationDay(j)
        nation_day.writeData()
    # ALL REGION DATAS
    r = requests.get(_DATA_REPO_ALL_REGION_URL)
    parsed_json = r.json()
    for j in parsed_json:
        region_day = RegionDay(j)
        region_day.writeData()
    # ALL PROVINCE DATAS
    r = requests.get(_DATA_REPO_ALL_PROVINCE_URL)
    parsed_json = r.json()
    for j in parsed_json:
        region_day = ProvinceDay(j)
        region_day.writeData()
