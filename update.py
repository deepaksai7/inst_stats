import pandas as pd
import requests
from pathlib import Path
import csv
from datetime import date
import os

filename="data\{}.csv"
url="https://www.instagram.com/{}/?__a=1"

def update(username,response_json):
    file=filename.format(username)
    fname = Path(file)
    if fname.is_file():
        pass
    else:
       
        fname.touch(exist_ok=True)
        os.chmod(file, 0o777)

    followers=response_json["graphql"]["user"]["edge_followed_by"]["count"]
    following=response_json["graphql"]["user"]["edge_follow"]["count"]
    with open (file, "a", newline = "") as csvfile:
        d = csv.writer(csvfile)
        row=[date.today(),followers,following]
        d.writerow(row)
        
if __name__=="__main__":
    username=input("Enter a username")
    u=url.format(username)
    response = requests.get(u)
    response_json=response.json()
    if not response_json:
        print("check the username again")
    else:
        update(username,response_json)

