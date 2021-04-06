# Controlleur-youtube-webcam
Ceci est une extension permettant de gérer youtube avec sa webcam ( mouvement de main ), c'est à dire mettre en pose, monter, baisser le son etc...

Tout d'abord voyons comment l'utiliser.



Une fois le projet installé sur votre machine il ne vous sufirat plus qu'à éxécuter le programme main.py. 

ATTENTION : Il faut bien installer le projet entier car il y a un programme qui sert de "Bliblihotèques".

Pour commencer nous allons lancer le programme de test qui se nomme "test.py", celui-ci servira de test pour voir si vous possédez bien toutes les bliblihotèques requises et pour modifier un peu le programme si besoin pour choisir une webcam précise.



Lancez le Programme et voyez ce qu'il se passe.

Possibilités:

 - Il vous manque des bliblihotèques, il vous suffit de les installer.

   cv2 : 
   pip3 install opencv-python
   
   mediapipe:
   pip3 install mediapipe
   
   pyautogui:
   pip3 install pyautogui
   
   keyboard:
   pip3 install keyboard
   
   win32api:
   pip3 install pywin32
   
   pygame:
   pip3 install pygame
   
 - Le programme se lance sur une webcam non voulue ou vous voulez passer sur une autre webcam. Il vous suffit de modifier dans le programme la ligne :

![image](https://user-images.githubusercontent.com/72353621/113747781-06876080-9708-11eb-99aa-bb27e809c813.png)

   Il vous suffit de changer le 0 qui selectionne la webcam par défaut, pour aller sur une autre webcam il suffit de monter le chiffre (ex : 1, 2, 3, etc...)

 - Si le programme se lance sans erreur et sur la webcam voulue, alors tout est parfait on peut passer à la suite.


Vous aurez un affichage de la webcam avec le "squelette" de la main dans la fenêtre de cv2.

C'est grâce à ces points de repères que j'ai pus créer les différentes positions de la main grâce à la distance entre chaque points.



Vous devez arriver à ce résultat : 

![image](https://user-images.githubusercontent.com/72353621/113748870-47cc4000-9709-11eb-9ae6-dc037893e376.png)


Maintenant nous pouvons commencer à regarder le programme principal.

Voici les différentes options disponibles avec la position de main à avoir pour les faire :

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


Voici pour l'instant toutes les commandes possibles.

Libre à vous d'en rajouter ou d'en modifier. 

Il y a pas mal de beug liés aux croisements de doigts. Mais tous ces beugs sont dûs à la bliblihotèque de reconnaissance et sont assez durs à corriger car il faudrait améliorer l'IA qui detecte les points.

Ce projet reste à compléter. En effet j'ai fait ce projet assez rapidement par curiosité. Il faut l'optimiser. Il fonctionne et peut servir d'example pour d'autres programmes quand à eux plus poussée. A vous d'innovez à votre sauce. 

