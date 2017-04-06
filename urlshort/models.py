from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class LongUrl(db.Model):
    """
    URL ORM model
    """
    id = db.Column(db.Integer(), primary_key=True)
    long_url = db.Column(db.String())

    def __init__(self, long_url):
        self.long_url = long_url

    def get_id(self):
        return self.id
