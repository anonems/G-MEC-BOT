# G-MEC-BOT
Robot interactif, intervient pour apporter de l'aide aux nouveaux étudiants en bachelor developpement web au sein d'Hetic.

Ce robot à été crée dans le cadre de notre dormation de développeur web chez HETIC, encadré par Janin Loïc.

Il nous ai demander de crée un bot qui doit mener une discussion avec le(la) nouvel(le) etudiant(e), afin de filtrer et apporter un réponse précise à sa demande.

Nous proposont alors en groupe de quatre, le robot discord G-MEC, qui regroupe les fonctionnalitées suivantes :
  
  Le robot fonctionne dans un serveur qui comporte deux channels: 
    -Le channel Général : seul les commandes (lister plus bas) pourront y etre appliquer.
    -le channel G-MEC Help : résérvé à l'aide personnaliser en discutant avec le bot, on commence une discussion sur ce channel avec la commande suivante : <b>'g-mec!'.</b>, les commande sont aussi applicable sur ce channel.
    
  Les commandes possibles (toute commande devra débuter par '$') :
      - $info -> permet d'afficher la liste des commandes possible
      - $date -> affiche la date
      - $heure -> affiche l'heure
      - $serveur -> afiche les informations relatives au serveur
      - $memes -> affiche un meme orienter developpement tiré au hazard
      - $citation -> affiche une citation tirée au hazard
      - $play -> faire jouer un morceau à travers un lien
      - $modo @username -> demander à un utilisateur de vous contacter
      - $add entrée sortie -> contribuer au developpement du robot en ajoutant une réponse à une entrée inconnue
      - $clear nb -> nettoyer l'historique de discussion en supprimer un nombre 'nb' de messages 
      - g-mec! -> démarrer une discussion avec le bot.

  Une fois le mode discussion activé avec 'g-mec!', et en supplément des commandes précédentes, pour mieux géré la discussion vous avez à disposition les commendes       suivantes:
      - return -> reviens à la question précédente dans la chronologie de la discussion
      - reset -> redémarrer la discussion depuis le début
      - fin -> arreter la discussion

coté technique : 
  La discussion et la chronologie de la discussion est géré avec un 'Arbre' et ses 'Nodes'.
  L'historique de discussion est géré avec les 'Classes' et les 'Listes', une fois la discussion terminer la 'Valeur'(en forme de liste) de la 'Clefs'(qui est le username) est vidée.
  La fonction de contribution '$add' est géré par un 'Dictionnaire'.
  
Membre du groupe et répartition des taches : 
Répartition des taches (chaqu'un c'est chargé de la partie sur laquelle il est plus à l'aise): <br><br>
<a href="https://www.linkedin.com/in/emir-hakiri/">EMIR HAKIRI</a> : Partie Discussion avec le bot, Commandes $info, $dates, $heure, $add, $memes, g-mec!.
<br>
<a href="https://www.linkedin.com/in/gajan-baskaran-/">GAJAN BASKARAN </a> : Commandes $citation, $memes, $modo. Ajout de question/réponse et liens de redirection.
<br>
<a href="https://www.linkedin.com/in/diouf-maguette-2735ba204/">MAGUETTE DIOUF</a> : Commandes $memes, $clear.
<br>
<a href="linkedin.com/in/carime-belazzoug-b773901b3/">BELAZZOUG CARIM</a> : Commande $play
<br>
<br>




Merci pour le temps accordé.
<a href="https://www.linkedin.com/in/emir-hakiri/">@anonems</a>
