# Application de Recherche Gencod/EAN et Marque

Cette application web Flask permet aux utilisateurs de rechercher des codes Gencod/EAN à 13 chiffres dans un fichier CSV, de récupérer la marque et le code de situation associés, et d'identifier si un produit est de faible valeur. En cas de code barre inexistant, l'application permet de rechercher une marque dans un autre fichier CSV pour obtenir des informations sur le traitement SAV.

## Fonctionnalités

- Saisie et validation de codes Gencod/EAN à 13 chiffres.
- Recherche dans `gencod.csv` pour obtenir la marque et le code de situation.
- Identification des produits de faible valeur (code situation 'F9').
- Recherche de traitement SAV dans `marque.csv` si le code barre n'est pas trouvé.

## Structure du Projet

```
.
├── .github/
│   └── copilot-instructions.md
├── static/
│   └── style.css
├── templates/
│   └── index.html
├── app.py
├── gencod.csv
└── marque.csv
```

## Comment exécuter l'application

1.  **Assurez-vous d'avoir Python et Flask installés.** Si ce n'est pas le cas, vous pouvez les installer via pip :

    ```bash
    pip install Flask
    ```

2.  **Exécutez l'application Flask :**

    ```bash
    python app.py
    ```

3.  **Accédez à l'application :**

    Ouvrez votre navigateur web et accédez à `http://127.0.0.1:5000/`

## Fichiers de données

-   `gencod.csv`: Contient les codes Gencod/EAN, les marques et les codes de situation.
    Exemple :
    ```
    1234567890123,MarqueA,F9
    2345678901234,MarqueB,G0
    ```

-   `marque.csv`: Contient les marques et les informations sur le traitement SAV.
    Exemple :
    ```
    MarqueA,TraitementSAV_A
    MarqueB,TraitementSAV_B
    ```

