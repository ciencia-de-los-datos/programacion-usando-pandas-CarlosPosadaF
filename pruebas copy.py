import pandas as pd
from pandas import Series

tbl0 = pd.read_csv("tbl0.tsv", sep="\t")
tbl1 = pd.read_csv("tbl1.tsv", sep="\t")
tbl2 = pd.read_csv("tbl2.tsv", sep="\t")

# letras = ["A", "B", "C", "D", "E"]
# dic = {}

# for letra in letras:
#     df = tbl0.set_index("_c1").loc[letra]
#     max = df.describe().iloc[7, 1]
#     dic[letra] = max

# _c1 = pd.Series(dic).
# print(_c1)

# df = pd.DataFrame(tbl1["_c4"].str.upper().sort_values())["_c4"].unique()

# print(df)


# duplicates = (tbl1['_c4'].groupby(_c4, group_keys=True).unique().apply(lambda x: lista.append(str(x[[0]]).upper())))
# duplicates = (tbl1['_c4'].groupby(_c4, group_keys=True).unique().apply(lambda x: str(x[[0]]).upper()))

# print(duplicates[1])
# print(tbl1['_c4'].duplicated(keep=False).str.upper().groupby(_c4, group_keys=True).apply(lambda x: x))
# print(tbl1.groupby(_c4, group_keys=True).apply(lambda x: x['_c4'].str.upper()))

# print(tbl1.sort_values(by="_c4").apply(lambda x: x.))
# print(sorted(tbl1.groupby(_c4, group_keys=True)["_c0 _c4"]))

# _c1 = tbl0["_c1"]
# _c2 = tbl0["_c2"]

# r = _c2.groupby(_c1).apply(lambda x: ':'.join(sorted(x.astype(str)))).reset_index(name = "_c2")
# r = (_c2.groupby(_c1).apply(lambda x: ':'.join(sorted(x.astype(str)))).reset_index(name = "_c2")).set_index("_c1")

# _c0 = tbl2["_c0"]
# _c5a = tbl2["_c5a"]
# _c5b = tbl2["_c5b"]


# # r = (_c5a.groupby(_c0).apply(lambda x: ','.join(sorted(x.astype(str)+":"+"___"))).reset_index(name = "_c5a")).set_index("_c0")
# r = (_c5b.groupby(_c0).apply(lambda x: ','.join(sorted(x.astype(str)))).reset_index()).set_index("_c0")


# print(r.reset_index())

# def pregunta_03():
#     """
#     ¿Cuál es la cantidad de registros por cada letra de la columna _c1 del archivo
#     `tbl0.tsv`?

#     Rta/
#     A     8
#     B     7
#     C     5
#     D     6
#     E    14
#     Name: _c1, dtype: int64

#     """

#     letras = pd.DataFrame(tbl0["_c1"].str.upper().sort_values())["_c1"].unique()
#     dic = {}

#     for letra in letras:
#         cant = tbl0.set_index("_c1").loc[letra].shape[0]
#         dic[letra] = cant

#     # En la última línea, no muestra Name: _c1, sólo muestra dtype: int64

#     _c1 = tbl0["_c1"]

#     r = tbl0.groupby(_c1)["_c1"].count()
#     return pd.Series(dic)

# def pregunta_04():
#     """
#     Calcule el promedio de _c2 por cada letra de la _c1 del archivo `tbl0.tsv`.

#     Rta/
#     A    4.625000
#     B    5.142857
#     C    5.400000
#     D    3.833333
#     E    4.785714
#     Name: _c2, dtype: float64
#     """

#     letras = pd.DataFrame(tbl0["_c1"].str.upper().sort_values())["_c1"].unique()
#     dic = {}

#     for letra in letras:
#         df = tbl0.set_index("_c1").loc[letra]

#         prom = df.describe().iloc[1, 1]
#         dic[letra] = prom
    
#     # En la última línea, no muestra Name: _c1, sólo muestra dtype: int64
#     return pd.Series(dic)

# letras = pd.DataFrame(tbl0["_c1"].str.upper().sort_values())["_c1"].unique()
#     dic = {}

#     for letra in letras:
#         df = tbl0.set_index("_c1").loc[letra]
#         max = df.describe().iloc[7, 1]
#         dic[letra] = max

#     # Al principio, no muestra el nombre de la columna _c1
#     # En la última línea, no muestra Name: _c1, sólo muestra dtype: int64
#     return pd.Series(dic)

#     # Mustra el formato como indica la respuesta, pero muestra todos los registros por cada letra
#     # return(df["_c2"])