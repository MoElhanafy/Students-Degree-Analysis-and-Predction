import pandas as pd
from moduleV2 import module
df = pd.read_csv('./student_lifestyle_dataset.csv')

y = df['GPA'].values[:1999]
df.drop(index=1, columns=['Stress_Level','GPA','Student_ID'], inplace=True)
X = df.values



myMod = module(X, y)
myMod.fit()
myMod.performance()
myMod.predict([8, 4, 8, 1, 3]) #Study,Extracurricular,Sleep,Social,Physical