import tkinter as tk
#Ricardo Armando Fuentes Arevalo 7/septiempre/2024
texto = []
def cojerTexto():
    texto.append(cajita.get())
    for i in range(len(texto)):
        Lista.insert(0, texto[0])
        texto.pop(0)


ventana = tk.Tk()
ventana.title("Agragar Nombres")
ventana.geometry("300x300")

label = tk.Label(ventana, text="Nombre:")
label.grid(row=0, column=0, padx=10)

cajita = tk.Entry(ventana, textvariable=tk.StringVar(ventana,value=""))
cajita.grid(row=0, column=1,padx=10,pady=10,sticky="n")

btn = tk.Button(ventana, text="Agregar", padx=5, pady=5, command=cojerTexto)
btn.grid(row=0, column=2)

Lista = tk.Listbox(ventana)
Lista.grid(row=1, column=1, pady=10)

ventana.mainloop()