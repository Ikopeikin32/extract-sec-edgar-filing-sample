
<p align="center">
    <img alt="alt_text" width="40px" src="favicon.ico" />  eDataPOle - Business Connect  https://edatapole.com/
</p>

# Code sample to extract Sec (EDGAR) 10-K Form Filing in TXT format.

To run a sample
1. Get access token - [sign-up](https://edatapole.com/profile) in www.eDataPole.com. Subscription is free and does not requred credit card information
2. download extract-sec-edgar-filing-sample.py sample code and place your token access. 

```python
    # replace with your access code.
    # You can find YOUR API KEY on 
    # https://www.eDataPole.com/profile paqe.
    api_key="YOUR API KEY"
```

3. run
   python extract-sec-edgar-filing-sample.py
 
Sample code below shows REST API  request parameters usage and handling the response.

```python
    # replace with your API KEY.
    # You can find access code on https://www.eDataPole.com/profile paqe.
    api_key = "YOU API KEY"
    host = "edatapole.com"
    port = 80
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
```
Same call with curl:
```curl
curl -v "http://edatapole.com/api/messages/edgar_extract?ticker=MMM&years_back=2&sections=1A%2C7A&api_key=YOUR_API_KEY"
```

Below is the response sample:

```python
{
  list: [
    {
      cik: "0000066740",
      cmp_name: "3M CO",
      sic: "3841",
      term: "10-K",
      updated: "2024-02-07 09:25:16-05:00",
      full_10k_url:
        "https://www.sec.gov/Archives/edgar/data/66740/000006674024000016/mmm-20231231.htm",
      accession_number: "0000066740-24-000016",
      data: "Item 1. Business 3M Company was incorporated in 1929 under the laws of the State of Delaware to continue operations begun in 1902. The Company s ticker symbol is MMM. As used herein, the term  3M  or  Company...",
    },
    {
      cik: "0000066740",
      cmp_name: "3M CO",
      sic: "3841",
      term: "10-K",
      updated: "2023-02-08 12:59:49-05:00",
      full_10k_url:
        "https://www.sec.gov/Archives/edgar/data/66740/000006674023000014/mmm-20221231.htm",
      accession_number: "0000066740-23-000014",
      data: "Item 1. Business 3M Capital expenditures for similar projects are presently expected to approach approximately $646 ...",
    },
  ],
  response_status: 200,
  response_reason: "OK",
};
```