from sqlalchemy import Boolean, Column, Integer, String, DateTime, func
#from sqlalchemy.orm import relationship
from app.database.database import Base

class Word(Base):
    __tablename__ = "words"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    word = Column(String(50), nullable=False)
    meaning = Column(String(50), nullable=False)
    example_sentence= Column(String(300), nullable=False)
    #full_name = Column(String(100), unique=True, index=True, nullable=True)
    is_enabled = Column(Boolean, default=True, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)