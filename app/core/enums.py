from enum import Enum


class Gender(Enum):
    DEFAULT = 'Choose a gender'
    MALE = 'male'
    FEMALE = 'female'

    @classmethod
    def choices(cls):
        return [(attr.name, attr.value) for attr in cls]

    def __str__(self):
        return self.value


class Role(Enum):
    DEFAULT = 'Select role'
    VISITOR = 'visitor'
    MODERATOR = 'moderator'
    ADMIN = 'admin'

    @classmethod
    def choices(cls):
        return [(attr.name, attr.value) for attr in cls]

    def __str__(self):
        return self.value


class Status(Enum):
    DEFAULT = 'Select status'
    PLANNING = 'planning'
    PROCESSING = 'processing'
    FINISHED = 'finished'

    @classmethod
    def choices(cls):
        return [(attr.name, attr.value) for attr in cls]

    def __str__(self):
        return self.value


class Palette(Enum):
    RED = 'red'
    BLUE = 'blue'
    GREEN = 'green'
    BLACK = 'black'
    GREY = 'grey'

    @classmethod
    def choices(cls):
        return [(attr.name, attr.value) for attr in cls]

    def __str__(self):
        return self.value


class Language(Enum):
    DEFAULT = 'select article language'
    EN = 'en'
    RUS = 'rus'
    PLN = 'pln'
    CZE = 'cze'
    GER = 'ger'
    FRE = 'fre'
    HIN = 'hin'
    JPN = 'jpn'
    CHI = 'chi'

    @classmethod
    def choices(cls):
        return [(attr.value, attr.name) for attr in cls]

    def __str__(self):
        return self.value


class Category(Enum):
    DEFAULT = 'Choose a category'
    INVESTMENT = 'Investment'
    INNOVATIVE = 'Innovative'
    SCIENTIFIC_RESEARCH = 'Scientific - research'
    TEACHING_EDUCATIONAL = 'Teaching - educational'
    MIXED = 'Mixed'

    @classmethod
    def choices(cls):
        return [(attr.name, attr.value) for attr in cls]

    def __str__(self):
        return self.value
