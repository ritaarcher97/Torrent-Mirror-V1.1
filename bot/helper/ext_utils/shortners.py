import urllib
import requests
from bot import SHORTENER, SHORTENER_API
import random
import base64
from urllib.parse import quote


def urlshortnners(theurlis):
    if SHORTENER == "shorte.st":
        return requests.get(
            f'http://api.{SHORTENER}/stxt/{SHORTENER_API}/{theurlis}', verify=False).text

    elif SHORTENER == "linkvertise.com":
        url = quote(base64.b64encode(theurlis.encode("utf-8")))
        linkvertise = [
            f"https://link-to.net/{SHORTENER_API}/{random.random() * 1000}/dynamic?r={url}",
            f"https://up-to-down.net/{SHORTENER_API}/{random.random() * 1000}/dynamic?r={url}",
            f"https://direct-link.net/{SHORTENER_API}/{random.random() * 1000}/dynamic?r={url}",
            f"https://file-link.net/{SHORTENER_API}/{random.random() * 1000}/dynamic?r={url}"]
        tiny_url = requests.get("http://tinyurl.com/api-create.php?" +
                                urllib.parse.urlencode({'url': random.choice(linkvertise)})).text

        # random.choice(linkvertise)
        return tiny_url

    else:
        return requests.get(
            f'https://{SHORTENER}/api?api={SHORTENER_API}&url={theurlis}&format=text', verify=False).text
