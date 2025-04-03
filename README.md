
# Instructions pour exécuter les scripts Python

Ce projet contient deux scripts Python : `congecture.py` et `jedelavie2.py`. Voici les étapes pour installer les dépendances nécessaires et exécuter ces scripts.

---

## Prérequis

Avant de commencer, assurez-vous d'avoir les éléments suivants installés sur votre machine :
- **Python 3.7 ou supérieur**
- **pip** (le gestionnaire de paquets Python)
- **Virtualenv** (optionnel mais recommandé)

---

## Installation

1. **Cloner ou télécharger le projet**  
   Téléchargez ou clonez ce projet dans un répertoire local.

2. **Créer un environnement virtuel (optionnel mais recommandé)**  
   Dans le terminal, exécutez les commandes suivantes :
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # Sur macOS/Linux
   ```

3. **Installer les dépendances**  
   Installez les bibliothèques nécessaires pour exécuter les scripts :
   ```bash
   pip install matplotlib numpy
   ```

---

## Exécution des scripts

### 1. **Exécuter `congecture.py`**

Ce script calcule et affiche la conjecture de Collatz pour un nombre donné par l'utilisateur. Il génère également un graphique montrant l'évolution des valeurs.

#### Étapes :
1. Lancez le script avec la commande suivante :
   ```bash
   python congecture.py
   ```
2. Entrez un nombre entier positif lorsque vous y êtes invité.
3. Le script affichera le temps de vol, l'altitude maximale et un graphique représentant l'évolution des valeurs.

---

### 2. **Exécuter `jedelavie2.py`**

Ce script implémente le jeu de la vie de Conway avec une configuration initiale contenant un canon à planeur. Il affiche une animation montrant l'évolution de la grille.

#### Étapes :
1. Lancez le script avec la commande suivante :
   ```bash
   python jedelavie2.py
   ```
2. Une fenêtre s'ouvrira pour afficher l'animation du jeu de la vie.

---

## Résolution des problèmes

### Erreur : `ModuleNotFoundError`
Si vous obtenez une erreur indiquant qu'un module est manquant (par exemple, `matplotlib` ou `numpy`), assurez-vous d'avoir installé les dépendances avec la commande :
```bash
pip install matplotlib numpy
```

### Erreur : "Permission denied" sur macOS
Si vous exécutez un fichier exécutable généré avec PyInstaller et que macOS bloque son exécution, allez dans **Préférences Système > Sécurité et confidentialité**, puis cliquez sur **Ouvrir quand même**.

---

## Générer un exécutable (optionnel)

Si vous souhaitez créer un fichier exécutable pour l'un des scripts, utilisez **PyInstaller** :
1. Installez PyInstaller :
   ```bash
   pip install pyinstaller
   ```
2. Générez un exécutable :
   ```bash
   pyinstaller --onefile congecture.py
   pyinstaller --onefile jedelavie2.py
   ```
3. Les exécutables seront disponibles dans le dossier `dist`.

---

## Auteurs

- **Script `congecture.py`** : Implémente la conjecture de Collatz avec visualisation graphique.
- **Script `jedelavie2.py`** : Implémente le jeu de la vie de Conway avec un canon à planeur.
