import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
# Importamos de dataset.
df = pd.read_csv("../data/wine_dataset.csv")
df
# Mostramos las primeras 5 entradas para ver qué tipo de datos tenemos.
df.head()
# Observo las columnas que tiene el dataset.
df.columns
# Veo la información de las columnas.
df.info()
# Veo el tipo de los datos de cada columna.
df.dtypes
# Hago una copia del DataFrame para limpiarlo y quedarme con lo que quiera analizar.
df_back_up = df.copy()
df2 = df
df2
# Observos los null que hay en las columnas para saber cuales elegir.
df2.isnull().sum()
# Obtengo la suma por países.
df2.country.value_counts()
# Selecciono solo las filas donde el país es España.
df3 = df2[df2.country.isin(["Spain"])]
df3
# Observo el total por bodegas.
df3.winery.value_counts()
# Selecciono las bodegas que tienen más de 40 entradas.
df3.winery.value_counts() > 40
# Elijo las 5 bodegas con mayor de 40 entradas y el país España.
df4 = df2[df.country.isin(["Spain"]) & df.winery.isin(["Bodegas Valdemar", "CVNE", "Torres", "Marqués de Cáceres", "Vicente Gandia"])]
df4
# Selecciono las columnas que quiero analizar.
df5 = df4[["country", "title", "winery"]]
df5
# Visualizo los datos a partir de un gráfico donde aparece el total por bodegas en España.
sns_plot= sns.countplot(x=df4.country, hue=df4.winery)
sns_plot.figure.savefig("g1.jpg", dpi=1000)
# Visualizo los datos a partir de un gráfico donde aparece dónde tienen las bodegas D.O. (Denominación de Origen) con tres tipos de gráficos. 
sns_plot2= sns.scatterplot(x="winery", y="region_1", data=df4)
plt.savefig("g2.jpg", bbox_inches='tight', dpi=1000)
g = sns.FacetGrid(data=df4, col="country", row="winery", sharex =False)
g.map_dataframe(sns.countplot, x="region_1")
plt.savefig("g4.jpg", bbox_inches='tight', dpi=1000)
# Exportamos el nuevo DataFrame con los datos que he valorado anteriormente.
df5.to_csv('wine_cleaning.csv')
