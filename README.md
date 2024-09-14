<p align="center">
    <img alt="alt_text" width="40px" src="favicon.ico" />  eDataPOle - Business Connect  https://edatapole.com/
</p>

# Code sample to extract Sec (EDGAR) 10-K, 3, 4, 5 , 8-K, 13f Form Filing and convert to csv format.

- **Form 10-K** is a comprehensive report filed annually by a publicly traded company about its financial performance.
- **Form 13F** is a quarterly report that is required to be filed by all institutional investment managers with at least $100 million in assets under management. It discloses their equity holdings and can provide insights into what the smart money is doing in the market.
- **Form 8-K** is a report of unscheduled material events or corporate changes at a company that could be of importance to the shareholders. Also known as a Form 8K, the report notifies the public of events, including acquisitions, bankruptcy, the resignation of directors, or changes in the fiscal year.
- **Form 3** is an Initial Statement of Beneficial Ownership of Securities.
- **Form 4** is a Statement of Changes in Beneficial Ownership .
- **Form 5** is an Annual Statement of Changes in Beneficial Ownership of Securities .

````
Call with curl:
```curl
curl -v "http://edatapole.com/api/messages/sec/edgar_extract?ticker=AMD&months_back=2&forms=10-K&sections=1A&api_key=YOUR_API_KEY"
````

**Or just click the link to call EDGAR FILING extract REST API**

[http://edatapole.com/api/messages/sec/edgar_extract?ticker=AMD&months_back=2&forms=10-K&sections=1A&api_key=YOUR_API_KEY](http://edatapole.com/api/messages/sec/edgar_extract?ticker=AMD&months_back=2&forms=10-K&sections=1A&api_key=YOUR_API_KEY)

**Mapping ticker to cik**

[http://edatapole.com/api/messages/sec/edgar_get_cmp?ticker=MMM&api_key=YOUR_API_KEY](http://edatapole.com/api/sec/messages/edgar_get_cmp?ticker=MMM&api_key=YOUR_API_KEY)

**Mapping cik to ticker**

[http://edatapole.com/api/messages/sec/edgar_get_cmp?cik=66740&api_key=YOUR_API_KEY](http://edatapole.com/api/messages/sec/edgar_get_cmp?cik=66740&api_key=YOUR_API_KEY)

**To run Python sample**

1. **Get API CODE** - [sign-up](https://edatapole.com/profile) in www.eDataPole.com. **_Subscription is free_** and does not requred credit card information
2. download extract-sec-edgar-filing project and place your token access.

```python
    # replace with your API CODE.
    # You can find access code on
    # https://www.eDataPole.com/profile paqe.
    # or you can use a temporary demo api key is expiring on 9/15/2024
    # api_key="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE3MjExMzc2MDcsImV4cCI6MTcyNjMyMTYwNywic3ViIjoiREVNTyJ9._ckRMgdDQL0wMjDwNmS4yHmwuoRd8U9uu7T7NDGg-Ow"
```

3. run
   python extract-sec-edgar-filing-sample.py

Sample code below shows REST API request parameters usage and handling the response.

```python
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
    forms = "10-K"  # comma separated list of forms. Available forms are  10-K,3,4,5,8-K,13f

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
```
