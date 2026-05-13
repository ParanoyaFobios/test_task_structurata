from pydantic import BaseModel, Field, ConfigDict


class PostSchema(BaseModel):
    """Data model for the post."""

    model_config = ConfigDict(populate_by_name=True)

    id: int
    user_id: int = Field(alias="userId")
    title: str
    body: str
