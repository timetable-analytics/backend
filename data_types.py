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
    name = ""

    def __init__(self, name):
        self.name = name

    def serialize(self):
        return {
            "name": self.name
        }
      
      
class GroupInfo(object):
    faculty = ""
    program = ""
    name = ""
    course = ""

    def __init__(self, faculty, program, name, course):
        self.faculty = faculty
        self.program = program
        self.name = name
        self.course = course

    def serialize(self):
        return {
            "faculty": self.faculty,
            "program": self.program,
            "name": self.name,
            "course": self.course
        }

