# code-20210420-Sumanta
✔ Python BMI Calculator Coding Challenge

# Project description:
This project has designed to calculate the BMI Rate, BMI Category and Health Risk of any person.User can provide  multiple dataset through JSON format(1 lakh Dataset at a time). Program will return the output in same JSON format.

# Necessary Libraries:
- pandas
- numpy
- os
- json

# How to install :
Please execute the below command in the command prompt.

pip install -r requirements.txt

# Project Structure:
This project contains the below folder and files .
1. BMICalculator.py
2. unittestcase.py
3. requirements.txt
4. /Data/Data.json
5. /Data/DataEmpty.json

# Solution Approach:

--Function EDA (Exploratory Data Analysis)-->input Data "filename"  --> Return type DataFrame:
- Reading Json files from Data.json
- Load Data insde DataFrame for faster response and perform easy calculation.
- Converting Height from cm to m2 and Calculating BMI.

--Function calculateBMI()-->input Data "filename" --> Return type JSON:
- Calculating BMI_Category and Health_risk inside dataframe using lambda function for less execution time.

--Function BMICategoryCount ()--> input Data "filename" and "BMI Category" --> Return type Integer:
- Count the total number of overweight people -> This problem has solved by two ways 
    - i>  Using groupby operation 
    - ii> Using list,filter and lambda 
- unittestcase.py is containing all test cases.
- "Data" folder is containing dataset for this project.

# Output File:
- tested inside unittestcase.py file

Note : If any test case is required will add as per business requirement. Also "Sumanta-POC.md" files are created for feasibility test.
