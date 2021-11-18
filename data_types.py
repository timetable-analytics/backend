# class with info about each adience and serialization method for jsonify
class AudienceInfo(object):
    id = ""
    building = ""
    audience_type = ""
    number = ""

    def __init__(self, _id, _building, _audience_type, _number):
        self.id = _id
        self.building = _building
        self.audience_type = _audience_type
        self.number = _number

    def serialize(self):
        return {
            "id": self.id,
            "building": self.building,
            "type": self.audience_type,
            "number": self.number
        }


class EducatorInfo(object):
    id = ""
    fio = ""
    faculty = ""
    position = ""
    degree = ""

    def __init__(self, _id, _fio, _faculty, _position, _degree):
        self.id = _id
        self.fio = _fio
        self.faculty = _faculty
        self.position = _position
        self.degree = _degree

    def serialize(self):
        return {
            "id": self.id,
            "fio": self.fio,
            "faculty": self.faculty,
            "position": self.position,
            "degree": self.degree
        }


class DisciplineInfo(object):
    id = ""
    name = ""

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name
        }


class GroupInfo(object):
    id = ""
    faculty = ""
    program = ""
    name = ""
    course = ""

    def __init__(self, id, faculty, program, name, course):
        self.id = id
        self.faculty = faculty
        self.program = program
        self.name = name
        self.course = course

    def serialize(self):
        return {
            "id": self.id,
            "faculty": self.faculty,
            "program": self.program,
            "name": self.name,
            "course": self.course
        }

class TimetableInfo(object):
    id = ""
    building = ""
    classroom_name = ""
    fio = ""
    discipline = ""
    group = ""
    time = ""

    def __init__(self, _id, _building, _fio, _discipline, _group, _time):
        self.id= _id
        self.building = _building
        self.fio = _fio
        self.discipline = _discipline
        self.group = _group
        self.time = _time

    def serialize(self):
        return {
            "id": self.id,
            "building": self.building,
            "classroom_name": self.classroom_name,
            "fio": self.fio,
            "name": self.discipline,
            "stGroups": self.group,
            "time": self.time
        }