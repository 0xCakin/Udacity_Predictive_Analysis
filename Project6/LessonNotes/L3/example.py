import numpy
import pandas
import os
import xlrd

df = pandas.read_excel('./weekly-sales-differencing (1).xlsx', sheet_name='Sheet1')

print(df)