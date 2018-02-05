import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style


if __name__ == "__main__":
    web_stats = {'Day':[1,2,3,4,5,6],
             'Customers':[43,34,65,56,29,76],
             'Bill (in Dollars)':[65,67,78,65,45,52]}
    
    df = pd.DataFrame(web_stats)
    print(df.head())
    print("_______________________________________")
    print(df.tail())
    print("_______________________________________")    
    df.set_index('Day', inplace=True)
    style.use('fivethirtyeight')
    print(df['Customers'])
    df['Customers'].plot()
    plt.show()
    df.plot()
    plt.show()
    print(df[['Customers','Bill (in Dollars)']])
    
    
    
    
    
'''
   Bill (in Dollars)  Customers  Day
0                 65         43    1
1                 67         34    2
2                 78         65    3
3                 65         56    4
4                 45         29    5
_______________________________________
   Bill (in Dollars)  Customers  Day
1                 67         34    2
2                 78         65    3
3                 65         56    4
4                 45         29    5
5                 52         76    6
_______________________________________
Day
1    43
2    34
3    65
4    56
5    29
6    76
Name: Customers, dtype: int64
*****************img1******************

*****************img2******************

     Customers  Bill (in Dollars)
Day                              
1           43                 65
2           34                 67
3           65                 78
4           56                 65
5           29                 45
6           76                 52
'''    