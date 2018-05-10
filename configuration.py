class Data:

    usr = 'your-user'
    pwd = 'your-password'

    def __init__(self):

        self.root = 'http://34.243.44.38/geonetwork'
        self.api = {'type': 'rest',
                    'entry_point': '%s/srv/api/0.1' % self.root,
                    'request_headers': {'Accept': 'application/json',
                                        "username": self.usr,
                                        "password": self.pwd}}
