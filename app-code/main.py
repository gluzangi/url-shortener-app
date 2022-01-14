from datetime import datetime, timezone

from sqlalchemy.orm import Session
from pydantic import HttpUrl
from fastapi import FastAPI, Depends, Body, HTTPException
from fastapi.responses import RedirectResponse

from .db import get_db_session, ShortenedUrl
from .service import create_short_link


app = FastAPI()

@app.post('/api/v1/shorten')
def get_short_link(
    db: Session = Depends(get_db_session),
    url: HttpUrl = Body(..., embed=True)):

    timestamp = datetime.now().replace(tzinfo=timezone.utc).timestamp()
    short_link = create_short_link(url, timestamp)
    obj = ShortenedUrl(original_url=url, short_link=short_link)
    db.add(obj)
    db.commit()

    return {'short_link': short_link}

@app.get('/api/v1/lookup/{short_link}')
def redirect(short_link: str, db: Session = Depends(get_db_session)):
    obj = db.query(ShortenedUrl).filter_by(short_link = short_link).first()
    if obj is None:
        raise HTTPException(
            status_code=404,
            detail='The link does not exist, could not redirect.'
        )
    return RedirectResponse(url=obj.original_url)
