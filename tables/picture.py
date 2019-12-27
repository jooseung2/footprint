from db import db


class PictureTable(db.Model):
    __tablename__ = "pictures"

    def __init__(self, entryid, url):
        self.entry_id = entry_id
        self.url = url
