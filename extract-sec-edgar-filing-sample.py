"""Module providing a function making  call eDataPole REST API."""

import http.client
import sys
import json
import urllib.parse

RSP_STATUS = "response_status"
RSP_REASON = "response_reason"


def extract_edgar_forms_txt(host, port, api_key, ticker, years_back, sections):
    """Extract  text section from 10-K SEC filing"""
    try:

        conn = http.client.HTTPConnection(host, port)
        # Connect to host
        conn.connect()

        query = {
            "ticker": ticker,
            "years_back": years_back,
            "sections": sections,
            "api_key": api_key,
        }
        params = "/api/messages/edgar_extract?" + urllib.parse.urlencode(query)
        print(params)
        # This will send a request to the server using the HTTP request
        # GET method /api/messages/edgar_extract?tiker=...&years_back=...&sections=...&apy_key=...
        conn.request("GET", params)
        response = conn.getresponse()
        data = response.read()
        entity_list = json.loads(data)
        entity_list[RSP_STATUS] = response.status
        entity_list[RSP_REASON] = response.reason
        return entity_list
    except Exception as e:
        print(e)
        error = {
            RSP_STATUS: 999,
            RSP_REASON: e,
        }
        return error
    finally:
        # Close the connection to the server.
        conn.close()


if __name__ == "__main__":
    # replace with your access code.
    # You can find access code on https://www.eDataPole.com/profile paqe.
    # this is a demo key with expiration on 9/15/24
    api_key = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE3MjExMzc2MDcsImV4cCI6MTcyNjMyMTYwNywic3ViIjoiREVNTyJ9._ckRMgdDQL0wMjDwNmS4yHmwuoRd8U9uu7T7NDGg-Ow"
    host = "edatapole.com"
    port = 80
    # host = "127.0.0.1"
    # port = 6060
    ticker = "MMM"
    years_back = 2
    sections = "1,1A,7A"
    json_response = extract_edgar_forms_txt(
        host, port, api_key, ticker, years_back, sections
    )

    print(json_response)
    if json_response[RSP_STATUS] != 200:
        print("Exception fetching data")
        print(json_response[RSP_STATUS], json_response[RSP_REASON])
        sys.exit()
    # if request is successful
    if "list" in json_response:
        entities = json_response["list"]
        print("-----------------Returned entities-------------")
        for entity in entities:
            print("------ Company Information----------")

            print(
                entity["cik"],
                entity["cmp_name"],
                entity["sic"],
                entity["updated"],
                entity["full_10k_url"],
                entity["accession_number"],
            )
            print(f"------ Extracted Sessions {sections} -----------")
            print(entity["data"])
