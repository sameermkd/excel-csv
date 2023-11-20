import pandas as pd

read_file=pd.read_excel("data.xlsx")

read_file.to_csv("test.csv", index=None, header=True)

df=pd.DataFrame(pd.read_csv("test.csv"))