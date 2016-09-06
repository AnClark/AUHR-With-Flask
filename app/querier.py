# -*- coding: UTF-8 -*-

from app import app, db, models
from .models import Member
import string


department_list = (
    "秘书部",
    "宣传部",
    "财务部",
    "行政监察部",
    "社团部",
    "公共关系部",
    "人力资源部",
    "外联部",
    "外联企划小组",
    "权益部",
    "媒体部",
    "新媒体工作室",
    "思存工作室",
    "文艺拓展部"
)

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

        if string.find(str_for_cmp, keyword) >= 0:
            result_assembly.append(member)
            print("***  FOUND One!")

    if result_assembly:
        return result_assembly
    else:
        return False


# FOR DEBUG
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

