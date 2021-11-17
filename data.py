from data_types import *

# test data
audiences_list = [
    AudienceInfo("1", "Университетский проспект, дом 35", "Лекционный зал", "202"),
    AudienceInfo("2", "Университетский проспект, дом 35", "Лекционный зал", "210"),
    AudienceInfo("3", "Университетский проспект, дом 35", "Лекционный зал", "204"),
    AudienceInfo("4", "Университетский проспект, дом 35", "Лекционный зал", "208"),

    AudienceInfo("5", "Университетский проспект, дом 35", "Кабинет", "215"),
    AudienceInfo("6", "Университетский проспект, дом 35", "Кабинет", "279"),
    AudienceInfo("7", "Университетский проспект, дом 35", "Кабинет", "480"),
    AudienceInfo("8", "Университетский проспект, дом 35", "Кабинет", "303"),

    AudienceInfo("9", "Университетский проспект, дом 28", "Лекционный зал", "4309"),
    AudienceInfo("10", "Университетский проспект, дом 28", "Лекционный зал", "4317"),
    AudienceInfo("11", "Университетский проспект, дом 28", "Лекционный зал", "2103"),
    AudienceInfo("12", "Университетский проспект, дом 28", "Лекционный зал", "3506"),

    AudienceInfo("13", "Университетский проспект, дом 28", "Кабинет", "215"),
    AudienceInfo("14", "Университетский проспект, дом 28", "Кабинет", "279"),
    AudienceInfo("15", "Университетский проспект, дом 28", "Кабинет", "480"),
    AudienceInfo("16", "Университетский проспект, дом 28", "Кабинет", "303"),

    AudienceInfo("17", "Университетский проспект, дом 28", "Кабинет", "215"),
    AudienceInfo("18", "Университетский проспект, дом 28", "Кабинет", "279"),
    AudienceInfo("19", "Университетский проспект, дом 28", "Кабинет", "480"),
    AudienceInfo("20", "Университетский проспект, дом 28", "Кабинет", "303"),
]


groups_list = [
    GroupInfo("1", "ПМ-ПУ", "Программирование и информационные технологии", "131", "1"),
    GroupInfo("2", "ПМ-ПУ", "Программирование и информационные технологии", "232", "2"),
    GroupInfo("3", "ПМ-ПУ", "Программирование и информационные технологии", "132", "1"),
    GroupInfo("4", "ПМ-ПУ", "Программирование и информационные технологии", "331", "3"),
    GroupInfo("5", "ПМ-ПУ", "Программирование и информационные технологии", "134", "1"),
    GroupInfo("6", "ПМ-ПУ", "Прикладная математика и информатика", "111", "1"),
    GroupInfo("7", "ПМ-ПУ", "Прикладная математика и информатика", "111", "1"),
    GroupInfo("8", "ПМ-ПУ", "Прикладная математика и информатика", "311", "3"),
    GroupInfo("9", "ПМ-ПУ", "Прикладная математика и информатика", "411", "4"),
    GroupInfo("10", "МатМех", "Механика и математическое моделирование", "111", "1"),
    GroupInfo("11", "МатМех", "Механика и математическое моделирование", "211", "2"),
    GroupInfo("12", "МатМех", "Механика и математическое моделирование", "212", "2"),
    GroupInfo("13", "МатМех", "Механика и математическое моделирование", "213", "2"),
    GroupInfo("14", "МатМех", "Механика и математическое моделирование", "311", "3"),
    GroupInfo("15", "МатМех", "Механика и математическое моделирование", "411", "4"),
    GroupInfo("16", "МатМех", "Механика и математическое моделирование", "412", "4"),
    GroupInfo("17", "МатМех", "Механика и математическое моделирование", "214", "2"),
    GroupInfo("18", "МатМех", "Механика и математическое моделирование", "112", "1"),
    GroupInfo("19", "МатМех", "Механика и математическое моделирование", "113", "1")

]


disciplines_list = [
    DisciplineInfo("1", "Алгебра"),
    DisciplineInfo("2", "Геометрия1"),
    DisciplineInfo("3", "Геометрия2"),
    DisciplineInfo("4", "Геометрия3"),
    DisciplineInfo("5", "Геометрия4"),
    DisciplineInfo("6", "Геометрия5"),
    DisciplineInfo("7", "Геометрия6"),
    DisciplineInfo("8", "Геометрия7"),
    DisciplineInfo("9", "Геометрия8"),
    DisciplineInfo("10", "Геометрия9"),
    DisciplineInfo("11", "Геометрия10"),
    DisciplineInfo("12", "Геометрия11"),
    DisciplineInfo("13", "Геометрия12"),
    DisciplineInfo("14", "Геометрия13"),
    DisciplineInfo("15", "Геометрия14"),
    DisciplineInfo("16", "Геометрия15"),
    DisciplineInfo("17", "Геометрия16"),
    DisciplineInfo("18", "Геометрия17"),
    DisciplineInfo("19", "Геометрия18"),
    DisciplineInfo("20", "Геометрия19"),
    DisciplineInfo("21", "Геометрия20"),
    DisciplineInfo("22", "Геометрия21"),
]


