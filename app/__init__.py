'''起動スクリプト
app.config.from_object(‘flaskr.config’)はFlaskのconfigが
設定ファイルを読み込む処理で、他にも以下のような処理があります。

app.config.from_envvar: 環境変数から読み込む
app.config.from_object: pythonオブジェクトから読み込む
app.config.from_pyfile: pythonファイルから読み込む
'''
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from redis import Redis
from flask_restful import Api

sample = Flask(__name__)
sample.config.from_object('config.development')
db = SQLAlchemy(sample)
redis = Redis()
sample.redis = redis
api = Api(sample)

import app.views

from app.views.entry import EntryView
api.add_resource(EntryView, '/entry/<int:entry_id>')
