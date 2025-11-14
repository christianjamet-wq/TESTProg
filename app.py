from flask import Flask, render_template, request
import csv

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        gencod = request.form['gencod']
        if len(gencod) != 13 or not gencod.isdigit():
            result = "Veuillez saisir un Gencod/EAN de 13 chiffres."
        else:
            # Search in gencod.csv
            found_in_gencod = False
            with open('gencod.csv', 'r') as f:
                reader = csv.reader(f)
                for row in reader:
                    if row and row[0] == gencod:
                        marque = row[1]
                        code_situation = row[2]
                        result = f"Marque: {marque}, Code situation: {code_situation}"
                        if code_situation == 'F9':
                            result += " (Produit faible valeur)"
                        else:
                            result += " (Pas un produit faible valeur)"
                        found_in_gencod = True
                        break

            if not found_in_gencod:
                result = "Code barre inexistant. Veuillez entrer une marque."

    return render_template('index.html', result=result)

@app.route('/search_marque', methods=['POST'])
def search_marque():
    marque = request.form['marque']
    traitement_sav = "Non trouvé"
    with open('marque.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if row and row[0].lower() == marque.lower():
                traitement_sav = row[1]
                break
    return render_template('index.html', result=f"Traitement SAV pour {marque}: {traitement_sav}")

if __name__ == '__main__':
    app.run(debug=True)
