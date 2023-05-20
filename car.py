from abc import ABC, abstractmethod


class Car(ABC):
    def __init__(self, Battery, engine):
        self.Battery = Battery
        self.engine = engine

    @abstractmethod
    def needs_service(self):
        return self.engine.needs_service() or self.Battery.needs_service()
