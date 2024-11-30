#!/usr/bin/python3
import sys
import requests

# Get the URL from the command line arguments
url = sys.argv[1]

# Send the GET request to the URL
response = requests.get(url)

# Get the value of the X-Request-Id header and print it
print(response.headers.get('X-Request-Id'))
