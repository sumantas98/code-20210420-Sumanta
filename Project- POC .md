```python
import pandas as pd
import json
```

### Reading Json files from Data.json


```python
filepath= 'Data.json'
f_open = open(filepath,'r')
loadfile = json.load(f_open)
```

### Query No ::1 <br>
        
1) Calculate the BMI (Body Mass Index) using Formula 1, BMI Category and Health
risk from Table 1 of the person and add them as 3 new columns

### Load Data insde DataFrame for faster response and perform easy calculation


```python
#print(loadfile)
```


```python
dataframe = pd.DataFrame(loadfile)
```

### Converting Height from cm to m2 and Calculating BMI


```python
dataframe['Heightm2']=dataframe['HeightCm']/100
dataframe['BMIrate']= (dataframe['WeightKg']/dataframe['Heightm2']).apply(lambda x:round(x,2))
```


```python
dataframe.drop('HeightCm',axis=1)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Gender</th>
      <th>WeightKg</th>
      <th>Heightm2</th>
      <th>BMIrate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Male</td>
      <td>96</td>
      <td>1.71</td>
      <td>56.14</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Male</td>
      <td>85</td>
      <td>1.61</td>
      <td>52.80</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Male</td>
      <td>77</td>
      <td>1.80</td>
      <td>42.78</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Female</td>
      <td>62</td>
      <td>1.66</td>
      <td>37.35</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Female</td>
      <td>70</td>
      <td>1.50</td>
      <td>46.67</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Female</td>
      <td>82</td>
      <td>1.67</td>
      <td>49.10</td>
    </tr>
  </tbody>
</table>
</div>



### Calculating BMI_Category and Health_risk inside dataframe using lambda function for less execution time


```python
dataframe['BMI_Category'] =  dataframe['BMIrate'].apply(lambda x: 'Underweight' if x<=18.4 else ('Normal weight' if x>=18.5 and x<=24.9 else('Overweight' if x>=25 and x<=29.9 else('Moderately obese' if x>=30 and x<=34.9 else('Severely obese' if x>=35 and x<=39.9 else 'Very severely obese' )))))
dataframe['Health_risk'] =   dataframe['BMIrate'].apply(lambda x: 'Malnutrition risk' if x<=18.4 else ('Low risk' if x>=18.5 and x<=24.9 else('Enhanced risk' if x>=25 and x<=29.9 else('Medium risk' if x>=30 and x<=34.9 else('High risk' if x>=35 and x<=39.9 else 'Very high risk' )))))    
```


```python
dataframe
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Gender</th>
      <th>HeightCm</th>
      <th>WeightKg</th>
      <th>Heightm2</th>
      <th>BMIrate</th>
      <th>BMI_Category</th>
      <th>Health_risk</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Male</td>
      <td>171</td>
      <td>96</td>
      <td>1.71</td>
      <td>56.14</td>
      <td>Very severely obese</td>
      <td>Very high risk</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Male</td>
      <td>161</td>
      <td>85</td>
      <td>1.61</td>
      <td>52.80</td>
      <td>Very severely obese</td>
      <td>Very high risk</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Male</td>
      <td>180</td>
      <td>77</td>
      <td>1.80</td>
      <td>42.78</td>
      <td>Very severely obese</td>
      <td>Very high risk</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Female</td>
      <td>166</td>
      <td>62</td>
      <td>1.66</td>
      <td>37.35</td>
      <td>Severely obese</td>
      <td>High risk</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Female</td>
      <td>150</td>
      <td>70</td>
      <td>1.50</td>
      <td>46.67</td>
      <td>Very severely obese</td>
      <td>Very high risk</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Female</td>
      <td>167</td>
      <td>82</td>
      <td>1.67</td>
      <td>49.10</td>
      <td>Very severely obese</td>
      <td>Very high risk</td>
    </tr>
  </tbody>
</table>
</div>




```python
dataframe.to_json(orient='records')
```




    '[{"Gender":"Male","HeightCm":171,"WeightKg":96,"Heightm2":1.71,"BMIrate":56.14,"BMI_Category":"Very severely obese","Health_risk":"Very high risk"},{"Gender":"Male","HeightCm":161,"WeightKg":85,"Heightm2":1.61,"BMIrate":52.8,"BMI_Category":"Very severely obese","Health_risk":"Very high risk"},{"Gender":"Male","HeightCm":180,"WeightKg":77,"Heightm2":1.8,"BMIrate":42.78,"BMI_Category":"Very severely obese","Health_risk":"Very high risk"},{"Gender":"Female","HeightCm":166,"WeightKg":62,"Heightm2":1.66,"BMIrate":37.35,"BMI_Category":"Severely obese","Health_risk":"High risk"},{"Gender":"Female","HeightCm":150,"WeightKg":70,"Heightm2":1.5,"BMIrate":46.67,"BMI_Category":"Very severely obese","Health_risk":"Very high risk"},{"Gender":"Female","HeightCm":167,"WeightKg":82,"Heightm2":1.67,"BMIrate":49.1,"BMI_Category":"Very severely obese","Health_risk":"Very high risk"}]'



### Query No ::2 <br>
2) Count the total number of overweight people using ranges in the column BMI
Category of Table 1, check this is consistent programmatically and add any other
observations in the documentation

<font color='red'>We have multile solution for second query. Solution 1 and soution 2 are given below.</font>

<font color='red'>Solution 1</font>


```python
df = dataframe.groupby(['BMI_Category'] ,as_index=False).count()[['BMI_Category','Gender']].rename(columns = {'Gender':'Count'}, inplace = False)
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>BMI_Category</th>
      <th>Count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Severely obese</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Very severely obese</td>
      <td>5</td>
    </tr>
  </tbody>
</table>
</div>




```python
testdata = 'Overweight'
return_val = df[df['BMI_Category']==testdata]['Count']
if return_val.empty:
    lx=0
else:
    lx=int(return_val)

lx
```




    0



<font color='red'>Solution 2</font>


```python
return_val2 = len(list(filter(lambda x: True if x=='Overweight' else False , dataframe['BMI_Category'])))
return_val2
```




    0




```python

```
