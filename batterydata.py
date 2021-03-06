import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


dfp = pd.read_csv('Battery_Data.csv', parse_dates=[0],infer_datetime_format=True,sep=',')

print(dfp.columns)


def getSelectedDataframe(nameField):
    soclist=[]
    replacedic={}
    for col in dfp.columns:
        if nameField in col: 
         print(col)
         soclist.append(col)
         replacedic[col]='-'
    
    soclist.append('human_readable_date') 
    dfrc = dfp[soclist]

    print("Intermediate Lists and Dictionaries") 
    print(soclist)
    print(replacedic)

    print("#################")
    print(dfrc.head())
    print(dfrc.index)
    dfrc['human_readable_date'] = pd.to_datetime(dfrc['human_readable_date'])

    dfrc.index = dfrc['human_readable_date']

    del dfrc['human_readable_date']

    dfrc = dfrc.replace(replacedic, np.nan)
    print(dfrc.head())
    print(dfrc.index)
    
    dfrc = dfrc.astype(float)
    
    return dfrc

#dfrc = getSelectedDataframe("curr")

dfrc1 = getSelectedDataframe("volt")

#fig, axes = plt.subplots(nrows=2, ncols=2)

#dfrc.plot(ax=axes[0,0],title="Current Variation",figsize=(10,5), grid=True)
#dfrc1.plot(ax=axes[0,1],title="Voltage Variation",figsize=(10,5), grid=True)
dfrc1.plot(title="Voltage Variation",figsize=(10,5), grid=True)

plt.show()

