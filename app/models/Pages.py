from app.db import db
from app.libs.date_utils import utcnow


class Page(db.Model):
    __tablename__ = "pages"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True)
    description = db.Column(db.String(255))
    layout = db.Column(db.Text)
    fragments = db.relationship("Fragment", secondary="page_fragment")

    def __str__(self):
        return self.name


# Text paragraphs
class Fragment(db.Model):
    __tablename__ = "fragments"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True)
    content = db.Column(db.Text, nullable=False)
    pages = db.relationship("Page", secondary="page_fragment")

    def __str__(self):
        return self.name


# img, video etc
# Should be uploaded from admin ui
class Asset(db.Model):
    __tablename__ = "assets"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True)
    file_path = db.Column(db.String(80), nullable=False)
    file_type = db.Column(db.String(10), nullable=False)

    def __str__(self):
        return self.name


class PageFragment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    page_id = db.Column(db.Integer, db.ForeignKey("pages.id"), nullable=False)
    fragment_id = db.Column(db.Integer, db.ForeignKey("fragments.id"), nullable=False)


class PageAsset(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    page_id = db.Column(db.Integer, db.ForeignKey("pages.id"), nullable=False)
    asset_id = db.Column(db.Integer, db.ForeignKey("assets.id"), nullable=False)
