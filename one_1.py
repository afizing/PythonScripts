import pandas as pd
from datetime import datetime, timedelta
 

xl = pd.ExcelFile('1/current.xlsx')
data = xl.parse()
data1 =[]


def add_one_month(t):
    one_day = timedelta(days=1)
    one_month_later = t + one_day
    while one_month_later.month == t.month:  # advance to start of next month
        one_month_later += one_day
    target_month = one_month_later.month
    while one_month_later.day < t.day:  # advance to appropriate day
        one_month_later += one_day
        if one_month_later.month != target_month:  # gone too far
            one_month_later -= one_day
            break
    return one_month_later


for i in data['timestamp(dd-mm-yyyy_hh:mm:ss.usecs)']:
    # 14-02-2016_14:10:15.159816
    data1.append(strftime(add_one_month(datetime.strptime(i,'%d-%m-%Y_%H:%M:%S.%f')))

data['timestamp(dd-mm-yyyy_hh:mm:ss.usecs)'] = data1
writer = pd.ExcelWriter('1/current.xlsx', engine='xlsxwriter')
data.to_excel(writer, index=False, sheet_name='current')
writer.save()



