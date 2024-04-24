
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://avnadmin:AVNS_Gt6exP7YUc62oQxImdj@mohamidz-mohamidz.a.aivencloud.com:13996/defaultdb'
app.config['SECRET_KEY'] = 'ec9439cfc6c796ae2029594d'

db = SQLAlchemy(app)

from expert_system import routes