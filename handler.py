from flask import Flask, jsonify, request, make_response
from booking_system.restaurent_booking_app import RestaurentBookingApp
from modals.restaurent_slot import RestaurentSlot
from utils.global_utils import Utils
from flask_cors import CORS

app = Flask(__name__)

# Enable CORS for all routes and origins
CORS(app)

restaurentBookingApp = RestaurentBookingApp()
utils = Utils()

@app.route('/search/restaurent', methods=['GET'])
def search_restaurents():
    key = request.args.get('key')
    value = request.args.get('value')
    restaurent_list = restaurentBookingApp.search(key, value)
    return make_response(utils.restaurent_list_serializer(restaurent_list), 200)

@app.route('/restaurent/<restaurent_name>', methods=['GET'])
def get_restaurent(restaurent_name):
    return make_response(jsonify(restaurentBookingApp.get(restaurent_name)), 200)

@app.route('/register/restaurent', methods=['POST'])
def register_restaurent():
    data = request.get_json()
    name = data.get("name")
    city = data.get("city")
    area = data.get("area")
    food_type = data.get("foodType")
    restaurentBookingApp.register(name, city, area, food_type)
    return make_response(jsonify({"message": "Restaurent got resgistered sucessfully"}), 200)

@app.route('/restaurent/<restaurent_name>/slot', methods=['PUT'])
def add_restaurent_slots(restaurent_name):
    data = request.get_json()
    start_time = data.get("startTime")
    end_time = data.get("endTime")
    date = data.get("date")
    total_table = int(data.get("totalTable"))
    slot = RestaurentSlot(start_time, end_time, date, total_table)
    restaurentBookingApp.add_restaurent_slots(restaurent_name, slot)
    return make_response(jsonify({"message": "Restaurent slot got resgistered sucessfully"}), 200)

@app.route('/restaurent/<restaurent_name>/book', methods=['POST'])
def book_restaurent_table(restaurent_name):
    data = request.get_json()
    user_name = data.get("userName")
    date = data.get("date")
    start_time = data.get("startTime")
    member_count = int(data.get("memberCount"))
    booked = restaurentBookingApp.book(user_name, restaurent_name, date, start_time, member_count)
    if booked : 
        return make_response(jsonify({"message": "Restaurent slot got resgistered sucessfully"}), 200)
    else :
        # seting 500 for now to make distinction from 200, error response will total depend upon on kind of exception
        return make_response(jsonify({"message": "Error occured while booking slot"}), 500)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8001)  # Change port here
