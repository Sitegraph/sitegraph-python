import urllib
import urllib2
import json

API_URL = "http://sitegraph.net/api/"
LIBRARY_VERSION = "1.0.0"
API_LIB = "Python " + LIBRARY_VERSION

class SitegraphException(Exception):
    "This is here for a more informative exception, and for possible future use"
    pass

class Api:
    def __init__(self, api_key):
        "Initializes the API by specifying the API key"
        self.api_key = api_key
        
    def increment(self, identifier, amount=1):
        "Increments a given statistic identified by `identifier`"
        data = {
            'authKey' : self.api_key,
            'statistic' : identifier,
            'amount' : amount,
            'api_info' : API_LIB,
        }
        response = self.make_request('increment', data)
        return True
    
    def decrement(self, identifier, amount=1):
        "Decrements a statistic by the given amount"
        data = {
            'authKey' : self.api_key,
            'statistic' : identifier,
            'amount' : amount,
            'api_info' : API_LIB,
        }
        response = self.make_request('decrement', data)
        return True
    
    def create_event(self, description):
        "Creates a new Sitegraph event"
        data = {
            'authKey' : self.api_key,
            'event' : description,
            'api_info' : API_LIB,
        }
        response = self.make_request('event', data)
        return True
    
    def make_request(self, url, data):
        data = urllib.urlencode(data)
        url = "%s%s/" % (API_URL, url)
        
        request = urllib2.Request(url, data)
        response = urllib2.urlopen(request)
        
        response_text = response.read()
        parsed = json.loads(response_text)
        
        try:
            error_message = parsed['error']
            raise SitegraphException(error_message)
        except KeyError:
            return parsed    # Everything is good if there is no error, so return the response