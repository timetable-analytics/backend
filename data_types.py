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