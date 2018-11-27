from .common import models, CommonModel
from hashlib import md5
from utilities.randomstring import randomstring

class UserRole(CommonModel):
    name = models.CharField(max_length=128, unique=True)

class User(CommonModel):
    username = models.CharField(max_length=128, unique=True)
    password_word = models.CharField(max_length=128)
    password_salt = models.CharField(max_length=128)
    nickname = models.CharField(max_length=128)
    roles = models.ManyToManyField(UserRole)

    @classmethod
    def create(cls, username=None, password=None, nickname=None, roles=None, **kwargs):
        if username: kwargs["username"] = username
        if nickname: kwargs["nickname"] = nickname
        user = User(**kwargs)
        if password:
            user.password = password
        user.save()
        if roles:
            for role in roles:
                user.roles.add(role)
        return user

    @property
    def password(self):
        return self.password_word
    @password.setter
    def password(self, password):
        encrypted = User.EncryptedPassword(password=password)
        self.password_word = encrypted.encrypted
        self.password_salt = encrypted.salt
        return self
    def test_password(self, password):
        return (self.password_word == User.EncryptedPassword(password=password, salt=self.password_salt))
    
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

class LoginToken(models.Model):
    token = models.CharField(max_length=128)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    createtime = models.DateTimeField()
    updatetime = models.DateTimeField()
    expiretime = models.DateTimeField()
    expiresecs = models.IntegerField()
    def __str__(self):
        return self.token
