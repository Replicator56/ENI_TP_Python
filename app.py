from flask import Flask, render_template, flash, url_for, redirect, request

from dal.dallmpl import get_all_pingouins, delete_pingouins, update_pingouins,get_pingouin

app = Flask(__name__)
app.secret_key = 'une_clef_secrete_pour_flash'
@app.route('/')
def accueil():
    # Récupérer tous les pingouins depuis la DAL
    liste_pingouins = get_all_pingouins()
    return render_template('accueil.html', pingouins=liste_pingouins)

@app.route('/supprimer/<int:id_pingouin>')
def supprimer_pingouin(id_pingouin):
    delete_pingouins(id_pingouin)
    flash(f"Le pingouin avec l'id {id_pingouin} à été supprimé avec succès !", 'success')
    return redirect(url_for('accueil'))

@app.route('/modifier/<int:id_pingouin>', methods=['GET', 'POST'])
def modifier_pingouin(id_pingouin):
    pingouin = get_pingouin(id_pingouin)
    if not pingouin:
        flash(f"Aucun pingouin trouvé avec l'id {id_pingouin}", 'error')
        return redirect(url_for('accueil'))

    if request.method == 'POST':
        pingouin.espece = request.form['espece']
        pingouin.ile = request.form['ile']
        pingouin.longueur_bec = float(request.form['longueur_bec'])
        pingouin.profondeur_bec = float(request.form['profondeur_bec'])
        pingouin.longueur_nageoire = float(request.form['longueur_nageoire'])
        pingouin.poids = float(request.form['poids'])
        pingouin.sex = request.form['sex']
        pingouin.annee_naissance = int(request.form['annee_naissance'])

        update_pingouins(pingouin)
        flash(f"Les informations du pingouin {id_pingouin} ont été mises à jour !", 'success')
        return redirect(url_for('accueil'))

    # Affichage du formulaire avec les données pré - remplies
    return render_template("modification.html", pingouin=pingouin)



if __name__ == '__main__':
    app.run(debug=True)
