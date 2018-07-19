import pandas as pd
import numpy as np
table = [
    ['A', 'Noah', 90, 92],
    ['B', 'Liam', 81, 83],
    ['C', 'William', 87,85],
    ['B', 'Benjamin.', 82,80],
    ['A', 'Emma.', 90,94],
    ['C', 'Olivia', 50,60],
    ['A', 'Isabella', 70,71],
    ['C', 'Amelia', 84,86],
    ['B', 'Mia', 88,85],
]
df = pd.DataFrame(table,columns = ['class', 'name', 'math_score', 'eng_score'])
print(df)
print('-'*50)
print(df['math_score'].mean())
print('-'*50)
A = df.groupby('class').mean()
print(A)
print('-'*50)
B = df.groupby('class').sum()
print(B)
print('-'*50)
C = df.corr()
print(C)

