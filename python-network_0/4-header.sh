#!/bin/bash
# Sends a GET request with a custom header and displays only the body of the response
curl -s -H "X-HolbertonSchool-User-Id: 98" "$1"
