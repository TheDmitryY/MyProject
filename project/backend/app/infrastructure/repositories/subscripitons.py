from app.domain.interfaces.subscriptions import SubscriptionsRepository
from app.infrastructure.entity.subscriptions import Subscriptions
from app.domain.entities.subscriptions import ResponseSubscriptionsDTO, CreateSubscriptionsDTO
import datetime
from sqlalchemy import select,delete, update
from sqlalchemy.ext.asyncio import AsyncSession


class PostgresRepository(SubscriptionsRepository):
    def __init__(self, session: AsyncSession):
        self.session = session
    
    async def get(self, skip: int, limit: int) -> list[ResponseSubscriptionsDTO]:
        query = (
            select(Subscriptions)
            .limit(limit)
            .offset(skip)
        )
        result = await self.session.execute(query)
        return result.scalars.all()

    async def delete(self,id: int):
        query = delete(Subscriptions).where(Subscriptions.id == id)
        await self.session.execute(query)
        await self.session.commit()
    
    async def create(
        self,
        email: str,
        name: str,
        location: str,
        budget: str,
        subject: str,
        message: str,
        created_at: datetime.datetime
    ) -> ResponseSubscriptionsDTO:
        subscriptions_model = Subscriptions(
            email=email,
            name=name,
            location=location,
            budget=budget,
            subject=subject,
            message=message,
            created_at=created_at
        )
        self.session.add(subscriptions_model)
        await self.session.flush()
        await self.session.refresh(subscriptions_model)
        await self.session.commit()
        return self._map_to_domain(subscriptions_model)
        

    async def putch(self, subscriptions: ResponseSubscriptionsDTO):
        stmt = update(Subscriptions).where(Subscriptions.id == subscriptions.id).values(
            **subscriptions.model_dump(exclude={"id"}, exclude_unset=True).returning(Subscriptions)
        )
        result = await self.session.execute(stmt)
        updated_model = result.scalar_one()
        await self.session.commit()
        return self._map_to_domain(updated_model)


    def _map_to_domain(self, model: Subscriptions) -> ResponseSubscriptionsDTO:
        return ResponseSubscriptionsDTO(
            id=model.id,
            email=model.email,
            name=model.name,
            location=model.location,
            budget=model.budget,
            subject=model.subject,
            message=model.message,
            created_at=model.created_at
        )

