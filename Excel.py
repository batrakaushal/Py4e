import xlrd

import pandas as pd

workbook = xlrd.open_workbook("gg")

worksheet = workbook.sheet_by_name("sheet1")

pd.value_counts(df.*A*)

s = pd.value_counts(df.*C*)

s1 = pd.Series({'nunique': len(s), 'unique values': s.index.tolist()})

s.append(s1)

print(s)
