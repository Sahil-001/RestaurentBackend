from modals.restaurent import Restaurent
from modals.restaurent_slot import RestaurentSlot
import json

class Utils:
    def __init__(self):
        pass

    # Custom serializer function
    def restaurent_serializer(self, obj):
        if isinstance(obj, Restaurent):
            return {
                "name": obj.name,
                "city": obj.city,
                "area": obj.area,
                "foodType" : obj.food_type,
                "id" : obj.restaurent_id,
                "slots" : [self.slot_serializer(slot) for slot in obj.slots]
            }
        raise TypeError(f"Type {type(obj)} not serializable")
    
    def slot_serializer(self, obj):
        if isinstance(obj, RestaurentSlot):
            return {
                "startTime": obj.start_time,
                "endTime": obj.end_time,
                "date": obj.date,
                "totalTable" : obj.total_table
            }
        raise TypeError(f"Type {type(obj)} not serializable")
    
    def restaurent_list_serializer(self, restaurent_list):
        return [self.restaurent_serializer(restaurent) for restaurent in restaurent_list]