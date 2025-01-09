from datetime import datetime
from typing import Optional
from pydantic import BaseModel,ConfigDict


class WordCreate(BaseModel):
    word: Optional[str] = None
    meaning: Optional[str] = None
    example_sentence: Optional[str] = None
    #full_name: Optional[str] = None
    is_enabled: Optional[bool] = None

class WordUpdate(BaseModel):
    word: Optional[str] = None
    meaning: Optional[str] = None
    example_sentence: Optional[str] = None
    #ull_name: Optional[str] = None
    is_enabled: Optional[bool] = None

class WordResponse(BaseModel):
    id: int
    word: Optional[str] = None
    meaning: Optional[str] = None
    example_sentence: Optional[str] = None
    #full_name: Optional[str] = None
    is_enabled: Optional[bool] = None
    created_at: datetime
    updated_at: datetime

    #class Config:
    #    orm_mode = True
    model_config = ConfigDict(from_attributes=True)