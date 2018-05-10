import configuration
from requests import get, post


class Data(configuration.Data):

    def __init__(self):
        configuration.Data.__init__(self)

        # This object is the response dictionary for each response from the GeoNetwork server and is updated with
        # every method used in this class.
        self.response = {'request_url': None, 'response_body': None, 'response_code': None,
                         'response_headers': None, 'response_time': None}

    def get(self, operation):
        """(str) -> dict
        Returns the request & response data into a dictionary for further processing
        :param operation: '/sources'
        :return: {'request_url': 'http://34.243.44.38/geonetwork/srv/api/0.1/processes/reports',
        'response_body': b'{"message":"AccessDeniedException","code":"runtime_exception","description":"Access is denied"}',
        'response_code': 400,
        'response_headers': {'Server': 'nginx/1.10.3 (Ubuntu)', 'Date': 'Wed, 09 May 2018 12:56:24 GMT',
        'Content-Type': 'application/json', 'Transfer-Encoding': 'chunked', 'Connection': 'keep-alive',
        'X-Frame-Options': 'DENY', 'Content-Security-Policy': "frame-ancestors 'none'",
        'Set-Cookie': 'JSESSIONID=7676EFB16D0FD50F49DF938494DC86E5; Path=/geonetwork/; HttpOnly'},
        'response_time': 0.060855}
        """

        request_url = self.api['entry_point']+operation
        data = get(url=request_url, headers=self.api['request_headers'])
        print(data.content)

        self.response['request_url'] = request_url
        self.response['response_body'] = data.content
        self.response['response_code'] = data.status_code
        self.response['response_headers'] = data.headers
        self.response['response_time'] = data.elapsed.total_seconds()

    def post(self, operation):
        post_data = {}
        self.content = None
