from db import db


class EntryTable(db.Model):
    __tablename__ = "entries"

    def __init__(self, entry_id, title, text, lon, lat, time):
        self.entry_id = entry_id
        self.title = title
        self.text = text
        self.lon = lon
        self.lat = lat
        self.time = time
