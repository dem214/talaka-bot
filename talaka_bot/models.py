from uuid import uuid4

from slugify import slugify
from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base, validates

Base = declarative_base()

class Room(Base):
    __tablename__ = 'room'
    id = Column(Integer, primary_key=True)
    uuid = Column(UUID(as_uuid=True), default=uuid4)
    slug = Column(String(30))

    @validates('slug')
    def validate_slug(self, key, slug):
        slugged_slug = slugify(slug)
        if not slug == slugged_slug:
            raise ValueError('not a slug', proposed=slugged_slug)
