from tkcalendar import DateEntry
import tkinter as tk 
from tkinter import ttk
from PIL import Image, ImageTk
import json

class App:
    def __init__(self, root):
        self.root = root
        self.root.state("zoomed")
        self.root.title("Application de vote électronique de EMINES")

        # CHARGEMENT DES IMAGES DES ARRIERE PLAN : 
        self.image_accueil = Image.open("New board 1.png")
        self.image_register = Image.open("Inscription.png")
        self.image_login = Image.open("Login.png")
        self.image_condidat = Image.open("condidat.png")
        self.image_mpo = Image.open("mot de passe oblié1.png")
        self.image_futurE =  Image.open("elections a venir.png")
        self.image_currentE =  Image.open("elections en cours.png")
        self.image_finishE =  Image.open("ELECTIONS TERMINES.png")

        # CREATION DES FRAMES : 
        self.accueil_frame=tk.Frame(root)
        self.register_frame=tk.Frame(root)
        self.login_frame=tk.Frame(root)
        self.mpo_frame=tk.Frame(root)
        self.condidat_frame=tk.Frame(root)
        self.futurE_frame=tk.Frame(root)
        self.currentE_frame=tk.Frame(root)
        self.finishE_frame=tk.Frame(root)

        # PACKAGE DES FRAMES :
        self.accueil_frame.pack(fill="both", expand=True)

        self.label_accueil = tk.Label(self.accueil_frame)
        self.label_accueil.pack(fill="both", expand=True)

        self.label_register = tk.Label(self.register_frame)
        self.label_register.pack(fill="both", expand=True)

        self.label_login = tk.Label(self.login_frame)
        self.label_login.pack(fill="both", expand=True)

        self.label_condidat = tk.Label(self.condidat_frame)
        self.label_condidat.pack(fill="both", expand=True)

        self.label_futurE = tk.Label(self.futurE_frame)
        self.label_futurE.pack(fill="both", expand=True)

        self.label_currentE = tk.Label(self.currentE_frame)
        self.label_currentE.pack(fill="both", expand=True)

        self.label_finishE = tk.Label(self.finishE_frame)
        self.label_finishE.pack(fill="both", expand=True)

        self.label_mpo = tk.Label(self.mpo_frame)
        self.label_mpo.pack(fill="both", expand=True)

        # METTRE A JOUR L'IMAGE QUAND LA FENETRE CHANGE

        self.accueil_frame.bind("<Configure>", self.resize_image_accueil)
        self.register_frame.bind("<Configure>", self.resize_image_register)
        self.login_frame.bind("<Configure>", self.resize_image_login)
        self.condidat_frame.bind("<Configure>", self.resize_image_condidat)
        self.futurE_frame.bind("<Configure>", self.resize_image_futurE)
        self.currentE_frame.bind("<Configure>", self.resize_image_currentE)
        self.finishE_frame.bind("<Configure>", self.resize_image_finishE)
        self.mpo_frame.bind("<Configure>", self.resize_image_mpo)
       
       # LES BOUTTONS DE L'APPLICATION
        self.button_register = tk.Button(root,
    text="S'inscrire",
    fg="white",              
    bg="#048b9a",           
    activeforeground="white",
    borderwidth=0,
    highlightthickness=0,
    relief="flat",command=self.show_register_frame)
        self.button_register.place(relx=0.13, rely=0.05, anchor="center")

        self.button_login = tk.Button(root, text="Login",
    fg="white",              
    bg="#048b9a",           
    activeforeground="white",
    borderwidth=0,
    highlightthickness=0,
    relief="flat",command=self.show_login_frame)
        self.button_login.place(relx=0.24, rely=0.05, anchor="center")

        self.button_futurE = tk.Button(root, text="Accéder",
    fg="white",              
    bg="#073763",           
    activeforeground="white",
    borderwidth=0,
    highlightthickness=0,
    relief="flat",command=self.show_futurE_frame)
        self.button_futurE.place(relx=0.24, rely=0.05, anchor="center")

        self.button_currentE = tk.Button(root, text="Accéder",
    fg="white",              
    bg="#073763",           
    activeforeground="white",
    borderwidth=0,
    highlightthickness=0,
    relief="flat")
        self.button_currentE.place(relx=0.24, rely=0.05, anchor="center")

        self.button_finishE= tk.Button(root, text="Accéder",
    fg="white",              
    bg="#073763",           
    activeforeground="white",
    borderwidth=0,
    highlightthickness=0,
    relief="flat")
        self.button_finishE.place(relx=0.24, rely=0.05, anchor="center")
        

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
        
        self.button_mpo = tk.Button(root, text="Mot de passe oublié?",
    fg="black",              
    bg="white",           
    activeforeground="white",
    borderwidth=0,
    highlightthickness=0,
    relief="flat",font=20,command=self.show_mpo_frame)

        # LES AUTRES ELEMENT DE L'APPLICATION
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

        classes=["2026","2027","2028","2029","2030"]
        self.combo_classe = ttk.Combobox(root, values=classes, state="normal")  # "normal" = on peut écrire
        self.combo_classe.set("classe")
        self.root.after(100, self.fix_layout)

       
        # LES FONCTIONS D'AJUSTEMENT DE TAILLE
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
    def resize_image_condidat(self, event):
        # éviter bug quand fenêtre très petite
        if event.width > 1 and event.height > 1:
            resized = self.image_condidat.resize((event.width, event.height))
            self.photo_condidat = ImageTk.PhotoImage(resized)
            self.label_condidat.config(image=self.photo_condidat)
    def resize_image_futurE(self, event):
        # éviter bug quand fenêtre très petite
        if event.width > 1 and event.height > 1:
            resized = self.image_futurE.resize((event.width, event.height))
            self.photo_futurE = ImageTk.PhotoImage(resized)
            self.label_futurE.config(image=self.photo_futurE)
    def resize_image_currentE(self, event):
        # éviter bug quand fenêtre très petite
        if event.width > 1 and event.height > 1:
            resized = self.image_currentE.resize((event.width, event.height))
            self.photo_currentE = ImageTk.PhotoImage(resized)
            self.label_currentE.config(image=self.photo_currentE)
    def resize_image_finishE(self, event):
        # éviter bug quand fenêtre très petite
        if event.width > 1 and event.height > 1:
            resized = self.image_finishE.resize((event.width, event.height))
            self.photo_finishE = ImageTk.PhotoImage(resized)
            self.label_finishE.config(image=self.photo_finishE)
    def resize_image_mpo(self, event):
         # éviter bug quand fenêtre très petite
        if event.width > 1 and event.height > 1:
            resized = self.image_mpo.resize((event.width, event.height))
            self.photo_mpo = ImageTk.PhotoImage(resized)
            self.label_mpo.config(image=self.photo_mpo)
        
        # LES FONCTION DE CHANGEMENT DU STYLE DES BOUTTONS
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

        # LES FONCTION D'AFFICHAGE DES FRAMES 
    def show_register_frame(self):
        #CACHER LES AUTRES FRAMES 
        self.accueil_frame.pack_forget()
        self.login_frame.pack_forget()
        self.condidat_frame.pack_forget()
        self.mpo_frame.pack_forget()

        #AFFICHER LA BONNE FRAME
        self.register_frame.pack(fill="both", expand=True)
        
        #CACHER LES ELEMENTS DES AUTRES FRAMES
        self.button_register.place_forget()
        self.button_send2.place_forget()
        self.button_send3.place_forget()
        self.button_mpo.place_forget()
        self.email2.place_forget()
        self.password2.place_forget()

        #AFFICHER ET PLACER LES BOUTTONS DE LA FRAME
        self.button_send1.place(relx=0.71, rely=0.83, anchor="center",width=100)
        self.button_accueil.place(relx=0.1, rely=0.06, anchor="center",height=30,width=100)
        self.button_login.place(relx=0.22, rely=0.6, anchor="center",height=30,width=100)
        self.style_login(2)

        #AFFICHER ET PLACER LES AUTRES ELEMENTS DE LA FRAME
        self.email1.place(relx=0.8, rely=0.23, anchor="center",width=180,height=30)
        self.password1.place(relx=0.8, rely=0.33, anchor="center",width=180,height=30)
        self.nom.place(relx=0.56, rely=0.33, anchor="center",width=180,height=30)
        self.prenom.place(relx=0.56, rely=0.23, anchor="center",width=180,height=30)
        self.confirm.place(relx=0.8, rely=0.47, anchor="center",width=180,height=30)
        self.date_entry.place(relx=0.56, rely=0.47, anchor="center",width=180,height=30)
        self.combo_classe.place(relx=0.56, rely=0.58, anchor="center",width=180,height=30)
        
        
       
    def show_login_frame(self):
        #CACHER LES AUTRES FRAMES
        self.accueil_frame.pack_forget()
        self.register_frame.pack_forget()
        self.mpo_frame.pack_forget()
        self.condidat_frame.pack_forget()

        #AFFICHER LA BONNE FRAME
        self.login_frame.pack(fill="both", expand=True)
        
        #CACHER LES ELEMENTS DES AUTRES FRAMES
        self.nom.place_forget()
        self.prenom.place_forget()
        self.confirm.place_forget()
        self.email1.place_forget()
        self.password1.place_forget()
        self.date_entry.place_forget()
        self.button_login.place_forget()
        self.combo_classe.place_forget()
        self.button_send1.place_forget()

        #AFFICHER ET PLACER LES BOUTTONS DE LA FRAME
        self.button_accueil.place(relx=0.13, rely=0.08, anchor="center",height=30,width=100)
        self.button_register.place(relx=0.82, rely=0.55, anchor="center",height=30,width=100)
        self.style_register(2)
        self.button_send2.place(relx=0.48, rely=0.5, anchor="center",width=150,height=35)
        self.button_mpo.place(relx=0.3, rely=0.56, anchor="center") 

        #AFFICHER ET PLACER LES AUTRES ELEMENTS DE LA FRAME
        self.email2.place(relx=0.3, rely=0.4, anchor="center",width=320,height=30)
        self.password2.place(relx=0.3, rely=0.5, anchor="center",width=320,height=30)
        
    
    def show_accueil_frame(self):
        #CACHER LES AUTRES FRAMES
        self.login_frame.pack_forget()
        self.condidat_frame.pack_forget()
        self.register_frame.pack_forget()
        self.mpo_frame.pack_forget()

        #AFFICHER LA BONNE FRAME
        self.accueil_frame.pack(fill="both", expand=True)

        #CACHER LES ELEMENTS DES AUTRES FRAMES
        self.nom.place_forget()
        self.prenom.place_forget()
        self.confirm.place_forget()
        self.date_entry.place_forget()
        self.combo_classe.place_forget()
        self.button_send1.place_forget()
        self.button_send2.place_forget()
        self.password1.place_forget()
        self.password2.place_forget()   
        self.button_accueil.place_forget()
        self.email1.place_forget()
        self.email2.place_forget()
        self.button_futurE.place_forget()
        self.button_currentE.place_forget()
        self.button_finishE.place_forget()
        self.button_mpo.place_forget()
        
        #AFFICHER ET PLACER LES BOUTTONS DE LA FRAME
        self.button_login.place(relx=0.25, rely=0.05, anchor="center",height=30,width=100)
        self.button_register.place(relx=0.125, rely=0.05, anchor="center",height=30,width=100)
        self.style_register(1)
        self.style_login(1)
        #AFFICHER ET PLACER LES AUTRES ELEMENTS DE LA FRAME
        
        
    def show_condidat_frame(self):
        #CACHER LES AUTRES FRAMES
        self.login_frame.pack_forget()
        self.register_frame.pack_forget()
        self.accueil_frame.pack_forget()
        self.mpo_frame.pack_forget()

        #AFFICHER LA BONNE FRAME
        self.condidat_frame.pack(fill="both", expand=True)

        #CACHER LES ELEMENTS DES AUTRES FRAMES
        self.nom.place_forget()
        self.prenom.place_forget()
        self.confirm.place_forget()
        self.date_entry.place_forget()
        self.combo_classe.place_forget()
        self.button_send1.place_forget()
        self.button_send2.place_forget()
        self.password1.place_forget()
        self.password2.place_forget()   
        self.email1.place_forget()
        self.email2.place_forget()
        self.button_login.place_forget()
        self.button_register.place_forget()
        self.button_mpo.place_forget()

        #AFFICHER ET PLACER LES BOUTTONS DE LA FRAME
        self.button_accueil.place(relx=0.125, rely=0.05, anchor="center",height=30,width=100)
        self.button_futurE.place(relx=0.17, rely=0.8, anchor="center",height=30,width=100)
        self.button_currentE.place(relx=0.5, rely=0.8, anchor="center",height=30,width=100)
        self.button_finishE.place(relx=0.83, rely=0.8, anchor="center",height=30,width=100)
        #AFFICHER ET PLACER LES AUTRES ELEMENTS DE LA FRAME
        
        
    def show_mpo_frame(self):
        #CACHER LES AUTRES FRAMES
        self.login_frame.pack_forget()
        self.register_frame.pack_forget()
        self.accueil_frame.pack_forget()
        self.condidat_frame.pack_forget()
        self.futurE_frame.pack_forget()
        self.currentE_frame.pack_forget()
        self.finishE_frame.pack_forget()


        #AFFICHER LA BONNE FRAME
        self.mpo_frame.pack(fill="both", expand=True)

        #CACHER LES ELEMENTS DES AUTRES FRAMES
        self.nom.place_forget()
        self.button_login.place_forget()
        self.button_register.place_forget()
        self.prenom.place_forget()
        self.confirm.place_forget()
        self.date_entry.place_forget()
        self.combo_classe.place_forget()
        self.email1.place_forget()
        self.email2.place_forget() 
        self.button_send1.place_forget()
        self.button_send2.place_forget()
        self.button_mpo.place_forget()
        self.password1.place_forget()
        self.password2.place_forget() 
        self.button_accueil.place_forget() 
        self.button_futurE.place_forget()
        self.button_currentE.place_forget()
        self.button_finishE.place_forget() 

        #AFFICHER ET PLACER LES BOUTTONS DE LA FRAME
        
        #AFFICHER ET PLACER LES AUTRES ELEMENTS DE LA FRAME
    
    def show_futurE_frame(self):
        # CACHER LES AUTRES FRAMES
        self.login_frame.pack_forget()
        self.register_frame.pack_forget()
        self.accueil_frame.pack_forget()
        self.condidat_frame.pack_forget()
        self.mpo_frame.pack_forget()

        # AFFICHER LA BONNE FRAME
        self.futurE_frame.pack(fill="both", expand=True)

        # CACHER LES ELEMENTS DES AUTRES FRAMES
        self.nom.place_forget()
        self.prenom.place_forget()
        self.confirm.place_forget()
        self.date_entry.place_forget()
        self.combo_classe.place_forget()
        self.email1.place_forget()
        self.email2.place_forget()
        self.button_send1.place_forget()
        self.button_send2.place_forget()
        self.button_mpo.place_forget()
        self.password1.place_forget()
        self.password2.place_forget()
        self.button_accueil.place_forget()
        self.button_futurE.place_forget()
        self.button_currentE.place_forget()
        self.button_finishE.place_forget()

        # AFFICHER ET PLACER LE BOUTON ACCUEIL
        self.button_accueil.place(relx=0.05, rely=0.06, anchor="center", height=30, width=100)

        # CHARGER ET AFFICHER LES ELECTIONS
        self.afficher_elections_futur()

        
    # LES FONCTIONS DES BOUTTONS DE L'APPLICATION
    def register(self):
        email = self.email1.get()
        prenom = self.prenom.get()
        nom=self.nom.get()
        password=self.password1.get()
        date_naissance=self.date_entry.get()
        classe=self.combo_classe.get()

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
            self.show_condidat_frame()
        else:
            self.label_error = tk.Label(self.login_frame, text="email ou mot de passe incorrecte", bg="white", fg="red", font=15)

        self.label_error.place(relx=0.3, rely=0.3, anchor="center", width=250)

        self.email2.delete(0, tk.END)
        self.password2.delete(0, tk.END)
    def afficher_elections_futur(self):
        # Supprimer l'ancien canvas s'il existe
        if hasattr(self, 'canvas_futur'):
            self.canvas_futur.destroy()
        if hasattr(self, 'scrollbar_futur'):
            self.scrollbar_futur.destroy()

        # Charger les élections depuis le fichier JSON
        try:
            with open("Fichier_Elections.json", "r", encoding="utf-8") as f:
                elections = json.load(f)
        except:
            elections = []

        # Filtrer les élections à venir (optionnel selon ta logique)
        elections_futur = [e for e in elections if e.get("statut") == "futur"]

        # Créer un canvas scrollable positionné sur la frame
        self.canvas_futur = tk.Canvas(self.futurE_frame, bg="#7fafc0", highlightthickness=0)
        self.scrollbar_futur = tk.Scrollbar(self.futurE_frame, orient="vertical", command=self.canvas_futur.yview)
        self.canvas_futur.configure(yscrollcommand=self.scrollbar_futur.set)

        # Positionner le canvas et la scrollbar sur la frame (zone centrale)
        self.canvas_futur.place(relx=0.28, rely=0.27, relwidth=0.43, relheight=0.72)
        self.scrollbar_futur.place(relx=0.72, rely=0.27, relheight=0.72)

        # Frame intérieure dans le canvas
        inner_frame = tk.Frame(self.canvas_futur, bg="#7fafc0")
        canvas_window = self.canvas_futur.create_window((0, 0), window=inner_frame, anchor="nw")
        def on_canvas_resize(event):
            self.canvas_futur.itemconfig(canvas_window, width=event.width)
        self.canvas_futur.bind("<Configure>", on_canvas_resize)

        # Afficher chaque élection
        for election in elections_futur:
            self.creer_carte_election(inner_frame, election)

        # Mettre à jour la scrollregion après le rendu
        inner_frame.update_idletasks()
        self.canvas_futur.configure(scrollregion=self.canvas_futur.bbox("all"))

        # Scroll avec la molette
        self.canvas_futur.bind("<MouseWheel>", lambda e: self.canvas_futur.yview_scroll(-1*(e.delta//120), "units"))

    
    def creer_carte_election(self, parent, election):
        # Carte blanche pour chaque élection
        carte = tk.Frame(parent, bg="white", bd=1, relief="solid")
        carte.pack(fill="x", padx=10, pady=8, ipady=8)

        # Titre
        tk.Label(carte, text=election.get("titre", ""), bg="white",
                font=("Arial", 11, "bold"), anchor="w").pack(anchor="w", padx=10, pady=(8, 2))

        # Dates
        tk.Label(carte, text=f"Date de départ d'élection :    {election.get('date_debut', '')}",
                bg="white", font=("Arial", 9), anchor="w").pack(anchor="w", padx=10)
        tk.Label(carte, text=f"Date de fin d'élection :           {election.get('date_fin', '')}",
                bg="white", font=("Arial", 9), anchor="w").pack(anchor="w", padx=10)

        # Frame pour les boutons
        btn_frame = tk.Frame(carte, bg="white")
        btn_frame.pack(fill="x", padx=10, pady=(7, 4))

        # Bouton "Voir les candidats" - à gauche
        tk.Button(btn_frame, text="Voir les condidats",
          fg="white", bg="#073763",
          activeforeground="white",
          borderwidth=0, highlightthickness=0, relief="flat",
          width=20, height=2,
          command=lambda e=election: self.voir_candidats(e)
          ).pack(side="left")

        # Bouton "Postuler comme candidat" - à droite
        tk.Button(btn_frame, text="Postuler comme candidat",
          fg="white", bg="#073763",
          activeforeground="white",
          borderwidth=0, highlightthickness=0, relief="flat",
          width=20, height=2,
          command=lambda e=election: self.postuler_candidat(e)
          ).pack(side="right")


    def voir_candidats(self, election):
        print(f"Voir candidats pour : {election.get('titre')}")
        # Tu peux naviguer vers une autre frame ici


    def postuler_candidat(self, election):
        print(f"Postuler pour : {election.get('titre')}")
        # Tu peux ouvrir un formulaire ici

    def fix_layout(self):
        # forcer recalcul des dimensions
        self.root.update_idletasks()

        # relancer affichage accueil pour repositionner correctement
        self.show_accueil_frame()

root = tk.Tk()
app = App(root)
root.mainloop()