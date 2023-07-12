from abc import ABC, abstractmethod

class NotificationFactory(ABC):
    @abstractmethod
    def send_notification(self, payload):
        pass