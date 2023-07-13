# Projet 7 OpenClassRoom : Résolvez des problèmes en utilisant des algorithmes en Python
![](https://raw.githubusercontent.com/waleedos/2023_P7_Python_Algorithmes_Finance/main/Mission/logo.png)

## Compétences évaluées :
- Déconstruire un problème.
- Développer un algorithme pour résoudre un problème.

## Présentation du projet :
En tant que développeur Web Python travaillant dans une une société financière spécialisée dans l'investissement « AlgoInvest&Trade », je doit développer un algorithme en python pour optimiser les solutions des clients de la société afin de rendre les programmes d'investissement à court terme plus compétitifs. Cet algorithme doit maximiser le profit réalisé par les clients de la société après deux ans d'investissement.

## Composition du projet :
Tous les fichiers nécessaires pour faire fonctionner le site se trouvent dans ce ripositoire.

Ces fichiers sont :
- /1-brutforce/brutforce.py.
- /2-optimized/optimized.py. 
- /3-analyse/ : contenant 2 fichiers .py pour la démonstartion et la comparaison des algorithmes.
- /date : contenant les fichiers de trade à analyser par les algorithmes et sont en .csv.

## Lancement du site en 4 étapes:
Afin de pouvoir lancer et tester ce projet vous devriez passer par ces 4 étapes : 

### 1- Création d'un répertoire vide :
Quelque part sur votre ordinateur, créez un répertoire vide et nommez le 'Algorithme-Finance'
```
mkdir Algorithme-Finance
```
Puis, rendez vous dans ce répertoire créé :
```
cd Algorithme-Finance
```

### 2- Clonage du projet :
```
git clone https://github.com/waleedos/2023_P7_Python_Algorithmes_Finance.git
```
Puis mettez vous dans la racine du projet : 
```
cd Algorithme-Finance
```
### 3- Construisez votre environnement virtuel
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

### 4- Démarrez le projet :

#### - Pour executer l'algorithme "brutforce" :
```
python 1-brutforce/brutforce.py
```

#### - Pour executer l'algorithme "optimized" :
```
python 2-optimized/optimized.py
```

#### - Pour executer une analyse de l'algorithme "brutforce" :
```
python 3-analyse/optcomplexite-brutforce.py
```

#### - Pour executer une analyse de l'algorithme "optimized" :
```
python 3-analyse/optcomplexite-optimized.py
```

