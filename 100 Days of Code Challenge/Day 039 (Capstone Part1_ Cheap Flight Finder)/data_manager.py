from pprint import pprint
import requests
import config

SHEETY_PRICES_ENDPOINT = F'https://api.sheety.co/{config.SHEETY_PRICES_API}/flightDeals/prices'


class DataManager:
    """This class is responsible for talking to the Google Sheet."""
    def __init__(self):
        """This method is called when you create a new DataManager object."""
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)


