# -*- coding: utf-8 -*-
import logging
from suds.client import Client
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    logging.getLogger('suds.client').setLevel(logging.DEBUG)
    hello_client = Client('http://localhost:8080/testWebService/services/TestQryInfo?wsdl', cache=None)
    result = hello_client.service.qrySex(0)
    print result
