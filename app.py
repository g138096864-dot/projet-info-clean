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
        self.image_ajouterelec = Image.open("ajouter une election.png")

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
        self.ajouterelec_frame         = tk.Frame(root)

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

        self.label_ajouterelec = tk.Label(self.ajouterelec_frame)
        self.label_ajouterelec.pack(fill="both", expand=True)

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
        self.ajouterelec_frame.bind("<Configure>", self.resize_image_ajouterelec)
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

        self.button_mpo = tk.Button(self.login_frame, text="Mot de passe oublié ?",
            fg="#048b9a", bg="white",
            activeforeground="#073763", borderwidth=0, highlightthickness=0,
            relief="flat", font=("Arial", 10, "underline"),
            cursor="hand2", command=self.mp)
        self.button_mpo.bind("<Enter>", lambda e: self.button_mpo.config(fg="#073763"))
        self.button_mpo.bind("<Leave>", lambda e: self.button_mpo.config(fg="#048b9a"))

        self.button_candidat = tk.Button(root, text="Page candidat",
            fg="white", bg="#048b9a",
            activeforeground="white", borderwidth=0, highlightthickness=0,
            relief="flat", font=20, command=self.show_condidat_frame)

        self.button_admin = tk.Button(root, text="Page admin",
            fg="white", bg="#048b9a",
            activeforeground="white", borderwidth=0, highlightthickness=0,
            relief="flat", font=20, command=self.show_admin_frame)

        self.button_logout = tk.Button(root, text="Déconnexion",
            fg="white", bg="#c62828",
            activeforeground="white", borderwidth=0, highlightthickness=0,
            relief="flat", font=20, command=self.show_accueil_frame)

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
        self.button_ajouterele = tk.Button(self.gererele_frame, text="Ajouter une éléction",
            fg="black", bg="#bcc0c5",
            activeforeground="white", borderwidth=0, highlightthickness=0,
            font=("Arial", 18), relief="flat" , command=self.ajouter_elec)
        
        self.button_ajouterele1 = tk.Button(self.ajouterelec_frame, text="Ajouter ",
            fg="white", bg="#073763",
            activeforeground="white", borderwidth=0, highlightthickness=0,
            font=("Arial", 18), relief="flat", command=self.enregistrer_election)
        # ------------------------------------------------------------------ #
        #  AUTRES ÉLÉMENTS                                                     #
        # ------------------------------------------------------------------ #
        
        self.email1    = tk.Entry(root, bg="white")
        self.password1 = tk.Entry(root, bg="white", show="*")
        self.btn_eye1 = tk.Button(root, text="👁", bg="white", relief="flat",
                                borderwidth=0, cursor="hand2",
                                command=lambda: self._toggle_password(self.password1, self.btn_eye1))
        self.email2    = tk.Entry(root, bg="#eeeeee")
        self.password2 = tk.Entry(root, bg="#eeeeee", show="*")
        self.btn_eye2 = tk.Button(root, text="👁", bg="#eeeeee", relief="flat",
                                borderwidth=0, cursor="hand2",
                                command=lambda: self._toggle_password(self.password2, self.btn_eye2))

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
        self.btn_eye3 = tk.Button(self.nmpo_frame, text="👁", bg="#eeeeee", relief="flat",
                                    borderwidth=0, cursor="hand2",
                                    command=lambda: self._toggle_password(self.npassword, self.btn_eye3))

        self.cpassword = tk.Entry(self.nmpo_frame, bg="#eeeeee", show="*")
        self.btn_eye4 = tk.Button(self.nmpo_frame, text="👁", bg="#eeeeee", relief="flat",
                                borderwidth=0, cursor="hand2",
                                command=lambda: self._toggle_password(self.cpassword, self.btn_eye4))
        
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

        self.classes = ["2026", "2027", "2028", "2029", "2030"]
        self.combo_classe  = ttk.Combobox(root, values=self.classes, state="normal")
        self.combo_classe.set("classe")
        self.combo_classe1 = ttk.Combobox(root, values=self.classes, state="normal")
        self.combo_classe1.set("classe")

        # Widgets spécifiques à postuler_liste — initialisés ici pour pouvoir
        # les cacher proprement partout sans AttributeError
        self.search_entry       = tk.Entry(root, bg="white")
        self.listbox_suggestions = tk.Listbox(root, font=("Arial", 10))
        self.label_membres      = tk.Label(root, text="Membres : ", bg="white",
            fg="black", font=("Arial", 10), wraplength=400, justify="left")
        self.label_nomE         = tk.Label(root, text="", fg="black", font=14, bg="#BAD2D7")
        self.nomE1    = tk.Entry(self.ajouterelec_frame, fg="black", font=12, bg="white")
        self.objectif = tk.Text(self.ajouterelec_frame, fg="black", font=12, bg="white")
        self.role = tk.StringVar(value="Admin")
        self.radio_admin = tk.Radiobutton(self.login_frame, text="Admin",
            variable=self.role, value="Admin", bg="white", font=("Arial", 13, "bold"))
        self.radio_candidat = tk.Radiobutton(self.login_frame, text="Candidat",
            variable=self.role, value="Candidat", bg="white", font=("Arial", 13, "bold"))
        self.radio_admin.place(relx=0.23, rely=0.68, anchor="center")
        self.radio_candidat.place(relx=0.235, rely=0.74, anchor="center")

        self.root.after(100, self.fix_layout)

        self.typelec = tk.StringVar(value="Individuelle")
        self.radio_individuelle = tk.Radiobutton(self.ajouterelec_frame, text="Individuelle",
            variable=self.typelec, value="individuelle", bg="#BAD2D7", font=("Arial", 13, "bold"))
        self.radio_liste = tk.Radiobutton(self.ajouterelec_frame, text="Liste",
            variable=self.typelec, value="liste", bg="#BAD2D7", font=("Arial", 13, "bold"))

    # ====================================================================== #
    #  AIDE : cache TOUS les widgets mobiles                                  #
    # ====================================================================== #
    def _hide_all_widgets(self):
        """Cache tous les widgets placés dynamiquement via place()."""
        widgets = [
            self.button_register, self.button_login, self.button_accueil,
            self.button_send1, self.button_send2, self.button_send3,
            self.button_mpo, self.button_candidat,self.button_admin, self.button_logout, self.button_verifier,
            self.button_creer, self.button_candidater,
            self.button_futurE, self.button_currentE, self.button_finishE,
            self.button_gérerE, self.button_gérerC, self.button_voirR,
            self.email1, self.email2, self.password1, self.password2,
            self.nom, self.nom1, self.nom2, self.prenom, self.prenom1,
            self.confirm, self.date_entry, self.combo_classe, self.combo_classe1,
            self.question, self.ecole, self.motivation,
            self.npassword, self.cpassword,self.btn_eye1, self.btn_eye2,
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
            self.gererele_frame, self.gerercon_frame, self.voirres_frame,self.ajouterelec_frame,
        ]
        for f in frames:
            f.pack_forget()

    def _toggle_password(self, entry, btn):
        if entry.cget("show") == "*":
            entry.config(show="")
            btn.config(text="🙈")
        else:
            entry.config(show="*")
            btn.config(text="👁")
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

    def resize_image_ajouterelec(self, event):
        if event.width > 1 and event.height > 1:
            resized = self.image_ajouterelec.resize((event.width, event.height))
            self.photo_ajouterelec = ImageTk.PhotoImage(resized)
            self.label_ajouterelec.config(image=self.photo_ajouterelec)

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
        self.btn_eye1.place(relx=0.85, rely=0.33, anchor="w", width=25, height=28)
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
        self.btn_eye2.place(relx=0.4, rely=0.5, anchor="w", width=25, height=28)
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
        self.btn_eye3.place(relx=0.68, rely=0.45, anchor="w", width=25, height=30)
        self.cpassword.place(relx=0.48, rely=0.55, anchor="center", width=600, height=35)
        self.btn_eye4.place(relx=0.68, rely=0.55, anchor="w", width=25, height=30)
    
    def show_condidat_frame(self):
        self._hide_all_frames()
        self._hide_all_widgets()

        self.condidat_frame.pack(fill="both", expand=True)

        # Boutons
        self.button_accueil.place(relx=0.125, rely=0.05, anchor="center", height=30, width=100)
        self.button_logout.place(relx=0.9, rely=0.05, anchor="center", height=30, width=100)
        self.button_futurE.place(relx=0.17, rely=0.8, anchor="center", height=30, width=100)
        self.button_currentE.place(relx=0.5, rely=0.8, anchor="center", height=30, width=100)
        self.button_finishE.place(relx=0.83, rely=0.8, anchor="center", height=30, width=100)

    def show_admin_frame(self):
        self._hide_all_frames()
        self._hide_all_widgets()

        self.admin_frame.pack(fill="both", expand=True)

        # Boutons
        self.button_accueil.place(relx=0.1, rely=0.06, anchor="center", height=30, width=100)
        self.button_logout.place(relx=0.9, rely=0.06, anchor="center", height=30, width=100)
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
        self.button_ajouterele.place(relx=0.485, rely=0.235, anchor="center", height=40, width=800)
        self.button_admin.place(relx=0.2, rely=0.06, anchor="center", height=30, width=150)

        # Contenu dynamique
        self.afficher_gérer_election()
    def show_gerercon_frame(self):
        self._hide_all_frames()
        self._hide_all_widgets()

        self.gerercon_frame.pack(fill="both", expand=True)

        # Boutons
        self.button_accueil.place(relx=0.1, rely=0.06, anchor="center", height=30, width=100)
        self.button_admin.place(relx=0.2, rely=0.06, anchor="center", height=30, width=150)
        # Contenu dynamique
        self.afficher_gérer_candidature()

    def show_voirres_frame(self):
        self._hide_all_frames()
        self._hide_all_widgets()

        self.voirres_frame.pack(fill="both", expand=True)

        # Boutons
        self.button_accueil.place(relx=0.1, rely=0.06, anchor="center", height=30, width=100)
        self.button_admin.place(relx=0.2, rely=0.06, anchor="center", height=30, width=150)
        # Contenu dynamique
        self.résultats_admin()
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

    def show_ajouterelec_frame(self):
        self._hide_all_frames()
        self._hide_all_widgets()

        self.button_accueil.place(relx=0.7, rely=0.06, anchor="center", height=30, width=100)
        self.button_admin.place(relx=0.8, rely=0.06, anchor="center", height=30, width=100)
        

        self.ajouterelec_frame.pack(fill="both", expand=True)


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
        email = getattr(self, 'email_reset', '')

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

        classe_connecte = getattr(self, "utilisateur_connecte", {}).get("classe", "")
        elections_futur = [e for e in elections if e.get("statut", "").strip().lower() == "futur" and classe_connecte in e.get("public_concerne", [])]

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

        classe_connecte = getattr(self, "utilisateur_connecte", {}).get("classe", "")
        elections_encours = [e for e in elections if e.get("statut", "").strip().lower() == "en cours" and classe_connecte in e.get("public_concerne", [])]

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

        classe_connecte = getattr(self, "utilisateur_connecte", {}).get("classe", "")
        elections_finies = [e for e in elections if e.get("statut", "").strip().lower() == "terminé" and classe_connecte in e.get("public_concerne", [])]

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
            # Vote blanc
            rb_blanc = tk.Radiobutton(self.voter1_frame, text="🗳  Vote blanc",
                variable=self.choix_vote, value="Vote blanc",
                bg="#CCC6DC", font=("Arial", 15), fg="#555555")
            rb_blanc.place(relx=0.2, rely=0.5 + len(candidats) * 0.08, anchor="w")
            self._vote_radio_widgets.append(rb_blanc)
        else:
            for i, c in enumerate(candidats):
                choix = c.get("nom_liste", "")
                rb = tk.Radiobutton(self.voter1_frame, text=choix,
                    variable=self.choix_vote, value=choix,
                    bg="#CCC6DC", font=("Arial", 15))
                rb.place(relx=0.2, rely=0.5 + i * 0.08, anchor="w")
                self._vote_radio_widgets.append(rb)
            # Vote blanc
            rb_blanc = tk.Radiobutton(self.voter1_frame, text="🗳  Vote blanc",
                variable=self.choix_vote, value="Vote blanc",
                bg="#CCC6DC", font=("Arial", 15), fg="#555555")
            rb_blanc.place(relx=0.2, rely=0.5 + len(candidats) * 0.08, anchor="w")
            self._vote_radio_widgets.append(rb_blanc)

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

                horodatage = datetime.now().strftime("%Y-%m-%d %H:%M")

                election_trouvee = False
                for v in votes:
                    if v["titre"] == titre_v:
                        election_trouvee = True
                        if choix_v not in v["resultats"]:
                            v["resultats"][choix_v] = 0
                        v["resultats"][choix_v] += 1
                        if email_v not in v["votants"]:
                            v["votants"].append(email_v)
                        # Ajouter l'horodatage
                        if "horodatages" not in v:
                            v["horodatages"] = []
                        v["horodatages"].append(horodatage)
                        break

                if not election_trouvee:
                    votes.append({
                        "titre": titre_v,
                        "resultats": {choix_v: 1},
                        "votants": [email_v],
                        "horodatages": [horodatage]
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

        email_admin = getattr(self, "utilisateur_connecte", {}).get("email", "")
        elections_futur = [e for e in elections if e.get("statut", "").strip().lower() == "futur" and e.get("email admin", "") == email_admin]

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
        if type_election == "individuelle":
            nom_affiche = f"{candidature.get('prenom', '')} {candidature.get('nom', '')}"
        else:
            nom_affiche = candidature.get("nom_liste", "")

        confirmation = tk.messagebox.askyesno(
            "Confirmation",
            f"Êtes-vous sûr de vouloir refuser et supprimer la candidature de :\n« {nom_affiche } » ?"
        )
        if not confirmation:
            return

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
        
    #gerere les elections

    def afficher_gérer_election(self):
        if hasattr(self, 'canvas_gérerE'):
            self.canvas_gérerE.destroy()
        if hasattr(self, 'scrollbar_gérerE'):
            self.scrollbar_gérerE.destroy()

        try:
            with open("Fichier_Elections.json", "r", encoding="utf-8") as f:
                elections = json.load(f)
        except:
            elections = []

        elections_futur = [e for e in elections if e.get("statut", "").strip().lower() == "futur"]

        self.canvas_gérerE = tk.Canvas(self.gererele_frame, bg="white", highlightthickness=0)
        self.scrollbar_gérerE = tk.Scrollbar(self.gererele_frame, orient="vertical",
            command=self.canvas_gérerE.yview)
        self.canvas_gérerE.configure(yscrollcommand=self.scrollbar_gérerE.set)

        self.canvas_gérerE.place(relx=0.145, rely=0.27, relwidth=0.68, relheight=0.57)
        self.scrollbar_gérerE.place(relx=0.82, rely=0.13, relheight=0.71)

        inner_frame = tk.Frame(self.canvas_gérerE, bg="white")
        canvas_window = self.canvas_gérerE.create_window((0, 0), window=inner_frame, anchor="nw")

        def on_canvas_resize1(event):
            self.canvas_gérerE.itemconfig(canvas_window, width=event.width)
        self.canvas_gérerE.bind("<Configure>", on_canvas_resize1)

        for election in elections_futur:
            self.creer_carte_gérerE(inner_frame, election)

        inner_frame.update_idletasks()
        self.canvas_gérerE.configure(scrollregion=self.canvas_gérerE.bbox("all"))
        self.canvas_gérerE.bind("<MouseWheel>",
            lambda e: self.canvas_gérerE.yview_scroll(-1*(e.delta//120), "units"))

    def creer_carte_gérerE(self, parent, election):
        email_admin = getattr(self, "utilisateur_connecte", {}).get("email", "")
        
        # N'afficher que les élections créées par cet admin
        if election.get("email admin", "") != email_admin:
            return

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

        tk.Button(btn_frame, text="Modifier",
            fg="white", bg="#073763", activeforeground="white",
            borderwidth=0, highlightthickness=0, relief="flat",
            width=20, height=2,
            command=lambda e=election: self.modifier_election(e)
        ).pack(side="right")
        tk.Button(btn_frame, text="Supprimer",
            fg="white", bg="#c62828", activeforeground="white",
            borderwidth=0, highlightthickness=0, relief="flat",
            width=20, height=2,
            command=lambda e=election: self.supprimer_election(e)
        ).pack(side="right")
    
        
    def ajouter_elec(self):
        self.show_ajouterelec_frame()
    # --- Champ Nom d'élection ---
        
        self.nomE1.place(relx=0.17, rely=0.25, anchor="w", width=400, height=35)
    # --- Type de candidat (radio) ---
        self.radio_individuelle.place(relx=0.21, rely=0.384, anchor="w")
        self.radio_liste.place(relx=0.33, rely=0.385, anchor="w")
    # --- Objectif ---
        
        self.objectif.place(relx=0.17, rely=0.585, anchor="w", width=400, height=180)
    # --- Public concerné (Listbox originale) ---
        self.public = tk.Listbox(self.ajouterelec_frame, selectmode=tk.MULTIPLE)
        for element in self.classes:
            self.public.insert(tk.END, element)
        self.public.place(relx=0.54, rely=0.32, anchor="w", width=180, height=130)
    # --- Date de début ---
        self.date_debut = DateEntry(self.ajouterelec_frame,
        date_pattern='dd/mm/yyyy', bg="white", width=12)
        self.date_debut.place(relx=0.54, rely=0.55, anchor="w", height=30)
    # --- Date de fin ---
        self.date_fin = DateEntry(self.ajouterelec_frame,
        date_pattern='dd/mm/yyyy', bg="white", width=12)
        self.date_fin.place(relx=0.72, rely=0.55, anchor="w", height=30)
    # --- Heure de début ---
        self.h_debut = tk.Spinbox(self.ajouterelec_frame,
        from_=0, to=23, width=3, format="%02.0f")
        self.m_debut = tk.Spinbox(self.ajouterelec_frame,
        from_=0, to=59, width=3, format="%02.0f")
        self.h_debut.place(relx=0.54, rely=0.642, anchor="w", width=45, height=28)
        tk.Label(self.ajouterelec_frame, text=":",
        bg="#BAD2D7", font=("Arial", 12, "bold")).place(relx=0.57, rely=0.642, anchor="w")
        self.m_debut.place(relx=0.58, rely=0.642, anchor="w", width=45, height=28)
    # --- Heure de fin ---
        self.h_fin = tk.Spinbox(self.ajouterelec_frame,
        from_=0, to=23, width=3, format="%02.0f")
        self.m_fin = tk.Spinbox(self.ajouterelec_frame,
        from_=0, to=59, width=3, format="%02.0f")
        self.h_fin.place(relx=0.72, rely=0.642, anchor="w", width=45, height=28)
        tk.Label(self.ajouterelec_frame, text=":",
        bg="#BAD2D7", font=("Arial", 12, "bold")).place(relx=0.75, rely=0.642, anchor="w")
        self.m_fin.place(relx=0.76, rely=0.642, anchor="w", width=45, height=28)
    # --- Bouton Ajouter ---
        self.button_ajouterele1.place(relx=0.50, rely=0.80, anchor="center", height=50, width=200) 




    def calculer_statut(self, date_debut_str, heure_debut_str, date_fin_str, heure_fin_str):
        """Calcule le statut de l'élection selon la date/heure actuelle."""
        try:
            debut = datetime.strptime(f"{date_debut_str.strip()} {heure_debut_str.strip()}", "%d/%m/%Y %H:%M")
            fin   = datetime.strptime(f"{date_fin_str.strip()} {heure_fin_str.strip()}",   "%d/%m/%Y %H:%M")
            now   = datetime.now()
            if now < debut:
                return "futur"
            elif now > fin:
                return "terminé"
            else:
                return "en cours"
        except Exception:
            return "futur"

    def enregistrer_election(self):
        """Lit les champs du formulaire ajouter_elec et enregistre dans Fichier_Elections.json."""
        titre     = self.nomE1.get().strip()
        objectif  = self.objectif.get("1.0", tk.END).strip()
        type_elec = self.typelec.get()

        # Public concerné (sélection multiple dans la Listbox)
        indices_selectionnes = self.public.curselection()
        public = [self.public.get(i) for i in indices_selectionnes]

        date_debut_str = self.date_debut.get().strip()
        date_fin_str   = self.date_fin.get().strip()
        h_debut_str    = f"{int(self.h_debut.get()):02d}:{int(self.m_debut.get()):02d}"
        h_fin_str      = f"{int(self.h_fin.get()):02d}:{int(self.m_fin.get()):02d}"

        # Validation basique
        if not titre:
            tk.messagebox.showerror("Erreur", "Le nom de l'élection est obligatoire.")
            return
        if not public:
            tk.messagebox.showerror("Erreur", "Veuillez sélectionner au moins un public concerné.")
            return

        # Récupérer l'email de l'admin connecté
        email_admin = getattr(self, "utilisateur_connecte", {}).get("email", "")

        statut = self.calculer_statut(date_debut_str, h_debut_str, date_fin_str, h_fin_str)

        nouvelle_election = {
            "titre":          titre,
            "date_debut":     date_debut_str,
            "date_fin":       date_fin_str,
            "heure de debut": h_debut_str,
            "heure de fin":   h_fin_str,
            "statut":         statut,
            "type":           type_elec,
            "objectif":       objectif,
            "public_concerne": public,
            "email admin":    email_admin
        }

        try:
            with open("Fichier_Elections.json", "r", encoding="utf-8") as f:
                elections = json.load(f)
        except:
            elections = []

        # Vérifier que le titre n'existe pas déjà
        for e in elections:
            if e["titre"].strip().lower() == titre.lower():
                tk.messagebox.showerror("Erreur", "Une élection avec ce nom existe déjà.")
                return

        elections.append(nouvelle_election)

        with open("Fichier_Elections.json", "w", encoding="utf-8") as f:
            json.dump(elections, f, indent=4, ensure_ascii=False)

        tk.messagebox.showinfo("Succès", f"L'élection « {titre} » a été ajoutée avec succès !")

        # Vider les champs
        self.nomE1.delete(0, tk.END)
        self.objectif.delete("1.0", tk.END)
        self.public.selection_clear(0, tk.END)

        # Retourner à la page gérer élections
        self.show_gererele_frame()


    def modifier_election(self, election):
        """Ouvre une fenêtre pour modifier une élection existante (seulement si créée par l'admin connecté)."""
        email_admin = getattr(self, "utilisateur_connecte", {}).get("email", "")

        if election.get("email admin", "") != email_admin:
            tk.messagebox.showerror("Accès refusé",
                "Vous ne pouvez modifier que les élections que vous avez créées.")
            return

        win = tk.Toplevel(self.root)
        win.title("Modifier l'élection")
        win.geometry("650x600")
        win.configure(bg="#BAD2D7")

        # --- Titre ---
        tk.Label(win, text="Nom de l'élection", bg="#BAD2D7",
            font=("Arial", 11, "bold")).place(relx=0.05, rely=0.04)
        entry_titre = tk.Entry(win, bg="white", font=("Arial", 11))
        entry_titre.insert(0, election.get("titre", ""))
        entry_titre.place(relx=0.05, rely=0.10, width=580, height=32)

        # --- Type ---
        tk.Label(win, text="Type de candidat", bg="#BAD2D7",
            font=("Arial", 11, "bold")).place(relx=0.05, rely=0.19)
        type_var = tk.StringVar(value=election.get("type", "individuelle"))
        tk.Radiobutton(win, text="Individuelle", variable=type_var,
            value="individuelle", bg="#BAD2D7", font=("Arial", 11)).place(relx=0.05, rely=0.25)
        tk.Radiobutton(win, text="Liste", variable=type_var,
            value="liste", bg="#BAD2D7", font=("Arial", 11)).place(relx=0.28, rely=0.25)

        # --- Objectif ---
        tk.Label(win, text="Objectif", bg="#BAD2D7",
            font=("Arial", 11, "bold")).place(relx=0.05, rely=0.33)
        text_objectif = tk.Text(win, bg="white", font=("Arial", 11), wrap="word")
        text_objectif.insert("1.0", election.get("objectif", ""))
        text_objectif.place(relx=0.05, rely=0.39, width=580, height=100)

        # --- Public concerné ---
        tk.Label(win, text="Public concerné", bg="#BAD2D7",
            font=("Arial", 11, "bold")).place(relx=0.05, rely=0.57)
        classes = ["2026", "2027", "2028", "2029", "2030"]
        listbox_public = tk.Listbox(win, selectmode=tk.MULTIPLE, font=("Arial", 10))
        for c in classes:
            listbox_public.insert(tk.END, c)
        # Pré-sélectionner les classes déjà choisies
        public_actuel = election.get("public_concerne", [])
        for i, c in enumerate(classes):
            if c in public_actuel:
                listbox_public.selection_set(i)
        listbox_public.place(relx=0.05, rely=0.63, width=150, height=100)

        # --- Dates ---
        tk.Label(win, text="Date début", bg="#BAD2D7",
            font=("Arial", 10, "bold")).place(relx=0.40, rely=0.57)
        date_d = DateEntry(win, date_pattern='dd/mm/yyyy', bg="white")
        try:
            date_d.set_date(datetime.strptime(election.get("date_debut","").strip(), "%d/%m/%Y"))
        except:
            pass
        date_d.place(relx=0.40, rely=0.63, width=120, height=28)

        tk.Label(win, text="Date fin", bg="#BAD2D7",
            font=("Arial", 10, "bold")).place(relx=0.68, rely=0.57)
        date_f = DateEntry(win, date_pattern='dd/mm/yyyy', bg="white")
        try:
            date_f.set_date(datetime.strptime(election.get("date_fin","").strip(), "%d/%m/%Y"))
        except:
            pass
        date_f.place(relx=0.68, rely=0.63, width=120, height=28)

        # --- Heures ---
        tk.Label(win, text="Heure début", bg="#BAD2D7",
            font=("Arial", 10, "bold")).place(relx=0.40, rely=0.74)
        h_d = tk.Spinbox(win, from_=0, to=23, width=3, format="%02.0f")
        m_d = tk.Spinbox(win, from_=0, to=59, width=3, format="%02.0f")
        try:
            hd, md = election.get("heure de debut", "00:00").split(":")
            h_d.delete(0, tk.END); h_d.insert(0, hd.strip())
            m_d.delete(0, tk.END); m_d.insert(0, md.strip())
        except:
            pass
        h_d.place(relx=0.40, rely=0.80, width=45, height=26)
        tk.Label(win, text=":", bg="#BAD2D7", font=("Arial", 12, "bold")).place(relx=0.475, rely=0.80)
        m_d.place(relx=0.50, rely=0.80, width=45, height=26)

        tk.Label(win, text="Heure fin", bg="#BAD2D7",
            font=("Arial", 10, "bold")).place(relx=0.68, rely=0.74)
        h_f = tk.Spinbox(win, from_=0, to=23, width=3, format="%02.0f")
        m_f = tk.Spinbox(win, from_=0, to=59, width=3, format="%02.0f")
        try:
            hf, mf = election.get("heure de fin", "00:00").split(":")
            h_f.delete(0, tk.END); h_f.insert(0, hf.strip())
            m_f.delete(0, tk.END); m_f.insert(0, mf.strip())
        except:
            pass
        h_f.place(relx=0.68, rely=0.80, width=45, height=26)
        tk.Label(win, text=":", bg="#BAD2D7", font=("Arial", 12, "bold")).place(relx=0.755, rely=0.80)
        m_f.place(relx=0.77, rely=0.80, width=45, height=26)

    def supprimer_election(self, election):
        # Message d'alerte de confirmation avant suppression
        confirmation = tk.messagebox.askyesno(
            "Confirmation",
            "Êtes-vous sûr de bien vouloir supprimer cette élection ?"
        )
        if not confirmation:
            return  # l'utilisateur a cliqué sur "Non" → on ne fait rien

        try:
            with open("Fichier_Elections.json", "r", encoding="utf-8") as f:
                elections = json.load(f)
        except:
            elections = []

        # On retire l'élection dont le titre correspond
        elections = [e for e in elections if e["titre"].strip() != election["titre"].strip()]

        with open("Fichier_Elections.json", "w", encoding="utf-8") as f:
            json.dump(elections, f, indent=4, ensure_ascii=False)

        tk.messagebox.showinfo("Succès", "Élection supprimée avec succès !")
        self.show_gererele_frame()  # recharge l'affichage pour faire disparaître la carte

        # --- Bouton Enregistrer ---
        def sauvegarder():
            nouveau_titre  = entry_titre.get().strip()
            nouveau_type   = type_var.get()
            nouvel_obj     = text_objectif.get("1.0", tk.END).strip()
            indices        = listbox_public.curselection()
            nouveau_public = [listbox_public.get(i) for i in indices]
            nd_str = date_d.get().strip()
            nf_str = date_f.get().strip()
            nh_d   = f"{int(h_d.get()):02d}:{int(m_d.get()):02d}"
            nh_f   = f"{int(h_f.get()):02d}:{int(m_f.get()):02d}"

            if not nouveau_titre:
                tk.messagebox.showerror("Erreur", "Le nom est obligatoire.", parent=win)
                return
            if not nouveau_public:
                tk.messagebox.showerror("Erreur", "Sélectionnez au moins un public.", parent=win)
                return

            nouveau_statut = self.calculer_statut(nd_str, nh_d, nf_str, nh_f)

            try:
                with open("Fichier_Elections.json", "r", encoding="utf-8") as f:
                    elections = json.load(f)
            except:
                elections = []

            for e in elections:
                if e["titre"].strip() == election["titre"].strip():
                    e["titre"]          = nouveau_titre
                    e["type"]           = nouveau_type
                    e["objectif"]       = nouvel_obj
                    e["public_concerne"]= nouveau_public
                    e["date_debut"]     = nd_str
                    e["date_fin"]       = nf_str
                    e["heure de debut"] = nh_d
                    e["heure de fin"]   = nh_f
                    e["statut"]         = nouveau_statut
                    break

            with open("Fichier_Elections.json", "w", encoding="utf-8") as f:
                json.dump(elections, f, indent=4, ensure_ascii=False)

            tk.messagebox.showinfo("Succès", "Élection modifiée avec succès !", parent=win)
            win.destroy()
            self.show_gererele_frame()

        tk.Button(win, text="Enregistrer les modifications",
            fg="white", bg="#073763", activeforeground="white",
            borderwidth=0, highlightthickness=0, relief="flat",
            font=("Arial", 13, "bold"), cursor="hand2",
            command=sauvegarder).place(relx=0.5, rely=0.91, anchor="center", width=280, height=42)
    
    #Voir les résultat version admin 
    def résultats_admin(self):
        if hasattr(self, 'canvas_résultatsA'):
            self.canvas_résultatsA.destroy()
        if hasattr(self, 'scrollbar_résultatsA'):
            self.scrollbar_résultatsA.destroy()

        try:
            with open("Fichier_Elections.json", "r", encoding="utf-8") as f:
                elections = json.load(f)
        except:
            elections = []

        email_admin = getattr(self, "utilisateur_connecte", {}).get("email", "")
        elections_finies = [e for e in elections if e.get("statut", "").strip().lower() == "terminé" and e.get("email admin", "") == email_admin]
        
        self.canvas_résultatsA = tk.Canvas(self.voirres_frame, bg="white", highlightthickness=0)
        self.scrollbar_résultatsA = tk.Scrollbar(self.voirres_frame, orient="vertical",
            command=self.canvas_résultatsA.yview)
        self.canvas_résultatsA.configure(yscrollcommand=self.scrollbar_résultatsA.set)

        self.canvas_résultatsA.place(relx=0.14, rely=0.27, relwidth=0.68, relheight=0.57)
        self.scrollbar_résultatsA.place(relx=0.815, rely=0.13, relheight=0.71)

        inner_frame = tk.Frame(self.canvas_résultatsA, bg="white")
        canvas_window = self.canvas_résultatsA.create_window((0, 0), window=inner_frame, anchor="nw")

        def on_canvas_resize(event):
            self.canvas_résultatsA.itemconfig(canvas_window, width=event.width)
        self.canvas_résultatsA.bind("<Configure>", on_canvas_resize)

        for election in elections_finies:
            self.creer_carte_résultats_admin(inner_frame, election)

        inner_frame.update_idletasks()
        self.canvas_résultatsA.configure(scrollregion=self.canvas_résultatsA.bbox("all"))
        self.canvas_résultatsA.bind("<MouseWheel>",
            lambda e: self.canvas_résultatsA.yview_scroll(-1*(e.delta//120), "units"))

    def creer_carte_résultats_admin(self, parent, election):
        carte = tk.Frame(parent, bg="#7fafc0", bd=1, relief="solid")
        carte.pack(fill="x", padx=10, pady=8, ipady=8)

        tk.Label(carte, text=election.get("titre", ""), bg="#7fafc0",
            font=("Arial", 11, "bold"), anchor="w").pack(anchor="w", padx=10, pady=(8, 2))
        tk.Label(carte, text=f"Date de départ d'élection :    {election.get('date_debut', '')}",
            bg="#7fafc0", font=("Arial", 9), anchor="w").pack(anchor="w", padx=10)
        tk.Label(carte, text=f"Date de fin d'élection :           {election.get('date_fin', '')}",
            bg="#7fafc0", font=("Arial", 9), anchor="w").pack(anchor="w", padx=10)

        btn_frame = tk.Frame(carte, bg="#7fafc0")
        btn_frame.pack(fill="x", padx=10, pady=(7, 4))

        tk.Button(btn_frame, text="Voir les résultats",
            fg="white", bg="#073763", activeforeground="white",
            borderwidth=0, highlightthickness=0, relief="flat",
            width=20, height=2,
            command=lambda e=election: self.voir_résultats_admin(e)
        ).pack(side="right")

    def voir_résultats_admin(self, election):
        try:
            with open("Fichier_Votes.json", "r", encoding="utf-8") as f:
                votes = json.load(f)
        except:
            votes = []

        résultats = {}
        total_votes = 0
        for v in votes:
            if v["titre"] == election["titre"]:
                résultats = v.get("resultats", {})
                total_votes = sum(résultats.values())
                break

        try:
            with open("Fichier_candidatures.json", "r", encoding="utf-8") as f:
                candidatures = json.load(f)
        except:
            candidatures = []

        nb_candidats = 0
        for c in candidatures:
            if c["titre"] == election["titre"]:
                nb_candidats = len(c.get("candidats", []))
                break

        # Calcul durée
        try:
            d1 = datetime.strptime(election.get("date_debut", ""), "%Y-%m-%d")
            d2 = datetime.strptime(election.get("date_fin", ""), "%Y-%m-%d")
            duree = abs((d2 - d1).days)
        except:
            duree = "?"

        # Gagnant
        résultats_sans_blanc = {k: v for k, v in résultats.items() if k != "Vote blanc"}
        if not résultats_sans_blanc:
            gagnant = "Aucun"
        else:
            max_votes = max(résultats_sans_blanc.values())
            gagnants = [k for k, v in résultats_sans_blanc.items() if v == max_votes]
            if len(gagnants) > 1:
                gagnant = f"ÉGALITÉ : {' / '.join(gagnants)}"
            else:
                gagnant = gagnants[0]
        win = tk.Toplevel(self.root)
        win.title(election.get("titre", "Résultats"))
        win.geometry("680x520")
        win.configure(bg="white")
        win.resizable(False, False)

        # En-tête
        tk.Label(win, text=election.get("titre", ""), bg="white",
            font=("Arial", 14, "bold"), fg="#073763").pack(pady=(15, 5))

        # Stats rapides
        stats_frame = tk.Frame(win, bg="white")
        stats_frame.pack(fill="x", padx=30, pady=(0, 10))

        tk.Label(stats_frame, text=f"Nombre de candidatures : {nb_candidats}",
            bg="white", font=("Arial", 10), fg="#333333").pack(anchor="w")
        tk.Label(stats_frame, text=f"Nombre de votes : {total_votes}",
            bg="white", font=("Arial", 10), fg="#333333").pack(anchor="w")
        tk.Label(stats_frame, text=f"Durée totale de l'élection : {duree} jours",
            bg="white", font=("Arial", 10), fg="#333333").pack(anchor="w")

        # Zone centrale pour les dropdowns et contenu dynamique
        centre = tk.Frame(win, bg="white")
        centre.pack(fill="both", expand=True, padx=30)

        # --- Dropdown Résultats ---
        res_var = tk.StringVar(value="Résultats :")
        res_dropdown = ttk.Combobox(centre, textvariable=res_var,
            values=["Résultats :"], state="readonly", width=35)
        res_dropdown.pack(anchor="w", pady=(5, 0))

        res_content = tk.Frame(centre, bg="white", bd=1, relief="solid")

        def toggle_resultats(event):
            if res_content.winfo_ismapped():
                res_content.pack_forget()
            else:
                stat_content.pack_forget()
                # Remplir le tableau
                for w in res_content.winfo_children():
                    w.destroy()
                header = tk.Frame(res_content, bg="#e8f0f5")
                header.pack(fill="x")
                tk.Label(header, text="Nom et prénom du candidats",
                    bg="#e8f0f5", font=("Arial", 9, "bold"),
                    width=30, anchor="w").grid(row=0, column=0, padx=5, pady=3)
                tk.Label(header, text="|", bg="#e8f0f5",
                    font=("Arial", 9)).grid(row=0, column=1)
                tk.Label(header, text="Nombre de votes",
                    bg="#e8f0f5", font=("Arial", 9, "bold"),
                    width=15, anchor="w").grid(row=0, column=2, padx=5)

                sorted_res = sorted(résultats.items(), key=lambda x: x[1], reverse=True)
                for i, (cand, nb) in enumerate(sorted_res, 1):
                    row_bg = "white" if i % 2 == 1 else "#f5f5f5"
                    row = tk.Frame(res_content, bg=row_bg)
                    row.pack(fill="x")
                    tk.Label(row, text=f"{i}) {cand}",
                        bg=row_bg, font=("Arial", 9),
                        width=30, anchor="w").grid(row=0, column=0, padx=5, pady=2)
                    tk.Label(row, text="|", bg=row_bg,
                        font=("Arial", 9)).grid(row=0, column=1)
                    tk.Label(row, text=str(nb),
                        bg=row_bg, font=("Arial", 9),
                        width=15, anchor="w").grid(row=0, column=2, padx=5)

                res_content.pack(anchor="w", pady=(0, 5))

        res_dropdown.bind("<<ComboboxSelected>>", toggle_resultats)

        # --- Dropdown Statistiques ---
        stat_var = tk.StringVar(value="Statistiques :")
        stat_dropdown = ttk.Combobox(centre, textvariable=stat_var,
            values=["Statistiques :"], state="readonly", width=35)
        stat_dropdown.pack(anchor="w", pady=(8, 0))

        stat_content = tk.Frame(centre, bg="white")

        def toggle_stats(event):
            if stat_content.winfo_ismapped():
                stat_content.pack_forget()
            else:
                res_content.pack_forget()
                for w in stat_content.winfo_children():
                    w.destroy()
                self._dessiner_graphique(stat_content, election)
                stat_content.pack(anchor="w", pady=(5, 0))

        stat_dropdown.bind("<<ComboboxSelected>>", toggle_stats)

        # --- Candidat gagnant en bas ---
        bottom = tk.Frame(win, bg="white")
        bottom.pack(side="bottom", fill="x", padx=30, pady=20)

        if gagnant.startswith("ÉGALITÉ"):
            texte_bas = f"⚠  {gagnant}"
            couleur_bas = "#c62828"
        else:
            texte_bas = f"Candidat gagnant :   {gagnant}"
            couleur_bas = "#048b9a"

        tk.Label(bottom,
                text=texte_bas,
                bg=couleur_bas, fg="white",
                font=("Arial", 12, "bold"),
                pady=10).pack(fill="x")

    def _dessiner_graphique(self, parent, election):
        try:
            with open("Fichier_Votes.json", "r", encoding="utf-8") as f:
                votes = json.load(f)
        except:
            votes = []

        try:
            horodatages = []
            for v in votes:
                if v["titre"] == election["titre"]:
                    horodatages = v.get("horodatages", [])
                    break

            canvas_g = tk.Canvas(parent, bg="white", width=480, height=220,
                highlightthickness=1, highlightbackground="#cccccc")
            canvas_g.pack(padx=10, pady=10)

            if not horodatages:
                canvas_g.create_text(240, 110, text="Aucune donnée temporelle disponible",
                    font=("Arial", 10), fill="#999999")
                return

            from collections import Counter
            dates = [datetime.strptime(h, "%Y-%m-%d %H:%M") for h in horodatages]
            date_min = min(dates)
            date_max = max(dates)
            duree_heures = max(1, int((date_max - date_min).total_seconds() / 3600))

            if duree_heures > 48:
                comptage = Counter(d.strftime("%Y-%m-%d") for d in dates)
                labels = sorted(comptage.keys())
                valeurs = [comptage[l] for l in labels]
                unite = "jour"
                labels_affich = [l[5:] for l in labels]
            else:
                comptage = Counter(d.strftime("%Y-%m-%d %Hh") for d in dates)
                all_labels = []
                current = date_min.replace(minute=0, second=0, microsecond=0)
                end = date_max.replace(minute=0, second=0, microsecond=0)
                while current <= end:
                    all_labels.append(current.strftime("%Y-%m-%d %Hh"))
                    if current.hour == 23:
                        current = current.replace(
                            year=current.year if current.month < 12 or current.day < 31 else current.year + 1,
                            hour=0
                        )
                        current = datetime(current.year, current.month, current.day, 0)
                        from datetime import timedelta
                        current = date_min.replace(minute=0, second=0, microsecond=0)
                        current = datetime.strptime(all_labels[-1], "%Y-%m-%d %Hh")
                        current = current.replace(hour=0) if current.hour == 23 else current.replace(hour=current.hour + 1)
                    else:
                        current = current.replace(hour=current.hour + 1)
                labels = all_labels
                valeurs = [comptage.get(l, 0) for l in labels]
                unite = "heure"
                labels_affich = [l.split(" ")[1] for l in labels]

            padding_left = 45
            padding_bottom = 45
            padding_top = 20
            padding_right = 20
            w = 480
            h = 220

            max_val = max(valeurs) if valeurs else 1
            n = len(labels)
            zone_w = w - padding_left - padding_right
            zone_h = h - padding_bottom - padding_top

            for i in range(1, 5):
                y_grid = (h - padding_bottom) - (i / 4) * zone_h
                canvas_g.create_line(padding_left, y_grid, w - padding_right, y_grid,
                    fill="#eeeeee", width=1)
                val_grid = round(max_val * i / 4)
                canvas_g.create_text(padding_left - 5, y_grid,
                    text=str(val_grid), font=("Arial", 7), anchor="e", fill="#777777")

            canvas_g.create_line(padding_left, padding_top,
                padding_left, h - padding_bottom, fill="#333333", width=2)
            canvas_g.create_line(padding_left, h - padding_bottom,
                w - padding_right, h - padding_bottom, fill="#333333", width=2)

            canvas_g.create_text(padding_left - 5, h - padding_bottom,
                text="0", font=("Arial", 7), anchor="e", fill="#555555")
            canvas_g.create_text(padding_left - 5, padding_top,
                text=str(max_val), font=("Arial", 7), anchor="e", fill="#555555")
            canvas_g.create_text(w // 2, h - 8,
                text=f"par {unite}", font=("Arial", 8), fill="#555555")
            canvas_g.create_text(12, h // 2,
                text="votes", font=("Arial", 8), fill="#555555", angle=90)

            if n == 1:
                x = padding_left + zone_w // 2
                y = (h - padding_bottom) - (valeurs[0] / max_val) * zone_h
                points = [(x, y)]
            else:
                step = zone_w / (n - 1)
                points = []
                for i, val in enumerate(valeurs):
                    x = padding_left + i * step
                    y = (h - padding_bottom) - (val / max_val) * zone_h
                    points.append((x, y))

            if len(points) > 1:
                poly_points = [padding_left, h - padding_bottom]
                for px, py in points:
                    poly_points += [px, py]
                poly_points += [points[-1][0], h - padding_bottom]
                canvas_g.create_polygon(poly_points, fill="#d0eaf0", outline="")

            if len(points) > 1:
                for i in range(len(points) - 1):
                    canvas_g.create_line(
                        points[i][0], points[i][1],
                        points[i+1][0], points[i+1][1],
                        fill="#048b9a", width=2, smooth=True)

            max_labels = 8
            step_label = max(1, n // max_labels)
            for i, (px, py) in enumerate(points):
                canvas_g.create_oval(px-3, py-3, px+3, py+3,
                    fill="#073763", outline="white", width=1)
                nb = valeurs[i]
                if nb > 0:
                    canvas_g.create_text(px, py - 10,
                        text=str(nb), font=("Arial", 7, "bold"), fill="#073763")
                if i % step_label == 0:
                    canvas_g.create_text(px, h - padding_bottom + 12,
                        text=labels_affich[i], font=("Arial", 7),
                        fill="#555555")

            if n > 1:
                moyenne = sum(valeurs) / n
                for i, val in enumerate(valeurs):
                    if moyenne > 0 and val > 3 * moyenne:
                        px, py = points[i]
                        canvas_g.create_oval(px-7, py-7, px+7, py+7,
                            outline="#c62828", width=2)
                        canvas_g.create_text(px, py - 20,
                            text="pic!", font=("Arial", 7, "bold"), fill="#c62828")

        except Exception as ex:
            tk.Label(parent, text=f"Erreur graphique : {ex}",
                bg="white", fg="red", font=("Arial", 9)).pack()
    # ====================================================================== #
    #  FIX LAYOUT                                                             #
    # ====================================================================== #
    def fix_layout(self):
        self.root.update_idletasks()
        self.show_accueil_frame()


root = tk.Tk()
app = App(root)
root.mainloop()