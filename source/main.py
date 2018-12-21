'''
Created on 06-Dec-2018

@author: vaibhav
'''

from libs.LoadData import view_data
import os




if __name__ == "__main__":
    print(os.getcwd())
    data = view_data(os.getcwd())
    print(data.filenames)
    print(data.DATA_DICT)
    for file in data.filenames:
        print(file)
        df = data.read_data(file, rows=1000)
        if not df.empty:
            data.save_data(df,file)

