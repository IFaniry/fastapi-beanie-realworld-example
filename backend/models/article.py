from typing import List, Tuple
from datetime import datetime

from pydantic import Field, BaseModel, root_validator
from beanie import Document, Link
from beanie.odm.fields import PydanticObjectId
from nanoid import generate
from slugify import slugify

from models.user import User


class Comment(BaseModel):
    """Comment embedded model with a unique id field"""

    id: PydanticObjectId = Field(default_factory=generate)
    body: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    authorId: PydanticObjectId

class Article(Document):
    title: str
    slug: str
    description: str
    body: str
    tag_list: List[str] = []
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    author: Link[User]
    favorited_user_ids: Tuple[PydanticObjectId, ...] = ()
    comments: Tuple[Comment, ...] = ()

    @root_validator(pre=True)
    def generate_slug(cls, values):
        if values.get("slug") is not None:
            return values
        title = values.get("title", "")
        values["slug"] = slugify(title)
        # Note on why the tag_list is sorted:
        # https://github.com/gothinkster/realworld/issues/839
        if values.get("tag_list") is not None and isinstance(values["tag_list"], list):
            values["tag_list"].sort()
        return values
