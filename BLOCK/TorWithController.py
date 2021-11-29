import requests
from stem import Signal
from stem.control import Controller


def get_new_connection():

    with Controller.from_port(port=9051) as controller:
        controller.authenticate(password="pass")
        controller.signal(Signal.NEWNYM)


def get_tor_session():

    session = requests.session()
    session.proxies = {'http':  'socks5://127.0.0.1:9050',
                       'https': 'socks5://127.0.0.1:9050'}
    return session


session = get_tor_session()
print(session.get("http://httpbin.org/ip").text)
print(requests.get("http://httpbin.org/ip").text)
get_new_connection()
session = get_tor_session()
print(session.get("http://httpbin.org/ip").text)
