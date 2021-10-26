from flask import Flask
from flask import request
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from flask_cors import CORS

from data import *
import urllib

app = Flask(__name__)
CORS(app)

# DB connection
#                                                      PLACE YOUR SERVER AND DATABASE HERE
params = urllib.parse.quote_plus('DRIVER={SQL Server};SERVER=HARRISONS-THINK;DATABASE=LendApp;Trusted_Connection=yes;')
app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pyodbc:///?odbc_connect=%s" % params
db = SQLAlchemy(app)

# just hello world
@app.route('/')
def hello():
    return "Hello World!"


# get all auditories with some possible params:
#   @building - name of some university building
#   @type - one of the audiences types
#   @number - valid number of this audience
# return list of audiences with the same parameters
@app.route('/audiences/all/', methods=["GET"])
def all_audiences():
    # obtain parameters from get request
    building = request.args.get("building")
    audience_type = request.args.get("type")
    number = request.args.get("number")

    # SQL request for auditories (uncomment next code if start working with DB!)
    #                                PLACE YOUR REQUEST HERE
    # sql_request = text('select building, audience_type, number from audiences')
    # sql_result = db.engine.execute(sql)
    # audiences_list = [AudienceInfo(row[0],row[1],row[2]) for row in result]

    # filter test audiences list and select all suitable
    audiences = list(filter(lambda audience:
        (building is None or audience.building == building) and
        (audience_type is None or audience.audience_type == audience_type) and
        (number is None or audience.number == number),
    audiences_list))

    # return json with suitable audiences
    return jsonify(audiences=[a.serialize() for a in audiences])
