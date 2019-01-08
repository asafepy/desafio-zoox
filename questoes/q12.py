import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class Frequencia:
    def __init__(self):
        self.data_file = 'files/consolidated_weather_V03.csv'
        self.data_frame = None

    def read_csv(self):
        self.data_frame = pd.read_csv(self.data_file)

    def get_frist_eight(self):
        dataset_CA = self.data_frame.groupby('state')
        freq = dataset_CA.describe(include='all')['city']['count']
        return freq.head(50).sort_values()[-8:]

    @property
    def run(self):
        self.read_csv()
        return self.get_frist_eight()


if __name__ == '__main__':

    frequencia = Frequencia()
    frequencia_grafico = frequencia.run

    frequencia_grafico.plot.bar(x='states', y='count', rot=0)
    plt.title('Frequencia Acumulada dos oitos estados com mais registros.')
    plt.ylabel('Numero de Registros')
    plt.xlabel('Estados')
    plt.show()
