#!/usr/bin/python3
import requests


"""
This script fetches the status from the URL https://alu-intranet.hbtn.io/status
and prints the response's type and content in a specific format.

Usage:
    ./4-hbtn_status.py

Dependencies:
    - requests: To make an HTTP GET request to the URL.

Output:
    - type: The type of the response body (should be <class 'str'>).
    - content: The content of the response body (should be 'OK').
"""

if __name__ == "__main__":
    # Fetch the URL
    r = requests.get("https://alu-intranet.hbtn.io/status")

    # Print the body response in the specified format
    print("Body response:")
    print(f"\t- type: {type(r.text)}")
    print(f"\t- content: {r.text}")
