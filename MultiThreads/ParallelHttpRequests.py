import requests
from requests_futures.sessions import FuturesSession

urls = [
    "http://httpbin.org/ip",
    "http://httpbin.org/xml",
    "http://httpbin.org/json",
    "http://httpbin.org/image",
    "http://httpbin.org/image/png",
    "http://httpbin.org/image/jpg",
    "http://httpbin.org/image/jpeg",
    "http://httpbin.org/headers",
]

with requests.Session() as session:
    list(map(session.get, urls))