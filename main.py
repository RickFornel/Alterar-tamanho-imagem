from tkinter import *
from tkinter.filedialog import *
from tkinter import messagebox
from PIL import Image

# cores

co0 = "#000000"  # black
co1 = "#cc1d4e"  # red
co2 = "#feffff"  # white
co3 = "#0074eb"  # blue
co4 = "#435e5a"  # green-water
co5 = "#59b356"  # green
co6 = "#d9d9d9"  # grey

# criando window

janela = Tk()
janela.title('')
janela.geometry('350x300')
janela.config(bg=co2)

# criando frame

frame_principal = Frame(janela, width=350, height=300, bg=co2)
frame_principal.grid(row=0, column=0, sticky=NSEW)

# funções

def clique_new():
    # abrindo imagem
    global img
    ficheiro = askopenfilename()
    img = Image.open(ficheiro)
    # pegando dimensões originais
    img_largura, img_altura = img.size
    
    label_2 = Label(frame_principal, text='Altura e largura original: ' +str(img_largura) + ' x ' + str(img_altura), font='Arial 10 bold', width=28, height=1,
                                    padx= 5, pady= 5, anchor=CENTER, bg= co2, fg= co0)
    label_2.grid(row=3, column=0, columnspan=2, sticky=NSEW, pady=1)

    label_3 = Label(frame_principal, text='Digite a nova largura:', font='Arial 10 ', width=10, height=1,
                                    padx= 5, pady= 5, anchor=CENTER, bg= co2, fg= co0)
    label_3.grid(row=4, column=0,  sticky=NSEW, pady=1)

    label_4 = Label(frame_principal, text='Digite a nova altura:', font='Arial 10 ', width=10, height=1,
                                    padx= 5, pady= 5, anchor=CENTER, bg= co2, fg= co0)
    label_4.grid(row=4, column=1,  sticky=NSEW, pady=1)

    entry_widht.grid(row=5, column=0,  sticky=NSEW, pady=1)
    entry_height.grid(row=5, column=1,  sticky=NSEW, pady=1)
    
    button_converter = Button(frame_principal,command=converter_img, text='CONVERTER', font='Arial 10 bold', bg= co5, fg= co2)
    button_converter.grid(row=6, column=0, columnspan=2,  pady=1)

    
    

def converter_img():
    new_height = int(entry_height.get())
    new_width = int(entry_widht.get())
    new_tam = new_height, new_width
    nova_img = img.resize(new_tam)
    img_salvar = asksaveasfilename()
    nova_img.save(img_salvar+'.jpg')

    messagebox.showinfo('','Tamanho da imagem alterado com sucesso!')

# criando labels

label_1 = Label(frame_principal, text='Comprensor de Imagem', font='Arial 15 bold', width=28, height=1,
                                    padx= 5, pady= 5, anchor=CENTER, bg= co2, fg= co0)
label_1.grid(row=0, column=0, columnspan=2, sticky=NSEW, pady=1)

button_add = Button(frame_principal, text='+ NOVO', font='Arial 10 bold', bg= co3, fg= co2, command=clique_new)
button_add.grid(row=1, column=0, columnspan=2, sticky=NSEW, pady=1)

entry_widht = Entry(frame_principal, text='', font='Arial 10 ', width=10)
#entry_widht.grid(row=5, column=0,  sticky=NSEW, pady=1)

entry_height = Entry(frame_principal, text='', font='Arial 10 ', width=10)
#entry_height.grid(row=5, column=1,  sticky=NSEW, pady=1)

janela.mainloop()