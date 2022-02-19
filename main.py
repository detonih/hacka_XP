from urllib import response
from get_token import GetToken
from make_requests import MakeRequests

class Main:
    def __init__(self, client_id, client_secret):
      self.credentials = {
        'client_id': client_id,
        'client_secret': client_secret
      }
      self.token = GetToken(
        self.credentials["client_id"],
        self.credentials["client_secret"]
        ).access_token
      self.requests = MakeRequests(self.token, self.credentials)

      response = self.requests.try_request(self.requests.users, 1)
      print(response.text)


if __name__ == "__main__":
    Main(
      "",
      ""
    )