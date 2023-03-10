import pandas as pd
from pandas import Series

tbl0 = pd.read_csv("tbl0.tsv", sep="\t")
tbl1 = pd.read_csv("tbl1.tsv", sep="\t")
tbl2 = pd.read_csv("tbl2.tsv", sep="\t")

# tbl = tbl2
# tbl["_c5b"] = tbl2["_c5b"].astype("string")
# tbl = tbl.sort_values(["_c0", "_c5a", "_c5b"], ascending=[True, True, True])
# tbl["_c5"] = tbl["_c5a"] + ":" + tbl["_c5b"].astype("string")
# df = tbl.groupby(["_c0"])["_c5"].apply(lambda x: ",".join(map(str, sorted(list(x))))).reset_index()
    
# print(df)
# Dataframes.column[]

_c1 = tbl0["_c1"]
_c2 = tbl0["_c2"]

# EL nombre de la columna _c1 aparece al mismo nivel de _c0
# Error al ejecutar tests.py
# r = (_c2.groupby(_c1).apply(lambda x: ':'.join( map(str, sorted(list(x.astype(str)))))))

 # EL nombre de la columna _c1 aparece al mismo nivel de _c0
    # Error al ejecutar tests.py
    # r = (_c2.groupby(_c1).apply(lambda x: ':'.join(map(str, sorted(list(x))))).reset_index())
    # r = (_c2.groupby(_c1).apply(lambda x: ':'.join( map(str, sorted(list(x.astype(str))))))).reset_index().rename(columns={"_c1": "_c0", "_c2":"_c1"})
    # new_df = pd.DataFrame(df).reset_index().rename(columns={"_c1": "_c0", "_c2":"_c1"})

    
df = tbl0.groupby("_c1")["_c2"].apply(lambda x: ":".join(map(str,sorted(list(x)))))
new_df = pd.DataFrame(df)
print(new_df)