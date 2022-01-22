# Flask✕JavaScriptでURLを短縮するアプリを開発

# 環境構築

## ライブラリのインストール

まずは以下のコマンドを入力して開発に必要なライブラリをインストールする。

```
py -m venv env
pip install requests flask python-decouple
```

## サーバサイド用のPythonファイルの用意

次に、[URL Shortener Service](https://rapidapi.com/BigLobster/api/url-shortener-service/)にアクセスする。その際、`app.py`を作成して以下のプログラムを書いておく。

<small>`app.py`</small>

```py
import requests
from decouple import config

url = "https://url-shortener-service.p.rapidapi.com/shorten"

payload = "url=https%3A%2F%2Fgoogle.com%2F"
headers = {
    'content-type': "application/x-www-form-urlencoded",
    'x-rapidapi-host': "url-shortener-service.p.rapidapi.com",
    'x-rapidapi-key': config('API_KEY')
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
```

これで以下のコマンドを入力して、何も問題が発生しなければ大丈夫。

```
py app.py
```

## 仮想サーバの立ち上げ

次に、`app.py`を用意して仮想サーバを立ち上げる。

<small>`app.py`</small>

```py
import requests
from decouple import config
from flask import Flask, render_template #追加

url = "https://url-shortener-service.p.rapidapi.com/shorten"

payload = "url=https%3A%2F%2Fgoogle.com%2F"
headers = {
    'content-type': "application/x-www-form-urlencoded",
    'x-rapidapi-host': "url-shortener-service.p.rapidapi.com",
    'x-rapidapi-key': config('API_KEY')
    }

# response = requests.request("POST", url, data=payload, headers=headers)

# print(response.text)

# 以下、追加

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
```

`render_template`で用意されているテンプレート`index.html`を反映させるために、ルートディレクトリに新しく`templates`フォルダを用意して`index.html`を作成する。

<small>`templates/index.html`</small>

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flask URL Shortener</title>
</head>
<body>
    <h1>Hello World</h1>
</body>
</html>
```

仮想サーバの実行方法は以下の通り。

```
py app.py
```

ターミナルが以下のように表示されたら環境構築は終了。

```

```

# 開発環境

* Visual Studio Code 1.63
* Python 3.10.2
* Flask 2.0.x