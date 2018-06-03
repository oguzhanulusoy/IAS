from .lists import *


def grade_point(grade):
    if grade == "AA":
        return 4
    if grade == "BA":
        return 3.5
    if grade == "BB":
        return 3.0
    if grade == "CB":
        return 2.5
    if grade == "CC":
        return 2
    if grade == "DC":
        return 1.5
    if grade == "DD":
        return 1
    return 0


def semester_status(gpa):
    if gpa > 2:
        return 'Satisfactory'

    return 'Non-Satisfactory'


def maximum_credit(gpa):
    if gpa < 2.0:
        return 19
    if gpa >= 2.0:
        return 21
    if gpa >= 2.5:
        return 24


def standing(credit):
    if credit < 34:
        return YEAR_IN_SCHOOL_CHOICES[0][1]

    if credit < 72:
        return YEAR_IN_SCHOOL_CHOICES[1][1]

    if credit < 104:
        return YEAR_IN_SCHOOL_CHOICES[2][1]

    if credit >= 104:
        return YEAR_IN_SCHOOL_CHOICES[3][1]