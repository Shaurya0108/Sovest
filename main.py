import streamlit as st
import pandas as pd
import excel2json
import xlrd
from collections import OrderedDict
import json
st.set_page_config(page_title='Social Investments')
st.sidebar.header('Please select your risk tolerance')
choice = st.sidebar.slider('In the range (1) Risky, (3) Super Safe', 1, 3)
st.title('Social Investment')

st.markdown("""Please consider owning these stocks based on your risk tolerance""")
tables = []
for i in range(0, 3):
    if choice == 1:
         url = 'https://www.marketwatch.com/tools/screener/stock?exchange=all&skip=0&orderbyfield=&direction=&visiblecolumns=Symbol,CompanyName,Price,NetChange,ChangePercent,Volume,PeRatio&pricemin=0&pricemax=35&volumemin=1000000&volumemax=10000000&peratiomin=0&peratiomax=10&marketcapmax=10000&outperform200dayavg=1&PagingIndex={0}'.format(
            i * 100)
    elif choice == 2:
        url = 'https://www.marketwatch.com/tools/screener/stock?exchange=all&skip=0&orderbyfield=&direction=&visiblecolumns=Symbol,CompanyName,Price,NetChange,ChangePercent,Volume,PeRatio&pricemin=50&pricemax=100&volumemax=100000000&peratiomin=0&peratiomax=50&marketcapmax=10000&outperform200dayavg=1&PagingIndex={0}'.format(
            i * 100)
    elif choice == 3:
        url = 'https://www.marketwatch.com/tools/screener/stock?exchange=all&skip=0&orderbyfield=&direction=&visiblecolumns=Symbol,CompanyName,Price,NetChange,ChangePercent,Volume,PeRatio&pricemin=200&volumemin=5000000&PagingIndex={0}'.format(
            i * 100)
    print('Processing Index {0}'.format(i * 100))

    try:
        df = pd.read_html(url)[0]
        tables.append(df)
    except Exception as e:
        print(e)
        continue

results = pd.concat(tables, axis=0)
results.to_excel('ScreenResults.xlsx', index=False)

df = pd.read_excel('ScreenResults.xlsx',
                   usecols='A:F',
                   header=0)
st.dataframe(df)
st.title('Highest social score of these stocks')

df.to_json(r'topPicks.json')
with open('topPicks.json') as json_file:
    data = json.load(json_file)
symbols = []
i = 0
while (i<10):
    directive = 'Symbol'
    symbol = data[directive][str(i)]
    i +=1
    symbols.append(symbol)
