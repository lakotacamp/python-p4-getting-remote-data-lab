import requests
import json

# - create a GetRequester class that is able to initialize with a string URL
# - should have a get_response_body method that sends a GET request to the URL passed in on initialization.
# - This method should return the body of the response.
# - should have a load_json method that should use get_response_body to send a request, then return a Python
#   list or dictionary made up of data converted from the response of that request.
class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        URL =  "https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"
        response = requests.get(URL)
        return response.content

    def load_json(self):
        programs_list = []
        programs = json.loads(self.get_response_body())
        for data in programs:
            programs_list.append(data)
        return programs_list