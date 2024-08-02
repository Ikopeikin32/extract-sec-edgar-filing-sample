import pandas as pd
from pandas import json_normalize
import json


class edgar_data_collector:
    def __init__(self):
        self.pds_345 = []
        self.pds_8K = []
        self.pds_10K = []
        self.pds_13f = []
        self.cik = None

    def set_pd(self, item, data):
        tmp = pd.json_normalize(data)
        tmp.insert(0, "term", item["term"])
        tmp.insert(0, "cik", item["cik"])
        tmp.insert(0, "accession_number", item["accession_number"])
        tmp.insert(0, "updated", item["updated"])
        return tmp

    def response_to_pd(self, response):
        for item in response["list"]:
            self.cik = item["cik"]
            self.add_item(item)

    def add_item(self, item):
        form = item["form"]
        match form:
            case "10-K":
                self.pds_10K.append(self.set_pd(item, item["data"]))
            case "3":
                data = json.loads(item["data"])
                self.pds_345.append(self.set_pd(item, data))
                return
            case "4":
                data = json.loads(item["data"])
                self.pds_345.append(self.set_pd(item, data))
            case "5":
                data = json.loads(item["data"])
                self.pds_345.append(self.set_pd(item, data))
            case "8-K":
                data = json.loads(item["data"])
                self.pds_8K.append(self.set_pd(item, data))
            case "13f":
                data = json.loads(item["data"])
                self.pds_13f.append(self.set_pd(item, data))
            case _:
                return

    def to_csv(self):
        if len(self.pds_10K) > 0:
            final_pd = pd.concat(self.pds_10K, ignore_index=True)
            file = f"extract_{self.cik}_10-K.csv"
            final_pd.to_csv(file)
            print(f"10-K extracted to {file} file ")
        if len(self.pds_345) > 0:
            final_pd = pd.concat(self.pds_345, ignore_index=True)
            file = f"extract_{self.cik}_345.csv"
            final_pd.to_csv(file)
            print(f"3,4,5 forms  extracted to {file} file ")
        if len(self.pds_8K) > 0:
            final_pd = pd.concat(self.pds_8K, ignore_index=True)
            file = f"extract_{self.cik}_8-K.csv"
            final_pd.to_csv(file)
            print(f"8 - K form  extracted to {file} file ")
        if len(self.pds_13f) > 0:
            final_pd = pd.concat(self.pds_13f, ignore_index=True)
            file = f"extract_{self.cik}_13f.csv"
            final_pd.to_csv(file)
            print(f"13f form  extracted to {file} file ")
