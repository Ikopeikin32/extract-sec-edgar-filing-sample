"""Module providing a function making  call eDataPole REST API."""

import http.client
import json
import urllib.parse


RSP_STATUS = "response_status"
RSP_REASON = "response_reason"


class edgar_data_request:
    def __init__(self, host="edatapole.com", port=80):
        self.host = host
        self.port = port

    def extract_edgar_forms_by_cik(
        self, access_token, cik, months_back, forms, sections=None
    ):
        """This is a function to extract EDGAR SEC forms by specified CIK"""
        try:

            conn = http.client.HTTPConnection(self.host, self.port)
            # pass access token with header
            # headers = { 'authorization': "Bearer "+ access_token}
            # Connect to the host
            conn.connect()
            query = {
                "cik": cik,
                "months_back": months_back,
                "sections": sections,
                "forms": forms,
                "api_key": access_token,
            }
            params = "/api/messages/sec/edgar_extract?" + urllib.parse.urlencode(query)

            print(params)
            conn.request("GET", params)
            response = conn.getresponse()
            data = response.read()
            # Close the connection to the server.
        except Exception as e:
            print(e)
            error = {
                RESPONSE_STATUS: 999,
                RESPONSE_REASON: e,
            }
            return error
        finally:
            conn.close()
        entity_list = json.loads(data)
        return entity_list

    def extract_edgar_forms_by_ticker(
        self,
        access_token,
        ticker,
        months_back,
        forms,
        sections=None,
    ):
        """This is a function to extract EDGAR SEC forms by specified ticker"""
        try:
            conn = http.client.HTTPConnection(self.host, self.port)
            # pass access token with header
            # headers = { 'authorization': "Bearer "+ access_token}
            # Connect to the host
            conn.connect()
            query = {
                "ticker": ticker,
                "months_back": months_back,
                "sections": sections,
                "forms": forms,
                "api_key": access_token,
            }
            params = "/api/messages/sec/edgar_extract?" + urllib.parse.urlencode(query)
            print(params)
            conn.request("GET", params)  # , headers=headers)
            response = conn.getresponse()
            data = response.read()
            # Close the connection to the server.
        except Exception as e:
            print(e)
            error = {
                RESPONSE_STATUS: 999,
                RESPONSE_REASON: e,
            }
            return error
        finally:
            conn.close()
        entity_list = json.loads(data)
        return entity_list
