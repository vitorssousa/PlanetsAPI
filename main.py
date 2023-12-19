from flask import Flask, render_template
import requests

headers = {
	"X-RapidAPI-Key": "",
	"X-RapidAPI-Host": "planets-info-by-newbapi.p.rapidapi.com"
}

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/planets/<parameter>')
def planets(parameter=""):
    url = f"https://planets-info-by-newbapi.p.rapidapi.com/api/v1/planets/{parameter}"
    response = requests.get(url, headers=headers).json()
    info = {'planet_image': response['imgSrc']['img'], 'planet_name': response['name'], 'planet_desc': response['description'], 'planet_volume': response['basicDetails']['volume'], 'planet_mass': response['basicDetails']['mass']}
    return render_template('planet.html', info = info)

app.run()
