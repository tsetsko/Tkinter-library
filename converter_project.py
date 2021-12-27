from tkinter import *
from tkinter import messagebox
import re

windows = Tk()

# Functions
def converter():
    kilo = float(input_kilo.get())
    print(kilo)
    gram.insert(END, kilo * 1000)
    pounds.insert(END, kilo * 2.20462)
    ounces.insert(END, kilo * 35.274)
    
def delete_fields():
    gram.delete(0, 'end')
    pounds.delete(0, 'end')
    ounces.delete(0, 'end')

def validation():
    name = input_kilo.get()
    msg = ''

    if len(name) == 0:
        msg = 'name can\'t be empty'
    else:
        try:
            if re.search('[a-zA-Z]', name):
                msg = 'Name can\'t have letters'
            # elif len(name) <= 1:
            #     msg = 'name is too short.'
            # elif len(name) > 5:
            #     msg = 'name is too long.'
            else:
                msg = 'Success!'
        except Exception as ep:
            messagebox.showerror('error', ep)
        
    messagebox.showinfo('message', msg)

# Buttons
convert_button = Button(windows, text='Convert', command=lambda:[validation(), converter()])
convert_button.grid(row=0, column=2)

delete_button = Button(windows, text='Clear', command=delete_fields)
delete_button.grid(row=3, column=2)

# Results
label_text = Label(windows, text='Kilograms to convert:')
label_text.grid(row=0, column=0)

input_kilo = StringVar()
kilo_field = Entry(windows, textvariable=input_kilo)
kilo_field.grid(row=0, column=1)

gram_text = Label(windows, text='Kilograms to gram:')
gram_text.grid(row=1, column=0)

return_gram = StringVar()
gram = Entry(windows, textvariable=return_gram)
gram.grid(row=2, column=0)

pound_text = Label(windows, text='Kilograms to pound:')
pound_text.grid(row=1, column=1)

return_pounds = StringVar()
pounds = Entry(windows, textvariable=return_pounds)
pounds.grid(row=2, column=1)

ounces_text = Label(windows, text='Kilograms to ounces:')
ounces_text.grid(row=1, column=2)

return_ounces = StringVar()
ounces = Entry(windows, textvariable=return_ounces)
ounces.grid(row=2, column=2)

windows.mainloop()