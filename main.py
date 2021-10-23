from flask import Flask
from flask import request
from flask import jsonify

from data import *


app = Flask(__name__)


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

    # filter test audiences list and select all suitable
    audiences = list(filter(lambda audience:
        (building is None or audience.building == building) and
        (audience_type is None or audience.audience_type == audience_type) and
        (number is None or audience.number == number),
    audiences_list))

    # return json with suitable audiences
    return jsonify(audiences=[a.serialize() for a in audiences])
