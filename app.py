from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    pages = request.args.get('page', default = 1, type = int)
    r = requests.get('http://rickandmortyapi.com/api/character/?page={}'.format(pages))
    rickapi = r.json()
    rickapi_count = len(rickapi['results'])
    rickapi_pages = rickapi['info']['pages']

    return render_template('index.html', rickapi_count = rickapi_count, rickapi = rickapi, rickapi_pages = rickapi_pages, pages=pages, title='PyRick&Morty')

if __name__ == "__main__":
  app.run(debug=True)