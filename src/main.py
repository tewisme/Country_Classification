#lib
import pandas as pd

#file
import algorithms as aas
import processing_data as prodas

def main():
    data_path = '..\\data\\country-data.csv'
    data_dict_path = '..\\data\\data-dictionary.csv'
    data = pd.read_csv(data_path)
    data_dict = pd.read_csv(data_dict_path)
    #prodas.proc(data, data_dict)
    aas.proc(data, data_dict)

if __name__ == '__main__':
    main()
