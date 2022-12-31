import pandas as pd
import numpy as np

filename = "in.csv"
columname = "name"
columns = columname.lower()
#d)
try:
    open(filename, 'r')
except:
    print("[ERROR] - IO error")#%%
    exit(1)

df = pd.read_csv(filename)
coloane = [str(val.lower()) for val in df.columns.values]
df.columns = coloane

# a)
if columname.lower() not in coloane:
    print("[ERROR] - unknown column name")
    exit(2)

#b)
fisier = open(filename, 'r').readlines()
header_length = len(fisier[0].split(","))
for idx in range(1,len(fisier)):
    if (len(fisier[idx].split(",")) != header_length):
        print("[ERROR] - invalid format - different words on line",idx)
        exit(3)


#c)
if (len(coloane) > len(set(coloane))):
    print("[ERROR] - invalid format - duplicate columns")
    exit(4)

print("[OK]")
## dupa validari
output = df[columname]
output = [val.lower() for val in output]
output = pd.DataFrame(output).value_counts().keys()
rezultat = [val[0] for (val) in output]

for rez in rezultat:
    print(rez)

#%%
