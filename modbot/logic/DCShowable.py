# from abc import ABC, abstractmethod
import abc

class DCShowable(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def dc_show(self):
        """Returns a string that can be displayed on discord channel"""
        pass

