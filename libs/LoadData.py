'''
Created on 06-Dec-2018

@author: vaibh
'''

import pandas as pd
from os import listdir
from os.path import isfile, join



class view_data():
    
    def __init__(self,base_dir):
        self.basedir = base_dir
        self.DATA_DIRECTORY = join(base_dir,"data")
        self.DATA_DICT = pd.read_excel(join(self.DATA_DIRECTORY,"Data_Dictionary.xlsx"))
        self.filenames = [f for f in listdir(self.DATA_DIRECTORY) if isfile(join(self.DATA_DIRECTORY, f))]
        
   
        
    def read_data(self,file_name,rows=None):
        if file_name.split(".")[1] == "csv":
            return pd.read_csv(join(self.DATA_DIRECTORY,file_name), nrows = rows)
        #elif file_name.split(".")[1] == "xlsx":
        #    return pd.read_excel(join(self.DATA_DIRECTORY,file_name), nrows = rows)
        else:
            return pd.DataFrame(None)
            
            
    def save_data(self,df,filename):
        df.to_csv(join(self.basedir,"output_data",filename))
        