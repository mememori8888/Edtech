# backend/app/models/population.py
from pydantic import BaseModel, Field

class PopulationData(BaseModel):
    country_name: str = Field(..., description="国名")
    country_code: str = Field(..., min_length=2, max_length=3)
    year: int = Field(..., ge=1950, le=2050)
    midyear_population: int = Field(..., ge=0)