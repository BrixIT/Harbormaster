from flask import Flask
import pymysql

pymysql.install_as_MySQLdb()
app = Flask(__name__)

#from harbormaster.models import db

#db.init_app(app)

import harbormaster.base_routes
import harbormaster.controllers.containers
import harbormaster.controllers.containerdetails
import harbormaster.controllers.images