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

    # SQL request for auditories (uncomment next code if start working with DB!)
    #                                PLACE YOUR REQUEST HERE
    sql_request = f"""
        select [Classroom].[id], [Address].[address], [Classroom_kind].[name], [Classroom].[name]
        from [Address], [Classroom], [Classroom_kind]
        where [Classroom].[classroom_kind] = [Classroom_kind].[id]
            and [Classroom].[address] = [Address].[id] and [Address].[address] like '%{building}%'
            and [Classroom].[name] like '%{number}%'
            and [Classroom_kind].[name] like '%{audience_type}%'"""
    sql_result = db.engine.execute(sql_request)
    audiences = [AudienceInfo(row[0], row[1], row[2], row[3]) for row in sql_result]

    # # filter test audiences list and select all suitable
    # audiences = list(filter(lambda audience:
    #                         (building is None or audience.building == building) and
    #                         (audience_type is None or audience.audience_type == audience_type) and
    #                         (number is None or audience.number == number),
    #                         audiences_list))

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

    sql_request = f"""
        select [Educator].[id], [Division].[name], [Educator].[full_name], [EducatorPosition].[name], [EducatorGroup].[name]
        from [Division], [Educator], [EducatorPosition], [EducatorGroup], [EducatorEmployment], [EducatorDivision]
        where [Division].[id] = [EducatorDivision].[division]
            and [Educator].[id] = [EducatorEmployment].[educator]
            and [EducatorPosition].[id] = [EducatorEmployment].[position]
            and [EducatorGroup].[id] = [EducatorEmployment].[educator_group]
            and [EducatorEmployment].[id] = [EducatorDivision].[educator_employment]
            and [EducatorEmployment].[is_active] = 1 
            and [Division].[name] like '%{faculty}%'
            and [Educator].[full_name] like '%{fio}%'
            and [EducatorPosition].[name] like '%{position}%'
            and [EducatorGroup].[name] like '%{degree}%'
        group by [Division].[name], [Educator].[full_name], [EducatorPosition].[name], [EducatorGroup].[name], [Educator].[id] 
        order by [Educator].[full_name]"""

    sql_result = db.engine.execute(sql_request)
    educators = [EducatorInfo(row[0], row[1], row[2], row[3],  row[4]) for row in sql_result]

    # educators = list(filter(lambda educator:
    #                         (fio is None or educator.fio == fio) and
    #                         (faculty is None or educator.faculty == faculty) and
    #                         (position is None or educator.position == position) and
    #                         (degree is None or educator.degree == degree),
    #                         educators_list))

    return jsonify(countRecords=str(len(educators)),
                   educators=[a.serialize() for a in educators[limit * page:limit * (page + 1)]])


@app.route('/disciplines/search/', methods=["GET"])
def search_disciplines():
    # obtain parameters from get request
    name = toStr(request.args.get("name"))
    limit = int(request.args.get("limit"))
    page = int(request.args.get("page"))

    sql_request = f"""select [Discipline].[id], [Discipline].[name]
        from [Discipline]
        where [Discipline].[name] like '%{name}%'
        order by [Discipline].[name]"""
    sql_result = db.engine.execute(sql_request)
    disciplines = [DisciplineInfo(row[0], row[1]) for row in sql_result]

    # disciplines = list(filter(lambda discipline:
    #                           (name is None or discipline.name == name),
    #                           disciplines_list))

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

    sql_request = f"""select [Group_union].[id], [Division].[name], [Group_union].[name], [Group_union].[course]
        from [Division], [Group_union], [Group_union_Division]
        where [Division].[id] = [Group_union_Division].[division]
        and [Group_union].[id] = [Group_union_Division].[group_union]
        and [Division].[name] like '%{faculty}%'
        and [Group_union].[name] like '%{name}%'
        and [Group_union].[course] like '%{course}%'
        order by [Group_union].[name]"""
    sql_result = db.engine.execute(sql_request)
    groups = [GroupInfo(row[0], row[1], "", row[2], row[3]) for row in sql_result]

    # # filter test audiences list and select all suitable
    # groups = list(filter(lambda group:
    #                      (faculty is None or group.faculty == faculty) and
    #                      (program is None or group.program == program) and
    #                      (name is None or group.name == name) and
    #                      (course is None or group.course == course),
    #                      groups_list))

    # return json with suitable audiences
    return jsonify(countRecords=str(len(groups)),
                   groups=[a.serialize() for a in groups[limit * page:limit * (page + 1)]])


@app.route('/timetable/search/', methods=["POST"])
def timetable():
    place = request.form["place"]
    startData = request.form["startData"]
    endData = request.form["endData"]
    id = request.form["id"]
    limit = int(request.args.get("limit"))
    page = int(request.args.get("page"))

    sql_request = f"""
        select 	[Event].[id],
                [Address].[address]+' '+[Classroom].[name], 
                [Educator].[full_name], 
                [Discipline].[name], 
                [Group_union].[name], 
                (convert(nvarchar, [Event].[start]) + ' - ' + ltrim(right(convert(varchar(20), [Event].[end], 100), 7))) as times
        from	[Address], [Classroom], [Educator], [Discipline], 
                [Group_union], [Event], [EducatorEmployment],
                [EducatorAssigmentUnit], [EventLocation]
        where [Address].[id] = [Classroom].[address]
            and [Classroom].[id] = [EventLocation].[classroom]
            and [EventLocation].[event] = [Event].[id]
            and [EducatorEmployment].[educator] = [Educator].[id]
            and [EducatorEmployment].[id] = [EducatorAssigmentUnit].[educator_employment]
            and [Event].[educator_assigment] = [EducatorAssigmentUnit].[educator_assigment]
            and [Event].[discipline] = [Discipline].[id]
            and [Group_union].[id] = [Event].[group_union]
            and convert(date, [Event].[start]) >= '{startData}'
            and convert(date, [Event].[end]) <= '{endData}' """

    if place == "audiences":
        sql_request = sql_request + f"and [Classroom].[id] in ('{id}') "
    elif place == "educators":
        sql_request = sql_request + f"and [Educator].[id] in ('{id}')"
    elif (place == "groups"):
        sql_request = sql_request + f"and [Group_union].[id] in ('{id}')"
    elif (place == "disciplines"):
        sql_request = sql_request + f"and [Discipline].[id] in ('{id}')"


    sql_result = db.engine.execute(sql_request)
    timetable = [TimetableInfo(row[0], row[1], row[2], row[3], row[4], row[5]) for row in sql_result]

    return jsonify(countRecords=str(len(timetable)),
                   timetables=[a.serialize() for a in timetable[limit * page:limit * (page + 1)]])
