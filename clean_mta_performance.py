import pandas as pd
#read in CSV and put into Pandas dataframe
#https://chrisalbon.com/python/pandas_dataframe_importing_csv.html
data = pd.read_csv('Mta_monthly_ridership_beginning_2008.csv')

#total number of rows containing null data is 8365 which is less than 5% of data, choosing to remove rows with null
#https://stackoverflow.com/questions/26266362/how-to-count-the-nan-values-in-the-column-in-panda-data-frame
count_nan = len(data) - data.count()

#confirm no null data
print(count_nan)

#list column rows
#https://stackoverflow.com/questions/19482970/get-list-from-pandas-dataframe-column-headers
list(data.columns.values)

#removing Columns with no data (Indicator Unit and Decimal Places)
#https://stackoverflow.com/questions/28538536/deleting-multiple-columns-based-on-column-names-in-pandas
data = data.drop(['Indicator Unit', 'Decimal Places'], axis=1)

#print data
print(data)

#export cleaned data back to csv
#https://chrisalbon.com/python/pandas_saving_dataframe_as_csv.html
data.to_csv('mta_performance_clean.csv')
