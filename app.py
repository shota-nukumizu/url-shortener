import requests
from decouple import config
from flask import Flask, render_template, request

url = "https://url-shortener-service.p.rapidapi.com/shorten"



app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = request.get_json()

        long_url = data.get('long_url')

        payload = f"url={long_url}"
        headers = {
            'content-type': "application/x-www-form-urlencoded",
            'x-rapidapi-host': "url-shortener-service.p.rapidapi.com",
            'x-rapidapi-key': config('API_KEY')
            }

        response = requests.request("POST", url, data=payload, headers=headers)

        print(response.json()['result_url'])

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)