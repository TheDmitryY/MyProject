from typing import List, Optional
import datetime
import uuid

from sqlalchemy import String, Text, ForeignKey, DateTime, func, UUID, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.configs.database import Base

class Subscriptions(Base):
    __tablename__ = "subscriptions"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email: Mapped[str] = mapped_column(String, unique=True, index=True, nullable=False)
    name: Mapped[Optional[str]] = mapped_column(String, unique=True)
    location: Mapped[str] = mapped_column(String, index=True)
    budget: Mapped[int] = mapped_column(Integer, nullable=False)
    subject: Mapped[str] = mapped_column(String)
    message: Mapped[str] = mapped_column(String)
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())