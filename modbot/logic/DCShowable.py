from abc import ABC, abstractmethod


class DCShowable(ABC):
    @abstractmethod
    def dc_show(self):
        """Returns a string that can be displayed on discord channel"""
        pass

