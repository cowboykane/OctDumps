from abc import ABC, abstractmethod

class BaseScreen(ABC):
    @abstractmethod
    def render(self):
        pass

    @abstractmethod
    def handle_input(self, user_input: str):
        pass