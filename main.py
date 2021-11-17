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
params = urllib.parse.quote_plus('DRIVER={SQL Server};SERVER=LAPTOP-LSAPIF7D;DATABASE=local_db;Trusted_Connection=yes;')
app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pyodbc:///?odbc_connect=%s" % params
db = SQLAlchemy(app)

toStr = lambda x: x if x is not None else ""


# just hello world
@app.route('/')
def hello():
    return "Hello World!"


# get all auditories with some possible params:
#   @building - name of some university building
#   @type - one of the audiences types
#   @number - valid number of this audience
# return list of audiences with the same parameters
@app.route('/audiences/search/', methods=["GET"])
def search_audiences():
    # obtain parameters from get request
    building = toStr(request.args.get("building"))
    audience_type = toStr(request.args.get("type"))
    number = toStr(request.args.get("number"))
    limit = int(request.args.get("limit"))
    page = int(request.args.get("page"))

    # # filter test audiences list and select all suitable
    audiences = list(filter(lambda audience:
                            (audience.building.find(building)) and
                            (audience.audience_type.find(audience_type)) and
                            (audience.number.find(number)),
                            audiences_list))

    # return json with suitable audiences
    return jsonify(countRecords=str(len(audiences)),
                   audiences=[a.serialize() for a in audiences[limit * page:limit * (page + 1)]])


# Для теста
@app.route('/educators/search/', methods=["GET"])
def search_educators():
    # obtain parameters from get request
    global sql_request
    fio = toStr(request.args.get("fio"))
    faculty = toStr(request.args.get("faculty"))
    position = toStr(request.args.get("position"))
    degree = toStr(request.args.get("degree"))
    limit = int(request.args.get("limit"))
    page = int(request.args.get("page"))

    educators = list(filter(lambda educator:
                            (educator.fio.find(fio)) and
                            (educator.faculty.find(faculty)) and
                            (educator.position.find(position)) and
                            (educator.degree.find(degree)),
                            educators_list))

    return jsonify(countRecords=str(len(educators)),
                   educators=[a.serialize() for a in educators[limit * page:limit * (page + 1)]])


@app.route('/disciplines/search/', methods=["GET"])
def search_disciplines():
    # obtain parameters from get request
    name = toStr(request.args.get("name"))
    limit = int(request.args.get("limit"))
    page = int(request.args.get("page"))

    disciplines = list(filter(lambda discipline:
                              (discipline.name.find(name)),
                              disciplines_list))

    return jsonify(countRecords=str(len(disciplines)),
                   disciplines=[a.serialize() for a in disciplines[limit * page:limit * (page + 1)]])


@app.route('/groups/search/', methods=["GET"])
def search_group():
    # obtain parameters from get request
    faculty = toStr(request.args.get("faculty"))
    program = toStr(request.args.get("program"))
    name = toStr(request.args.get("name"))
    course = toStr(request.args.get("course"))
    limit = int(request.args.get("limit"))
    page = int(request.args.get("page"))

    groups = list(filter(lambda group:
                         (group.faculty.find(faculty)) and
                         (group.program.find(program)) and
                         (group.name.find(name)) and
                         (group.course.find(course)),
                         groups_list))


    # return json with suitable audiences
    return jsonify(countRecords=str(len(groups)),
                   groups=[a.serialize() for a in groups[limit * page:limit * (page + 1)]])


@app.route('/timetable/search/', methods=["POST"])
def timetable_search():
    place = request.form["place"]
    startData = request.form["startData"]
    endData = request.form["endData"]
    id = request.form["id"]
    limit = int(request.args.get("limit"))
    page = int(request.args.get("page"))

    timetable = list(filter( lambda timetable: timetable.id in id, timetables_list))

    return jsonify(countRecords=str(len(timetable)),
                   timetables=[a.serialize() for a in timetable[limit * page:limit * (page + 1)]])
