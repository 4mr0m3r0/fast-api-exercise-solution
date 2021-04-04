from typing import Optional
from fastapi import Depends
from pydantic import BaseModel
import fastapi
from services import openweather_service

router = fastapi.APIRouter()


class Location(BaseModel):
    city: str
    state: Optional[str] = None
    country: str = 'US'


@router.get('/api/weather/{city}')
async def index(location: Location = Depends(), units: Optional[str] = 'metrics'):
    report = await openweather_service.get_report_async(
        city=location.city,
        state=location.state,
        country=location.country,
        units=units
    )
    return report
