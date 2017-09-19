__doc__='''Provides simple functions to interact with the Catalogue Service for the Web (CSW)'''\
         +''' SSDI is supported by GeoNetwork and which ever services are applicable to GeoNetwork'''\
         +''' can also be used to support the SSDI.'''

try:
    import requests
except ImportError,e:
    print 'Install requests before using this software'
else:
    import requests

try:
    import xmltodict
except ImportError,e:
    print 'Install xmltodict before using this software'
    sys.exit()
else:
    import xmltodict

def geonetwork_service_url():
    '''
    Returns the web service URL endpoint for requesting data from SSDI.
    SSDI is supported from GeoNetwork and the URL returned by this function
    can be used to request a response from GeoNetwork.
    >>>geonetwork_service_url()
    https://www.spatialdata.gov.scot/geonetwork/srv/eng/csw?
    '''

    return 'https://www.spatialdata.gov.scot/geonetwork/srv/eng/csw?'

def geonetwork_service_request_and_parameters(url):
    '''(str)-> str
    Returns a concantenation of the web service URL endpoint and the URL parameters
    needed to request a response from GeoNetwork.
    >>>geonetwork_service_request_and_parameters('https://www.spatialdata.gov.scot/geonetwork/srv/eng/csw?')
    'https://www.spatialdata.gov.scot/geonetwork/srv/eng/csw?request=GetRecords
    &service=CSW&version=2.0.2&resultType=results&maxRecords=100&constraintLanguage=CQL_TEXT
    &constraint_language_version=1.1.0&constraint=AnyText=%27spatialhub@improvementservice.org.uk%27
    &outputSchema=csw:IsoRecord&typeNames=gmd:MD_Metadata&ElementSetName=full'
    '''

    #The URL contains all the parameters needed to return up to 100 metadata records
    #using the 'CSW' service and the 'GetRecords' operation of that service and limit
    #the records to only the ones containing the text 'spatialhub@improvementservice.org.uk'
    result = '{}'.format(url)\
             +'request=GetRecords'\
             +'&service=CSW'\
             +'&version=2.0.2'\
             +'&resultType=results'\
             +'&maxRecords=100'\
             +'&constraintLanguage=CQL_TEXT'\
             +'&constraint_language_version=1.1.0'\
             +'&constraint=AnyText=%27spatialhub@improvementservice.org.uk%27'\
             +'&outputSchema=csw:IsoRecord'\
             +'&typeNames=gmd:MD_Metadata'\
             +'&ElementSetName=full'

    return result

def geonetwork_service_response(url):
    '''(str)->list
    Returns a list of nested lists which include data for each record
    publishes in SSDI by the spatial hub.
    >>>geonetwork_service_response('https://www.spatialdata.gov.scot/geonetwork/srv/eng/csw?request=GetRecords
    &service=CSW&version=2.0.2&resultType=results&maxRecords=100&constraintLanguage=CQL_TEXT
    &constraint_language_version=1.1.0&constraint=AnyText=%27spatialhub@improvementservice.org.uk%27
    &outputSchema=csw:IsoRecord&typeNames=gmd:MD_Metadata&ElementSetName=full')
    {[u'csw:GetRecordsResponse']{...}
    '''

    server_response=requests.get(url)
    response_data= server_response.text

    return xmltodict.parse(response_data)
