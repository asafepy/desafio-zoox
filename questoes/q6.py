import json
from pprint import pprint


class FindKey:

    def __init__(self, file, value, provider):
        self.file = file
        self.value = value
        self.provider = provider
        self.response = None

    @staticmethod
    def make_response(key=None, provider=None):
        if key and provider:
            return "Chave: {} Provider: {}".format(key, provider)

    def _finditem(self, obj):

        for k, v in obj.items():
            try:
                if isinstance(v, dict):
                    self._finditem(v)
                elif isinstance(v, list):
                    for x in v:
                        self._finditem(x)
                elif v == self.value:
                    return print(FindKey.make_response(k, self.provider))
            except Exception as e:
                continue

    @property
    def get_key(self):
        self.response = self._finditem(self.file[self.provider])


if __name__ == '__main__':

    with open('files/pessoa.json') as f:
        data = json.load(f)

    for provider in ["facebook", "zooxwifi", "bigdata_corp", "additional_data"]:

        find_key = FindKey(data, "08151292709", provider)
        find_key.get_key
