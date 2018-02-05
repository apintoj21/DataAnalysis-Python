import pandas as pd



if __name__ == "__main__":
    web_stats = {'Day':[1,2,3,4,5,6],
             'Customers':[43,34,65,56,29,76],
             'Bill (in Dollars)':[65,67,78,65,45,52]}
    
    df = pd.DataFrame(web_stats)
    print(df.head())
    print("_______________________________________")
    print(df.tail())
    
    
    
    
    
    
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
'''    