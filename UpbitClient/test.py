import client
import unittest
import uuid

class ClientTest(unittest.TestCase):

    def setUp(self):
        self.client = client.UpbitClient()

    def test_load_upbit_keys_json(self):
        keys = self.client.load_upbit_keys_json()

        self.assertIsNotNone(keys)

    def test_create_authorization_token(self):
        this_uuid = uuid.uuid4()

        query = {
                "market": "KRW-ETH"
        }

        token = self.client.create_authorization_token(nonce=this_uuid, query=query)

        self.assertIsNotNone(token)


class FearGreedClientTest(unittest.TestCase):

    def setUp(self):
        

    def test_get_fear_greed_index(self):
        index = self.client.get_fear_greed_index()

        self.assertIsNotNone(index)


