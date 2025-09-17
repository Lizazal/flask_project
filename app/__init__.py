from flask import Flask

app = Flask(__name__)
# app = Flask(__name__, static_folder='my_static') для настройки названия папки
from app import routes
