import pandas as pd
from random import randint, seed
import plotly.express as px

seed(10)

df_dict = {
    '<10':[randint(0,9) for x in range(0,20)],
    '10-19':[randint(10,19) for x in range(0,20)],
    '20-29':[randint(20,29) for x in range(0,20)],
    '0-100':[randint(0,100) for x in range(0,20)],
}
index = [f'measure {x}' for x in range(0,20)]
df = pd.DataFrame(df_dict, index=index)

print(px.line(df, x=df.index, y=df.iloc[:, 1]))