import tkinter as tk

ventana=tk.Tk()
ventana.title("HolaMundo")
#anchoxAlto
ventana.geometry('380x300')
ventana.configure(background="dark turquoise")
etiqueta1=tk.Label(ventana,text="Colombia", bg="red", fg="white")
etiqueta1.pack(fill=tk.X)
etiqueta2=tk.Label(ventana,text="Argentina", bg="blue", fg="white")
etiqueta2.pack(side=tk.LEFT)

ventana.mainloop()

#comentario para ver que pas en git

