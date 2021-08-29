from typing import Optional
import httpx
from httpx import Response

from model.validation_error import ValidationError

api_key: Optional[str] = None


async def get_report_async(city: str, state: Optional[str], country: str, units: str) -> dict:
    if state:
        query = f'{city},{state},{country}'
    else:
        query = f'{city},{country}'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={query}&appid={api_key}&units={units}'
    async with httpx.AsyncClient() as client:
        resp: Response = await client.get(url)
        if resp.status_code != 200:
            raise ValidationError(resp.text, status_code=resp.status_code)
        resp.raise_for_status()
        data = resp.json()
        return data
