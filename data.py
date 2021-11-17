from data_types import *

# test data
audiences_list = [
    AudienceInfo("13241", "Университетский проспект, дом 35", "Лекционный зал", "202"),
    AudienceInfo("16542", "Университетский проспект, дом 35", "Лекционный зал", "210"),
    AudienceInfo("16763", "Университетский проспект, дом 35", "Лекционный зал", "204"),
    AudienceInfo("87654", "Университетский проспект, дом 35", "Лекционный зал", "208"),

    AudienceInfo("98765", "Университетский проспект, дом 35", "Кабинет", "215"),
    AudienceInfo("43567", "Университетский проспект, дом 35", "Кабинет", "279"),
    AudienceInfo("97685", "Университетский проспект, дом 35", "Кабинет", "480"),
    AudienceInfo("24378", "Университетский проспект, дом 35", "Кабинет", "303"),

    AudienceInfo("09879", "Университетский проспект, дом 28", "Лекционный зал", "4309"),
    AudienceInfo("24356", "Университетский проспект, дом 28", "Лекционный зал", "4317"),
    AudienceInfo("46734", "Университетский проспект, дом 28", "Лекционный зал", "2103"),
    AudienceInfo("76544", "Университетский проспект, дом 28", "Лекционный зал", "3506"),

    AudienceInfo("23534", "Университетский проспект, дом 28", "Кабинет", "215"),
    AudienceInfo("24636", "Университетский проспект, дом 28", "Кабинет", "279"),
    AudienceInfo("26436", "Университетский проспект, дом 28", "Кабинет", "480"),
    AudienceInfo("68956", "Университетский проспект, дом 28", "Кабинет", "303"),

    AudienceInfo("23888", "Университетский проспект, дом 28", "Кабинет", "215"),
    AudienceInfo("24234", "Университетский проспект, дом 28", "Кабинет", "279"),
    AudienceInfo("13123", "Университетский проспект, дом 28", "Кабинет", "480"),
    AudienceInfo("12352", "Университетский проспект, дом 28", "Кабинет", "303"),
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