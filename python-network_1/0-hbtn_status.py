#!/usr/bin/python3
"""
Fetches http://0.0.0.0:5050/status and displays information about the response.
"""

import urllib.request

if __name__ == "__main__":
    # You can update the URL here to either the local server or the remote one
    url = "http://0.0.0.0:5050/status"  # Update to the correct URL

    with urllib.request.urlopen(url) as response:
        body = response.read()

    # Display the body response
    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
    print("\t- utf8 content: {}".format(body.decode("utf-8")))
