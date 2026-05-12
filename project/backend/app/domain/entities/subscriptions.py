from pydantic import BaseModel, EmailStr
import datetime

class ResponseSubscriptionsDTO(BaseModel):
    id: int
    email: EmailStr
    name: str
    location: str
    budget: int
    subject: str
    message: str
    created_at: datetime.datetime

class CreateSubscriptionsDTO(ResponseSubscriptionsDTO):
    pass

