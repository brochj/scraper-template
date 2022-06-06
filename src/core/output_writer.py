from abc import ABC, abstractmethod

from src.core.model import Model


class OutputWriter(ABC):
    """Abstract class: An output writer is responsible for receive a model e save it"""

    @abstractmethod
    def save(self, model: Model) -> bool:
        pass