educators_list = [
    EducatorInfo("346346", "Смирнова Элина Марковна", "ПМ-ПУ", "доцент", "кандидат наук"),
    EducatorInfo("346357", "Тарасова Светлана Глебовна", "ПМ-ПУ", "доцент", ""),
    EducatorInfo("784688", "Трифонова Марьям Владиславовна", "ПМ-ПУ", "ассистент", ""),
    EducatorInfo("846858", "Богданов Матвей Львович", "ПМ-ПУ", "ассистент", ""),
    EducatorInfo("165384", "Федосеев Тимофей Даниилович", "ПМ-ПУ", "профессор", "кандидат наук"),
    EducatorInfo("252679", "Калмыков Пётр Артурович", "ПМ-ПУ", "профессор", "доктор наук"),
    EducatorInfo("463563", "Головина Арина Максимовна", "ПМ-ПУ", "профессор", "доктор наук"),
    EducatorInfo("637357", "Андреева Екатерина Григорьевна", "МатМех", "доцент", "кандидат наук"),
    EducatorInfo("246379", "Ларионова Марина Викторовна", "МатМех", "доцент", ""),
    EducatorInfo("235343", "Курочкина Полина Артёмовна", "МатМех", "ассистент", ""),
    EducatorInfo("674574", "Гришина Светлана Кирилловна", "МатМех", "ассистент", ""),
    EducatorInfo("168569", "Анохина Татьяна Артёмовна", "МатМех", "профессор", "доктор наук"),

]

timetables_list = [
    TimetableInfo("0","Здание 1", "Преподаватель", "Предмет", "группа", "9:30-11:05"),
    TimetableInfo("1", "Здание 2", "Преподаватель 1", "Предмет 1", "группа 1", "9:30-11:05"),
    TimetableInfo("2", "Здание 3", "Преподаватель 2", "Предмет 2", "группа 2", "9:30-11:05"),
    TimetableInfo("3", "Здание 4", "Преподаватель 3", "Предмет 3", "группа 3", "9:30-11:05"),
    TimetableInfo("4", "Здание 5", "Преподаватель 4", "Предмет 4", "группа 4", "9:30-11:05"),
    TimetableInfo("5", "Здание 6", "Преподаватель 5", "Предмет 5", "группа 5", "9:30-11:05"),
    TimetableInfo("6", "Здание 7", "Преподаватель 6", "Предмет 6", "группа 6", "9:30-11:05"),
    TimetableInfo("7", "Здание 8", "Преподаватель 7", "Предмет 7", "группа 7", "9:30-11:05"),
    TimetableInfo("8", "Здание 9", "Преподаватель 8", "Предмет 8", "группа 8", "9:30-11:05"),
    TimetableInfo("9", "Здание 10", "Преподаватель 9", "Предмет 9", "группа 9", "9:30-11:05"),
    TimetableInfo("10", "Здание 11", "Преподаватель 10", "Предмет 10", "группа 10", "9:30-11:05"),
    TimetableInfo("11", "Здание 12", "Преподаватель 11", "Предмет 11", "группа 11", "9:30-11:05"),
    TimetableInfo("12", "Здание 13", "Преподаватель 12", "Предмет 12", "группа 12", "9:30-11:05"),
    TimetableInfo("13", "Здание 14", "Преподаватель 13", "Предмет 13", "группа 13", "9:30-11:05"),
    TimetableInfo("14", "Здание 15", "Преподаватель 14", "Предмет 14", "группа 14", "9:30-11:05"),
    TimetableInfo("15", "Здание 15", "Преподаватель 15", "Предмет 15", "группа 15", "9:30-11:05"),
    TimetableInfo("16", "Здание 16", "Преподаватель 16", "Предмет 16", "группа 16", "9:30-11:05"),
    TimetableInfo("17", "Здание 17", "Преподаватель 17", "Предмет 17", "группа 17", "9:30-11:05"),
    TimetableInfo("18", "Здание 18", "Преподаватель 18", "Предмет 18", "группа 18", "9:30-11:05"),
    TimetableInfo("19", "Здание 19", "Преподаватель 19", "Предмет 19", "группа 19", "9:30-11:05"),
    TimetableInfo("20", "Здание 20", "Преподаватель 20", "Предмет 20", "группа 20", "9:30-11:05"),
    TimetableInfo("21", "Здание 21", "Преподаватель 21", "Предмет 21", "группа 21", "9:30-11:05")
]