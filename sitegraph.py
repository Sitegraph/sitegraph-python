
API_URL = "http://sitegraph.net/api/"
LIBRARY_VERSION = "1.0.0"
API_LIB = "Python " + LIBRARY_VERSION

class Api:
    def __init__(self, api_key):
        self.api_key = api_key
        
    def increment(self, identifier, amount=0):
        pass
    
    def decrement(self, identifier, amount=0):
        pass