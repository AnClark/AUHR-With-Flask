"""# -*- coding: UTF-8 -*-"""

from app import app, db, models
from .models import Member
import string


def MemberQuerier(keyword):

    result_assembly = []
    members = db.session.query(
        Member.Name,
        Member.Gender,
        Member.Mobile,
        Member.QQ,
        Member.Birthday,
        Member.Grade,
        Member.Faculty,
        Member.Class,
        Member.DormBuild,
        Member.Department,
        Member.GroupInDepart,
        Member.Occupation,
        Member.AUID,
        Member.ArrivalTime
    ).all()

    for member in members:
        str_for_cmp = ""
        for column in member:
            str_for_cmp = str_for_cmp + str(column) + ","
        # print(str_for_cmp)

        if string.find(str_for_cmp, keyword) > 0:
            result_assembly.append(member)
            print("***  FOUND One!")

    if result_assembly:
        return result_assembly
    else:
        return False


def print_all():

        members = db.session.query(
            Member.Name,
            Member.Gender,
            Member.Mobile,
            Member.QQ,
            Member.Birthday,
            Member.Grade,
            Member.Faculty,
            Member.Class,
            Member.DormBuild,
            Member.Department,
            Member.GroupInDepart,
            Member.Occupation,
            Member.AUID,
            Member.ArrivalTime
        ).all()

        for member in members:
            str_for_cmp = ""
            for column in member:
                str_for_cmp = str_for_cmp + str(column) + ","
            print(str_for_cmp)

