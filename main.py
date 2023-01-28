import tkinter
import customtkinter


def main_start():
    customtkinter.set_appearance_mode("System")
    customtkinter.set_default_color_theme("green")

    root = customtkinter.CTk()
    root.geometry("500x350")
    menu(root)


def hide_button(widget):
    # This will remove the widget from toplevel
    widget.pack_forget()


def show_button(widget):
    # This will recover the widget from toplevel
    widget.pack()


def menu(root):
    def login():
        def login_action():
            if entry1.get() == "user" and entry2.get() == "passwd":
                print("ol")
            else:
                print("null")
        hide_button(button)

        back = customtkinter.CTkButton(master=frame, text="Back", command=main_start)
        back.pack(pady=12, padx=10)

        label = customtkinter.CTkLabel(master=frame, text="Login")
        label.pack(pady=12, padx=10)

        entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
        entry1.pack(pady=12, padx=10)

        entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
        entry2.pack(pady=12, padx=10)

        button_log = customtkinter.CTkButton(master=frame, text="login", command=login_action)
        button_log.pack(pady=12, padx=10)

        checkbox = customtkinter.CTkCheckBox(master=frame, text="Remember me")
        checkbox.pack(pady=10, padx=10)



    frame = customtkinter.CTkFrame(master=root)
    frame.pack(pady=20, padx=10, fill="both", expand=True)

    button = customtkinter.CTkButton(master=frame, text="login", command=login)
    button.pack(pady=12, padx=10)
    root.mainloop()


main_start()
