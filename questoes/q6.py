import json
from pprint import pprint


class FindValue:

    def __init__(self, file, value):
        self.file = file
        self.value = value
        self.results = []

    def _finditem(self):
        import pdb; pdb.set_trace()

        for provider in ["facebook", "zooxwifi", "bigdata_corp", "additional_data"]:
            for k, v in self.file[provider].items():
                if isinstance(v, dict):
                    self._finditem(v, value, provider)

                elif v == value:
                    self.results.append(str("Chave:", k, "Provider:", provider))

    @property
    def get_key(self):
        
        self._finditem()
        print(self.results)


if __name__ == '__main__':

    with open('files/pessoa.json') as f:
        data = json.load(f)

    # for value in []:

    find_value = FindValue(data, "004893847")
    find_value.get_key
