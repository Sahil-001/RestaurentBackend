# abstract class for booking systems
from abc import ABC, abstractmethod


class AbstractBookingSystem(ABC):

    @abstractmethod
    def search(self, search_key, search_value):
        pass

    @abstractmethod
    def register(self, name, city, area, food_type):
        pass

    @abstractmethod
    def book(self, user_name, name, date, start_time, member_count):
        pass

    @abstractmethod
    def get(self, name):
        pass