'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
// SmartFly                                                        //
// Authored by Christopher Iliffe Sprague                          //
// Christopher.Iliffe.Sprague@gmail.com                            //
// +1 703 851 6842                                                 //
// https://github.com/CISprague/SmartFly.git                       //
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import json, requests, datetime
current_time = str(datetime.date.today())

def Flight_Data(adultCount=1, childCount=0, infantInLapCount=0, seniorCount=0,
    infantInSeatCount=0, origin=['JFK'], destination=['PEK'], alliance=[None],
    date=[current_time], maxStops=[None], maxConnectionDuration=[None],
    preferredCabin=[None], permittedCarrier=[[None]], latestTime=[None],
    prohibitedCarrier=[[None]], earliestTime=[None], maxPrice=None,
    saleCountry='US', refundable=None, solutions=20):

    def qpxExpressKey():
        return open(__file__.replace('SmartFly.py', 'API_Keys/qpxExpress.key')
        ).read()

    def params(adultCount=1, childCount=0, infantInLapCount=0, seniorCount=0,
        infantInSeatCount=0, origin=['JFK'], destination=['PEK'], maxPrice=None,
        alliance=[None], date=[current_time], maxStops=[None], refundable=None,
        maxConnectionDuration=[None], preferredCabin=[None], latestTime=[None],
        permittedCarrier=[[None]], prohibitedCarrier=[[None]], saleCountry='US',
        earliestTime=[None], solutions=20):
        param_dict = locals(); mk = 'request'; params = {mk: {}}

        def passengers(adultCount=1, childCount=0, infantInLapCount=0,
            seniorCount=0, infantInSeatCount=0, kind='qpxexpress#passengerCounts'):
            return locals()

        def slice(origin=['JFK'], destination=['PEK'], date=[current_time],
            maxStops=[None], maxConnectionDuration=[None], alliance=[None],
            preferredCabin=[None], permittedCarrier=[[None]], latestTime=[None],
            prohibitedCarrier=[[None]], earliestTime=[None]):
            slice_dict = locals(); slice = []

            def slice_item(origin='JFK', destination='PEK', date=current_time,
                maxStops=None, maxConnectionDuration=None, preferredCabin=None,
                permittedCarrier=[None], alliance=None, latestTime=None,
                prohibitedCarrier=[None], earliestTime=None,
                kind='qpxexpress#sliceInput'):
                slice_dict = locals()

                def permittedDepartureTime(earliestTime=None, latestTime=None,
                    kind='qpxexpress#timeOfDayRange'):
                    return locals()

                slice_dict[permittedDepartureTime.__name__] = (
                permittedDepartureTime(*[slice_dict.pop(arg) for arg in
                permittedDepartureTime.__code__.co_varnames[:-1]]))
                return slice_dict

            for trip in range(len(origin)):
                slice.append(slice_item(**dict([(arg[0], arg[1][trip]) for arg
                in slice_dict.items()])))
            return slice

        for funct in [passengers, slice]:
            params[mk][funct.__name__] = funct(
            **{arg: param_dict.pop(arg) for arg in funct.__code__.co_varnames
            if param_dict.has_key(arg)}); params[mk].update(param_dict)
        return params

    api_key = qpxExpressKey()
    url = "https://www.googleapis.com/qpxExpress/v1/trips/search?key="
    url += api_key; headers = {'content-type': 'application/json'}
    response = requests.post(url, data=json.dumps(params()), headers=headers)
    return response.json()

if __name__ == '__main__':
    print Flight_Data()
