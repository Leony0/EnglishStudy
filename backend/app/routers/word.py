from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session, joinedload

from app.database.database import get_db
from app.models.sqlalchemy.word import Word as DBWord
from app.models.pydantic.word import WordCreate, WordResponse, WordUpdate

router = APIRouter()



@router.post("/word/", response_model=WordResponse)
async def create_word(word: WordCreate, db: Session = Depends(get_db)):
    db_word = DBWord(**word.dict())
    db.add(db_word)
    db.commit()
    db.refresh(db_word)
    return db_word

# (省略)

@router.get("/word/all/")
def read_word_all(db: Session = Depends(get_db)):
    try:
        words_data = db.query(DBWord).all()
        results = [
            {
                "id": word.id,
                "word": word.word,
                "meaning": word.meaning,
                "example_sentence": word.example_sentence,
                #"full_name": word.full_name,
                "is_enabled": word.is_enabled,
                "created_at": word.created_at.isoformat() if word.created_at else None,
                "updated_at": word.updated_at.isoformat() if word.updated_at else None,
            }
            for word in words_data
        ]
        return JSONResponse(content=results)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/word/{word_id}", response_model=WordResponse)
def read_word_by_id(word_id: int, db: Session = Depends(get_db)):
    db_word = db.query(DBWord).filter(DBWord.id == word_id).first()
    if db_word is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Word not found")
    return db_word


@router.put("/word/{word_id}", response_model=WordResponse)
async def update_word(word_id: int, word_update: WordUpdate, db: Session = Depends(get_db)):
    try:
        db_word = db.query(DBWord).filter(DBWord.id == word_id).first()
        if db_word is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Word not found")

        for key, value in word_update.dict(exclude_unset=True).items():
            setattr(db_word, key, value)

        db.commit()
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)) from e
    finally:
        db.refresh(db_word)
        return db_word


@router.delete("/word/{word_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_word(word_id: int, db: Session = Depends(get_db)):
    db_word = db.query(DBWord).filter(DBWord.id == word_id).first()
    if db_word is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="word not found")

    db.delete(db_word)
    db.commit()
