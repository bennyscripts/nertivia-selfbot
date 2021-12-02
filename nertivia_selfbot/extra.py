__authtoken = ""

class Extra:
    def setauthtoken(token):
        global __authtoken
        __authtoken = token
        
    def getauthtoken():
        return __authtoken