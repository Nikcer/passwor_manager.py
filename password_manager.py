from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import webbrowser


#-------------SAVE---------------

def save():


    # Append-adds at last
    website = wbsite_entry.get()
    email = email_entry.get()
    password = password_entry.get()


    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Errore", message="Controlla che il campo email o password non siano vuoti!")
    else:


        is_ok= messagebox.askokcancel(title=website, message="Salvare la password?" )

    #salvare in file txt

        if is_ok:

            with open("data.txt", "a") as data_file: # append mode

                data_file.write(f"{website} | {email} | {password}\n")
                # cancellare i box dopo salvataggio
                wbsite_entry.delete(0, END)
                email_entry.delete(0, END)
                password_entry.delete(0, END)













#--------------UI setup-----------
root = Tk()
root.title("Password Manager")
root.geometry("600x200")
root.config(padx=20, pady=20)

#Label
wbsite_label =Label(text="Website:", font=("Times New Roman", 15))
wbsite_label.grid(row=0, column=0)


email_label =Label(text="Email/UserName:", font=("Times New Roman", 15))
email_label.grid(row=1, column=0)

password_label =Label(text="Password:", font=("Times New Roman", 15))
password_label.grid(row=2, column=0)

#ENTRY

wbsite_entry = Entry(width=27, font=("Times New Roman", 20))
wbsite_entry.grid(row=0, column=1)

email_entry = Entry(width=27, font=("Times New Roman", 20))
email_entry.grid(row=1, column=1)


password_entry = Entry(width=27, font=("Times New Roman", 20))
password_entry.grid(row=2, column=1)
# my_entry= Entry(wbsite_label,font=("Times New Roman" , 20))
# my_entry.pack(pady=20)

#BOTTONE
add_button = Button(text="Salva la password!", width=36, command=save)
add_button.grid(row=3, column=1, padx=10)


root.mainloop()