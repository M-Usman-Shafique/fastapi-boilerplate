from datetime import UTC, datetime

from beanie import Document, Insert, Replace, before_event
from pydantic import Field


class User(Document):
    username: str
    email: str
    password: str

    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(UTC))

    class Settings:
        name = "users"

    @before_event([Insert, Replace])
    def update_timestamp(self):
        self.updated_at = datetime.now(UTC)
