import  tkinter
import customtkinter
from configparser import ConfigParser


def main_start():
    setup = ConfigParser()
    setup.read("conf.ini")
    initial_color = setup.get('THEME', 'color')
    initial_appearance = setup.get('THEME', 'appearance')
    if setup.get('THEME', 'color') == "":
        initial_color = "blue"
    if setup.get('THEME', 'appearance') == "":
        initial_appearance = "light"
    customtkinter.set_appearance_mode(initial_appearance)
    customtkinter.set_default_color_theme(initial_color) #To można zmienić w ustawieniach

    root = customtkinter.CTk() #Główne pole działania(kontener), lepiej nie tykac
    root.geometry("300x400")
    menu(root)


def hide(widget): #Jak chcesz cos schować, to wywołaj tą funkcje z nazwą elemntu
    widget.pack_forget()


def show(widget): #A tu magicznie przywracać
    widget.pack()


def menu(root):
    def login():
        def login_action():
            # Tu ma być logika bazy danych logowania
            if entry1.get() == "user" and entry2.get() == "passwd": #Test działania - check
                print("ol")
            else:
                print("null")

        def hide_frame():
            # Chowanie frame logowania - Powrót do menu
            frame.pack_forget()

        hide(frame_main)
        # chowanie menu
        # Panel logowania należy do login()
        frame = customtkinter.CTkFrame(master=root)
        frame.pack(pady=20, padx=10, fill="both", expand=True)

        back = customtkinter.CTkButton(master=frame, text="Back", command=lambda: [hide_frame(), menu(root)]) #Powrót do menu, usuwa frame i odpala główną funcje menu od nowa
        back.pack(pady=12, padx=10)

        label = customtkinter.CTkLabel(master=frame, text="Login")  # Napis nad panelem logowania
        label.pack(pady=12, padx=10)

        entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
        entry1.pack(pady=12, padx=10)

        entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
        entry2.pack(pady=12, padx=10)

        button_log = customtkinter.CTkButton(master=frame, text="login", command=login_action)  #Przycisk login odwołuje do login_action() czyli skrypt łaczenia do bazy
        button_log.pack(pady=12, padx=10)

        checkbox = customtkinter.CTkCheckBox(master=frame, text="Remember me")
        checkbox.pack(pady=10, padx=10)

    def settings():
        def save_set(coloor, appearancew):
            conf = ConfigParser()
            conf["THEME"] = {
                "color": coloor,
                "appearance": appearancew
            }
            with open("conf.ini", "w") as w:
                conf.write(w)

        def color_change(value):
            customtkinter.set_default_color_theme(value)

        def theme_change(value):
            customtkinter.set_appearance_mode(value)
        hide(frame_main)

        frame_set = customtkinter.CTkFrame(master=root)
        frame_set.pack(pady=20, padx=10, fill="both", expand=True)

        label = customtkinter.CTkLabel(master=frame_set, text="Main theme")  # Napis nad panelem logowania
        label.pack(pady=12, padx=10)

        theme = customtkinter.CTkSegmentedButton(master=frame_set,dynamic_resizing=True, values=["blue", "green", "dark-blue"], command=color_change)
        theme.pack(pady=12, padx=10)

        appearance = customtkinter.CTkSegmentedButton(master=frame_set, dynamic_resizing=True, values=["dark", "light", "system"], command=theme_change)
        appearance.pack(pady=12, padx=10)

        back = customtkinter.CTkButton(master=frame_set, text="Apply", command=lambda: [save_set(theme.get(), appearance.get()), hide(frame_set), menu(root)])  # Powrót do menu, usuwa frame i odpala główną funcje menu od nowa
        back.pack(pady=12, padx=10)

    #panel menu poniżej należy do menu(root)
    frame_main = customtkinter.CTkFrame(master=root)
    frame_main.pack(pady=20, padx=10, fill="both", expand=True)

    login_button = customtkinter.CTkButton(master=frame_main, text="login", command=login)
    login_button.pack(pady=12, padx=10)

    settings = customtkinter.CTkButton(master=frame_main, text="Settings", command=settings)
    settings.pack(pady=12, padx=10)

    exit_button = customtkinter.CTkButton(master=frame_main, text="Exit", command=quit)
    exit_button.pack(pady=12, padx=10)

    root.mainloop()


main_start()
