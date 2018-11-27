#!/usr/bin/env python
#-*- coding: utf-8 -*-
import os, re
from .utils.util import django_management_execute

def initialize_db():
    from mainapp.models.auth import UserRole, User
    from mainapp.models.person import Person
    role_admin = UserRole(name=u"管理员")
    role_admin.save()
    print("created role %s" % role_admin.name)
    role_normal = UserRole(name=u"普通用户")
    role_normal.save()
    print("created role %s" % role_normal.name)
    user = User.create(username="admin", password="admin", nickname=u"管理员", roles=[role_admin,role_normal])
    user_admin = user
    print("created user %s (%s)" % (user.nickname, user.username))
    user = User.create(username="zhangsan", password="zhangsan", nickname=u"张三", roles=[role_normal])
    print("created user %s (%s)" % (user.nickname, user.username))
    person = Person.create(name="张三", createuser=user_admin)
    print("created person %s" % (person.name))
    person = Person.create(name="张康", createuser=user_admin)
    print("created person %s" % (person.name))
    person = Person.create(name="李四", createuser=user_admin)
    print("created person %s" % (person.name))
    person = Person.create(name="王五", createuser=user_admin)
    print("created person %s" % (person.name))
    person = Person.create(name="单俍", createuser=user_admin)
    print("created person %s" % (person.name))

def execute(argv):
    basedir = os.path.join(os.path.dirname(__file__), "..")
    django_management_execute(["manage.py", "makemigrations"])
    django_management_execute(["manage.py", "migrate"])
    initialize_db()
