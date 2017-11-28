import pandas as pd
#read in CSV and put into Pandas dataframe
#https://chrisalbon.com/python/pandas_dataframe_importing_csv.html
data = pd.read_csv('MTA_Customer_Feedback_Data__Beginning_2014.csv')

#total number of rows containing null data is 8365 which is less than 5% of data, choosing to remove rows with null
#https://stackoverflow.com/questions/26266362/how-to-count-the-nan-values-in-the-column-in-panda-data-frame
count_nan = len(data) - data.count()

#https://chrisalbon.com/python/pandas_missing_data.html
data1 = data.dropna()

print (data1)