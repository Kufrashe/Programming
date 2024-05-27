"""
    THIS IS A SIMPLE BOT, FOR GENERAL COMMUNICATION
"""

import tkinter as tk

window = tk.Tk()
window.title("AI Bot 101")

main_frame = tk.Frame(window, bg="grey", relief="ridge", borderwidth=5)
main_frame.rowconfigure([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], minsize=1, pad=5)
main_frame.columnconfigure([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], minsize=1, pad=5)
main_frame.grid(row= 1, column=1, sticky="nsew")

def bot():
    lbl_bot_name = tk.Label(main_frame, bg="grey", fg="blue", font=("Unispace", 15), text="Bot Name")
    ent_bot_name = tk.Entry(main_frame, bg="white", fg="black", font=("Unispace", 15), relief="groove")
    lbl_bot_name.grid(row=0, column=0, sticky="nsew")
    ent_bot_name.grid(row=1, column=0, sticky="nsew")
    def submit():
        details = ent_bot_name.get()
        if details == "":
            ent_bot_name.insert(1, "Invalid Option")
        print(details)
        return details
    bot_name = submit()
    btn_submit = tk.Button(window, bg="blue", fg="yellow", font=("Unispace", 15), text="SUBMIT", command=submit)
    btn_submit.grid(row=2, column=0, sticky="nsew")
    return bot_name

bot_1 = bot()

def user():
    lbl_username = tk.Label(main_frame, bg="grey", fg="blue", font=("Unispace",15), relief="ridge", text="Username")
    ent_username = tk.Entry(main_frame, bg="white", fg="blue", font=("Unispace", 15), relief="ridge")
    lbl_username.grid(row=0, column=1, sticky="nsew")
    ent_username.grid(row=1, column=1, sticky="nsew")
    def submit_user():
        user_det = ent_username.get()
        if user_det == "":
            ent_username.insert(0, "Unspecified User")
        print(user_det)
        return user_det
    username = submit_user()
    btn_user_submit = tk.Button(window, bg="blue", fg="yellow", font=("Unispace", 15), text="SUBMIT USERNAME", command=submit_user)
    btn_user_submit.grid(row=2, column=1, sticky="nsew")
    return username

user_1 = user()
def communication():
    txt_comm_box= tk.Text(main_frame, bg="black", fg="green", font=("Arial", 15), relief="sunken", borderwidth=10, padx=10, pady=10)
    txt_comm_box.insert(tk.END, "Hello there {} how can l help you today".format(user_1))
    txt_comm_box.grid(row=3, column=0, sticky="nsew")
    def communicate():
        comm_text = txt_comm_box.get(0, tk.END)
        return comm_text
    btn_communicate = tk.Button(window, bg="yellow", fg="green", font=("Unispace", 20), text="COMMUNICATE", command=communicate)
    btn_communicate.grid(row=2, column=2, sticky="nsew")
    text_fetch = communicate
    return text_fetch

comm = communication()

print(comm)
    

window.mainloop()