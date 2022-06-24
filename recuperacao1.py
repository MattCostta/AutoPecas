from tkinter import *




root = Tk()
root.title


frame1 = LabelFrame(root)
frame2 = LabelFrame(root)
frame3 = Frame(root)

frame1.pack()

root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_rowconfigure(4, weight=1)
root.grid_rowconfigure(5, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_columnconfigure(3, weight=1)
root.grid_columnconfigure(4, weight=1)
root.grid_columnconfigure(5, weight=1)


#frame1


lb1_fr1 = Label (frame1, text= 'EletroInfo do Joao banana', font='arial 25')
bt1_fr1 = Button(frame1, text='Cadastrar peças', font='arial 18', command= lambda : [frame1.pack_forget(), frame2.pack()])
bt2_fr1 = Button(frame1, text='Listagem/Estoque', font='arial 18', command= lambda : [frame1.pack_forget(), frame3.pack()])




#Labels and Buttons
lb1_fr1.grid(row= 0, column=0, columnspan=4, sticky=NSEW)
bt1_fr1.grid(row=3, column= 1, sticky=NSEW)
bt2_fr1.grid(row=4, column= 1, sticky=NSEW)


#frame2

lb1_fr2 = Label (frame2, text= 'Cadastro', font='arial 25')

en1_fr2 = Entry (frame2, font='arial 15')

lb2_fr2 = Label (frame2, text='Código', font='arial 15' )
en2_fr2 = Entry (frame2, font='arial 15')

lb3_fr2 = Label (frame2, text='Descrição', font='arial 15')
en3_fr2 = Entry (frame2, font='arial 15')

lb4_fr2 = Label (frame2, text='Fabricante', font='arial 15')
en4_fr2 = Entry (frame2,font='arial 15')

lb5_fr2 = Label(frame2, text='Quantidade', font='arial 15')
en5_fr2 = Entry (frame2, font='arial 15')

lb6_fr2 = Label(frame2, text='Valor', font='arial 15')
en6_fr2 = Entry (frame2, font='arial 15')

bt1_fr2 = Button (frame2, text='Finalizar cadastro', font='arial 18', command= lambda : [frame2.pack_forget(),frame3.pack()])
bt2_fr2 = Button (frame2, text='Voltar', font='arial 18', command= lambda : [frame2.pack_forget(),frame1.pack()])
bt3_fr2 = Button (frame2, text='Cadastrar fabricante', font='arial 18')

#Labels
lb1_fr2.grid(row=0, column=0, columnspan=4, sticky=NSEW)
lb2_fr2.grid(row=1, column=0)
lb3_fr2.grid(row=2, column=0)
lb4_fr2.grid(row=3, column=0)
lb5_fr2.grid(row=4, column=0)
lb6_fr2.grid(row=4, column=2)

#Entry
en1_fr2.grid(row=1, column=1, sticky=NSEW)
en2_fr2.grid(row=2, column=1, sticky=NSEW)
en3_fr2.grid(row=3, column=1, sticky=NSEW)
en4_fr2.grid(row=4, column=1, sticky=NSEW)
en5_fr2.grid(row=4, column=1, sticky=NSEW)
en6_fr2.grid(row=4, column=3, sticky=NSEW)

#Buttons
bt1_fr2.grid(row=5, column=1, sticky = NSEW)
bt2_fr2.grid(row=5, column=2, sticky = NSEW)
bt3_fr2.grid(row=4, column=5)


#frame3
lb3_fr3 = Label (frame3, text= 'Estoque do Joao Banana', font='arial 25')























root.mainloop()