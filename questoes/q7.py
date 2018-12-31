import json
from pprint import pprint
from .q5 import FindValue

class OrderList:

    def __init__(self, data, key):
        self.data = data
        self.key = key
    
    def get_cpf(self):

        find_value = FindValue(self.data, self.key)
        find_value.get_value
        

        print(find_value.results)


if __name__ == '__main__':

    cpf_order_list = ['zooxwifi', 'bigdata_corp', 'fnrh', 'ipiranga_kmv' ] 

    with open('files/pessoa.json') as f:
        data = json.load(f)

    # for provider in cpf_order_list:

    order_list = OrderList(data['zooxwifi'], "cpf")

    order_list.get_cpf()
