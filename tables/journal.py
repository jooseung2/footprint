from db import db


class JournalTable(db.Model):
    __tablename__ = "journals"

    def __init__(self, userid, entryid):
        self.userid = userid
        self.entryid = entryid
