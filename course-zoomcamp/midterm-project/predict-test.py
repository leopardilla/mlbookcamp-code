#!/usr/bin/env python
# coding: utf-8

import requests


url = 'http://localhost:9696/predict'

passanger = {
    "passengerid": "10",
    "pclass": "2",
    "name": "Nasser, Mrs. Nicholas (Adele Achem)",
    "sex": "female",
    "age": "14.0",
    "sibsp": "1",
    "parch": "0",
    "ticket": "237736",
    "fare": "30.0708",
    "cabin": "NaN",
    "embarked": "C"
}

response = requests.post(url, json=passanger).json()
print(response)
