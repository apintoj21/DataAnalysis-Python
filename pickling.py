import quandl as Quandl
import pandas as pd
import sys
# Not necessary, I just do this so I do not show my API key.
api_key = open('quandlapikey.txt','r').read()
fiddy_states = pd.read_html('/root/python/DataAnalysis-Python/PDreadCSV.html')

main_df = pd.DataFrame(fiddy_states)

for abbv in fiddy_states[0][1:]:
    if main_df.empty:
        main_df = df
    else:
        main_df = main_df.join(df)