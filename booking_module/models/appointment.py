from datetime import datetime
from enum import Enum
from pydantic import BaseModel, Field
from typing import Optional
from .objectid_utils import ObjectId


# Class Definitions
class AppointmentStatus(str, Enum):
    UPCOMING = "upcoming"
    PASSED = "passed"


class ProviderName(BaseModel):
    first: str
    last: str


class Appointment(BaseModel):
    id: ObjectId = Field(alias="_id")
    user_id: ObjectId
    provider_id: int
    provider_name: ProviderName
    start_datetime: datetime
    status: AppointmentStatus = AppointmentStatus.UPCOMING
    reason: str
    notes: Optional[str] = ""
