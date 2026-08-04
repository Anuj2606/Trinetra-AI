from abc import ABC, abstractmethod
from typing import Any, Dict


class BaseProvider(ABC):
    """
    Base class that every provider must inherit.
    """

    @abstractmethod
    async def analyze(self, url: str) -> Dict[str, Any]:
        """
        Analyze the given URL and return a standardized dictionary.
        """
        pass