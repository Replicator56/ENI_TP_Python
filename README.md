Application de gestion de la population de pingouins.

Utilisant Python/Flask avec script de la création de la DB pour SSMS dans le répertoire ressources
le fichier config.py contient les paramètres pour accéder à la BDD et seront donc à modifier.
L'acces à l'application se fait en lançant app.py et est accessible sous http://localhost:5000/

Toutes les requêtes dynamiques utilisent %s + tuple pour injecter les valeurs.
Cela empêche l’utilisateur d’injecter du SQL malveillant (injection SQL).
Même les valeurs numériques (id_pingouin) sont passées comme paramètre, pas concaténées dans la requête.

Code HTML/Jinja2

