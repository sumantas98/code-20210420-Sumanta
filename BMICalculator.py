import pandas as pd
import numpy as np
import json
import os
from os import path

class BMI:

    def EDA(self,filename):
        try:
            # Reading Json files from Data.json
            
            #filepath= 'Data.json'
            filepath= filename
            if not path.exists(filepath):
                return "File not exits"
            if os.stat(filepath).st_size==0 :
                return pd.DataFrame()
            f_open = open(filepath,'r')
            
            loadfile = json.load(f_open)
            f_open.close()
    

            # Load Data insde DataFrame for faster response and perform easy calculation

            dataframe = pd.DataFrame(loadfile)

            # Converting Height from cm to m2 and Calculating BMI

            dataframe['Heightm2']=dataframe['HeightCm']/100
            dataframe['BMIrate']= (dataframe['WeightKg']/dataframe['Heightm2']).apply(lambda x:round(x,2))

            dataframe.drop('HeightCm',axis=1)

            # Calculating BMI_Category and Health_risk inside dataframe using lambda function for less execution time

            dataframe['BMI_Category'] =  dataframe['BMIrate'].apply(lambda x: 'Underweight' if x<=18.4 else ('Normal weight' if x>=18.5 and x<=24.9 else('Overweight' if x>=25 and x<=29.9 else('Moderately obese' if x>=30 and x<=34.9 else('Severely obese' if x>=35 and x<=39.9 else 'Very severely obese' )))))
            dataframe['Health_risk'] =   dataframe['BMIrate'].apply(lambda x: 'Malnutrition risk' if x<=18.4 else ('Low risk' if x>=18.5 and x<=24.9 else('Enhanced risk' if x>=25 and x<=29.9 else('Medium risk' if x>=30 and x<=34.9 else('High risk' if x>=35 and x<=39.9 else 'Very high risk' )))))    

            return dataframe

        except IOError:
            print("File not accessible")
        except Exception as e:
            return "Exception Occured "+str(e)
            
        


    def calculateBMI(self,filename):
        df = self.EDA(filename)
        
        if 'File not exits' in df:
            return "File not exits"
        elif df.empty:
            return "File is empty"
        else:
            return df.to_json(orient='records')




    def BMICategoryCount(self ,filename,testdata1):
        df = self.EDA(filename)

        if 'File not exits' in df:
            return "File not exits"
        elif df.empty:
            return "File is empty"
        else:
            testdata = testdata1

            '''
            We have multile solution for second query. Solution 1 and soution 2 are given below.
            # Solution 1

            
            df = df.groupby(['BMI_Category'] ,as_index=False).count()[['BMI_Category','Gender']].rename(columns = {'Gender':'Count'}, inplace = False)
            return_val = df[df['BMI_Category']==testdata]['Count']
            if return_val.empty:
                return_val=0
            else:
                return_val=int(return_val)

            '''
            
            # Solution 2

            return_val = len(list(filter(lambda x: True if x == testdata else False , df['BMI_Category'])))

            return return_val

