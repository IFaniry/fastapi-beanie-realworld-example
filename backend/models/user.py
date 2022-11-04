from typing import Optional, Tuple

from beanie import Document
from beanie.odm.fields import PydanticObjectId


class User(Document):
    username: str
    email: str
    hashed_password: str
    bio: Optional[str] = None
    image: Optional[str] = None
    following_ids: Tuple[PydanticObjectId, ...] = ()
