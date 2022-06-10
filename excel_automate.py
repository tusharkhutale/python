from calendar import calendar
from fileinput import filename
import pandas as pd
import datetime as dt
import calendar 
import plotly
import plotly.express as px

files = ['sales.xlsx','sales_two.xlsx']
combined = pd.DataFrame()

for file in files:
    df = pd.read_excel(file)
    df['Date'] = df['Date'].dt.date
    df['Sales']= df['Sales']
    df['Day'] = pd.DatetimeIndex(df['Date']).day
    df['Month'] = pd.DatetimeIndex(df['Date']).month
    df['Year'] = pd.DatetimeIndex(df['Date']).year
    df['Month_Name'] = df['Month'].apply(lambda x: calendar.month_abbr[x])
    combined = combined.append(df, ignore_index=True)

# create bar chart
fig = px.bar(combined, x='Month', y='Sales', title = 'Sales 2022')

#save bar chart and export to HTML
plotly.offline.plot(fig, filename='Sales_2022.html')

combined.to_excel('sales_final.xlsx', index = False, sheet_name='2022 sales')
