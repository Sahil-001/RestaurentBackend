# Currently only for data persistence purpose
class Booking:
    def __init__(self, user_name, restaurent_name, date, start_time, member_count):
        self.user_name = user_name
        self.restaurent_name = restaurent_name
        self.date = date
        self.start_time = start_time
        self.member_count = member_count