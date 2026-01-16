import requests
import json
import time

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        max_retries = 3
        for attempt in range(max_retries):
            try:
                response = requests.get(self.url)
                return response.content
            except requests.exceptions.ConnectionError:
                if attempt < max_retries - 1:
                    time.sleep(1)  # Wait 1 second before retrying
                else:
                    raise

    def load_json(self):
        response_body = self.get_response_body()
        return json.loads(response_body)