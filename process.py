# -*-coding:utf8 -*-
import pandas as pd

from pandas import Series, DataFrame
import xlwt


df = pd.read_csv('/Users/edward/Desktop/change/zongheyuanshi.csv')
i = 0
file = xlwt.Workbook()
table = file.add_sheet('sheet name')
# read data
while i < 199:
    school = str(df['school'][i]).decode("utf8")
    subject = str(df['Subject'][i]).decode("utf8")
    years_09 = int(df['2009'][i])-546
    years_10 = int(df['2010'][i])-547
    years_11 = int(df['2011'][i])-536
    years_12 = int(df['2012'][i])-570
    years_13 = int(df['2013'][i])-530
    years_14 = int(df['2014'][i])-493
    years_15 = int(df['2015'][i])-534
    years_16 = int(df['2016'][i])-515
    avg_default = (years_14 + years_15 + years_16) // 3 + 520
    avg1 = (years_14 + years_15 + years_16) // 3
    if avg1 > years_13 + 5 or avg1 < years_13 - 5:
        years_17 = avg_default
    else:
        avg2 = (avg1 + years_12 + years_13) // 3
        if avg2 > years_11 + 5 or avg2 < years_11 - 5:
            years_17 = avg_default

        else:
            avg3 = (avg2 + years_10 + years_11) // 3
            if avg3 > years_16 + 5 or avg3 < years_16 - 5:
                years_17 = avg_default
            else:
                years_17 = (avg3 + years_09) // 2 + 520
    table.write(i, 0, school)
    table.write(i, 1, subject)
    table.write(i, 2, int(df['2009'][i]))
    table.write(i, 3, int(df['2010'][i]))
    table.write(i, 4, int(df['2011'][i]))
    table.write(i, 5, int(df['2012'][i]))
    table.write(i, 6, int(df['2013'][i]))
    table.write(i, 7, int(df['2014'][i]))
    table.write(i, 8, int(df['2015'][i]))
    table.write(i, 9, int(df['2016'][i]))
    table.write(i, 10, years_17)
    i += 1
j=200
while j<354:
    school = str(df['school'][j]).decode("utf8")
    subject = str(df['Subject'][j]).decode("utf8")
    years_09 = int(df['2009'][j])-545
    years_10 = int(df['2010'][j])-548
    years_11 = int(df['2011'][j])-533
    years_12 = int(df['2012'][j])-543
    years_13 = int(df['2013'][j])-539
    years_14 = int(df['2014'][j])-507
    years_15 = int(df['2015'][j])-526
    years_16 = int(df['2016'][j])-513
    avg_default = (years_14 + years_15 + years_16) // 3 + 520
    avg1 = (years_14 + years_15 + years_16) // 3
    if avg1 > years_13 + 5 or avg1 < years_13 - 5:
        years_17 = avg_default
    else:
        avg2 = (avg1 + years_12 + years_13) // 3
        if avg2 > years_11 + 5 or avg2 < years_11 - 5:
            years_17 = avg_default

        else:
            avg3 = (avg2 + years_10 + years_11) // 3
            if avg3 > years_16 + 5 or avg3 < years_16 - 5:
                years_17 = avg_default
            else:
                years_17 = (avg3 + years_09) // 2 + 520
    table.write(j, 0, school)
    table.write(j, 1, subject)
    table.write(j, 2, int(df['2009'][j]))
    table.write(j, 3, int(df['2010'][j]))
    table.write(j, 4, int(df['2011'][j]))
    table.write(j, 5, int(df['2012'][j]))
    table.write(j, 6, int(df['2013'][j]))
    table.write(j, 7, int(df['2014'][j]))
    table.write(j, 8, int(df['2015'][j]))
    table.write(j, 9, int(df['2016'][j]))
    table.write(j, 10, years_17)
    j += 1

file.save('demo.xls')
