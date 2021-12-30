import hashlib
import json
import jwt
import logging
import requests
import uuid

from urllib.parse import urlencode

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)
logger.addHandler(stream_handler)


class UpbitClient:

    def __init__(self, filepath=None):
        if filepath is None:
            self.keys = self.load_upbit_keys_json()
        else:
            self.keys = self.load_upbit_keys_json(filepath)

        self.access_key = self.keys["Access key"]
        self.secret_key = self.keys["Secret key"]
        self.server_url = self.keys["Server url"]
        self.fear_greed_url = self.keys["FearGreed url"]

    def load_upbit_keys_json(self, filepath="../../resource/upbit_config.json"):
        with open(filepath, "r") as fd:
            keys = json.load(fd)

        logger.info(keys)

        return keys

    def create_authorization_token(self, access_key=None, secret_key=None, nonce=None, query=None, query_hash_alg="SHA512"):
        if access_key is None:
            access_key = self.access_key

        if secret_key is None:
            secret_key = self.secret_key

        if nonce is None:
            nonce = uuid.uuid4()

        payload = {
            "access_key": access_key,
            "nonce": str(nonce)
        }

        if query is not None:
            query_string = urlencode(query).encode()
            m = hashlib.sha512()
            m.update(query_string)
            query_hash = m.hexdigest()
            payload["query_hash"] = query_hash
            payload["query_hash_alg"] = query_hash_alg

        jwt_token = jwt.encode(payload, secret_key)
        authorization_token = "Bearer {}".format(jwt_token)

        logger.info(authorization_token)

        return authorization_token


    def get_accounts(self, access_key=None, secret_key=None, server_url=None):
        if access_key is None:
            access_key = self.access_key
        if secret_key is None:
            secret_key = self.secret_key
        if server_url is None:
            server_url = self.server_url

        this_uuid = uuid.uuid4()

        authorization_token = self.create_authorization_token(access_key, secret_key, this_uuid)
        headers = {"Authorization": authorization_token}

        res = requests.get(server_url + "/v1/accounts", headers = headers, stream=True)
        logger.info(res.raw._connection.sock.getsockname())
        logger.info(res.text)

        return json.loads(res.text)


    def get_orders_chance(access_key, secret_key, server_url, code1, code2):
        this_uuid = uuid.uuid4()

        query = {"market": "{}-{}".format(code1, code2).upper()}
        authorization_token = create_authorization_token(access_key, secret_key, this_uuid, query=query)
        headers = {"Authorization": authorization_token}

        res = requests.get(server_url + "/v1/orders/chance", params=query, headers=headers)

        logger.info(res.text)

        return json.loads(res.text)


class FearGreedClient:


    def get_fear_greed_index(url, limit=1, form="json", date_format="world"):
        res = requests.get(url + "/fng/?limit={}&format={}&date_format={}".format(limit, form, date_format))

        logger.info(res.text)

        if form == "json":
            return json.loads(res.text)
    
        return res.text

