#!/usr/bin/env python
#-*- coding: utf-8 -*-
import os, re
from .utils.util import django_management_execute

def initialize_db():
    from mainapp.models.auth import UserRole, User
    role_admin = UserRole(name=u"管理员")
    role_admin.save()
    print("created role %s" % role_admin.name)
    role_normal = UserRole(name=u"普通用户")
    role_normal.save()
    print("created role %s" % role_normal.name)
    user = User(username="admin", nickname=u"管理员").set_password("admin")
    user.save()
    user.add_role(role_admin).add_role(role_normal)
    print("created user %s (%s)" % (user.nickname, user.username))
    user = User(username="zhangsan", nickname=u"张三").set_password("zhangsan")
    user.save()
    user.add_role(role_normal)
    print("created user %s (%s)" % (user.nickname, user.username))

def execute(argv):
    basedir = os.path.join(os.path.dirname(__file__), "..")
    django_management_execute(["manage.py", "makemigrations"])
    django_management_execute(["manage.py", "migrate"])
    initialize_db()
