import json
from pprint import pprint


class FindKey:

    def __init__(self, file, key):
        self.file = file
        self.key = key
        self.results = []

    def _finditem(self, obj, key):

        if key in obj:
            self.results.append(obj[key])

        elif type(key) is str and key.title() in obj:
            self.results.append(obj[key.title()])

        elif type(key) is str and key.upper() in obj:
            self.results.append(obj[key.upper()])

        for k, v in obj.items():
            if isinstance(v, dict):
                self._finditem(v, key)

    @property
    def get_value(self):
        self._finditem(self.file, self.key)
        print(self.results)


if __name__ == '__main__':

    with open('files/pessoa.json') as f:
        data = json.load(f)

    for key in ["age", "name", "cpf", "gender", 7]:

        results = FindKey(data, key)
        results.get_value
