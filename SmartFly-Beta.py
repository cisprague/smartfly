'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
// SmartFly                                                        //
// Authored by Christopher Iliffe Sprague                          //
// Christopher.Iliffe.Sprague@gmail.com                            //
// +1 703 851 6842                                                 //
// https://github.com/CISprague/SmartFly.git                       //
// Implementation using SkyScanner API                             //
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

import skyscanner.skyscanner as ss
Key = open(__file__.replace('SmartFly-Beta.py', 'SkyScanner.key')).read().strip()

class Trip(object):

    def __init__(self, key, org, dest, outd, ind, pos='UK', cur='USD', lang='en-GB', ads=1):
        [setattr(self, attr, eval(attr)) for attr in self.__init__.__code__.co_varnames]

    def Live_Price(self):
        flights_service = ss.Flights(self.key)
        result = flights_service.get_result(
            country=self.pos,
            currency=self.cur,
            locale=self.lang,
            originplace=self.org,
            destinationplace=self.dest,
            outbounddate=self.outd,
            inbounddate=self.ind,
            adults=self.ads
        ).parsed
        return result

if __name__ == '__main__':
    Winter = Trip(Key, 'NYCA-sky', 'DEL-sky', '2016-12-20', '2017-01-14')
    print(Winter.Live_Price())
