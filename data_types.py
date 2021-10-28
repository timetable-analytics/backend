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

class EducatorInfo(object):
    fio = ""
    faculty = ""
    position = ""
    degree = ""

    def __init__(self, _fio, _faculty, _position, _degree):
        self.fio = _fio
        self.faculty = _faculty
        self.position = _position
        self.degree = _degree

    def serialize(self):
        return {
            "fio": self.fio,
            "faculty": self.faculty,
            "position": self.position,
            "degree": self.degree
        }