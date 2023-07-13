# Projet 7 OpenClassRoom : Résolvez des problèmes en utilisant des algorithmes en Python
![](https://raw.githubusercontent.com/waleedos/2023_P7_Python_Algorithmes_Finance/main/Mission/logo.png)

## Compétences évaluées :
- Interagir avec une API REST.
- Développer la partie Front-End d’une application avec HTML, CSS et JavaScript.

## Présentation du projet :
Le but de ce projet est de créer un site web de référencement de films de cinémas. Le but de ce site est de donner différentes informations sur plus ou moins 85000 films. Les informations comprennent le titre du film , son image, un résumé , son classement IMDB etc..

Ce site a pour but d'aider les cinéphiles lors de l'achat de dvd ou choix de programmes télé; Il est développé en html ,css et javascript( vanilla javascript); Et doit fonctionner sous Edge, Firefox et Chrome.

## Composition du projet :
Tous les fichiers nécessaires pour faire fonctionner le site se trouvent dans le répertoire /frontend.

Ces fichiers sont :
- index.html .
- style.css . 
- main.js .
- et un répertoire /img qui contient les images du site comme le logo et les flèches.

## Lancement du site en 4 étapes:
Afin de pouvoir lancer et tester ce projet vous devriez passer par ces 4 étapes : 

### 1- Création d'un répertoire vide :
Quelque part sur votre ordinateur, créez un répertoire vide et nommez le 'JustStreamIt'
```
mkdir JustStreamIt
```
Puis, rendez vous dans ce répertoire créé :
```
cd JustStreamIt
```

### 2- Clonage du projet :
```
git clone https://github.com/waleedos/2023_P6_JustStreamIt.git
```
Puis mettez vous dans la racine du projet : 
```
cd 2023_P6_JustStreamIt
```
### 3- Construisez votre API dans le répertoire /backend
```
cd backend
```
Puis créer un environnement virtuel :
```
python -m venv env
```
Puis activez votre environnement virtuel :
```
source env/bin/activate
```
Puis installer les dependances du projet :
```
pip install -r requirements.txt
```
Puis Créez et « populez » la base de donnée du projet :
```
python manage.py create_db
```
Et enfin, démarrez le serveur avec : 
```
python manage.py runserver
```

### 4- Démarrez le projet :
Ouvrez le fichier index.html se trouvant dans le dossier /frontend avec n'importe quel navigateur installé sur votre machine.

### Présentation du site
Sur l'interface de ce projet, les sections sont:

    -   Le meilleur film
        - Un bouton "plus d'infos" pour avoir un descriptif complet du film.
        - Un bouton pour fermer ce descriptif ouvert. 

    -   Section des 7 meilleurs films "Classement Global".

    -   1 section avec les 7 meilleurs films pour la catégorie Crime.
    -   1 section avec les 7 meilleurs films pour la catégorie Drame.
    -   1 section avec les 7 meilleurs films pour la catégorie Famille.
    -   1 section avec les 7 meilleurs films pour la catégorie Sport.

    -   Sur chaque image de chaque film un clic est possible pour ouvrir une fenêtre modale avec un descriptif     complet du film
    - Par défaut, dans chaque section, l'utilisateur trouve 5 films, et il doit cliquer sur une petite fleche à droite pour voir les deux autres films clic par clic
    - Une foi la flèche de droite cliquée, l'utilisateur peut retourner en arrière avec une autre flèche à gauche.

Bonne navigation...

## Validation HTML et CSS

Résultat de la validation du HTML sur le site du W3C    - OK

Résultat de la validation du CSS sur le site du W3C     - OK

Félicitations ! Aucune erreur trouvée.

## API Utilisée :
* Il utilise une API REST: OCMovies-API-EN-FR développée par OpenClassrooms

## Pour la vérification :
* Concernant l'installation de l'API, suivez les instructions données dans le repository Guthub :
[dépôt de OCMovies-API-EN-FR](https://github.com/OpenClassrooms-Student-Center/OCMovies-API-EN-FR)
* Testé sur les navigateurs Edge, Chrome et Firefox
* L'API tourne par défaut sur le port 8000

