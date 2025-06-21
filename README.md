# NUMBER_TO_WORD
projet de fin du cours d'algorithmique : un convertisseur de nombre en lettre en python
markdown


Ce projet a été réalisé dans le cadre d’un travail d’équipe en programmation Pytho. Il a pour objectif de convertir un nombre (entier, négatif ou décimal) en sa représentation écrite en toutes lettres, selon les règles du français.

membre du projet
- Mbuyi bilolo Ryan
- mbuyi ntita Ketsia
- mbuyi banza astride
- monga lumbu seraphin
- mbuyu kasongo sarah 

Objectifs pédagogiques

- Mettre en œuvre une **architecture modulaire** claire et testable
- Travailler la **collaboration via GitHub** (branches, commits, fusions)
- Maîtriser la lecture et la conversion de **nombres complexes** (grands, négatifs, décimaux)
- Proposer une interface **en ligne de commande** simple à utiliser
- Appliquer des concepts de **réutilisation de code**, de structure, et de lisibilité

  
 Structure du projet


convertisseur-nombres-en-lettres/
├── module1-number-parser/
│   └── number_parser.py
├── module2-core-converter/
│   └── core_converter.py
├── module3-large-number-handler/
│   └── large_number_handler.py
├── module4-output-formatter/
│   └── output_formatter.py
├── module5-main-cli/
│   └── main_cli.py
└── README.md


 Répartition des modules

| Module                        | Fichier                   | Responsable |
|------------------------------|---------------------------|-------------|
| Analyse de l’entrée          | `number_parser.py`        | Sarah       |
| Conversion des triplets      | `core_converter.py`       | Séraphin    |
| Regroupement & décimales     | `large_number_handler.py` | Astrid      |
| Formatage final              | `output_formatter.py`     | Ryan        |
| Interface CLI                | `main_cli.py`             | Ketsia      |

 Utilisation

 Exécuter une conversion

bash
python module5-main-cli/main_cli.py 123456.78


→ Résultat attendu :

cent vingt-trois mille quatre cent cinquante-six virgule sept huit


 Installation rapide

1. Cloner le projet :

bash
git clone git@github.com:TonPseudo/convertisseur-nombres-en-lettres.git
cd convertisseur-nombres-en-lettres


2. (Optionnel) Créer un environnement virtuel :

bash
python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate sur Windows


3. Installer les éventuelles dépendances :

bash
pip install -r requirements.txt


> ⚠ Aucun package externe n’est requis pour faire tourner la version de base du projet.



 Fonctionnement technique

 Module 1 – Analyse (parser)
- Nettoie l'entrée utilisateur
- Gère les `-`, les virgules/points et les erreurs de saisie

 Module 2 – Conversion de base
- Convertit les nombres de 0 à 999 avec les règles du français (liaisons, exceptions, accords)

 Module 3 – Grands nombres & décimales
- Coupe les nombres en segments de 3 chiffres
- Applique les échelles (`mille`, `million`, `milliard`, ...)
- Convertit chaque chiffre après la virgule individuellement

 Module 4 – Formatage
- Assemble les parties entières et décimales avec les bons espaces
- Applique les options de sortie (ex : tout en minuscules)

 Module 5 – Ligne de commande (CLI)
- Lit les arguments utilisateur
- Ordonne l'appel des modules et affiche le résultat final

 Exemple de conversions testées

| Entrée     | Résultat attendu                                  |
|------------|---------------------------------------------------|
| `0`        | zéro                                              |
| `21`       | vingt et un                                       |
| `80`       | quatre-vingts                                     |
| `105`      | cent cinq                                         |
| `1000000`  | un million                                        |
| `-3.14`    | moins trois virgule un quatre                     |
| `123456.78`| cent vingt-trois mille quatre cent cinquante-six virgule sept huit |


 À retenir

- Le projet respecte le principe **“un fichier = une responsabilité”**
- La fonction qui convertit les décimales **réutilise** celle des entiers (DRY)
- Le travail a été distribué via **branches GitHub**, puis fusionné en `main`
- Chaque module a été testé individuellement avant l'intégration finale




