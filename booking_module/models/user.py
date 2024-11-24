from datetime import datetime
from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List
from enum import Enum
from .appointment import Appointment


class AccountStatus(str, Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    SUSPENDED = "suspended"


class FullName(BaseModel):
    first: str
    last: str


class User(BaseModel):
    name: FullName
    email: EmailStr
    date_of_birth: datetime
    hashed_password: str
    appointments: Optional[List[Appointment]] = []
    account_status: AccountStatus = Field(default=AccountStatus.ACTIVE)

    def full_name(self) -> str:
        return f"{self.name['first']} {self.name['last']}"
