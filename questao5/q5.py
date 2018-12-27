import json
from pprint import pprint


class FindKey:

    def __init__(self, file, key):
        self.file = file
        self.key = key

    def _finditem(self, obj, key):
        # import pdb; pdb.set_trace()
        if key in obj:
            return obj[key]
        elif key.title() in obj:
            return obj[key.title()]

        for k, v in obj.items():
            if isinstance(v, dict):
                self._finditem(v, key)

    @property
    def get_value(self):
        print(self._finditem(self.file, self.key))


if __name__ == '__main__':

    with open('files/pessoa.json') as f:
        data = json.load(f)

    key = "age"
    results = FindKey(data, key)
    print(results.get_value)
