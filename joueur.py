import paquet
import carte
import random
import time
import sys
import keyboard
# import keyboard  A INSTALLER !!!!




class Joueur:
	JOUEURS = []
	NOMS_JOUEURS_REELS = ["Maxime", "Cauchy", "David", "Lucas"]
	NOMS_JOUEURS_ORDI = ["Jean-Paul", "Alphonse", "Pascal"]
	AUTORISATION_TAPER = False
	AUTORISATION_JOUER = 666
	AUTORISATION_PRENDRE = 666
	FIN = False
	GAGNANT = 666
	JOUEUR_QUI_JOUE = 666
	JOUEUR_QUI_TAPE = 666
	JOUEUR_QUI_PREND = 666
	TETE_EN_COURS = False


	@classmethod
	def initialize(self, nombre_joueurs, nombre_joueurs_reels):
		print("Création des joueurs")
		for numero in range(nombre_joueurs_reels):
			joueur = Joueur_reel(Joueur.NOMS_JOUEURS_REELS[numero], numero + 1)
			self.JOUEURS.append(joueur)
			print("Joueur n°", joueur.numero, " : ", joueur.nom, " ", type(joueur))
			if str(type(joueur)) == "<class \'joueur.Joueur_reel\'>" :
				print("Ce joueur est un être humain")
		for numero in range(nombre_joueurs - nombre_joueurs_reels):
			joueur = Joueur_ordi(Joueur.NOMS_JOUEURS_ORDI[numero], numero + nombre_joueurs_reels + 1)
			self.JOUEURS.append(joueur)
			print("Joueur n°", joueur.numero, " : ", joueur.nom, " ", type(joueur))
			if str(type(joueur)) == "<class \'joueur.Joueur_ordi\'>" :
				print("Ce joueur est un ordinateur")
		self.AUTORISATION_JOUER = 0

	@classmethod
	def jeu(self):
		while self.FIN == False :

			if self.AUTORISATION_JOUER != 666:
				if str(type(self.JOUEURS[AUTORISATION_JOUER])) == "<class \'joueur.Joueur_ordi\'>":
					self.JOUEURS[AUTORISATION_JOUER].jouer()
			if self.AUTORISATION_TAPER != 666:
				for joueur in self.JOUEURS:
					if str(type(joueur)) == "<class \'joueur.Joueur_ordi\'>" :
						joueur.taper()
			if self.AUTORISATION_PRENDRE != 666:
				if str(type(self.JOUEURS[AUTORISATION_PRENDRE])) == "<class \'joueur.Joueur_ordi\'>":
					self.JOUEURS[AUTORISATION_PRENDRE].prendre()

			if self.JOUEUR_QUI_JOUE != 666 :
				if self.JOUEUR_QUI_JOUE == self.AUTORISATION_JOUER:
					self.JOUEURS[JOUEUR_QUI_JOUE].poser_carte()
					passer_perdants = 0
					while len(paquet.Paquet.PAQUETS[1 + self.AUTORISATION_JOUER + 1 + passer_perdants].liste) == 0:
						passer_perdants = passer_perdants + 1
					self.AUTORISATION_JOUER = self.AUTORISATION_JOUER + 1 + passer_perdants
					paquet.Paquet_central.verifier_autorisations()
				else : self.JOUEURS[JOUEUR_QUI_JOUE].poser_penalite()
				self.JOUEUR_QUI_JOUE = 666
			if self.JOUEUR_QUI_TAPE != 666 :
				if AUTORISATION_TAPER == True :
					self.JOUEURS[JOUEUR_QUI_TAPE].recuperer()
					self.AUTORISATION_TAPER = False
					self.AUTORISATION_PRENDRE = 666
					self.AUTORISATION_JOUER = self.JOUEUR_QUI_TAPE
				else : self.JOUEURS[JOUEUR_QUI_TAPE].poser_penalite()
				self.JOUEUR_QUI_TAPE = 666
			if self.JOUEUR_QUI_PREND != 666 :
				if self.JOUEUR_QUI_PREND == self.AUTORISATION_PRENDRE:
					self.JOUEURS[JOUEUR_QUI_PREND].recuperer()
					self.AUTORISATION_TAPER = False
					self.AUTORISATION_PRENDRE = 666
					self.AUTORISATION_JOUER = self.JOUEUR_QUI_PREND
				else : self.JOUEURS[JOUEUR_QUI_PREND].poser_penalite()
				self.JOUEUR_QUI_PREND = 666






	def __init__(self, nom, numero):
		self.nom = nom
		self.numero = numero
		self.droit_jouer = False
		self.droit_taper = False


	def jouer(self):
		pass

	def taper(self):
		pass

	def prendre(self):
		pass


	def poser_carte(self):
		if len(paquet.Paquet.PAQUETS[self.numero].liste) != 0:
			print(self.nom, "pose une carte")
			carte = paquet.Paquet.PAQUETS[self.numero].liste[0]
			paquet.Paquet.PAQUETS[self.numero].liste.pop(0)
			paquet.Paquet.PAQUETS[0].liste.insert(0, carte)
			paquet.Paquet.PAQUETS[0].montrer_n_cartes(5)
			if carte.nom == "Valet" or carte.nom == "Dame" or carte.nom == "Roi" or carte.nom == "As":
				Joueur.TETE_EN_COURS = True
			paquet.Paquet.PAQUETS[0].verification_autorisations()
		else : 
			Joueur.verifier_fin_jeu()
			Joueur.regler_tete()




	def recuperer(self):
		print(self.nom, "récupère le paquet")
		Joueur.TETE_EN_COURS = False
		while len(paquet.Paquet.PAQUETS[0].liste) != 0 :
			carte = paquet.Paquet.PAQUETS[0].liste[-1]
			carte.devenir_normale()
			paquet.Paquet.PAQUETS[0].liste.pop()
			paquet.Paquet.PAQUETS[self.numero].liste.append(carte)
		paquet.Paquet.PAQUETS[0].montrer_paquet()


	def poser_penalite(self):
		if len(paquet.Paquet.PAQUETS[self.numero].liste) != 0:
			print(self.nom, "pose une pénalité")
			carte = paquet.Paquet.PAQUETS[self.numero].liste[0]
			carte.devenir_penalite()
			paquet.Paquet.PAQUETS[self.numero].liste.pop(0)
			paquet.Paquet.PAQUETS[0].liste.append(carte)
			paquet.Paquet.PAQUETS[0].montrer_n_cartes(5)

	@classmethod
	def verifier_fin_jeu(self):
		nombre_perdants = 0
		for numero_joueur in range(len(self.JOUEURS)):
			if len(paquet.Paquet.PAQUETS[numero_joueur + 1].liste) == 0:
				nombre_perdants = nombre_perdants + 1
			else : self.GAGNANT = numero_joueur
		if nombre_perdants == paquet.Paquet.PAQUETS - 1:
			self.FIN = True
			print(self.JOUEURS[self.GAGNANT].nom, "a gagné !!!!")
			sys.exit()
		else : self.GAGNANT = 666


	@classmethod
	def regler_tete(self):
		pass


