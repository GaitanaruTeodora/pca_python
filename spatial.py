import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def harta(shp, S, camp_legatura, nume_instante, titlu="Harta scoruri"):
    m = np.shape(S)[1]
    t = pd.DataFrame(data={"coduri": nume_instante})
    for i in range(m):
        t["v" + str(i + 1)] = S[:, i]
    shp1 = pd.merge(shp, t, left_on=camp_legatura, right_on="coduri")
    for i in range(m):
        f = plt.figure(titlu + "-" + str(i + 1), figsize=(10, 7))
        ax = f.add_subplot(1, 1, 1)
        ax.set_title(titlu + "-" + str(i + 1))
        shp1.plot("v" + str(i + 1), cmap="Reds", ax=ax, legend=True)
    plt.show()
