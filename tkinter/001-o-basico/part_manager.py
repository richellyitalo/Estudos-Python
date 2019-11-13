from tkinter import *

# Instancia do programa
app = Tk()

# bloco
part_text = StringVar()
part_label = Label(app, text='Part', font=('bold', 11), pady=20, padx=5)
part_label.grid(row=0, column=0, sticky=W)
part_entry = Entry(app, textvariable=part_text)
part_entry.grid(row=0, column=1)

# Cliente
cliente_text = StringVar()
cliente_label = Label(app, text='Cliente', font=('bold', 11), pady=20, padx=5)
cliente_label.grid(row=0, column=2, sticky=W)
cliente_entry = Entry(app, textvariable=cliente_text)
cliente_entry.grid(row=0, column=3)

# Varejista
varejista_text = StringVar()
varejista_label = Label(app, text='Varejista', font=('bold', 11), pady=0, padx=5)
varejista_label.grid(row=1, column=0, sticky=W)
varejista_entry = Entry(app, textvariable=varejista_text)
varejista_entry.grid(row=1, column=1)

# Preço
preco_text = StringVar()
preco_label = Label(app, text='Preço', font=('bold', 11), pady=0, padx=5)
preco_label.grid(row=1, column=2, sticky=W)
preco_entry = Entry(app, textvariable=preco_text)
preco_entry.grid(row=1, column=3)

# lista
parts_list = Listbox(app, height=8)

app.title('Gerenciador de qualquer coisa')
app.geometry('800x600')

# inicio do programa'
app.mainloop()
