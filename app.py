import requests
from decouple import config
from flask import Flask, render_template

url = "https://url-shortener-service.p.rapidapi.com/shorten"

# print(response.text)

app = Flask(__name__)

@app.route('/')
def index():
    payload = "url="
    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'x-rapidapi-host': "url-shortener-service.p.rapidapi.com",
        'x-rapidapi-key': config('API_KEY')
        }

# response = requests.request("POST", url, data=payload, headers=headers)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)