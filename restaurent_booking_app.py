from restaurent import Restaurent
from booking import Booking

class RestaurentBookingApp:
    restaurent_list = []
    booking_list = []

    def __init__(self):
        pass

    # search key can be a restaurent name, city, area, food type
    def search_restaurent(self, 
                          search_key = None, 
                          search_value = None):
        restaurent_list = []

        # name search processor
        if search_key == "name":
            for restaurent in RestaurentBookingApp.restaurent_list:
                if restaurent.name == search_value:
                    restaurent_list.append(restaurent)
        elif search_key == "city":
            for restaurent in RestaurentBookingApp.restaurent_list:
                if restaurent.city == search_value:
                    restaurent_list.append(restaurent)
        elif search_key == "area":
            for restaurent in RestaurentBookingApp.restaurent_list:
                if restaurent.city == search_value:
                    restaurent_list.append(restaurent)
        elif search_key == "food_type":
            for restaurent in RestaurentBookingApp.restaurent_list:
                if restaurent.city == search_value:
                    restaurent_list.append(restaurent)
        elif not search_value: 
            print("hi56")
            restaurent_list = RestaurentBookingApp.restaurent_list
        else : 
            ## it is debateable on what to return in case of empty
            print("hi")
            restaurent_list = RestaurentBookingApp.restaurent_list

        if not search_value : 
            restaurent_list = RestaurentBookingApp.restaurent_list

        return restaurent_list

    def add_restaurent_slots(self, name, slot): 
        for restaurent in RestaurentBookingApp.restaurent_list:
                if restaurent.name == name:
                    restaurent.slots.append(slot)
                    break

    def get_restaurent(self, name): 
        for restaurent in RestaurentBookingApp.restaurent_list:
                if restaurent.name == name:
                    return restaurent

    def register_restaurent(self, name, city, area, food_type):
        new_restaurent = Restaurent(name, city, area, food_type)
        RestaurentBookingApp.restaurent_list.append(new_restaurent)

    def book_table(self, user_name, restaurent_name, date, start_time, member_count):
        for restaurent in RestaurentBookingApp.restaurent_list:
                if restaurent.name == restaurent_name:
                    booked = restaurent.book_table(date, start_time, member_count)
                    if booked : 
                        new_booking = Booking(user_name, restaurent_name, date, start_time, member_count)
                        RestaurentBookingApp.booking_list.append(new_booking)
                    return booked
        return False
