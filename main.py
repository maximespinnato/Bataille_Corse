import joueur
import paquet
import carte
import random
import time

# Faire la logique lorsqu'on n'a plus de cartes
# Sauter les joueurs qui n'ont plus de cartes
# Faire les conditions pour la fin d'une partie
# Régler plus finement le niveau des ordis
# Essayer la classe Jeu ! 
# Installer le module keyboard pour la détection des touches
# Commencer le graphique


### VERIFIER LA CLASSE Conditions fin de partie

### VERIFIER LA CLASSE Sauter les joueurs qui n'ont plus de cartes



### Logique lorsque plus de cartes:
# Si il y a une tête : 
	# TETE EN COURS = TRUE

# Si joueur n n'a plus de cartes et TETE EN COURS et JOUEUR AIDEE = 0:
	# AUTORISATION JOUER = n+1 
	# JOUEUR AIDEE = n

# Si joueur n+1 n'a plus de cartes et TETE EN COURS et JOUEUR AIDEE = n:
	# AUTORISATION JOUER = n+2 

# Si un joueur récupère (en prenant ou tapant) :
	# JOUEUR AIDEE = 0

# Si il y a une tete et JOUEUR AIDEE = n :
	# JOUEUR AIDEE = 0
	# AUTORISATION PRENDRE = n
	# AUTORISATION JOUER = n + 1






def main():
	print("Réalisation du main")

	joueur.Joueur.initialize(7,4)
	#joueur.Joueur.AUTORISATION_TAPER = True
	print(joueur.Joueur.AUTORISATION_TAPER)
	print(joueur.Joueur.AUTORISATION_JOUER)

	paquet_complet = paquet.Paquet("Paquet complet")
	paquet_complet.creation_paquet_52_cartes()
	print(len(paquet_complet.liste))
	paquet_complet.melange()
	paquet_complet.montrer_paquet()
	paquet_complet.distribution_cartes(len(joueur.Joueur.JOUEURS))

	joueur.Joueur.JOUEURS[0].poser_carte()
	joueur.Joueur.JOUEURS[1].poser_carte()
	joueur.Joueur.JOUEURS[2].poser_carte()
	joueur.Joueur.JOUEURS[3].poser_carte()
	joueur.Joueur.JOUEURS[4].poser_carte()
	joueur.Joueur.JOUEURS[5].poser_carte()
	joueur.Joueur.JOUEURS[6].poser_carte()
	joueur.Joueur.JOUEURS[0].poser_carte()
	joueur.Joueur.JOUEURS[1].poser_carte()
	joueur.Joueur.JOUEURS[2].poser_carte()
	joueur.Joueur.JOUEURS[3].poser_carte()
	joueur.Joueur.JOUEURS[4].poser_carte()
	joueur.Joueur.JOUEURS[5].poser_carte()
	joueur.Joueur.JOUEURS[6].poser_carte()
	joueur.Joueur.JOUEURS[0].poser_carte()
	joueur.Joueur.JOUEURS[1].poser_carte()
	joueur.Joueur.JOUEURS[2].poser_carte()
	joueur.Joueur.JOUEURS[3].poser_carte()
	joueur.Joueur.JOUEURS[4].poser_carte()
	joueur.Joueur.JOUEURS[5].poser_carte()
	joueur.Joueur.JOUEURS[6].poser_carte()
	joueur.Joueur.JOUEURS[0].poser_carte()
	joueur.Joueur.JOUEURS[1].poser_carte()
	joueur.Joueur.JOUEURS[2].poser_carte()
	joueur.Joueur.JOUEURS[3].poser_carte()
	joueur.Joueur.JOUEURS[4].poser_carte()
	joueur.Joueur.JOUEURS[5].poser_carte()
	joueur.Joueur.JOUEURS[6].poser_carte()
	joueur.Joueur.JOUEURS[0].poser_carte()
	joueur.Joueur.JOUEURS[1].poser_carte()
	joueur.Joueur.JOUEURS[2].poser_carte()
	joueur.Joueur.JOUEURS[3].poser_carte()
	joueur.Joueur.JOUEURS[4].poser_carte()
	joueur.Joueur.JOUEURS[5].poser_carte()
	joueur.Joueur.JOUEURS[6].poser_carte()
	joueur.Joueur.JOUEURS[0].poser_carte()
	joueur.Joueur.JOUEURS[1].poser_carte()
	joueur.Joueur.JOUEURS[2].poser_carte()
	joueur.Joueur.JOUEURS[3].poser_carte()
	joueur.Joueur.JOUEURS[4].poser_carte()
	joueur.Joueur.JOUEURS[5].poser_carte()
	joueur.Joueur.JOUEURS[6].poser_carte()
	joueur.Joueur.JOUEURS[0].poser_carte()
	joueur.Joueur.JOUEURS[1].poser_carte()
	joueur.Joueur.JOUEURS[2].poser_carte()
	joueur.Joueur.JOUEURS[3].poser_carte()
	joueur.Joueur.JOUEURS[4].poser_carte()
	joueur.Joueur.JOUEURS[5].poser_carte()
	joueur.Joueur.JOUEURS[6].poser_carte()
	joueur.Joueur.JOUEURS[0].poser_carte()
	joueur.Joueur.JOUEURS[1].poser_carte()
	joueur.Joueur.JOUEURS[2].poser_carte()
	joueur.Joueur.JOUEURS[3].poser_carte()
	joueur.Joueur.JOUEURS[4].poser_carte()
	joueur.Joueur.JOUEURS[5].poser_carte()
	joueur.Joueur.JOUEURS[6].poser_carte()
	print("Attendons un peu...")
	time.sleep(10)
	print("Voilà, c'est bon !")


main()