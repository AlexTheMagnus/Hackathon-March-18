# -*- coding: utf-8 -*
from flask import Flask

app = Flask(__name__)


@app.route('/get_name_parsed')
def get_name_parsed(full_name):
    full_name = full_name.lower()
    for letter in full_name:     
        if letter == ' ':
            full_name = full_name.replace(letter, '-')
        if letter == 'ñ':
            full_name = full_name.replace(letter, 'n')
        if letter == 'á':
            full_name = full_name.replace(letter, 'a')
        if letter == 'é':
            full_name = full_name.replace(letter, 'e')
        if letter == 'í':
            full_name = full_name.replace(letter, 'i')
        if letter == 'ó':
            full_name = full_name.replace(letter, 'o')
        if letter == 'ú':
            full_name = full_name.replace(letter, 'u')
        if letter == 'ü':
            full_name = full_name.replace(letter, 'u')
    return full_name

@app.route('/get_url')
def get_url(parsed_name):
    url = "https://transparentia.newtral.es/api/get/byName/" + parsed_name
    return url
