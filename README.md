# Compte rendu

Nous avons le fichier shadow composé de 9 chaines de caractères séparéré chacune du caratère suivant ":".    
On remarque que sur la disposition suivante seul les 6 premières chainde de caractères sont affiché.   
Suite à la rechercher suivante:   
[https://www.tldp.org/LDP/lame/LAME/linux-admin-made-easy/shadow-file-formats.html](https://www.tldp.org/LDP/lame/LAME/linux-admin-made-easy/shadow-file-formats.html)   
On sait comment marche le format des codes shadow   
[https://security.stackexchange.com/questions/92149/what-are-hashes-that-begin-with-1](https://security.stackexchange.com/questions/92149/what-are-hashes-that-begin-with-1)   
On apprends que le mot de passe est chiffré suivant la méthode MD5   
On a donc la chaine de caractère suivante   
root:$1$934b4a210c17493f68bf6bfe74bff77a:16749:0:99999:7:::   
user:password(sousMD5):DayFrom1Jan1970:daysLeftBeforePswdShouldChange:daysLeftBeforePswdMustChange:DayToWarn:::    

## Brute force

Suite à ces découvertes nous décidons de mettre en place un code force brute dans lequel nous aurons trois fonctions principales

un    --> crée une chaine aléatoire avec une fonction recusive (redo)     
deux  --> chiffré cette chaine en MD5 si les caractères dépasse une longueur requise     
trois --> lire stocker et comparer avec le fichier shadow     

proposition de solution:
[Force Brute python scritp](https://github.com/JujuDesFruits/bruteForce-dictionary/blob/master/hackThisShitDumber.py)

## Dictionary

pour la méthode utilisant un dictionnaire de mot de passe connu, c'est plus simple et plus rapide.

un    --> lire stocker le fichier shadow     
deux  --> lire et chiffrer en md5 le dictionnaire     
trois --> comparé les valeurs obtenu du dico avec le ficier shadow     

proposition de solution:     
[Dictionary python scritp](https://github.com/JujuDesFruits/bruteForce-dictionary/blob/master/hackThisShit.py)
