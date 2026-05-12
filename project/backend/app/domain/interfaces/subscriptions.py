from abc import ABC, abstractmethod

class SubscriptionsRepository(ABC):
    @abstractmethod
    async def get(skip: int, limit: int):
        pass

    @abstractmethod
    async def delete():
        pass

    @abstractmethod
    async def putch():
        pass

    @abstractmethod
    async def create():
        pass


