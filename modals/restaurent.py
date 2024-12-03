from enum import Enum
import uuid

class food_type(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

class Restaurent:
    def __init__(self, name, city, area, food_type):
        self.name = name
        self.restaurent_id = uuid.uuid4() # unique identier to identify the restaurent
        self.city = city
        self.area = area
        self.food_type = food_type
        self.slots = []

    # slots will have start time, end time, date, total table
    def book_table(self, date, start_time, member_count):
        for slot in self.slots:
            if slot.date == date and slot.start_time == start_time: 
                if slot.total_table >= member_count:
                    slot.total_table = slot.total_table - member_count
                    return True
                else :
                    return False
        return False
