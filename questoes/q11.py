import pandas as pd
import numpy as np


class MediaTemp:
    def __init__(self, *args, **kwargs):
        self.data_file = 'files/consolidated_weather_V03.csv'
        self.data_frame = None

    def read_csv(self):
        self.data_frame = pd.read_csv(self.data_file)

    def make_list_index(self, key, value):
        return self.data_frame[self.data_frame[key] != value].index

    def remove_state(self):
        self.data_frame.drop(self.make_list_index('state', 'CA'))

    def make_defaultdict(self):
        
        dataset_CA = self.data_frame.head().describe()
        
        media_month = dataset_CA.groupby(["month"])['temp'].mean()
        media_year = dataset_CA.groupby(["year"])['temp'].mean()

        return {'average_month': round(media_month, 2),
                'average_year': round(media_year, 2)
                }

    def write_csv_out(self):
        df_media = pd.DataFrame(
            self.make_defaultdict(), columns=['average_month', 'average_year'], index=[0])

        df_media.to_csv('files/cw_out.csv', sep='\t',
                        encoding='utf-8')

        return df_media

    @property
    def run(self):
        self.read_csv()
        self.remove_state()
        return self.write_csv_out()




if __name__ == "__main__":
    media_temp = MediaTemp()
    print(media_temp.run)