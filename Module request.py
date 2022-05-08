"""
The requests module in Python allows you to exchange requests on the web. It is a very useful library that has many
essential methods and features to send HTTP requests. As mentioned earlier, HTTP works as a request-response system
between a server and a client.
"""
import requests
r = requests.get("https://github.com/Raahul252000/python-exercises")   # get() is used to send request to get the data from the server.

print(r.text)
print(r.status_code)