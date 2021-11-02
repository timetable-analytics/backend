# class with info about each adience and serialization method for jsonify
class AudienceInfo(object):
    building = ""
    audience_type = ""
    number = ""

    def __init__(self, _building, _audience_type, _number):
        self.building = _building
        self.audience_type = _audience_type
        self.number = _number

    def serialize(self):
        return {
            "building": self.building,
            "type": self.audience_type,
            "number": self.number
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
