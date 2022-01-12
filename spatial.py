import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import geopandas as gp
import tk_gui as gui

def plot_map(nume_fisier_shape, S, coduri, titlu="Harta scoruri", clasificator=False):
    m = np.shape(S)[1]
    shp = gp.GeoDataFrame.from_file(nume_fisier_shape)
    campuri_shape = [shp.columns[i] for i in range(0, len(shp.columns))]
    camp_legatura = gui.Check(campuri_shape, "Selectati variabila index")[0]
    t = pd.DataFrame(data={'coduri': coduri})
    for i in range(m):
        t.insert(1, 'v' + str(i + 1), S[:, i], allow_duplicates=True)
    shp1 = pd.merge(shp, t, left_on=camp_legatura, right_on='coduri')
    for i in range(m):
        f = plt.figure(titlu + str(i + 1), figsize=(8, 7))
        f1 = f.add_subplot(1, 1, 1)
        f1.set_title(titlu + str(i + 1))
        if clasificator:
            shp1.plot('v' + str(i + 1), cmap='Reds', ax=f1, legend=True, scheme='fisher_jenks')
        else:
            shp1.plot('v' + str(i + 1), cmap='Reds', ax=f1, legend=True)