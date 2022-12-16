#!/usr/bin/python3
"""displays the value of the X-Request-Id variable found in
the header of the response.
"""


if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import sys

    value = {"email": sys.argv[2]}
    request = urllib.request.Request(
            sys.argv[1], urllib.parse.urlencode().encode("ascii"))
    with urllib.request.urlopen(request) as response:
        head = response.headers.get('X-Request-Id')
        print(response.read().decode('utf-8'))
