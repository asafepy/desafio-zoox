import json
from questoes.q5 import FindValue


class OrderList(FindValue):

    def get_cpf(self):
        return self.get_value


if __name__ == '__main__':

    cpf_order_list = ['zooxwifi', 'bigdata_corp', 'fnrh', 'ipiranga_kmv']

    with open('files/pessoa.json') as f:
        data = json.load(f)

    for provider in cpf_order_list:

        try:
            order_list = OrderList(data[provider], "cpf")
            order_list.get_cpf()

        except KeyError:
            continue
