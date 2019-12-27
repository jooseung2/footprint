from db import db


class UserTable(db.Model):
    __tablename__ = "users"

    def __init__(self, userid, loginid, password):
        self.userid = userid
        self.loginid = loginid
        self.password = password
