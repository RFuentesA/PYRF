from tkinter import *
import tkinter as tk
#Ricardo Armando Fuentes Arevalo 10/09/2024
class ventanaInicio(Tk):

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.title("Ventana Inicio")
        self.geometry("285x225")
        boton1 = tk.Button(self, text="Ventana principal", command=self.abrirVentanaPrincipal)
        boton1.pack(anchor="c", pady=85)
        self.mainloop()

    def abrirVentanaPrincipal(self):
        if not VentanaPrincipal.en_uso:
            self.ventanaPrincipal = VentanaPrincipal()
            self.ventanaPrincipal.ventanaInicio = self
            self.iconify()


class VentanaPrincipal(Toplevel):
    en_uso = False
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Ventana principal")
        self.geometry("285x225")

        menubar1 = tk.Menu(self)
        self.config(menu=menubar1)
        opciones1 = tk.Menu(menubar1)
        opciones1.add_command(label="Salir", command=self.salirVentanaPrincipal)
        menubar1.add_cascade(label="Archivo", menu=opciones1)         

    def salirVentanaPrincipal(self):
        self.__class__.en_uso = False
        self.ventanaInicio.deiconify()
        return super().destroy()

ventana1 = ventanaInicio()