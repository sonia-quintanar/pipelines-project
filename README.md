# pipelines-project
# WINE IN SPAIN

![imagen_vino](https://github.com/sonia-quintanar/pipelines-project/blob/main/src/imagen_vino.jpg)

# Descripción del proyecto
Hemos descargado un dataset donde aparecen datos de la venta de vino en los distintos países, así como su D.O (Denominación de Origen), precios, y bodegas.

Datos obtenidos en Kaggle Data Sets.
Wine Reviews
https://www.kaggle.com/zynicide/wine-reviews?select=winemag-data-130k-v2.csv

Hemos realizado una limpieza del dataset y hemos seleccionado las columnas de los vinos que se venden en España, por denominación de origen y bodega.

En este proyecto, analizamos las 5 bodegas que mayor número de ventas tienen siendo Bodegas Valdemar, CVNE, Torres, Marqués de Cáceres y Vicente Gandia.

A continuación, mostramos los resultados a través de distintos gráficos:

![gráfico1](https://github.com/sonia-quintanar/pipelines-project/blob/main/output/g1.jpg)

![gráfico2](https://github.com/sonia-quintanar/pipelines-project/blob/main/output/g2.jpg)

![gráfico3](https://github.com/sonia-quintanar/pipelines-project/blob/main/output/g3.jpg)

![gráfico4](https://github.com/sonia-quintanar/pipelines-project/blob/main/output/g4.jpg)

Después de analizar los datos anteriores, vamos realizar llamadas a la API de Amazon para que nos devuelva los vinos españoles que se venden en su página web y si coinciden con las ventas obtenidas en los datos anteriomente mencionados.

Como resultado, podemos observar que