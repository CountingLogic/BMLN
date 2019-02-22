import pandas as pd
import io

data = io.StringIO('''Person,Smokes,Cancer
Anna,True,True
Bob,True,False
Clara,True,True

''')

df = pd.read_csv(data)
df["f"] = df.Smokes & df.Cancer
print(df.set_index(['Smokes']))

