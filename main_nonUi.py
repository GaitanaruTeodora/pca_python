import numpy as np
from pandas import *
from acp import acp
from functii import nan_replace, tabelare_matrice
from grafice import plot_corelatii, corelograma, plot_instante

t = read_csv("DMed2.csv", index_col=0)
print(t)

if any(t.isna()):
    nan_replace(t)
print("----")
variabile = list(t)[:]
print(variabile)

model_acp = acp(t, variabile)
model_acp.creare_model(std=True,nlib=0)
# print(model_acp.alfa)

tabel_varianta = model_acp.tabelare_varianta()
tabel_varianta.to_csv("Output/Varianta.csv")
print(tabel_varianta)
model_acp.plot_varianta()
r_xc = model_acp.r_xc
# print(r_xc)
r_xc_t = tabelare_matrice(r_xc, variabile,
                          model_acp.etichete_componente, "Output/r_xc.csv")

plot_corelatii(r_xc_t, "comp1", "comp2", aspect=1)
plot_corelatii(r_xc_t, "comp3", "comp4", aspect=1)
corelograma(r_xc_t)

c = model_acp.c
c_t = tabelare_matrice(c, t.index, model_acp.etichete_componente, "Output/c.csv")

nrcomp = model_acp.nrcomp_p
if model_acp.nrcomp_c is not None:
    if model_acp.nrcomp_c<nrcomp:
        nrcomp=model_acp.nrcomp_c
if model_acp.nrcomp_k is not None:
    if model_acp.nrcomp_k<nrcomp:
        nrcomp=model_acp.nrcomp_k

for i in range(1, nrcomp):
    plot_instante(c_t, "comp1", model_acp.etichete_componente[i], aspect=1)

s = c / np.sqrt(model_acp.alfa)
# Tabelare si desenare plot pentru scoruri

# Calcul cosinusuri
c2 = c * c
cosin = np.transpose(c2.T / np.sum(c2, axis=1))
cosin_t = tabelare_matrice(cosin, t.index,
                           model_acp.etichete_componente, "Output/cosin.csv")
# Calcul contributii
beta = c2 * 100 / np.sum(c2, axis=0)
beta_t = tabelare_matrice(beta, t.index,
                          model_acp.etichete_componente,
                          "Output/contrib.csv")
# Calcul comunalitati
r_xc2 = r_xc * r_xc
comm = np.cumsum(r_xc2, axis=1)
comm_t = tabelare_matrice(comm, variabile, model_acp.etichete_componente, "Output/comm.csv")
corelograma(comm_t, vmin=0, titlu="Comunalitati")

model_acp.show_grafice()
