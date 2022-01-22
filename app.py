import requests
from decouple import config
from flask import Flask, render_template

url = "https://url-shortener-service.p.rapidapi.com/shorten"

payload = "url=https%3A%2F%2Fgoogle.com%2F"
headers = {
    'content-type': "application/x-www-form-urlencoded",
    'x-rapidapi-host': "url-shortener-service.p.rapidapi.com",
    'x-rapidapi-key': config('API_KEY')
    }

# response = requests.request("POST", url, data=payload, headers=headers)

# print(response.text)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)