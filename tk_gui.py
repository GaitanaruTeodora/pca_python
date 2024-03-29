import tkinter as tk
import tkinter.ttk as ttk

def Check2(optiuni1, optiuni2, mesaj="Selectati una sau mai multe optiuni"):
    def selectie_toate():
        for o_chk in variabile_continut1:
            o_chk.set(1)
        for o_chk in variabile_continut2:
            o_chk.set(1)

    def deselectare():
        for o_chk in variabile_continut1:
            o_chk.set(0)
        for o_chk in variabile_continut2:
            o_chk.set(0)

    frame = tk.Tk()
    tk.Label(master=frame, text=mesaj, font=('Times', '14')).grid(row=0, sticky=tk.W)
    tk.Button(master=frame, command=selectie_toate, text="Selectie toate", font=('Times', '14')).grid(row=1, column=0,
                                                                                                      sticky=tk.W)
    tk.Button(master=frame, command=deselectare, text="Deselectare", font=('Times', '14')).grid(row=1, column=1,
                                                                                                sticky=tk.W)
    variabile_continut1 = []
    for i in range(len(optiuni1)):
        variabile_continut1.append(tk.IntVar())
        tk.Checkbutton(master=frame, text=optiuni1[i],
                       variable=variabile_continut1[i]).grid(row=i + 2, column=0, sticky=tk.W)
    variabile_continut2 = []
    for i in range(len(optiuni2)):
        variabile_continut2.append(tk.IntVar())
        tk.Checkbutton(master=frame, text=optiuni2[i],
                       variable=variabile_continut2[i]).grid(row=i + 2, column=1, sticky=tk.W)
    tk.mainloop()
    selectii1 = []
    selectii2 = []
    for i in range(len(optiuni1)):
        if variabile_continut1[i].get() == 1:
            selectii1.append(optiuni1[i])
    for i in range(len(optiuni2)):
        if variabile_continut2[i].get() == 1:
            selectii2.append(optiuni2[i])
    return selectii1, selectii2


def Combo(optiuni, mesaj="Selectati o optiune"):
    optiuni_str = [str(o) for o in optiuni]
    frame = tk.Tk()
    frame.geometry("300x150")
    frame.title("Selector Combobox")
    ttk.Label(master=frame, text=mesaj, font=('Times', '14')).grid(row=1, sticky=tk.W)
    variabila_continut = tk.StringVar()
    cb = ttk.Combobox(master=frame, textvariable=variabila_continut,
                      values=optiuni_str, font=('Times', '14'))
    cb.grid(row=3, sticky=tk.W)
    cb.current(0)
    frame.mainloop()
    return variabila_continut.get()


def Check(optiuni, mesaj="Selectati una sau mai multe optiuni"):
    def selectie_toate():
        for o_chk in variabile_continut:
            o_chk.set(1)

    def deselectare():
        for o_chk in variabile_continut:
            o_chk.set(0)

    frame = tk.Tk()
    tk.Label(master=frame, text=mesaj, font=('Times', '14')).grid(row=0, sticky=tk.W)
    tk.Button(master=frame, command=selectie_toate, text="Selectie toate", font=('Times', '14')).grid(row=1, column=0,
                                                                                                      sticky=tk.W)
    tk.Button(master=frame, command=deselectare, text="Deselectare", font=('Times', '14')).grid(row=1, column=1,
                                                                                                sticky=tk.W)
    variabile_continut = []
    for i in range(len(optiuni)):
        variabile_continut.append(tk.IntVar())
        chk_b = tk.Checkbutton(master=frame, text=optiuni[i],
                               variable=variabile_continut[i]).grid(row=i + 2, sticky=tk.W)
    tk.mainloop()
    selectii = []
    for i in range(len(optiuni)):
        if variabile_continut[i].get() == 1:
            selectii.append(optiuni[i])
    return selectii