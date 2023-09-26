import codecademylib
import pandas as pd

df = pd.DataFrame([
  ['January', 100, 100, 23, 100],
  ['February', 51, 45, 145, 45],
  ['March', 81, 96, 65, 96],
  ['April', 80, 80, 54, 180],
  ['May', 51, 54, 54, 154],
  ['June', 112, 109, 79, 129]],
  columns=['month', 'clinic_east',
           'clinic_north', 'clinic_south',
           'clinic_west']
)
#df.loc[[select rows]]
df2 = df.loc[[1, 3, 5]]
#reset_index will create a temp table with new index column, inplace = True will cause temp table to overwrite original table, drop = True will drop the new index column
df3 = df2.reset_index(inplace=True, drop=True)
print(df3)