import helpers.response as content
import json
from json.decoder import JSONDecodeError
import sys


class Pre(content.Data):

    def __init__(self):
        content.Data.__init__(self)
        self.pre_processed = None

    def transform_response_body_to_a_python_data_structure_for_further_processing(self, operation):
        """(binary string) -> list
        Transforms the response body of the request into a python data structure to be used for further processing.
        :param operation: '/sources'
        :return: [{'uuid': 'af5aec2c-223f-498a-9640-c8c3d36b913f',
        'name': 'BGS datasets and services Metadata for SSDI',
        'label': {}}, {'uuid': '413548c4-fbd3-4e40-9908-e88cbf82fcee',
        'name': 'dummy', 'label': {}},
        {'uuid': '0c65841d-256e-410c-98d8-d76c00d76cbb', 'name': 'dummy', 'label': {}},
        {'uuid': '55832271-1e0a-4f09-b0a0-1e728bd061ad', 'name': 'dummy', 'label': {}},
        {'uuid': 'f3b136b8-ef21-4eec-99e0-59139b2ff653', 'name': 'Dundee', 'label': {}},
        {'uuid': '48e84e1c-d7ac-4c19-a03f-2689dc991a51', 'name': 'Scottish SDI', 'label': {}}]
        """

        # Get the content using the get method from the content module
        self.get(operation)

        # Load the data into a python data structure which can be used further for post processing
        if self.response['response_code'] == 200:
            response_body = self.response['response_body']
            response_headers = self.response['response_headers']
            try:
                self.pre_processed = json.loads(response_body.decode('utf-8'))
            except JSONDecodeError as e:
                print("JSON decoding error when trying to create a python data structure using content: %s"
                      % response_body)
                print("Specific error is - %s" % e)
                print("Response headers were %s" % response_headers)
                sys.exit(1)
            else:
                self.pre_processed = [self.response]
        else:
            self.pre_processed = [self.response]

        return self.pre_processed


class Post:

    def __init__(self):
        self.post_processed = None