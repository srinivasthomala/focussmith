"""Which account is this? Lets the extension show "Connected as you@...".

The API keys only identify a user id, so the email is copied from the verified
sign-in token whenever the dashboard loads (POST /me/sync). It is never taken
from the request body, so a client can't set someone else's address.
"""

from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.auth import get_current_user, get_current_web_claims
from app.database import get_db
from app.db_models import UserSettings

router = APIRouter(prefix="/me", tags=["me"])


class MeResponse(BaseModel):
    email: str | None


@router.get("", response_model=MeResponse)
def get_me(user_id: str = Depends(get_current_user), db: Session = Depends(get_db)) -> MeResponse:
    row = db.get(UserSettings, user_id)
    return MeResponse(email=row.email if row else None)


@router.post("/sync", response_model=MeResponse)
def sync_me(claims: dict = Depends(get_current_web_claims), db: Session = Depends(get_db)) -> MeResponse:
    user_id = claims["sub"]
    email = (claims.get("email") or "").strip()[:320] or None
    row = db.get(UserSettings, user_id)
    if row is None:
        # Same defaults as an unsaved settings row, so nothing changes for the user.
        row = UserSettings(user_id=user_id, blocklist="[]", blocking_mode="focus-only", email=email)
        db.add(row)
        db.commit()
    elif row.email != email:
        row.email = email
        db.commit()
    return MeResponse(email=email)
