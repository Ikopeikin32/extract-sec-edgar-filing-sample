"""Module providing a function making  call eDataPole REST API."""

import sys
from edgar_data_collector import *
from edgar_data_request import *


if __name__ == "__main__":
    # replace with your access code.
    # You can find access code on https://www.eDataPole.com/profile paqe.
    # this is a demo key with expiration on 9/15/24
    api_key = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE3MjExNTIzNzQsImV4cCI6MTcyNjMzNjM3NCwic3ViIjoiYXV0aDB8NjY3YWEwMTQ1YjdiMmVkZjdmODc2ZTQ4In0.-wmcTCwYaT-0oWUdXUdU-1eT01qCXZzLx6dOnLKkYks"

    # keywords = "3M also makes [a-z]* free of charge through its website,3M expended approximately $316,PFAS manufacturing"
    keywords = None  # used only for 10-K
    ticker = "AMD"
    months_back = 12
    sections = "1A,7A"  # used only for 10-K
    forms = "10-K"  # available forms - "10-K,3,4,5,8-K,13f

    dr = edgar_data_request()

    json_response = dr.extract_edgar_forms_by_ticker(
        api_key, ticker, months_back, forms, sections
    )

    print(json_response)
    if json_response[RSP_STATUS] != 200:
        print("Exception fetching data")
        print(json_response[RSP_STATUS], json_response[RSP_REASON])
        sys.exit()
    # if request is successful
    data = edgar_data_collector()
    data.response_to_pd(json_response)
    # extract to csv files
    data.to_csv()
