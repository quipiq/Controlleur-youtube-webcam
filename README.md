# Controlleur-youtube-webcam
Ceci est une extension permettant de gérer youtube avec sa webcam ( mouvement de main ), c'est a dire mettre en pose, monter, baisser le son etc...

Tout d'abord voyons comment l'utiliser.



Une fois le projet installer sur votre machine ils ne vous sufirat plus qu'a éxécuter le programme main.py. 

ATTENTION : Il faut bien installer le projet entier car il y a un programme qui sert de "Bliblihotèques".

Pour commencer nous allons lancer le programme de test qui se nomme "test.py", celui-ci servira de test pour voir si vous possédés bien toute les bliblihotèques requise et pour modifier un peut le programme si besoins pour choisir une webcam précise.



Lancer le Programme et voyer ce qu'il se passe.

Possibilitées:

 - Il vous manque des bliblihotèques, il vous suffit de les installer.

 - Le programme ce lance sur une webcam non voulue ou vous voulez passer sur une autres webcam. Il vous suffit de modifier dans le programme la ligne :

![image](https://user-images.githubusercontent.com/72353621/113747781-06876080-9708-11eb-99aa-bb27e809c813.png)

   ls vous suffit de changer le 0 qui selectionne la webcam par défaut, pour aller sur une autre webcam il suffit de monter le chiffre (ex : 1, 2, 3, etc...)

 - Si le programme ce lance sans erreur et sur la webcam voulue, alors tout est parfait on peut passer a la suite.


Vous aurez un affichage de la webcam avec le "squelette" de la main dans la fenetre de cv2.

C'est grace a ces points de repaires que j'ai peut créé les différentes positions de la main grace a la distance entre chaque points.



Vous devez arriver a ce résultats : 

![image](https://user-images.githubusercontent.com/72353621/113748870-47cc4000-9709-11eb-9ae6-dc037893e376.png)


Maintenant nous pouvons commencer a regarder le programme principale.

Voici les différentes options disponibles avec la positions de main a avoir pour les faire :

 - Pour ne rien faire il faut avoir la main ouverte : 
   
   ![image](https://user-images.githubusercontent.com/72353621/113749421-f2446300-9709-11eb-8f39-369574bfd08a.png)


 - Mettre en pause ou redémarrer la vidéo : 
   
   ![Pause](https://user-images.githubusercontent.com/72353621/113749286-caed9600-9709-11eb-88a9-58abf98d9293.PNG)

 - Passer 5 secondes :
   
   ![Passe](https://user-images.githubusercontent.com/72353621/113749745-47807480-970a-11eb-83d6-bd2328f6dbb9.PNG)
   
 - Retour 5 secondes :
   
   ![Retour](https://user-images.githubusercontent.com/72353621/113749811-5c5d0800-970a-11eb-9abe-25853b80f13c.PNG)
  
 - Monter le son : 
   
   ![MonteSon](https://user-images.githubusercontent.com/72353621/113749917-7696e600-970a-11eb-978a-51d8ebab3329.PNG)
   
 - Baisser le son :

   ![BaisseSon](https://user-images.githubusercontent.com/72353621/113749970-84e50200-970a-11eb-9320-74a67f47ccdb.PNG)


Voici pour l'instant toute les commandes possibles.

Libre a vous d'en r'ajouter ou dans modifier. 

Il y a pas mal de beug liée aux croisements de doigts qui se fait honnêtement pas si mal. Mais tous ces beugs sont du a la bliblihotèques de reconnaissent et sont assez dur a corriger car il faudrait carremment améliorer l'IA qui detecte les points.

Ce projet reste a compléter. En effet j'ai fait se projet assez rapidement pour m'occuper un peut mais n'est pas très optimiser. Mais fonctionne comme même et peut servir d'examples pour d'autre programme quand a eu plus poussée. A vous d'innovez a votre sauce. 

