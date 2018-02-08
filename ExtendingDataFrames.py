import pandas as pd
#declare data frames
if __name__ =='__main__':
  df1 = pd.DataFrame({'HPI':[80,85,88,85],
                      'Int_rate':[2, 3, 2, 2],
                      'US_GDP_Thousands':[50, 55, 65, 55]},
                     index = [2001, 2002, 2003, 2004])

  df2 = pd.DataFrame({'HPI':[80,85,88,85],
                      'Int_rate':[2, 3, 2, 2],
                      'US_GDP_Thousands':[50, 55, 65, 55]},
                     index = [2005, 2006, 2007, 2008])

<<<<<<< HEAD
df2 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55]},
                   index = [2005, 2006, 2007, 2008])

df3 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2, 3, 2, 2],
                    'Low_tier_HPI':[50, 52, 50, 53]},
                   index = [2001, 2002, 2003, 2004])
concat = pd.concat([df1,df2])
print(concat)
print("_____________________________________________")
concat = pd.concat([df1,df2,df3])
print(concat)
print("_____________________________________________")
df4 = df1.append(df2)
print(df4)
print("_____________________________________________")
df4 = df1.append(df3)
print(df4)
s = pd.Series([80,2,50], index=['HPI','Int_rate','US_GDP_Thousands'])
df4 = df1.append(s, ignore_index=True)
print(df4)
print("Merged dataframe\n",pd.merge(df1,df3, on='HPI'))
print(pd.merge(df1,df2, on=['HPI','Int_rate']))
=======
  df3 = pd.DataFrame({'HPI':[80,85,88,85],
                      'Int_rate':[2, 3, 2, 2],
                      'Low_tier_HPI':[50, 52, 50, 53]},
                     index = [2001, 2002, 2003, 2004])
  concat = pd.concat([df1,df2])
  print(concat)
  print("_____________________________________________")
  concat = pd.concat([df1,df2,df3])
  print(concat)
  print("_____________________________________________")
  df4 = df1.append(df2)
  print(df4)
  print("_____________________________________________")
  df4 = df1.append(df3)
  print(df4)
  s = pd.Series([80,2,50], index=['HPI','Int_rate','US_GDP_Thousands'])
  df4 = df1.append(s, ignore_index=True)
  print(df4)
>>>>>>> 0c2b0bc6cde3f692904eee794eacde4ae04c2f93
'''
      HPI  Int_rate  US_GDP_Thousands
2001   80         2                50
2002   85         3                55
2003   88         2                65
2004   85         2                55
2005   80         2                50
2006   85         3                55
2007   88         2                65
2008   85         2                55
_____________________________________________
      HPI  Int_rate  Low_tier_HPI  US_GDP_Thousands
2001   80         2           NaN              50.0
2002   85         3           NaN              55.0
2003   88         2           NaN              65.0
2004   85         2           NaN              55.0
2005   80         2           NaN              50.0
2006   85         3           NaN              55.0
2007   88         2           NaN              65.0
2008   85         2           NaN              55.0
2001   80         2          50.0               NaN
2002   85         3          52.0               NaN
2003   88         2          50.0               NaN
2004   85         2          53.0               NaN
_____________________________________________
      HPI  Int_rate  US_GDP_Thousands
2001   80         2                50
2002   85         3                55
2003   88         2                65
2004   85         2                55
2005   80         2                50
2006   85         3                55
2007   88         2                65
2008   85         2                55
_____________________________________________
      HPI  Int_rate  Low_tier_HPI  US_GDP_Thousands
2001   80         2           NaN              50.0
2002   85         3           NaN              55.0
2003   88         2           NaN              65.0
2004   85         2           NaN              55.0
2001   80         2          50.0               NaN
2002   85         3          52.0               NaN
2003   88         2          50.0               NaN
2004   85         2          53.0               NaN
   HPI  Int_rate  US_GDP_Thousands
0   80         2                50
1   85         3                55
2   88         2                65
3   85         2                55
4   80         2                50
<<<<<<< HEAD
Merged dataframe
    HPI  Int_rate_x  US_GDP_Thousands  Int_rate_y  Low_tier_HPI
0   80           2                50           2            50
1   85           3                55           3            52
2   85           3                55           2            53
3   85           2                55           3            52
4   85           2                55           2            53
5   88           2                65           2            50
   HPI  Int_rate  US_GDP_Thousands_x  US_GDP_Thousands_y
0   80         2                  50                  50
1   85         3                  55                  55
2   88         2                  65                  65
3   85         2                  55                  55
'''
=======
'''
>>>>>>> 0c2b0bc6cde3f692904eee794eacde4ae04c2f93
