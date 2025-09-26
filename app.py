from flask import Flask, render_template, flash, url_for, redirect, request
# Import des fonctions de la DAL pour manipuler les pingouins
from dal.dallmpl import get_all_pingouins, delete_pingouins, update_pingouins, get_pingouin

app = Flask(__name__)  # Création de l'application Flask
app.secret_key = 'une_clef_secrete_pour_flash'  # Clé secrète pour les messages flash


@app.route('/')  # Route de la page d'accueil
def accueil():
    liste_pingouins = get_all_pingouins()  # Récupère tous les pingouins
    return render_template('accueil.html', pingouins=liste_pingouins)  # Affiche la page avec les pingouins


@app.route('/supprimer/<int:id_pingouin>')  # Route pour supprimer un pingouin par son ID
def supprimer_pingouin(id_pingouin):
    delete_pingouins(id_pingouin)  # Supprime le pingouin dans la DAL
    flash(f"Le pingouin avec l'id {id_pingouin} à été supprimé avec succès !", 'success')  # Message flash
    return redirect(url_for('accueil'))  # Redirection vers la page d'accueil


@app.route('/modifier/<int:id_pingouin>', methods=['GET', 'POST'])  # Route pour modifier un pingouin
def modifier_pingouin(id_pingouin):
    pingouin = get_pingouin(id_pingouin)  # Récupère le pingouin depuis la DAL

    if not pingouin:  # Vérifie si le pingouin existe
        flash(f"Aucun pingouin trouvé avec l'id {id_pingouin}", 'error')
        return redirect(url_for('accueil'))  # Redirection si pingouin inexistant

    if request.method == 'POST':  # Si le formulaire est soumis
        # Mise à jour des données du pingouin avec le formulaire
        pingouin.espece = request.form['espece']
        pingouin.ile = request.form['ile']
        pingouin.longueur_bec = float(request.form['longueur_bec'])
        pingouin.profondeur_bec = float(request.form['profondeur_bec'])
        pingouin.longueur_nageoire = float(request.form['longueur_nageoire'])
        pingouin.poids = float(request.form['poids'])
        pingouin.sex = request.form['sex']
        pingouin.annee_naissance = int(request.form['annee_naissance'])

        update_pingouins(pingouin)  # Sauvegarde les modifications dans la DAL
        flash(f"Les informations du pingouin {id_pingouin} ont été mises à jour !", 'success')
        return redirect(url_for('accueil'))  # Redirection vers la page d'accueil

    # Si GET, affichage du formulaire avec les données pré-remplies
    return render_template("modification.html", pingouin=pingouin)


if __name__ == '__main__':
    app.run(debug=True)  # Démarrage du serveur Flask en mode debug
