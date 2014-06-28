from uuid import uuid4

from scraper import db
from scraper.models import ModelMixin


class Twitter(db.Model, ModelMixin):
    __tablename__ = "Twitter"

    id = db.Column(db.String(36), default=str(uuid4()), autoincrement=False)
    username = db.Column(db.String(50), primary_key=True, info={"label": "User"})
    full_name = db.Column(db.String(50), info={"label": "Name"})
    description = db.Column(db.String(500), info={"label": "description"})
    picture_url = db.Column(db.String(500))
    popularity_index = db.Column(db.String(10))
