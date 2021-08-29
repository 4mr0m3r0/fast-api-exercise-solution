from typing import Optional
from fastapi import Depends
from pydantic import BaseModel
import fastapi

from model.validation_error import ValidationError
from services import openweather_service

router = fastapi.APIRouter()


class Location(BaseModel):
    city: str
    state: Optional[str] = None
    country: str = 'US'


@router.get('/api/weather/{city}', name='weather')
async def index(location: Location = Depends(), units: Optional[str] = 'metrics'):
    try:
        return await openweather_service.get_report_async(
            city=location.city,
            state=location.state,
            country=location.country,
            units=units
        )
    except ValidationError as failure:
        return fastapi.Response(content=failure.error_msg, status_code=failure.status_code)

