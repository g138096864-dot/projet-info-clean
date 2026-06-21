from tkcalendar import DateEntry
import tkinter as tk 
from tkinter import ttk
from PIL import Image, ImageTk
import json
import os
import subprocess
import platform
from datetime import datetime
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from tkinter import messagebox

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
        self.image_nmpo = Image.open("nouveau mot de passe.png")
        self.image_admin = Image.open("Admin.png")
        self.image_postuler_individuelle =  Image.open("voir les details.png")
        self.image_postuler_liste =  Image.open("Candidater liste.png")
        self.image_voter1 =  Image.open("participer au vote.png")
        self.image_voter2 =  Image.open("participer au vote copy.png")
        self.image_voter3 =  Image.open("participer au vote copy 2.png")
        self.image_voter4 =  Image.open("participer au vote copy 3.png")

        self.image_gererele = Image.open("gérer les elections.png")
        self.image_gerercon = Image.open("Gérer les candidature.png")
        self.image_voirres = Image.open("Voir les résultats.png")

        # CREATION DES FRAMES : 
        self.accueil_frame             = tk.Frame(root)
        self.register_frame            = tk.Frame(root)
        self.login_frame               = tk.Frame(root)
        self.mpo_frame                 = tk.Frame(root)
        self.condidat_frame            = tk.Frame(root)
        self.futurE_frame              = tk.Frame(root)
        self.currentE_frame            = tk.Frame(root)
        self.finishE_frame             = tk.Frame(root)
        self.nmpo_frame                = tk.Frame(root)
        self.admin_frame               = tk.Frame(root)
        self.postuler_individuelle_frame = tk.Frame(root)
        self.postuler_liste_frame      = tk.Frame(root)
        self.voter1_frame              = tk.Frame(root)
        self.voter2_frame              = tk.Frame(root)
        self.voter3_frame              = tk.Frame(root)
        self.voter4_frame              = tk.Frame(root)
        # FRAMES ADMIN — créées ici pour éviter AttributeError dans les pack_forget
        self.gererele_frame            = tk.Frame(root)
        self.gerercon_frame            = tk.Frame(root)
        self.voirres_frame             = tk.Frame(root)

        # PACKAGE DES FRAMES :
        self.accueil_frame.pack(fill="both", expand=True)

        # Labels de fond (backgrounds)
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

        self.label_nmpo = tk.Label(self.nmpo_frame)
        self.label_nmpo.pack(fill="both", expand=True)

        self.label_admin = tk.Label(self.admin_frame)
        self.label_admin.pack(fill="both", expand=True)

        self.label_postuler_individuelle = tk.Label(self.postuler_individuelle_frame)
        self.label_postuler_individuelle.pack(fill="both", expand=True)

        self.label_postuler_liste = tk.Label(self.postuler_liste_frame)
        self.label_postuler_liste.pack(fill="both", expand=True)

        self.label_voter1 = tk.Label(self.voter1_frame)
        self.label_voter1.pack(fill="both", expand=True)

        self.label_voter2 = tk.Label(self.voter2_frame)
        self.label_voter2.pack(fill="both", expand=True)

        self.label_voter3 = tk.Label(self.voter3_frame)
        self.label_voter3.pack(fill="both", expand=True)

        self.label_voter4 = tk.Label(self.voter4_frame)
        self.label_voter4.pack(fill="both", expand=True)

        # Labels fond pour frames admin
        self.label_gererele = tk.Label(self.gererele_frame)
        self.label_gererele.pack(fill="both", expand=True)

        self.label_gerercon = tk.Label(self.gerercon_frame)
        self.label_gerercon.pack(fill="both", expand=True)

        self.label_voirres = tk.Label(self.voirres_frame)
        self.label_voirres.pack(fill="both", expand=True)

        # METTRE A JOUR L'IMAGE QUAND LA FENETRE CHANGE
        self.accueil_frame.bind("<Configure>", self.resize_image_accueil)
        self.register_frame.bind("<Configure>", self.resize_image_register)
        self.login_frame.bind("<Configure>", self.resize_image_login)
        self.condidat_frame.bind("<Configure>", self.resize_image_condidat)
        self.futurE_frame.bind("<Configure>", self.resize_image_futurE)
        self.currentE_frame.bind("<Configure>", self.resize_image_currentE)
        self.finishE_frame.bind("<Configure>", self.resize_image_finishE)
        self.mpo_frame.bind("<Configure>", self.resize_image_mpo)
        self.nmpo_frame.bind("<Configure>", self.resize_image_nmpo)
        self.admin_frame.bind("<Configure>", self.resize_image_admin)
        self.postuler_individuelle_frame.bind("<Configure>", self.resize_image_postuler_individuelle)
        self.postuler_liste_frame.bind("<Configure>", self.resize_image_postuler_liste)
        self.voter1_frame.bind("<Configure>", self.resize_image_voter1)
        self.voter2_frame.bind("<Configure>", self.resize_image_voter2)
        self.voter3_frame.bind("<Configure>", self.resize_image_voter3)
        self.voter4_frame.bind("<Configure>", self.resize_image_voter4)
        self.gererele_frame.bind("<Configure>", self.resize_image_gererele)
        self.gerercon_frame.bind("<Configure>", self.resize_image_gerercon)
        self.voirres_frame.bind("<Configure>", self.resize_image_voirres)

        # ------------------------------------------------------------------ #
        #  BOUTONS DE L'APPLICATION (tous créés sur root sauf exceptions)      #
        # ------------------------------------------------------------------ #
        self.button_register = tk.Button(root,
            text="S'inscrire", fg="white", bg="#048b9a",
            activeforeground="white", borderwidth=0, highlightthickness=0,
            relief="flat", command=self.show_register_frame)
        self.button_register.place(relx=0.13, rely=0.05, anchor="center")

        self.button_login = tk.Button(root, text="Login",
            fg="white", bg="#048b9a",
            activeforeground="white", borderwidth=0, highlightthickness=0,
            relief="flat", command=self.show_login_frame)
        self.button_login.place(relx=0.24, rely=0.05, anchor="center")

        self.button_futurE = tk.Button(root, text="Accéder",
            fg="white", bg="#073763",
            activeforeground="white", borderwidth=0, highlightthickness=0,
            relief="flat", command=self.show_futurE_frame)
        self.button_futurE.place(relx=0.24, rely=0.05, anchor="center")

        self.button_currentE = tk.Button(root, text="Accéder",
            fg="white", bg="#073763",
            activeforeground="white", borderwidth=0, highlightthickness=0,
            relief="flat", command=self.show_currentE_frame)
        self.button_currentE.place(relx=0.24, rely=0.05, anchor="center")

        self.button_finishE = tk.Button(root, text="Accéder",
            fg="white", bg="#073763",
            activeforeground="white", borderwidth=0, highlightthickness=0,
            relief="flat", command=self.show_finishE_frame)
        self.button_finishE.place(relx=0.24, rely=0.05, anchor="center")

        self.button_gérerE = tk.Button(root, text="Accéder",
            fg="white", bg="#073763",
            activeforeground="white", borderwidth=0, highlightthickness=0,
            relief="flat", command=self.show_gererele_frame)
        self.button_gérerE.place(relx=0.24, rely=0.05, anchor="center")

        self.button_gérerC = tk.Button(root, text="Accéder",
            fg="white", bg="#073763",
            activeforeground="white", borderwidth=0, highlightthickness=0,
            relief="flat", command=self.show_gerercon_frame)
        self.button_gérerC.place(relx=0.24, rely=0.05, anchor="center")

        self.button_voirR = tk.Button(root, text="Accéder",
            fg="white", bg="#073763",
            activeforeground="white", borderwidth=0, highlightthickness=0,
            relief="flat", command=self.show_voirres_frame)
        self.button_voirR.place(relx=0.24, rely=0.05, anchor="center")

        self.button_accueil = tk.Button(root, text="Accueil",
            fg="white", bg="#048b9a",
            activeforeground="white", borderwidth=0, highlightthickness=0,
            relief="flat", command=self.show_accueil_frame)

        self.button_send1 = tk.Button(root, text="Envoyer",
            fg="white", bg="#073763",
            activeforeground="white", borderwidth=0, highlightthickness=0,
            relief="flat", font=20, command=self.register)

        self.button_send2 = tk.Button(root, text="Se connecter",
            fg="white", bg="#073763",
            activeforeground="white", borderwidth=0, highlightthickness=0,
            relief="flat", font=20, command=self.login)

        self.button_send3 = tk.Button(root, text="Vérifier",
            fg="white", bg="#6FA8DC",
            activeforeground="white", borderwidth=0, highlightthickness=0,
            relief="flat", font=20, command=self.login)

        self.button_mpo = tk.Button(self.login_frame, text="Mot de passe oublié?",
            fg="black", bg="white",
            activeforeground="white", borderwidth=0, highlightthickness=0,
            relief="flat", font=20, command=self.mp)

        self.button_candidat = tk.Button(root, text="Page candidat",
            fg="white", bg="#048b9a",
            activeforeground="white", borderwidth=0, highlightthickness=0,
            relief="flat", font=20, command=self.show_condidat_frame)

        self.button_verifier = tk.Button(self.mpo_frame, text="Vérifier",
            fg="white", bg="#048b9a",
            activeforeground="white", borderwidth=0, highlightthickness=0,
            font=("Arial", 18), relief="flat", command=self.verifier)

        self.button_creer = tk.Button(self.nmpo_frame, text="Créer",
            fg="white", bg="#048b9a",
            activeforeground="white", borderwidth=0, highlightthickness=0,
            font=("Arial", 18), relief="flat", command=self.nmpof)

        # Bouton candidater — créé une seule fois, replacé selon le contexte
        self.button_candidater = tk.Button(root, text="Candidater",
            fg="white", bg="#048b9a",
            activeforeground="white", borderwidth=0, highlightthickness=0,
            relief="flat", font=20)

        # ------------------------------------------------------------------ #
        #  AUTRES ÉLÉMENTS                                                     #
        # ------------------------------------------------------------------ #
        self.menu_bar = tk.Menu(root)
        self.root.config(menu=self.menu_bar)
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Français", menu=self.file_menu)
        self.file_menu.add_command(label="English")
        self.file_menu.add_command(label="العربية")

        self.email1    = tk.Entry(root, bg="white")
        self.password1 = tk.Entry(root, bg="white", show="*")
        self.email2    = tk.Entry(root, bg="#eeeeee")
        self.password2 = tk.Entry(root, bg="#eeeeee", show="*")

        self.label_mail = tk.Label(self.login_frame, text="Email",
            fg="black", font=14, bg="white")
        self.label_mail.place(relx=0.2, rely=0.35, anchor="center", width=320, height=30)

        self.label_password = tk.Label(self.login_frame, text="Mot de passe",
            fg="black", font=14, bg="white")
        self.label_password.place(relx=0.22, rely=0.45, anchor="center", width=320, height=30)

        self.label_npass = tk.Label(self.nmpo_frame, text="Saisir le nouveau mot de passe",
            fg="black", font=14, bg="white")
        self.label_npass.place(relx=0.37, rely=0.4, anchor="center", width=320, height=30)

        self.label_cpass = tk.Label(self.nmpo_frame, text="Confirmer le nouveau mot de passe",
            fg="black", font=14, bg="white")
        self.label_cpass.place(relx=0.38, rely=0.5, anchor="center", width=320, height=30)

        self.npassword = tk.Entry(self.nmpo_frame, bg="#eeeeee", show="*")
        self.cpassword = tk.Entry(self.nmpo_frame, bg="#eeeeee", show="*")

        self.prenom  = tk.Entry(root, bg="white")
        self.prenom1 = tk.Entry(root, bg="white")
        self.nom     = tk.Entry(root, bg="white")
        self.nom1    = tk.Entry(root, bg="white")
        self.nom2    = tk.Entry(root, bg="white")   # nom de liste

        self.confirm    = tk.Entry(root, bg="white", show="*")
        self.date_entry = DateEntry(root, date_pattern='yyyy-mm-dd', bg="white")
        self.ecole      = tk.Entry(root, bg="#CBC6C6")
        self.motivation = tk.Text(root, bg="white")
        self.question   = tk.Entry(root, bg="#eeeeee")

        self.label_question = tk.Label(self.register_frame,
            text="Question secrète\nQuel est le nom de ton école primaire ?",
            bg="#B4C9DE", fg="black", font=("italic", 12, "bold"), justify="left")
        self.label_question.place(relx=0.83, rely=0.53, anchor="center")

        classes = ["2026", "2027", "2028", "2029", "2030"]
        self.combo_classe  = ttk.Combobox(root, values=classes, state="normal")
        self.combo_classe.set("classe")
        self.combo_classe1 = ttk.Combobox(root, values=classes, state="normal")
        self.combo_classe1.set("classe")

        # Widgets spécifiques à postuler_liste — initialisés ici pour pouvoir
        # les cacher proprement partout sans AttributeError
        self.search_entry       = tk.Entry(root, bg="white")
        self.listbox_suggestions = tk.Listbox(root, font=("Arial", 10))
        self.label_membres      = tk.Label(root, text="Membres : ", bg="white",
            fg="black", font=("Arial", 10), wraplength=400, justify="left")
        self.label_nomE         = tk.Label(root, text="", fg="black", font=14, bg="#BAD2D7")

        self.role = tk.StringVar(value="Admin")
        self.radio_admin = tk.Radiobutton(self.login_frame, text="Admin",
            variable=self.role, value="Admin", bg="white", font=("Arial", 13, "bold"))
        self.radio_candidat = tk.Radiobutton(self.login_frame, text="Candidat",
            variable=self.role, value="Candidat", bg="white", font=("Arial", 13, "bold"))
        self.radio_admin.place(relx=0.23, rely=0.68, anchor="center")
        self.radio_candidat.place(relx=0.235, rely=0.74, anchor="center")

        self.root.after(100, self.fix_layout)

    # ====================================================================== #
    #  AIDE : cache TOUS les widgets mobiles                                  #
    # ====================================================================== #
    def _hide_all_widgets(self):
        """Cache tous les widgets placés dynamiquement via place()."""
        widgets = [
            self.button_register, self.button_login, self.button_accueil,
            self.button_send1, self.button_send2, self.button_send3,
            self.button_mpo, self.button_candidat, self.button_verifier,
            self.button_creer, self.button_candidater,
            self.button_futurE, self.button_currentE, self.button_finishE,
            self.button_gérerE, self.button_gérerC, self.button_voirR,
            self.email1, self.email2, self.password1, self.password2,
            self.nom, self.nom1, self.nom2, self.prenom, self.prenom1,
            self.confirm, self.date_entry, self.combo_classe, self.combo_classe1,
            self.question, self.ecole, self.motivation,
            self.npassword, self.cpassword,
            self.search_entry, self.listbox_suggestions,
            self.label_membres, self.label_nomE,
            self.radio_admin, self.radio_candidat,
        ]
        for w in widgets:
            try:
                w.place_forget()
            except Exception:
                pass
        # Bouton PDF dynamique
        if hasattr(self, 'btn_pdf'):
            try:
                self.btn_pdf.place_forget()
            except Exception:
                pass

    # ====================================================================== #
    #  AIDE : cache TOUTES les frames                                         #
    # ====================================================================== #
    def _hide_all_frames(self):
        frames = [
            self.accueil_frame, self.register_frame, self.login_frame,
            self.mpo_frame, self.nmpo_frame, self.condidat_frame,
            self.futurE_frame, self.currentE_frame, self.finishE_frame,
            self.admin_frame, self.postuler_individuelle_frame,
            self.postuler_liste_frame,
            self.voter1_frame, self.voter2_frame, self.voter3_frame, self.voter4_frame,
            self.gererele_frame, self.gerercon_frame, self.voirres_frame,
        ]
        for f in frames:
            f.pack_forget()

    # ====================================================================== #
    #  RESIZE                                                                 #
    # ====================================================================== #
    def resize_image_accueil(self, event):
        if event.width > 1 and event.height > 1:
            resized = self.image_accueil.resize((event.width, event.height))
            self.photo_accueil = ImageTk.PhotoImage(resized)
            self.label_accueil.config(image=self.photo_accueil)

    def resize_image_register(self, event):
        if event.width > 1 and event.height > 1:
            resized = self.image_register.resize((event.width, event.height))
            self.photo_register = ImageTk.PhotoImage(resized)
            self.label_register.config(image=self.photo_register)

    def resize_image_login(self, event):
        if event.width > 1 and event.height > 1:
            resized = self.image_login.resize((event.width, event.height))
            self.photo_login = ImageTk.PhotoImage(resized)
            self.label_login.config(image=self.photo_login)

    def resize_image_condidat(self, event):
        if event.width > 1 and event.height > 1:
            resized = self.image_condidat.resize((event.width, event.height))
            self.photo_condidat = ImageTk.PhotoImage(resized)
            self.label_condidat.config(image=self.photo_condidat)

    def resize_image_futurE(self, event):
        if event.width > 1 and event.height > 1:
            resized = self.image_futurE.resize((event.width, event.height))
            self.photo_futurE = ImageTk.PhotoImage(resized)
            self.label_futurE.config(image=self.photo_futurE)

    def resize_image_currentE(self, event):
        if event.width > 1 and event.height > 1:
            resized = self.image_currentE.resize((event.width, event.height))
            self.photo_currentE = ImageTk.PhotoImage(resized)
            self.label_currentE.config(image=self.photo_currentE)

    def resize_image_finishE(self, event):
        if event.width > 1 and event.height > 1:
            resized = self.image_finishE.resize((event.width, event.height))
            self.photo_finishE = ImageTk.PhotoImage(resized)
            self.label_finishE.config(image=self.photo_finishE)

    def resize_image_mpo(self, event):
        if event.width > 1 and event.height > 1:
            resized = self.image_mpo.resize((event.width, event.height))
            self.photo_mpo = ImageTk.PhotoImage(resized)
            self.label_mpo.config(image=self.photo_mpo)

    def resize_image_nmpo(self, event):
        if event.width > 1 and event.height > 1:
            resized = self.image_nmpo.resize((event.width, event.height))
            self.photo_nmpo = ImageTk.PhotoImage(resized)
            self.label_nmpo.config(image=self.photo_nmpo)

    def resize_image_postuler_individuelle(self, event):
        if event.width > 1 and event.height > 1:
            resized = self.image_postuler_individuelle.resize((event.width, event.height))
            self.photo_postuler_individuelle = ImageTk.PhotoImage(resized)
            self.label_postuler_individuelle.config(image=self.photo_postuler_individuelle)

    def resize_image_postuler_liste(self, event):
        if event.width > 1 and event.height > 1:
            resized = self.image_postuler_liste.resize((event.width, event.height))
            self.photo_postuler_liste = ImageTk.PhotoImage(resized)
            self.label_postuler_liste.config(image=self.photo_postuler_liste)

    def resize_image_voter1(self, event):
        if event.width > 1 and event.height > 1:
            resized = self.image_voter1.resize((event.width, event.height))
            self.photo_voter1 = ImageTk.PhotoImage(resized)
            self.label_voter1.config(image=self.photo_voter1)

    def resize_image_voter2(self, event):
        if event.width > 1 and event.height > 1:
            resized = self.image_voter2.resize((event.width, event.height))
            self.photo_voter2 = ImageTk.PhotoImage(resized)
            self.label_voter2.config(image=self.photo_voter2)

    def resize_image_voter3(self, event):
        if event.width > 1 and event.height > 1:
            resized = self.image_voter3.resize((event.width, event.height))
            self.photo_voter3 = ImageTk.PhotoImage(resized)
            self.label_voter3.config(image=self.photo_voter3)

    def resize_image_voter4(self, event):
        if event.width > 1 and event.height > 1:
            resized = self.image_voter4.resize((event.width, event.height))
            self.photo_voter4 = ImageTk.PhotoImage(resized)
            self.label_voter4.config(image=self.photo_voter4)

    def resize_image_gererele(self, event):
        if event.width > 1 and event.height > 1:
            resized = self.image_gererele.resize((event.width, event.height))
            self.photo_gererele = ImageTk.PhotoImage(resized)
            self.label_gererele.config(image=self.photo_gererele)

    def resize_image_gerercon(self, event):
        if event.width > 1 and event.height > 1:
            resized = self.image_gerercon.resize((event.width, event.height))
            self.photo_gerercon = ImageTk.PhotoImage(resized)
            self.label_gerercon.config(image=self.photo_gerercon)

    def resize_image_voirres(self, event):
        if event.width > 1 and event.height > 1:
            resized = self.image_voirres.resize((event.width, event.height))
            self.photo_voirres = ImageTk.PhotoImage(resized)
            self.label_voirres.config(image=self.photo_voirres)

    def resize_image_admin(self, event):
        if event.width > 1 and event.height > 1:
            resized = self.image_admin.resize((event.width, event.height))
            self.photo_admin = ImageTk.PhotoImage(resized)
            self.label_admin.config(image=self.photo_admin)

    # ====================================================================== #
    #  STYLE BOUTONS                                                          #
    # ====================================================================== #
    def style_login(self, a):
        if a == 1:
            self.button_login.config(bg="#048b9a", font=10)
        if a == 2:
            self.button_login.config(bg="#073763", font=20)

    def style_register(self, b):
        if b == 1:
            self.button_register.config(bg="#048b9a", fg="white", font=10)
        if b == 2:
            self.button_register.config(bg="#9fc5f8", font=20, fg="black")

    # ====================================================================== #
    #  FONCTIONS show_*                                                       #
    # ====================================================================== #

    def show_accueil_frame(self):
        self._hide_all_frames()
        self._hide_all_widgets()

        self.accueil_frame.pack(fill="both", expand=True)

        # Boutons visibles sur l'accueil
        self.button_login.place(relx=0.25, rely=0.05, anchor="center", height=30, width=100)
        self.button_register.place(relx=0.125, rely=0.05, anchor="center", height=30, width=100)
        self.style_register(1)
        self.style_login(1)

    def show_register_frame(self):
        self._hide_all_frames()
        self._hide_all_widgets()

        self.register_frame.pack(fill="both", expand=True)

        # Boutons
        self.button_send1.place(relx=0.71, rely=0.83, anchor="center", width=100)
        self.button_accueil.place(relx=0.1, rely=0.06, anchor="center", height=30, width=100)
        self.button_login.place(relx=0.22, rely=0.6, anchor="center", height=30, width=100)
        self.style_login(2)

        # Champs
        self.email1.place(relx=0.8, rely=0.23, anchor="center", width=180, height=30)
        self.password1.place(relx=0.8, rely=0.33, anchor="center", width=180, height=30)
        self.nom.place(relx=0.56, rely=0.33, anchor="center", width=180, height=30)
        self.prenom.place(relx=0.56, rely=0.23, anchor="center", width=180, height=30)
        self.confirm.place(relx=0.8, rely=0.47, anchor="center", width=180, height=30)
        self.date_entry.place(relx=0.56, rely=0.47, anchor="center", width=180, height=30)
        self.combo_classe.place(relx=0.56, rely=0.58, anchor="center", width=180, height=30)
        self.question.place(relx=0.8, rely=0.58, anchor="center", width=180, height=30)

    def show_login_frame(self):
        self._hide_all_frames()
        self._hide_all_widgets()

        self.login_frame.pack(fill="both", expand=True)

        # Boutons
        self.button_register.place(relx=0.82, rely=0.55, anchor="center", height=30, width=100)
        self.style_register(2)
        self.button_send2.place(relx=0.48, rely=0.5, anchor="center", width=150, height=35)
        self.button_mpo.place(relx=0.3, rely=0.56, anchor="center")

        # Champs
        self.email2.place(relx=0.3, rely=0.4, anchor="center", width=320, height=30)
        self.password2.place(relx=0.3, rely=0.5, anchor="center", width=320, height=30)

        # Radio buttons (sur login_frame, remis en place)
        self.radio_admin.place(relx=0.23, rely=0.68, anchor="center")
        self.radio_candidat.place(relx=0.235, rely=0.74, anchor="center")

    def show_mpo_frame(self):
        self._hide_all_frames()
        self._hide_all_widgets()

        self.mpo_frame.pack(fill="both", expand=True)

        # Boutons
        self.button_accueil.place(relx=0.1, rely=0.06, anchor="center", height=30, width=100)
        self.button_verifier.place(relx=0.48, rely=0.49, anchor="center", width=150, height=50)

        # Champs
        self.ecole.place(relx=0.48, rely=0.4, anchor="center", width=600, height=35)

    def show_nmpo_frame(self):
        self._hide_all_frames()
        self._hide_all_widgets()

        self.nmpo_frame.pack(fill="both", expand=True)

        # Boutons
        self.button_accueil.place(relx=0.1, rely=0.06, anchor="center", height=30, width=100)
        self.button_creer.place(relx=0.49, rely=0.65, anchor="center", width=200, height=35)

        # Champs
        self.npassword.place(relx=0.48, rely=0.45, anchor="center", width=600, height=35)
        self.cpassword.place(relx=0.48, rely=0.55, anchor="center", width=600, height=35)

    def show_condidat_frame(self):
        self._hide_all_frames()
        self._hide_all_widgets()

        self.condidat_frame.pack(fill="both", expand=True)

        # Boutons
        self.button_accueil.place(relx=0.125, rely=0.05, anchor="center", height=30, width=100)
        self.button_futurE.place(relx=0.17, rely=0.8, anchor="center", height=30, width=100)
        self.button_currentE.place(relx=0.5, rely=0.8, anchor="center", height=30, width=100)
        self.button_finishE.place(relx=0.83, rely=0.8, anchor="center", height=30, width=100)

    def show_admin_frame(self):
        self._hide_all_frames()
        self._hide_all_widgets()

        self.admin_frame.pack(fill="both", expand=True)

        # Boutons
        self.button_accueil.place(relx=0.1, rely=0.06, anchor="center", height=30, width=100)
        self.button_gérerE.place(relx=0.17, rely=0.8, anchor="center", height=30, width=100)
        self.button_gérerC.place(relx=0.5, rely=0.8, anchor="center", height=30, width=100)
        self.button_voirR.place(relx=0.83, rely=0.8, anchor="center", height=30, width=100)

    def show_futurE_frame(self):
        self._hide_all_frames()
        self._hide_all_widgets()

        self.futurE_frame.pack(fill="both", expand=True)

        # Boutons
        self.button_accueil.place(relx=0.05, rely=0.06, anchor="center", height=30, width=100)
        self.button_candidat.place(relx=0.15, rely=0.06, anchor="center", height=30, width=150)

        # Contenu dynamique
        self.afficher_elections_futur()

    def show_currentE_frame(self):
        self._hide_all_frames()
        self._hide_all_widgets()

        self.currentE_frame.pack(fill="both", expand=True)

        # Boutons
        self.button_accueil.place(relx=0.05, rely=0.06, anchor="center", height=30, width=100)
        self.button_candidat.place(relx=0.15, rely=0.06, anchor="center", height=30, width=150)

        # Contenu dynamique
        self.afficher_elections_encours()

    def show_finishE_frame(self):
        self._hide_all_frames()
        self._hide_all_widgets()

        self.finishE_frame.pack(fill="both", expand=True)

        # Boutons
        self.button_accueil.place(relx=0.05, rely=0.06, anchor="center", height=30, width=100)
        self.button_candidat.place(relx=0.15, rely=0.06, anchor="center", height=30, width=150)

        # Contenu dynamique
        self.afficher_elections_finies()

    def show_gererele_frame(self):
        self._hide_all_frames()
        self._hide_all_widgets()

        self.gererele_frame.pack(fill="both", expand=True)

        # Boutons
        self.button_accueil.place(relx=0.1, rely=0.06, anchor="center", height=30, width=100)

    def show_gerercon_frame(self):
        self._hide_all_frames()
        self._hide_all_widgets()

        self.gerercon_frame.pack(fill="both", expand=True)

        # Boutons
        self.button_accueil.place(relx=0.1, rely=0.06, anchor="center", height=30, width=100)

        # Contenu dynamique
        self.afficher_gérer_candidature()

    def show_voirres_frame(self):
        self._hide_all_frames()
        self._hide_all_widgets()

        self.voirres_frame.pack(fill="both", expand=True)

        # Boutons
        self.button_accueil.place(relx=0.1, rely=0.06, anchor="center", height=30, width=100)

    def show_postuler_individuelle_frame(self):
        self._hide_all_frames()
        self._hide_all_widgets()

        self.postuler_individuelle_frame.pack(fill="both", expand=True)

        # Boutons de navigation
        self.button_accueil.place(relx=0.7, rely=0.06, anchor="center", height=30, width=100)
        self.button_candidat.place(relx=0.8, rely=0.06, anchor="center", height=30, width=150)

        # Champs
        self.nom1.place(relx=0.23, rely=0.45, anchor="center", height=30, width=180)
        self.prenom1.place(relx=0.23, rely=0.6, anchor="center", height=30, width=180)
        self.combo_classe1.place(relx=0.63, rely=0.23, anchor="center", height=30, width=180)
        self.motivation.place(relx=0.7, rely=0.6, anchor="center", height=160, width=440)

    def show_postuler_liste_frame(self):
        self._hide_all_frames()
        self._hide_all_widgets()

        self.postuler_liste_frame.pack(fill="both", expand=True)

        # Boutons de navigation
        self.button_accueil.place(relx=0.7, rely=0.06, anchor="center", height=30, width=100)
        self.button_candidat.place(relx=0.8, rely=0.06, anchor="center", height=30, width=150)

    def show_voter1_frame(self):
        self._hide_all_frames()
        self._hide_all_widgets()
        # Nettoyer les anciens radiobuttons de vote si présents
        if hasattr(self, '_vote_radio_widgets'):
            for w in self._vote_radio_widgets:
                try:
                    w.destroy()
                except Exception:
                    pass
            self._vote_radio_widgets = []

        self.voter1_frame.pack(fill="both", expand=True)

        # Boutons de navigation
        self.button_accueil.place(relx=0.7, rely=0.06, anchor="center", height=30, width=100)
        self.button_candidat.place(relx=0.8, rely=0.06, anchor="center", height=30, width=150)

    def show_voter2_frame(self):
        self._hide_all_frames()
        self._hide_all_widgets()

        self.voter2_frame.pack(fill="both", expand=True)

        self.button_accueil.place(relx=0.7, rely=0.06, anchor="center", height=30, width=100)
        self.button_candidat.place(relx=0.8, rely=0.06, anchor="center", height=30, width=150)

    def show_voter3_frame(self):
        self._hide_all_frames()
        self._hide_all_widgets()

        self.voter3_frame.pack(fill="both", expand=True)

        self.button_accueil.place(relx=0.7, rely=0.06, anchor="center", height=30, width=100)
        self.button_candidat.place(relx=0.8, rely=0.06, anchor="center", height=30, width=150)

    def show_voter4_frame(self):
        self._hide_all_frames()
        self._hide_all_widgets()

        self.voter4_frame.pack(fill="both", expand=True)

        self.button_accueil.place(relx=0.7, rely=0.06, anchor="center", height=30, width=100)
        self.button_candidat.place(relx=0.8, rely=0.06, anchor="center", height=30, width=150)

    # ====================================================================== #
    #  LOGIQUE METIER                                                         #
    # ====================================================================== #

    def register(self):
        email = self.email1.get()
        prenom = self.prenom.get()
        nom = self.nom.get()
        password = self.password1.get()
        date_naissance = self.date_entry.get()
        classe = self.combo_classe.get()
        Qs = self.question.get()

        with open("Fichier_Student_Json.json", "r") as f:
            students = json.load(f)

        email_valide = any(s["email"] == email for s in students)

        if not email_valide:
            self.label_error = tk.Label(self.register_frame,
                text="email non valide,réssayer!", bg="#b4c9de", fg="red", font=15)
            self.label_error.place(relx=0.71, rely=0.9, anchor="center", width=200)
            for entry in [self.prenom, self.nom, self.email1, self.password1, self.confirm, self.question]:
                entry.delete(0, tk.END)
            self.date_entry.delete(0, tk.END)
            return

        try:
            with open("Fichier_personnes_inscrites.json", "r") as f:
                inscrits = json.load(f)
        except:
            inscrits = []

        for personne in inscrits:
            if personne["email"] == email:
                self.label_error = tk.Label(self.register_frame,
                    text="Vous êtes déjà inscrit !", bg="#b4c9de", fg="red", font=15)
                self.label_error.place(relx=0.71, rely=0.9, anchor="center", width=250)
                return

        inscrits.append({
            "prenom": prenom, "email": email, "nom": nom,
            "password": password, "date_naissance": date_naissance,
            "classe": classe, "question_secrete": Qs
        })

        with open("Fichier_personnes_inscrites.json", "w") as f:
            json.dump(inscrits, f, indent=4)

        self.label_error = tk.Label(self.register_frame,
            text="Inscription réussie", bg="#b4c9de", fg="green", font=15)
        self.label_error.place(relx=0.71, rely=0.9, anchor="center", width=200)
        for entry in [self.prenom, self.nom, self.email1, self.password1, self.confirm, self.question]:
            entry.delete(0, tk.END)
        self.date_entry.delete(0, tk.END)

    def login(self):
        email = self.email2.get()
        password = self.password2.get()
        statut = self.role.get()

        try:
            with open("Fichier_personnes_inscrites.json", "r") as f:
                inscrits = json.load(f)
        except:
            inscrits = []

        utilisateur_trouve = False
        for personne in inscrits:
            if personne["email"] == email and personne["password"] == password:
                utilisateur_trouve = True
                self.utilisateur_connecte = personne
                break

        if utilisateur_trouve:
            if statut == "Candidat":
                self.show_condidat_frame()
            else:
                self.show_admin_frame()
        else:
            self.label_error = tk.Label(self.login_frame,
                text="email ou mot de passe incorrecte",
                bg="white", fg="red", font=15)
            self.label_error.place(relx=0.3, rely=0.3, anchor="center", width=400)

        self.email2.delete(0, tk.END)
        self.password2.delete(0, tk.END)

    def verifier(self):
        questions = self.ecole.get()
        email = self.email2.get()

        try:
            with open("Fichier_personnes_inscrites.json", "r") as f:
                inscrits = json.load(f)
        except:
            inscrits = []

        utilisateur_trouve = False
        for personne in inscrits:
            if personne["email"] == email and personne["question_secrete"] == questions:
                utilisateur_trouve = True
                break

        if utilisateur_trouve:
            self.show_nmpo_frame()
        else:
            self.label_error = tk.Label(self.mpo_frame,
                text="Réponse incorrecte", bg="white", fg="red", font=15)
            self.label_error.place(relx=0.48, rely=0.55, anchor="center", width=250)

        self.ecole.delete(0, tk.END)

    def mp(self):
        email = self.email2.get()

        try:
            with open("Fichier_personnes_inscrites.json", "r") as f:
                inscrits = json.load(f)
        except:
            inscrits = []

        utilisateur_trouve = False
        for personne in inscrits:
            if personne["email"] == email:
                utilisateur_trouve = True
                self.email_reset = email
                break

        if utilisateur_trouve:
            self.show_mpo_frame()
        else:
            self.label_error = tk.Label(self.login_frame,
                text="Saisir votre email", bg="white", fg="red", font=15)
            self.label_error.place(relx=0.3, rely=0.59, anchor="center", width=250)

        self.email2.delete(0, tk.END)

    def nmpof(self):
        email = getattr(self, 'email_reset', '')
        passwordn = self.npassword.get()
        passwordc = self.cpassword.get()

        try:
            with open("Fichier_personnes_inscrites.json", "r") as f:
                inscrits = json.load(f)
        except:
            inscrits = []

        utilisateur_trouve = False
        for personne in inscrits:
            if personne["email"] == email and passwordn == passwordc:
                utilisateur_trouve = True
                personne["password"] = passwordn
                break

        if utilisateur_trouve:
            with open("Fichier_personnes_inscrites.json", "w") as f:
                json.dump(inscrits, f, indent=4)
            self.show_login_frame()
        else:
            self.label_error = tk.Label(self.nmpo_frame,
                text="Mots de passe incorrects ou différents",
                bg="white", fg="red", font=15)
            self.label_error.place(relx=0.49, rely=0.72, anchor="center", width=300)

        self.npassword.delete(0, tk.END)
        self.cpassword.delete(0, tk.END)

    # ====================================================================== #
    #  ELECTIONS                                                              #
    # ====================================================================== #

    def afficher_elections_futur(self):
        if hasattr(self, 'canvas_futur'):
            self.canvas_futur.destroy()
        if hasattr(self, 'scrollbar_futur'):
            self.scrollbar_futur.destroy()

        try:
            with open("Fichier_Elections.json", "r", encoding="utf-8") as f:
                elections = json.load(f)
        except:
            elections = []

        elections_futur = [e for e in elections if e.get("statut", "").strip().lower() == "futur"]

        self.canvas_futur = tk.Canvas(self.futurE_frame, bg="#7fafc0", highlightthickness=0)
        self.scrollbar_futur = tk.Scrollbar(self.futurE_frame, orient="vertical", command=self.canvas_futur.yview)
        self.canvas_futur.configure(yscrollcommand=self.scrollbar_futur.set)

        self.canvas_futur.place(relx=0.28, rely=0.27, relwidth=0.43, relheight=0.72)
        self.scrollbar_futur.place(relx=0.72, rely=0.27, relheight=0.72)

        inner_frame = tk.Frame(self.canvas_futur, bg="#7fafc0")
        canvas_window = self.canvas_futur.create_window((0, 0), window=inner_frame, anchor="nw")

        def on_canvas_resize1(event):
            self.canvas_futur.itemconfig(canvas_window, width=event.width)
        self.canvas_futur.bind("<Configure>", on_canvas_resize1)

        for election in elections_futur:
            self.creer_carte_election_futur(inner_frame, election)

        inner_frame.update_idletasks()
        self.canvas_futur.configure(scrollregion=self.canvas_futur.bbox("all"))
        self.canvas_futur.bind("<MouseWheel>", lambda e: self.canvas_futur.yview_scroll(-1*(e.delta//120), "units"))

    def creer_carte_election_futur(self, parent, election):
        carte = tk.Frame(parent, bg="white", bd=1, relief="solid")
        carte.pack(fill="x", padx=10, pady=8, ipady=8)

        tk.Label(carte, text=election.get("titre", ""), bg="white",
            font=("Arial", 11, "bold"), anchor="w").pack(anchor="w", padx=10, pady=(8, 2))
        tk.Label(carte, text=f"Date de départ d'élection :    {election.get('date_debut', '')}",
            bg="white", font=("Arial", 9), anchor="w").pack(anchor="w", padx=10)
        tk.Label(carte, text=f"Date de fin d'élection :           {election.get('date_fin', '')}",
            bg="white", font=("Arial", 9), anchor="w").pack(anchor="w", padx=10)

        btn_frame = tk.Frame(carte, bg="white")
        btn_frame.pack(fill="x", padx=10, pady=(7, 4))

        tk.Button(btn_frame, text="Voir les condidats",
            fg="white", bg="#073763", activeforeground="white",
            borderwidth=0, highlightthickness=0, relief="flat",
            width=20, height=2,
            command=lambda e=election: self.voir_candidats(e)
        ).pack(side="left")

        tk.Button(btn_frame, text="Postuler comme candidat",
            fg="white", bg="#073763", activeforeground="white",
            borderwidth=0, highlightthickness=0, relief="flat",
            width=20, height=2,
            command=lambda e=election: self.postuler_candidat(e)
        ).pack(side="right")

    def afficher_elections_encours(self):
        if hasattr(self, 'canvas_encours'):
            self.canvas_encours.destroy()
        if hasattr(self, 'scrollbar_encours'):
            self.scrollbar_encours.destroy()

        try:
            with open("Fichier_Elections.json", "r", encoding="utf-8") as f:
                elections = json.load(f)
        except:
            elections = []

        elections_encours = [e for e in elections if e.get("statut", "").strip().lower() == "en cours"]

        email_connecte = getattr(self, "utilisateur_connecte", {}).get("email", "")
        try:
            with open("Fichier_Votes.json", "r", encoding="utf-8") as f:
                votes = json.load(f)
        except:
            votes = []

        titres_deja_votes = {v["titre"] for v in votes if email_connecte in v.get("votants", [])}
        elections_encours = [e for e in elections_encours if e["titre"] not in titres_deja_votes]

        self.canvas_encours = tk.Canvas(self.currentE_frame, bg="#7fafc0", highlightthickness=0)
        self.scrollbar_encours = tk.Scrollbar(self.currentE_frame, orient="vertical", command=self.canvas_encours.yview)
        self.canvas_encours.configure(yscrollcommand=self.scrollbar_encours.set)

        self.canvas_encours.place(relx=0.28, rely=0.27, relwidth=0.43, relheight=0.72)
        self.scrollbar_encours.place(relx=0.72, rely=0.27, relheight=0.72)

        inner_frame = tk.Frame(self.canvas_encours, bg="#7fafc0")
        canvas_window = self.canvas_encours.create_window((0, 0), window=inner_frame, anchor="nw")

        def on_canvas_resize2(event):
            self.canvas_encours.itemconfig(canvas_window, width=event.width)
        self.canvas_encours.bind("<Configure>", on_canvas_resize2)

        for election in elections_encours:
            self.creer_carte_election_encours(inner_frame, election)

        inner_frame.update_idletasks()
        self.canvas_encours.configure(scrollregion=self.canvas_encours.bbox("all"))
        self.canvas_encours.bind("<MouseWheel>", lambda e: self.canvas_encours.yview_scroll(-1*(e.delta//120), "units"))

    def creer_carte_election_encours(self, parent, election):
        carte = tk.Frame(parent, bg="white", bd=1, relief="solid")
        carte.pack(fill="x", padx=10, pady=8, ipady=8)

        tk.Label(carte, text=election.get("titre", ""), bg="white",
            font=("Arial", 11, "bold"), anchor="w").pack(anchor="w", padx=10, pady=(8, 2))
        tk.Label(carte, text=f"Date de départ d'élection :    {election.get('date_debut', '')}",
            bg="white", font=("Arial", 9), anchor="w").pack(anchor="w", padx=10)
        tk.Label(carte, text=f"Date de fin d'élection :           {election.get('date_fin', '')}",
            bg="white", font=("Arial", 9), anchor="w").pack(anchor="w", padx=10)

        btn_frame = tk.Frame(carte, bg="white")
        btn_frame.pack(fill="x", padx=10, pady=(7, 4))

        tk.Button(btn_frame, text="Voir les condidats",
            fg="white", bg="#073763", activeforeground="white",
            borderwidth=0, highlightthickness=0, relief="flat",
            width=20, height=2,
            command=lambda e=election: self.voir_candidats(e)
        ).pack(side="left")

        tk.Button(btn_frame, text="Participer au vote",
            fg="white", bg="#073763", activeforeground="white",
            borderwidth=0, highlightthickness=0, relief="flat",
            width=20, height=2,
            command=lambda e=election: self.participer_vote(e)
        ).pack(side="right")

    def afficher_elections_finies(self):
        if hasattr(self, 'canvas_finies'):
            self.canvas_finies.destroy()
        if hasattr(self, 'scrollbar_finies'):
            self.scrollbar_finies.destroy()

        try:
            with open("Fichier_Elections.json", "r", encoding="utf-8") as f:
                elections = json.load(f)
        except:
            elections = []

        elections_finies = [e for e in elections if e.get("statut", "").strip().lower() == "terminé"]

        self.canvas_finies = tk.Canvas(self.finishE_frame, bg="#7fafc0", highlightthickness=0)
        self.scrollbar_finies = tk.Scrollbar(self.finishE_frame, orient="vertical", command=self.canvas_finies.yview)
        self.canvas_finies.configure(yscrollcommand=self.scrollbar_finies.set)

        self.canvas_finies.place(relx=0.28, rely=0.27, relwidth=0.43, relheight=0.72)
        self.scrollbar_finies.place(relx=0.72, rely=0.27, relheight=0.72)

        inner_frame = tk.Frame(self.canvas_finies, bg="#7fafc0")
        canvas_window = self.canvas_finies.create_window((0, 0), window=inner_frame, anchor="nw")

        def on_canvas_resize3(event):
            self.canvas_finies.itemconfig(canvas_window, width=event.width)
        self.canvas_finies.bind("<Configure>", on_canvas_resize3)

        for election in elections_finies:
            self.creer_carte_election_finies(inner_frame, election)

        inner_frame.update_idletasks()
        self.canvas_finies.configure(scrollregion=self.canvas_finies.bbox("all"))
        self.canvas_finies.bind("<MouseWheel>", lambda e: self.canvas_finies.yview_scroll(-1*(e.delta//120), "units"))

    def creer_carte_election_finies(self, parent, election):
        carte = tk.Frame(parent, bg="white", bd=1, relief="solid")
        carte.pack(fill="x", padx=10, pady=8, ipady=8)

        tk.Label(carte, text=election.get("titre", ""), bg="white",
            font=("Arial", 11, "bold"), anchor="w").pack(anchor="w", padx=10, pady=(8, 2))
        tk.Label(carte, text=f"Date de départ d'élection :    {election.get('date_debut', '')}",
            bg="white", font=("Arial", 9), anchor="w").pack(anchor="w", padx=10)
        tk.Label(carte, text=f"Date de fin d'élection :           {election.get('date_fin', '')}",
            bg="white", font=("Arial", 9), anchor="w").pack(anchor="w", padx=10)

        btn_frame = tk.Frame(carte, bg="white")
        btn_frame.pack(fill="x", padx=10, pady=(7, 4))

        tk.Button(btn_frame, text="Voir les condidats",
            fg="white", bg="#073763", activeforeground="white",
            borderwidth=0, highlightthickness=0, relief="flat",
            width=20, height=2,
            command=lambda e=election: self.voir_candidats(e)
        ).pack(side="left")

        tk.Button(btn_frame, text="Voir les résultats",
            fg="white", bg="#073763", activeforeground="white",
            borderwidth=0, highlightthickness=0, relief="flat",
            width=20, height=2,
            command=lambda e=election: self.voir_résultats(e)
        ).pack(side="right")

    # ====================================================================== #
    #  CANDIDATS                                                              #
    # ====================================================================== #

    def afficher_candidats(self, election, frame):
        try:
            with open("Fichier_candidatures.json", "r", encoding="utf-8") as f:
                candidatures = json.load(f)
        except:
            candidatures = []

        candidats = []
        type_election = election.get("type", "")
        for e in candidatures:
            if e["titre"] == election["titre"]:
                candidats = e.get("candidats", [])
                type_election = e.get("type", "")
                break

        canvas = tk.Canvas(frame, bg="#BAD2D7", highlightthickness=0)
        scrollbar = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)

        inner_frame = tk.Frame(canvas, bg="#BAD2D7")
        window_id = canvas.create_window((0, 0), window=inner_frame, anchor="nw")

        canvas.bind("<Configure>", lambda e: canvas.itemconfig(window_id, width=e.width))
        inner_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.bind_all("<MouseWheel>", lambda e: canvas.yview_scroll(-1*(e.delta//120), "units"))

        for c in candidats:
            self.creer_carte_candidats(inner_frame, c, type_election)

    def creer_carte_candidats(self, parent, candidature, type_election):
        carte = tk.Frame(parent, bg="white", bd=1, relief="solid")
        carte.pack(fill="x", padx=10, pady=8, ipady=10)

        if type_election == "individuelle":
            tk.Label(carte, text=f"{candidature.get('prenom','')} {candidature.get('nom','')}",
                bg="white", font=("Arial", 12, "bold")).pack(anchor="center", padx=10)
            tk.Label(carte, text=f"Classe : {candidature.get('classe','')}",
                bg="white", font=("Arial", 10)).pack(anchor="center", padx=10)
        else:
            tk.Label(carte, text=candidature.get("nom_liste", ""),
                bg="white", font=("Arial", 12, "bold")).pack(anchor="center", padx=10)
            tk.Label(carte, text="Membres :",
                bg="white", font=("Arial", 10, "bold")).pack(anchor="center", padx=10, pady=(5, 0))
            tk.Label(carte, text="\n".join(candidature.get("membres", [])),
                bg="white", font=("Arial", 10)).pack(anchor="center", padx=20)

    def voir_candidats(self, election):
        win = tk.Toplevel(self.root)
        win.title("Candidats")
        win.geometry("600x500")
        win.configure(bg="#BAD2D7")
        self.afficher_candidats(election, win)

    # ====================================================================== #
    #  RÉSULTATS                                                              #
    # ====================================================================== #

    def afficher_résultats(self, election, frame):
        try:
            with open("Fichier_Votes.json", "r", encoding="utf-8") as f:
                votes = json.load(f)
        except:
            votes = []

        résultats = {}
        for v in votes:
            if v["titre"] == election["titre"]:
                résultats = v.get("resultats", {})
                break

        canvas = tk.Canvas(frame, bg="#BAD2D7", highlightthickness=0)
        scrollbar = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)

        inner_frame = tk.Frame(canvas, bg="#BAD2D7")
        window_id = canvas.create_window((0, 0), window=inner_frame, anchor="nw")

        canvas.bind("<Configure>", lambda e: canvas.itemconfig(window_id, width=e.width))
        inner_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.bind_all("<MouseWheel>", lambda e: canvas.yview_scroll(-1*(e.delta//120), "units"))

        for cand, nbrv in résultats.items():
            self.creer_carte_résultats(inner_frame, cand, nbrv)

    def creer_carte_résultats(self, parent, candidat, résultat):
        carte = tk.Frame(parent, bg="white", bd=1, relief="solid")
        carte.pack(fill="x", padx=10, pady=8, ipady=10)
        tk.Label(carte,
            text=f"Le candidat/La liste '{candidat}' a eu : {résultat} vote(s)",
            bg="white", font=("Arial", 12, "bold")).pack(anchor="center", padx=10)

    def voir_résultats(self, election):
        win = tk.Toplevel(self.root)
        win.title("Résultats")
        win.geometry("600x500")
        win.configure(bg="#BAD2D7")
        self.afficher_résultats(election, win)

    # ====================================================================== #
    #  POSTULER                                                               #
    # ====================================================================== #

    def postuler_candidat(self, election):
        if election.get('type') == "individuelle":
            self.show_postuler_individuelle_frame()

            self.label_nomE.place(relx=0.25, rely=0.26, anchor="center", width=320, height=30)
            self.label_nomE.config(text=election.get("titre", ""),
                bg="#BAD2D7", fg="black", font=14)

            self.button_candidater.config(command=lambda e=election: self.candidater(e))
            self.button_candidater.place(relx=0.52, rely=0.8, anchor="center", height=30, width=150)

        elif election.get('type') == "liste":
            self.show_postuler_liste_frame()

            self.label_nomE.place(relx=0.25, rely=0.26, anchor="center", width=320, height=30)
            self.label_nomE.config(text=election.get("titre", ""),
                bg="#BAD2D7", fg="black", font=14)

            self.membres_liste = []

            self.nom2.place(relx=0.32, rely=0.45, anchor="center", height=30, width=410)

            self.search_entry.place(relx=0.7, rely=0.23, anchor="center", height=30, width=420)
            self.listbox_suggestions.place(relx=0.7, rely=0.28, anchor="n", width=420, height=100)

            self.label_membres.config(text="Membres : ", bg="white", fg="black",
                font=("Arial", 10), wraplength=400, justify="left")
            self.label_membres.place(relx=0.7, rely=0.6, anchor="center", width=430, height=120)

            with open("Fichier_Student_Json.json", "r", encoding="utf-8") as f:
                self.etudiants = json.load(f)

            def rechercher(event):
                texte = self.search_entry.get().strip().lower()
                self.listbox_suggestions.delete(0, tk.END)
                if not texte:
                    return
                for etudiant in self.etudiants:
                    nom_complet = etudiant['nom_complet']
                    if texte in nom_complet.lower():
                        self.listbox_suggestions.insert(tk.END, nom_complet)

            self.search_entry.bind("<KeyRelease>", rechercher)

            def ajouter_membre(event):
                selection = self.listbox_suggestions.curselection()
                if not selection:
                    return
                nom_complet = self.listbox_suggestions.get(selection[0])
                if nom_complet not in self.membres_liste:
                    self.membres_liste.append(nom_complet)
                self.label_membres.config(text="Membres :\n" + "\n".join(self.membres_liste))
                self.search_entry.delete(0, tk.END)
                self.listbox_suggestions.delete(0, tk.END)

            self.listbox_suggestions.bind("<<ListboxSelect>>", ajouter_membre)

            self.motivation.place(relx=0.32, rely=0.65, anchor="center", height=150, width=410)

            self.button_candidater.config(text="Soumettre la liste",
                command=lambda e=election: self.candidater(e))
            self.button_candidater.place(relx=0.75, rely=0.8, anchor="center", height=35, width=180)

    # ====================================================================== #
    #  VOTE                                                                   #
    # ====================================================================== #

    def participer_vote(self, election):
        try:
            with open("Fichier_candidatures.json", "r", encoding="utf-8") as f:
                candidatures = json.load(f)
        except:
            candidatures = []

        candidats = []
        type_election = election.get("type", "")
        for e in candidatures:
            if e["titre"] == election["titre"]:
                candidats = e.get("candidats", [])
                break

        email_connecte = getattr(self, "utilisateur_connecte", {}).get("email", "")
        try:
            with open("Fichier_Votes.json", "r", encoding="utf-8") as f:
                votes = json.load(f)
        except:
            votes = []

        for v in votes:
            if v["titre"] == election["titre"]:
                if email_connecte in v.get("votants", []):
                    tk.messagebox.showwarning("Déjà voté",
                        f"Vous avez déjà voté pour l'élection :\n{election['titre']}")
                    return
                break

        self.show_voter1_frame()

        self.choix_vote = tk.StringVar()
        self._vote_radio_widgets = []

        if type_election == "individuelle":
            for i, c in enumerate(candidats):
                choix = f"{c.get('prenom', '')} {c.get('nom', '')}"
                rb = tk.Radiobutton(self.voter1_frame, text=choix,
                    variable=self.choix_vote, value=choix,
                    bg="#CCC6DC", font=("Arial", 15))
                rb.place(relx=0.2, rely=0.5 + i * 0.08, anchor="w")
                self._vote_radio_widgets.append(rb)
        else:
            for i, c in enumerate(candidats):
                choix = c.get("nom_liste", "")
                rb = tk.Radiobutton(self.voter1_frame, text=choix,
                    variable=self.choix_vote, value=choix,
                    bg="#CCC6DC", font=("Arial", 15))
                rb.place(relx=0.2, rely=0.5 + i * 0.08, anchor="w")
                self._vote_radio_widgets.append(rb)

        def aller_voter2():
            valeur = self.choix_vote.get()
            self.show_voter2_frame()
            tk.Label(self.voter2_frame, text=valeur, font=("Arial", 20),
                bg="#CCC6DC", fg="black").place(relx=0.5, rely=0.6,
                anchor="center", height=30, width=180)

        def aller_voter3():
            self.show_voter3_frame()
            tk.Button(self.voter3_frame, text="changer votre vote", font=("Arial", 15),
                bg="white", fg="black",
                command=self.show_voter1_frame).place(relx=0.3, rely=0.7, anchor="w")
            tk.Button(self.voter3_frame, text="confirmer votre vote", font=("Arial", 15),
                bg="#80350E", fg="white",
                command=aller_voter4).place(relx=0.6, rely=0.7, anchor="w")

        def aller_voter4():
            self.show_voter4_frame()

            self.label_confirm_pdf = tk.Label(self.label_voter4,
                text="télécharger vos choix comme pdf",
                bg="#CCC6DC", fg="#CCC6DC",
                font=("Arial", 11, "bold"), wraplength=400, justify="center")
            self.label_confirm_pdf.place(relx=0.4, rely=0.74,
                anchor="center", width=450, height=40)

            if hasattr(self, 'btn_pdf'):
                self.btn_pdf.destroy()

            def telecharger_recu_pdf():
                votant   = getattr(self, "utilisateur_connecte", {})
                prenom_v = votant.get("prenom", "")
                nom_v    = votant.get("nom", "")
                email_v  = votant.get("email", "")
                classe_v = votant.get("classe", "")
                choix_v  = self.choix_vote.get()
                titre_v  = election.get("titre", "")
                date_v   = datetime.now().strftime("%d/%m/%Y à %H:%M")

                nom_fichier = (
                    f"recu_vote_{prenom_v}_{nom_v}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
                ).replace(" ", "_")

                import winreg
                try:
                    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                        r"Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders")
                    bureau = winreg.QueryValueEx(key, "Desktop")[0]
                except:
                    bureau = os.path.join(os.path.expanduser("~"), "Desktop")

                chemin_pdf = os.path.join(bureau, nom_fichier)

                doc = SimpleDocTemplate(chemin_pdf, pagesize=A4,
                    topMargin=2*cm, bottomMargin=2*cm,
                    leftMargin=2.5*cm, rightMargin=2.5*cm)

                styles = getSampleStyleSheet()
                style_titre = ParagraphStyle("Titre", parent=styles["Title"],
                    fontSize=20, textColor=colors.HexColor("#073763"),
                    spaceAfter=6, alignment=TA_CENTER)
                style_sous_titre = ParagraphStyle("SousTitre", parent=styles["Normal"],
                    fontSize=12, textColor=colors.HexColor("#048b9a"),
                    spaceAfter=4, alignment=TA_CENTER)
                style_section = ParagraphStyle("Section", parent=styles["Heading2"],
                    fontSize=13, textColor=colors.HexColor("#073763"),
                    spaceBefore=14, spaceAfter=6)
                style_merci = ParagraphStyle("Merci", parent=styles["Normal"],
                    fontSize=12, textColor=colors.HexColor("#048b9a"),
                    alignment=TA_CENTER, spaceBefore=10, spaceAfter=4)
                style_footer = ParagraphStyle("Footer", parent=styles["Normal"],
                    fontSize=9, textColor=colors.grey, alignment=TA_CENTER)

                story = []
                story.append(Paragraph("EMINES - School of Industrial Management", style_titre))
                story.append(Paragraph("Application de Vote Électronique", style_sous_titre))
                story.append(Spacer(1, 0.3*cm))
                story.append(HRFlowable(width="100%", thickness=2, color=colors.HexColor("#073763")))
                story.append(Spacer(1, 0.5*cm))
                story.append(Paragraph("REÇU DE VOTE", style_titre))
                story.append(Spacer(1, 0.4*cm))

                story.append(Paragraph("Élection concernée", style_section))
                t_election = Table([["Titre :", titre_v], ["Date du vote :", date_v]],
                    colWidths=[5*cm, 11*cm])
                t_election.setStyle(TableStyle([
                    ("FONTNAME",      (0,0), (-1,-1), "Helvetica"),
                    ("FONTSIZE",      (0,0), (-1,-1), 11),
                    ("FONTNAME",      (0,0), (0,-1),  "Helvetica-Bold"),
                    ("TEXTCOLOR",     (0,0), (0,-1),  colors.HexColor("#073763")),
                    ("BOTTOMPADDING", (0,0), (-1,-1), 6),
                    ("TOPPADDING",    (0,0), (-1,-1), 6),
                    ("ROWBACKGROUNDS",(0,0), (-1,-1), [colors.HexColor("#f0f6ff"), colors.white]),
                ]))
                story.append(t_election)
                story.append(Spacer(1, 0.4*cm))

                story.append(Paragraph("Informations du votant", style_section))
                t_votant = Table([
                    ["Prénom :", prenom_v], ["Nom :", nom_v],
                    ["Email :", email_v],   ["Classe :", classe_v],
                ], colWidths=[5*cm, 11*cm])
                t_votant.setStyle(TableStyle([
                    ("FONTNAME",      (0,0), (-1,-1), "Helvetica"),
                    ("FONTSIZE",      (0,0), (-1,-1), 11),
                    ("FONTNAME",      (0,0), (0,-1),  "Helvetica-Bold"),
                    ("TEXTCOLOR",     (0,0), (0,-1),  colors.HexColor("#073763")),
                    ("BOTTOMPADDING", (0,0), (-1,-1), 6),
                    ("TOPPADDING",    (0,0), (-1,-1), 6),
                    ("ROWBACKGROUNDS",(0,0), (-1,-1), [colors.HexColor("#f0f6ff"), colors.white]),
                ]))
                story.append(t_votant)
                story.append(Spacer(1, 0.5*cm))

                story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#048b9a")))
                story.append(Spacer(1, 0.3*cm))
                story.append(Paragraph("Votre choix", style_section))
                story.append(Spacer(1, 0.2*cm))

                t_choix = Table([[choix_v]], colWidths=[16*cm])
                t_choix.setStyle(TableStyle([
                    ("FONTNAME",      (0,0), (-1,-1), "Helvetica-Bold"),
                    ("FONTSIZE",      (0,0), (-1,-1), 14),
                    ("TEXTCOLOR",     (0,0), (-1,-1), colors.HexColor("#073763")),
                    ("ALIGN",         (0,0), (-1,-1), "CENTER"),
                    ("VALIGN",        (0,0), (-1,-1), "MIDDLE"),
                    ("TOPPADDING",    (0,0), (-1,-1), 12),
                    ("BOTTOMPADDING", (0,0), (-1,-1), 12),
                    ("BACKGROUND",    (0,0), (-1,-1), colors.HexColor("#e8f4f8")),
                    ("BOX",           (0,0), (-1,-1), 2, colors.HexColor("#048b9a")),
                ]))
                story.append(t_choix)
                story.append(Spacer(1, 0.6*cm))
                story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#073763")))
                story.append(Spacer(1, 0.4*cm))
                story.append(Paragraph(f"Merci, {prenom_v}, pour votre participation au vote !", style_merci))
                story.append(Paragraph(
                    "Votre voix compte et contribue au bon fonctionnement démocratique de notre école.",
                    style_merci))
                story.append(Spacer(1, 0.3*cm))
                story.append(Paragraph(
                    "Ce document est votre preuve de participation. Conservez-le précieusement.",
                    style_footer))
                story.append(Spacer(1, 0.2*cm))
                story.append(Paragraph(
                    f"Généré le {date_v} — EMINES Vote Électronique", style_footer))

                # Enregistrement du vote
                try:
                    with open("Fichier_Votes.json", "r", encoding="utf-8") as f:
                        votes = json.load(f)
                except:
                    votes = []

                election_trouvee = False
                for v in votes:
                    if v["titre"] == titre_v:
                        election_trouvee = True
                        if choix_v not in v["resultats"]:
                            v["resultats"][choix_v] = 0
                        v["resultats"][choix_v] += 1
                        if email_v not in v["votants"]:
                            v["votants"].append(email_v)
                        break

                if not election_trouvee:
                    votes.append({
                        "titre": titre_v,
                        "resultats": {choix_v: 1},
                        "votants": [email_v]
                    })

                with open("Fichier_Votes.json", "w", encoding="utf-8") as f:
                    json.dump(votes, f, indent=4, ensure_ascii=False)

                doc.build(story)

                if hasattr(self, 'label_confirm_pdf'):
                    self.label_confirm_pdf.destroy()

                try:
                    if platform.system() == "Windows":
                        os.startfile(chemin_pdf)
                    elif platform.system() == "Darwin":
                        subprocess.call(["open", chemin_pdf])
                    else:
                        subprocess.call(["xdg-open", chemin_pdf])
                except Exception:
                    pass

            self.btn_pdf = tk.Button(self.label_voter4,
                text="📄  Télécharger mon reçu PDF",
                font=("Arial", 14, "bold"),
                bg="#073763", fg="white",
                activeforeground="white",
                borderwidth=0, highlightthickness=0,
                relief="flat", cursor="hand2",
                command=telecharger_recu_pdf)
            self.btn_pdf.place(relx=0.5, rely=0.65, anchor="center", height=45, width=280)

        tk.Button(self.voter1_frame, text="Suivant", font=("Arial", 15),
            bg="green", fg="white",
            command=aller_voter2).place(relx=0.8, rely=0.8, anchor="w")
        tk.Button(self.voter2_frame, text="Suivant", font=("Arial", 15),
            bg="green", fg="white",
            command=aller_voter3).place(relx=0.8, rely=0.8, anchor="w")

    # ====================================================================== #
    #  CANDIDATER                                                             #
    # ====================================================================== #

    def candidater(self, election):
        nomE  = election.get('titre')
        typeE = election.get('type')

        if typeE == "individuelle":
            nom    = self.nom1.get().strip()
            prenom = self.prenom1.get().strip()
            classe = self.combo_classe1.get().strip()
            frame_active = self.postuler_individuelle_frame

            if not nom or not prenom or not classe or classe == "classe":
                self.label_error = tk.Label(frame_active,
                    text="Erreur : veuillez remplir tous les champs",
                    bg="#BAD2D7", fg="red", font=15)
                self.label_error.place(relx=0.52, rely=0.88, anchor="center", width=350)
                return

            candidat = {"prenom": prenom, "nom": nom, "classe": classe}

        else:
            frame_active = self.postuler_liste_frame
            nom_liste  = self.nom2.get().strip()
            motivation = self.motivation.get("1.0", tk.END).strip()

            if not nom_liste or not motivation or len(getattr(self, 'membres_liste', [])) == 0:
                self.label_error = tk.Label(frame_active,
                    text="Erreur : veuillez remplir tous les champs",
                    bg="#BAD2D7", fg="red", font=15)
                self.label_error.place(relx=0.52, rely=0.88, anchor="center", width=350)
                return

            candidat = {
                "nom_liste": nom_liste,
                "membres": self.membres_liste,
                "motivation": motivation
            }

        try:
            with open("Fichier_candidatures.json", "r", encoding="utf-8") as f:
                elections = json.load(f)
        except:
            elections = []

        for e in elections:
            if e["titre"] == nomE:
                if "candidats" not in e:
                    e["candidats"] = []

                if typeE == "individuelle":
                    for c in e["candidats"]:
                        if c["nom"] == nom and c["prenom"] == prenom:
                            self.label_error = tk.Label(frame_active,
                                text="Vous avez déjà candidaté à cette élection",
                                bg="#BAD2D7", fg="red", font=15)
                            self.label_error.place(relx=0.52, rely=0.88, anchor="center", width=350)
                            return
                else:
                    for c in e["candidats"]:
                        if c.get("nom_liste") == nom_liste:
                            self.label_error = tk.Label(frame_active,
                                text="Cette liste existe déjà",
                                bg="#BAD2D7", fg="red", font=15)
                            self.label_error.place(relx=0.52, rely=0.88, anchor="center", width=350)
                            return

                e["candidats"].append(candidat)
                with open("Fichier_candidatures.json", "w", encoding="utf-8") as f:
                    json.dump(elections, f, indent=4, ensure_ascii=False)

                self.label_error = tk.Label(frame_active,
                    text="Candidature enregistrée avec succès !",
                    bg="#BAD2D7", fg="green", font=15)
                self.label_error.place(relx=0.52, rely=0.88, anchor="center", width=350)
                return

        elections.append({"titre": nomE, "type": typeE, "candidats": [candidat]})
        with open("Fichier_candidatures.json", "w", encoding="utf-8") as f:
            json.dump(elections, f, indent=4, ensure_ascii=False)

        self.label_error = tk.Label(frame_active,
            text="Candidature enregistrée avec succès !",
            bg="#BAD2D7", fg="green", font=15)
        self.label_error.place(relx=0.52, rely=0.88, anchor="center", width=350)

    # ====================================================================== #
    #  ADMIN                                                                  #
    # ====================================================================== #

    def afficher_gérer_candidature(self):
        if hasattr(self, 'canvas_gérerC'):
            self.canvas_gérerC.destroy()
        if hasattr(self, 'scrollbar_gérerC'):
            self.scrollbar_gérerC.destroy()

        try:
            with open("Fichier_Elections.json", "r", encoding="utf-8") as f:
                elections = json.load(f)
        except:
            elections = []

        elections_futur = [e for e in elections if e.get("statut", "").strip().lower() == "futur"]

        self.canvas_gérerC = tk.Canvas(self.gerercon_frame, bg="white", highlightthickness=0)
        self.scrollbar_gérerC = tk.Scrollbar(self.gerercon_frame, orient="vertical",
            command=self.canvas_gérerC.yview)
        self.canvas_gérerC.configure(yscrollcommand=self.scrollbar_gérerC.set)

        self.canvas_gérerC.place(relx=0.14, rely=0.27, relwidth=0.68, relheight=0.57)
        self.scrollbar_gérerC.place(relx=0.815, rely=0.13, relheight=0.71)

        inner_frame = tk.Frame(self.canvas_gérerC, bg="white")
        canvas_window = self.canvas_gérerC.create_window((0, 0), window=inner_frame, anchor="nw")

        def on_canvas_resize1(event):
            self.canvas_gérerC.itemconfig(canvas_window, width=event.width)
        self.canvas_gérerC.bind("<Configure>", on_canvas_resize1)

        for election in elections_futur:
            self.creer_carte_gérerC(inner_frame, election)

        inner_frame.update_idletasks()
        self.canvas_gérerC.configure(scrollregion=self.canvas_gérerC.bbox("all"))
        self.canvas_gérerC.bind("<MouseWheel>",
            lambda e: self.canvas_gérerC.yview_scroll(-1*(e.delta//120), "units"))

    def creer_carte_gérerC(self, parent, election):
        carte = tk.Frame(parent, bg="#7fafc0", bd=1, relief="solid")
        carte.pack(fill="x", padx=10, pady=8, ipady=8)

        tk.Label(carte, text=election.get("titre", ""), bg="#7fafc0",
            font=("Arial", 11, "bold"), anchor="center").pack(anchor="w", padx=10, pady=(8, 2))
        tk.Label(carte, text=f"Date de départ d'élection :    {election.get('date_debut', '')}",
            bg="#7fafc0", font=("Arial", 9), anchor="center").pack(anchor="w", padx=10)
        tk.Label(carte, text=f"Date de fin d'élection :           {election.get('date_fin', '')}",
            bg="#7fafc0", font=("Arial", 9), anchor="center").pack(anchor="w", padx=10)

        btn_frame = tk.Frame(carte, bg="#7fafc0")
        btn_frame.pack(fill="x", padx=10, pady=(7, 4))

        tk.Button(btn_frame, text="Voir les condidats",
            fg="white", bg="#073763", activeforeground="white",
            borderwidth=0, highlightthickness=0, relief="flat",
            width=20, height=2,
            command=lambda e=election: self.voir_candidats_admin(e)
        ).pack(side="right")

    def afficher_candidats_admin(self, election, frame):
        # On vide le frame avant de le re-remplir (utile pour le rafraîchissement)
        for widget in frame.winfo_children():
            widget.destroy()

        try:
            with open("Fichier_candidatures.json", "r", encoding="utf-8") as f:
                candidatures = json.load(f)
        except:
            candidatures = []

        candidats = []
        type_election = election.get("type", "")
        for e in candidatures:
            if e["titre"] == election["titre"]:
                candidats = e.get("candidats", [])
                type_election = e.get("type", "")
                break

        canvas = tk.Canvas(frame, bg="#BAD2D7", highlightthickness=0)
        scrollbar = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)

        inner_frame = tk.Frame(canvas, bg="#BAD2D7")
        window_id = canvas.create_window((0, 0), window=inner_frame, anchor="nw")

        canvas.bind("<Configure>", lambda e: canvas.itemconfig(window_id, width=e.width))
        inner_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.bind("<MouseWheel>", lambda e: canvas.yview_scroll(-1*(e.delta//120), "units"))

        for c in candidats:
            self.creer_carte_candidats_admin(inner_frame, c, type_election, election, frame)

    def creer_carte_candidats_admin(self, parent, candidature, type_election, election, parent_frame):
        carte = tk.Frame(parent, bg="white", bd=1, relief="solid")
        carte.pack(fill="x", padx=10, pady=8, ipady=10)

        if type_election == "individuelle":
            nom_affiche = f"{candidature.get('prenom','')} {candidature.get('nom','')}"
        else:
            nom_affiche = candidature.get("nom_liste", "")

        tk.Label(carte, text=nom_affiche,
            bg="white", font=("Arial", 12, "bold")).pack(side="left", padx=15, pady=10)

        tk.Button(carte, text="Voir les détails",
            fg="white", bg="#073763", activeforeground="white",
            borderwidth=0, highlightthickness=0, relief="flat",
            width=16, height=1,
            command=lambda c=candidature: self.voir_details_candidat_admin(election, c, type_election, parent_frame)
        ).pack(side="right", padx=15, pady=10)

    def voir_candidats_admin(self, election):
        win = tk.Toplevel(self.root)
        win.title("Candidats")
        win.geometry("600x500")
        win.configure(bg="#BAD2D7")
        self.afficher_candidats_admin(election, win)

    def voir_details_candidat_admin(self, election, candidature, type_election, parent_frame):
        win = tk.Toplevel(self.root)
        win.title("Détails du candidat")
        win.geometry("500x450")
        win.configure(bg="#BAD2D7")

        contenu = tk.Frame(win, bg="white", bd=1, relief="solid")
        contenu.pack(fill="both", expand=True, padx=20, pady=20)

        if type_election == "individuelle":
            tk.Label(contenu, text=f"{candidature.get('prenom','')} {candidature.get('nom','')}",
                bg="white", font=("Arial", 14, "bold")).pack(anchor="w", padx=15, pady=(15, 5))
            tk.Label(contenu, text=f"Classe : {candidature.get('classe','')}",
                bg="white", font=("Arial", 11)).pack(anchor="w", padx=15, pady=3)
        else:
            tk.Label(contenu, text=candidature.get("nom_liste", ""),
                bg="white", font=("Arial", 14, "bold")).pack(anchor="w", padx=15, pady=(15, 5))
            tk.Label(contenu, text="Membres :",
                bg="white", font=("Arial", 11, "bold")).pack(anchor="w", padx=15, pady=(10, 2))
            tk.Label(contenu, text="\n".join(candidature.get("membres", [])),
                bg="white", font=("Arial", 11), justify="left").pack(anchor="w", padx=15)
            tk.Label(contenu, text="Motivation :",
                bg="white", font=("Arial", 11, "bold")).pack(anchor="w", padx=15, pady=(10, 2))
            tk.Label(contenu, text=candidature.get("motivation", ""),
                bg="white", font=("Arial", 11), justify="left", wraplength=440).pack(anchor="w", padx=15)

        btn_frame = tk.Frame(win, bg="#BAD2D7")
        btn_frame.pack(fill="x", pady=15)

        tk.Button(btn_frame, text="Accepter",
            fg="white", bg="#2e7d32", activeforeground="white",
            borderwidth=0, highlightthickness=0, relief="flat",
            width=15, height=2,
            command=win.destroy
        ).pack(side="left", padx=(60, 10))

        tk.Button(btn_frame, text="Refuser",
            fg="white", bg="#c62828", activeforeground="white",
            borderwidth=0, highlightthickness=0, relief="flat",
            width=15, height=2,
            command=lambda: self.refuser_candidat(election, candidature, type_election, win, parent_frame)
        ).pack(side="right", padx=(10, 60))

    def refuser_candidat(self, election, candidature, type_election, win, parent_frame):
        try:
            with open("Fichier_candidatures.json", "r", encoding="utf-8") as f:
                candidatures = json.load(f)
        except:
            candidatures = []

        for e in candidatures:
            if e["titre"] == election["titre"]:
                if type_election == "individuelle":
                    e["candidats"] = [
                        c for c in e.get("candidats", [])
                        if not (c.get("nom") == candidature.get("nom")
                                and c.get("prenom") == candidature.get("prenom"))
                    ]
                else:
                    e["candidats"] = [
                        c for c in e.get("candidats", [])
                        if c.get("nom_liste") != candidature.get("nom_liste")
                    ]
                break

        with open("Fichier_candidatures.json", "w", encoding="utf-8") as f:
            json.dump(candidatures, f, indent=4, ensure_ascii=False)

        win.destroy()
        self.afficher_candidats_admin(election, parent_frame)

    # ====================================================================== #
    #  FIX LAYOUT                                                             #
    # ====================================================================== #
    def fix_layout(self):
        self.root.update_idletasks()
        self.show_accueil_frame()


root = tk.Tk()
app = App(root)
root.mainloop()