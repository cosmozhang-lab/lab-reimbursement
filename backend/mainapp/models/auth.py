from django.db import models
from hashlib import md5
from utilities.randomstring import randomstring

class UserRole(models.Model):
    name = models.CharField(max_length=128, unique=True)

class User(models.Model):
    username = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=128)
    passsalt = models.CharField(max_length=128)
    nickname = models.CharField(max_length=128)
    roles = models.ManyToManyField(UserRole)
    class EncryptedPassword:
        def __init__(self, password=None, salt=None, encrypted=None):
            if encrypted is None:
                if salt is None:
                    salt = randomstring()
                encrypted = md5((salt+password).encode("utf-8")).hexdigest()
            self.password = password
            self.salt = salt
            self.encrypted = encrypted
        def __eq__(self, other):
            if isinstance(other, User.EncryptedPassword):
                other = other.encrypted
            if not isinstance(other, str):
                raise ValueError("cannot compare EncryptedPassword with %s" % type(other))
            return self.encrypted == other
    def test_password(self, password):
        return (self.password == User.EncryptedPassword(password=password, salt=self.passsalt))
    def set_password(self, password):
        encrypted = User.EncryptedPassword(password=password)
        self.password = encrypted.encrypted
        self.passsalt = encrypted.salt
        return self
    def add_role(self, role):
        self.roles.add(role)
        return self
    def remove_role(self, role):
        self.roles.remove(role)
        return self

class LoginToken(models.Model):
    token = models.CharField(max_length=128)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    createtime = models.DateTimeField()
    updatetime = models.DateTimeField()
    expiretime = models.DateTimeField()
    expiresecs = models.IntegerField()
    def __str__(self):
        return self.token
