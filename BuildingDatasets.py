import pandas as pd

fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
print(fiddy_states)
print("_________________________________________________________")
print(fiddy_states[0])
print("_________________________________________________________")
for abbv in fiddy_states[0][0][1:]:
    print(abbv)
print("_________________________________________________________")
for abbv in fiddy_states[0][0][1:]:
    #print(abbv)
    print("FMAC/HPI_"+str(abbv))
print("_________________________________________________________")

