import numpy as np
from pandas import DataFrame
import matplotlib.pyplot as plt

class acp():
    def __init__(self, t, variabile=None):
        if variabile is None:
            variabile = list(t)
        self.__x = t[variabile].values

    def creare_model(self, std=True, nlib=0):
        x_ = self.x - np.mean(self.x, axis=0)
        if std:
            x_ = x_ / np.std(self.x, axis=0)
        n, m = np.shape(x_)
        r_cov = (1 / (n - nlib)) * x_.T @ x_
        valp, vecp = np.linalg.eig(r_cov)
        k = np.flipud(np.argsort(valp))
        self.__alfa = valp[k]
        self.__a = vecp[:, k]
        self.__c = x_ @ self.__a
        self.etichete_componente = ["comp" + str(i + 1) for i in range(m)]
        # Aplicare criterii de semnificatie pentru componente
        if std:
            self.nrcomp_k = np.where(self.alfa < 1)[0][0]
        else:
            self.nrcomp_k = None
        pondere = np.cumsum(self.alfa / sum(self.alfa))
        self.nrcomp_p = np.where(pondere > 0.8)[0][0] + 1
        eps = self.alfa[:(m - 1)] - self.alfa[1:]
        # print(eps)
        sigma = eps[:(m - 2)] - eps[1:]
        # print(sigma)
        negative = sigma < 0
        if any(negative):
            self.nrcomp_c = np.where(negative)[0][0] + 2
        else:
            self.nrcomp_c = None
        if std:
            self.r_xc = self.a*np.sqrt(self.alfa)
        else:
            self.r_xc = np.corrcoef(self.__x,self.__c,rowvar=False)[:m,m:]
        return self.__c

    def tabelare_varianta(self):
        procent_varianta = self.__alfa * 100 / np.sum(self.__alfa)
        tabel_varianta = DataFrame(
            data={
                "Varianta": self.__alfa,
                "Procent varianta": procent_varianta,
                "Varianta cumulata": np.cumsum(self.__alfa),
                "Procent cumulat": np.cumsum(procent_varianta)
            }, index=self.etichete_componente
        )
        return tabel_varianta

    def plot_varianta(self):
        fig = plt.figure("Plot Varianta", figsize=(12, 7))
        ax = fig.add_subplot(1, 1, 1)
        assert isinstance(ax, plt.Axes)
        ax.set_title("Plot varianta", fontdict={"fontsize": 18, "color": 'b'})
        ax.set_xlabel("Componente", fontdict={"fontsize": 12, "color": 'b'})
        ax.set_ylabel("Varianta", fontdict={"fontsize": 12, "color": 'b'})
        m = len(self.__alfa)
        x = np.arange(1, m + 1)
        ax.set_xticks(x)
        ax.plot(x, self.__alfa)
        ax.scatter(x, self.__alfa, c='r')
        if self.nrcomp_k is not None:
            ax.axhline(1, c='g', label="Kaiser")
        if self.nrcomp_c is not None:
            ax.axhline(self.alfa[self.nrcomp_c-1], c='m', label="Cattell")
        ax.axhline(self.alfa[self.nrcomp_p - 1], c='c', label="Procent acoperire > 80%")

        ax.legend()
        return self.nrcomp_c,self.nrcomp_k

    def show_grafice(self):
        plt.show()

    @property
    def x(self):
        return self.__x

    @property
    def a(self):
        return self.__a

    @property
    def alfa(self):
        return self.__alfa

    @property
    def c(self):
        return self.__c