class Joueur_reel(Joueur):

	def __init__(self, nom, numero):
		super().__init__(nom, numero)

	def jouer(self):
		print(self.nom, "joue")
		Joueur.JOUEUR_QUI_JOUE = self.numero

	def taper(self):
		print(self.nom, "tape !")
		Joueur.JOUEUR_QUI_TAPE = self.numero

	def prendre(self):
		print(self.nom, "prend")
		Joueur.JOUEUR_QUI_PREND = self.numero


	def detection_touche(touche):
		pass
	#	if touche = ENTREZ:
	#		self.jouer()
	#	elif touche = ESPACE:
	#		self.taper()





class Joueur_ordi(Joueur):

	def __init__(self, nom, numero):
		super().__init__(nom, numero)
		self.niveau = 1


	def regler_niveau(niveau):
		self.niveau = niveau

	@property
	def temps_min(self, niveau):
		self.temps_min = 2 / niveau
		return self.temps_min

	@property
	def temps_max(self, niveau):
		self.temps_max = 5 / niveau
		return self.temps_max
	

	def jouer(self):
		print(self.nom, "joue")
		temps = random.uniform(self.temps_min, self.temps_max)
		time.sleep(temps)
		Joueur.JOUEUR_QUI_JOUE = self.numero

	def taper(self):
		print(self.nom, "tape !")
		temps = random.uniform(self.temps_min, self.temps_max)
		time.sleep(temps)
		Joueur.JOUEUR_QUI_TAPE = self.numero

	def prendre(self):
		print(self.nom, "prend")
		temps = random.uniform(self.temps_min, self.temps_max)
		time.sleep(temps)
		Joueur.JOUEUR_QUI_PREND = self.numero