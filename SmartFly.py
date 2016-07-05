import json, requests

def qpxExpressKey():
    key = __file__.replace('SmartFly.py','') + 'API_Keys/qpxExpress.key'
    return open(key).read()

def Flight_Data(params):
    api_key = qpxExpressKey()
    url = "https://www.googleapis.com/qpxExpress/v1/trips/search?key="
    url += api_key; headers = {'content-type': 'application/json'}
    response = requests.post(url, data=json.dumps(params), headers=headers)
    return response.json()

if __name__ == '__main__':
    # For example: a flight from NYC to China.
    params = {
      "request": {
        "passengers": {
          "kind": "qpxexpress#passengerCounts",
          "adultCount": 1,
          "childCount": 0,
          "infantInLapCount": 0,
          "infantInSeatCount": 0,
          "seniorCount": 0
        },
        "slice": [
          {
            "kind": "qpxexpress#sliceInput",
            "origin": 'JFK',
            "destination": 'PEK',
            "date": '2016-07-30',
            "maxStops": None,
            "maxConnectionDuration": None,
            "preferredCabin": None,
            "permittedDepartureTime": {
              "kind": "qpxexpress#timeOfDayRange",
              "earliestTime": None,
              "latestTime": None
            },
            "permittedCarrier": [
              None
            ],
            "alliance": None,
            "prohibitedCarrier": [
              None
            ]
          }
        ],
        "maxPrice": None,
        "saleCountry": 'US',
        "refundable": None,
        "solutions": 10
      }
    }
    print Flight_Data(params)
