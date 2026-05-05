from tkcalendar import DateEntry
import tkinter as tk
from PIL import Image, ImageTk
import json

class App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("800x600")
        self.root.title("Application de vote électronique de EMINES")

        # charger image originale
        self.image_accueil = Image.open("New board 1.png")
        self.image_register = Image.open("Inscription.png")
        self.image_login = Image.open("Login.png")
        self.image_mot_de_passe_oublié = Image.open("mot de passe oblié1.png")
        self.accueil_frame=tk.Frame(root)
        self.register_frame=tk.Frame(root)
        self.login_frame=tk.Frame(root)
        self.mot_de_passe_oublié_frame=tk.Frame(root)

        self.accueil_frame.pack(fill="both", expand=True)
        # label pour afficher l'image
        self.label_accueil = tk.Label(self.accueil_frame)
        self.label_accueil.pack(fill="both", expand=True)

        self.label_register = tk.Label(self.register_frame)
        self.label_register.pack(fill="both", expand=True)

        self.label_login = tk.Label(self.login_frame)
        self.label_login.pack(fill="both", expand=True)

        self.label_mot_de_passe_oublié = tk.Label(self.mot_de_passe_oublié_frame)
        self.mot_de_passe_oublié_frame.pack(fill="both", expand=True)

        # mettre à jour l'image quand la fenêtre change

        self.accueil_frame.bind("<Configure>", self.resize_image_accueil)
        self.register_frame.bind("<Configure>", self.resize_image_register)
        self.login_frame.bind("<Configure>", self.resize_image_login)
        self.mot_de_passe_oublié_frame.bind("<Configure>", self.resize_image_mot_de_passe_oublié)
        self.button_register = tk.Button(root,
    text="S'inscrire",
    fg="white",              
    bg="#048b9a",           
    activeforeground="white",
    borderwidth=0,
    highlightthickness=0,height=1,
    relief="flat",command=self.show_register_frame)
        self.button_register.place(relx=0.13, rely=0.05, anchor="center")

        self.button_login = tk.Button(root, text="Login",
    fg="white",              
    bg="#048b9a",           
    activeforeground="white",
    borderwidth=0,
    highlightthickness=0,height=1,
    relief="flat",command=self.show_login_frame)
        self.button_login.place(relx=0.24, rely=0.05, anchor="center")
        

        self.button_accueil = tk.Button(root, text="Accueil",
    fg="white",              
    bg="#048b9a",           
    activeforeground="white",
    borderwidth=0,
    highlightthickness=0,
    relief="flat",command=self.show_accueil_frame)
        
        self.button_send1 = tk.Button(root, text="Envoyer",
    fg="white",              
    bg="#073763",           
    activeforeground="white",
    borderwidth=0,
    highlightthickness=0,
    relief="flat",font=20,command=self.register)
        
        self.button_send2 = tk.Button(root, text="Se connecter",
    fg="white",              
    bg="#073763",           
    activeforeground="white",
    borderwidth=0,
    highlightthickness=0,
    relief="flat",font=20,command=self.login)
        
        self.button_send3 = tk.Button(root, text="Vérifier",
    fg="white",              
    bg="#6FA8DC",           
    activeforeground="white",
    borderwidth=0,
    highlightthickness=0,
    relief="flat",font=20,command=self.login)
        
        self.button_send4 = tk.Button(root, text="Mot de passe oublié?",
    fg="black",              
    bg="white",           
    activeforeground="white",
    borderwidth=0,
    highlightthickness=0,
    relief="flat",font=20,command=self.login)

        self.menu_bar = tk.Menu(root)
        self.root.config(menu=self.menu_bar)
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)  
        self.menu_bar.add_cascade(label="Français", menu=self.file_menu)  
        self.file_menu.add_command(label="English")
        self.file_menu.add_command(label="العربية")

        self.email1=tk.Entry(root,bg="#eeeeee")
        self.password1=tk.Entry(root,bg="#eeeeee",show="*")

        self.email2=tk.Entry(root,bg="#eeeeee")
        self.password2=tk.Entry(root,bg="#eeeeee",show="*")

        self.label_mail=tk.Label(self.login_frame,text="Email",fg="black",font=14,bg="white")
        self.label_mail.place(relx=0.2, rely=0.35, anchor="center",width=320,height=30)

        self.label_password=tk.Label(self.login_frame,text="Mot de passe",fg="black",font=14,bg="white")
        self.label_password.place(relx=0.22, rely=0.45, anchor="center",width=320,height=30)

        self.prenom=tk.Entry(root,bg="#eeeeee")
        
        self.nom=tk.Entry(root,bg="#eeeeee")

        self.confirm=tk.Entry(root,bg="#eeeeee",show="*")

        self.date_entry = DateEntry(root, date_pattern='yyyy-mm-dd',bg="#eeeeee")

        self.choix = tk.StringVar()
        self.classe_2026 = tk.Radiobutton(root,text="2026", variable=self.choix, value="2026",bg="#b4c9de")
        self.classe_2027 = tk.Radiobutton(root,text="2027", variable=self.choix, value="2027",bg="#b4c9de")
        self.classe_2028 = tk.Radiobutton(root,text="2028", variable=self.choix, value="2028",bg="#b4c9de")
        self.classe_2029 = tk.Radiobutton(root,text="2029", variable=self.choix, value="2029",bg="#b4c9de")
        self.classe_2030 = tk.Radiobutton(root,text="2030", variable=self.choix, value="2030",bg="#b4c9de")
        self.root.after(100, self.fix_layout)
    def resize_image_accueil(self, event):
        # éviter bug quand fenêtre très petite
        if event.width > 1 and event.height > 1:
            resized = self.image_accueil.resize((event.width, event.height))
            self.photo_accueil = ImageTk.PhotoImage(resized)
            self.label_accueil.config(image=self.photo_accueil)
    def resize_image_register(self, event):
        # éviter bug quand fenêtre très petite
        if event.width > 1 and event.height > 1:
            resized = self.image_register.resize((event.width, event.height))
            self.photo_register = ImageTk.PhotoImage(resized)
            self.label_register.config(image=self.photo_register)
    def resize_image_login(self, event):
        # éviter bug quand fenêtre très petite
        if event.width > 1 and event.height > 1:
            resized = self.image_login.resize((event.width, event.height))
            self.photo_login = ImageTk.PhotoImage(resized)
            self.label_login.config(image=self.photo_login)
    def resize_image_mot_de_passe_oublié(self, event):
         # éviter bug quand fenêtre très petite
        if event.width > 1 and event.height > 1:
            resized = self.image_mot_de_passe_oublié.resize((event.width, event.height))
            self.photo_mot_de_passe_oublié = ImageTk.PhotoImage(resized)
            self.label_mot_de_passe_oublié.config(image=self.photo_mot_de_passe_oublié)

    def style_login(self, a):
        if a==1:
            self.button_login.config(bg="#048b9a",font=10)  
        if a==2:
            self.button_login.config(bg="#073763",font=20) 
    def style_register(self, b):
        if b==1:
            self.button_register.config(bg="#048b9a",fg="white",font=10)  
        if b==2:
            self.button_register.config(bg="#9fc5f8",font=20,fg="black")

    def show_register_frame(self):
        self.accueil_frame.pack_forget()
        self.login_frame.pack_forget()
        self.mot_de_passe_oublié_frame.pack_forget()
        self.register_frame.pack(fill="both", expand=True)
        self.button_accueil.place(relx=0.1, rely=0.06, anchor="center")
        self.button_login.place(relx=0.22, rely=0.6, anchor="center")
        self.style_login(2)
        self.button_register.place_forget()
        self.button_send2.place_forget()
        self.button_send3.place_forget()
        self.button_send4.place_forget()
        self.email1.place(relx=0.8, rely=0.23, anchor="center",width=180,height=30)
        self.password1.place(relx=0.8, rely=0.33, anchor="center",width=180,height=30)
        self.nom.place(relx=0.56, rely=0.33, anchor="center",width=180,height=30)
        self.prenom.place(relx=0.56, rely=0.23, anchor="center",width=180,height=30)
        self.confirm.place(relx=0.8, rely=0.47, anchor="center",width=180,height=30)
        self.date_entry.place(relx=0.56, rely=0.47, anchor="center",width=180,height=30)
        self.classe_2026.place(relx=0.52, rely=0.58, anchor="center",width=180)
        self.classe_2027.place(relx=0.52, rely=0.62, anchor="center",width=180)
        self.classe_2028.place(relx=0.52, rely=0.66, anchor="center",width=180)
        self.classe_2029.place(relx=0.52, rely=0.70, anchor="center",width=180)
        self.classe_2030.place(relx=0.52, rely=0.74, anchor="center",width=180)
        self.button_send1.place(relx=0.71, rely=0.83, anchor="center",width=100)
        self.email2.place_forget()
        self.password2.place_forget()
    def show_login_frame(self):
        self.accueil_frame.pack_forget()
        self.register_frame.pack_forget()
        self.mot_de_passe_oublié_frame.pack_forget()
        self.nom.place_forget()
        self.prenom.place_forget()
        self.confirm.place_forget()
        self.email1.place_forget()
        self.password1.place_forget()
        self.date_entry.place_forget()

        self.classe_2026.place_forget()
        self.classe_2027.place_forget()
        self.classe_2028.place_forget()
        self.classe_2029.place_forget()
        self.classe_2030.place_forget()
        self.button_send1.place_forget()
        self.login_frame.pack(fill="both", expand=True)
        self.button_accueil.place(relx=0.13, rely=0.08, anchor="center")
        self.button_login.place_forget()
        self.button_register.place(relx=0.82, rely=0.55, anchor="center")
        self.style_register(2)
        self.button_send2.place(relx=0.48, rely=0.5, anchor="center",width=150,height=35)
        self.email2.place(relx=0.3, rely=0.4, anchor="center",width=320,height=30)
        self.password2.place(relx=0.3, rely=0.5, anchor="center",width=320,height=30)
        self.button_send4.place(relx=0.3, rely=0.56, anchor="center")
    def show_accueil_frame(self):
        self.login_frame.pack_forget()
        self.register_frame.pack_forget()
        self.mot_de_passe_oublié_frame.pack_forget()
        self.nom.place_forget()
        self.prenom.place_forget()
        self.confirm.place_forget()
        self.date_entry.place_forget()

        self.classe_2026.place_forget()
        self.classe_2027.place_forget()
        self.classe_2028.place_forget()
        self.classe_2029.place_forget()
        self.classe_2030.place_forget()

        self.button_send1.place_forget()
        self.button_send2.place_forget()

        self.password1.place_forget()
        self.password2.place_forget()   # login aussi
        self.accueil_frame.pack(fill="both", expand=True)
        self.button_accueil.place_forget()
        self.button_login.place(relx=0.25, rely=0.05, anchor="center")
        self.button_register.place(relx=0.125, rely=0.05, anchor="center")
        self.style_register(1)
        self.style_login(1)
        self.email1.place_forget()
        self.email2.place_forget()

    def show_mot_de_passe_oublié_frame(self):
        self.login_frame.pack_forget()
        self.register_frame.pack_forget()
        self.accueil_frame.pack_forget()
        self.nom.place_forget()
        self.prenom.place_forget()
        self.confirm.place_forget()
        self.date_entry.place_forget()

        self.classe_2026.place_forget()
        self.classe_2027.place_forget()
        self.classe_2028.place_forget()
        self.classe_2029.place_forget()
        self.classe_2030.place_forget()

        self.button_send1.place_forget()
        self.button_send2.place_forget()
        self.button_send4.place_forget()
        self.password1.place_forget()
        self.password2.place_forget()   # login aussi
        self.accueil_frame.pack(fill="both", expand=True)
        self.button_accueil.place_forget()
        self.button_login.place(relx=0.25, rely=0.05, anchor="center")
        self.button_register.place(relx=0.125, rely=0.05, anchor="center")
        self.style_register(1)
        self.style_login(1)
        self.email1.place_forget()
        self.email2.place_forget() 









    def register(self):
        email = self.email1.get()
        prenom = self.prenom.get()
        nom=self.nom.get()
        password=self.password1.get()
        date_naissance=self.date_entry.get()
        classe=self.choix.get()

        # 1. Charger fichier étudiants
        with open("Fichier_Student_Json.json", "r") as f:
            students = json.load(f)

        # 2. Vérifier email
        email_valide = False
        for student in students:
            if student["email"] == email:
                email_valide = True
                break

        if not email_valide:
            self.label_error=tk.Label(self.register_frame,text="email non valide,réssayer!",bg="#b4c9de",fg="red",font=15)
            self.label_error.place(relx=0.71, rely=0.9, anchor="center",width=200)
            self.prenom.delete(0, tk.END)
            self.nom.delete(0, tk.END)
            self.date_entry.delete(0, tk.END)
            self.email1.delete(0, tk.END)
            self.password1.delete(0, tk.END)
            self.confirm.delete(0, tk.END)
            return

        # 3. Charger inscrits
        try:
            with open("Fichier_personnes_inscrites.json", "r") as f:
                inscrits = json.load(f)
        except:
            inscrits = []
        for personne in inscrits:
            if personne["email"] == email:
                self.label_error = tk.Label(self.register_frame,text="Vous êtes déjà inscrit !",bg="#b4c9de",fg="red", font=15)
                self.label_error.place(relx=0.71, rely=0.9, anchor="center", width=250)
                return

        # 4. Ajouter personne
        inscrits.append({
            "prenom": prenom,
            "email": email,
            "nom" : nom,
            "password" : password,
            "date_naissance" : date_naissance,
            "classe" : classe
        })

        # 5. Sauvegarder
        with open("Fichier_personnes_inscrites.json", "w") as f:
            json.dump(inscrits, f, indent=4)

            self.label_error=tk.Label(self.register_frame,text="Inscription réussie",bg="#b4c9de",fg="green",font=15)
            self.label_error.place(relx=0.71, rely=0.9, anchor="center",width=200)
            self.prenom.delete(0, tk.END)
            self.nom.delete(0, tk.END)
            self.date_entry.delete(0, tk.END)
            self.email1.delete(0, tk.END)
            self.password1.delete(0, tk.END)
            self.confirm.delete(0, tk.END)
    def login(self):
        email = self.email2.get()
        password = self.password2.get()

        try:
            with open("Fichier_personnes_inscrites.json", "r") as f:
                inscrits = json.load(f)
        except:
            inscrits = []

        utilisateur_trouve = False

        for personne in inscrits:
            if personne["email"] == email and personne["password"] == password:
                utilisateur_trouve = True
                break

        if utilisateur_trouve:
            self.label_error = tk.Label(self.login_frame, text="connexion réussie", bg="white", fg="green", font=15)
        else:
            self.label_error = tk.Label(self.login_frame, text="email ou mot de passe incorrecte", bg="white", fg="red", font=15)

        self.label_error.place(relx=0.3, rely=0.2, anchor="center", width=250)

        self.email2.delete(0, tk.END)
        self.password2.delete(0, tk.END)
    def fix_layout(self):
        # forcer recalcul des dimensions
        self.root.update_idletasks()

        # relancer affichage accueil pour repositionner correctement
        self.show_accueil_frame()

root = tk.Tk()
app = App(root)
root.mainloop()