#!/usr/bin/python3
import requests

if __name__ == "__main__":
    # Fetch the URL
    r = requests.get("https://alu-intranet.hbtn.io/status")

    # Print the body response in the specified format
    print("Body response:")
    print(f"\t- type: {type(r.text)}")
    print(f"\t- content: {r.text}")
