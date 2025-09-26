import pymssql
from config import SERVER, USER, PWD, BDD
from modele.pingouins import Pingouins


def get_all_pingouins():
    try:
        with pymssql.connect(SERVER, USER, PWD, BDD) as cnx:
            with cnx.cursor() as crs:
                crs.execute('SELECT * FROM PINGOUINS')
                rows = crs.fetchall()

                # Transformer les résultats en objets Pingouins
                liste_pingouins = [
                    Pingouins(
                        id_pingouin=row[0],
                        espece=row[1],
                        ile=row[2],
                        longueur_bec=row[3],
                        profondeur_bec=row[4],
                        longueur_nageoire=row[5],
                        poids=row[6],
                        sex=row[7],
                        annee_naissance=row[8]
                    )
                    for row in rows
                ]
                return liste_pingouins
    except pymssql.Error as e:
        print("Erreur lors de la récupération :", e)
        return []


def delete_pingouins(id_pingouin):
    try:
        with pymssql.connect(SERVER, USER, PWD, BDD) as cnx:
            with cnx.cursor() as crs:
                crs.execute('DELETE FROM PINGOUINS WHERE id_pingouin = %s', (id_pingouin,))
                cnx.commit()
                print(f"Le pingouin avec l'id {id_pingouin} a été supprimé avec succès.")
    except pymssql.Error as e:
        print("Erreur lors de la suppression :", e)


def update_pingouins(pingouin):
    try:
        with pymssql.connect(SERVER, USER, PWD, BDD) as cnx:
            with cnx.cursor() as crs:
                crs.execute("""
                            UPDATE PINGOUINS
                            SET espece            = %s,
                                ile               = %s,
                                longueur_bec      = %s,
                                profondeur_bec    = %s,
                                longueur_nageoire = %s,
                                poids             = %s,
                                sex               = %s,
                                annee_naissance   = %s
                            WHERE id_pingouin = %s
                            """, (
                                pingouin.espece,
                                pingouin.ile,
                                pingouin.longueur_bec,
                                pingouin.profondeur_bec,
                                pingouin.longueur_nageoire,
                                pingouin.poids,
                                pingouin.sex,
                                pingouin.annee_naissance,
                                pingouin.id_pingouin
                            ))
                cnx.commit()
                print(f"Pingouin avec l'id {pingouin.id_pingouin} mis à jour avec succès.")
    except pymssql.Error as e:
        print("Erreur lors de la mise à jour :", e)


def get_pingouin(id_pingouin):
    try:
        with pymssql.connect(SERVER, USER, PWD, BDD) as cnx:
            with cnx.cursor() as crs:
                crs.execute('SELECT * FROM PINGOUINS WHERE id_pingouin = %s', (id_pingouin,))
                row = crs.fetchone()
                if row:
                    pingouin = Pingouins(
                        id_pingouin=row[0],
                        espece=row[1],
                        ile=row[2],
                        longueur_bec=row[3],
                        profondeur_bec=row[4],
                        longueur_nageoire=row[5],
                        poids=row[6],
                        sex=row[7],
                        annee_naissance=row[8]
                    )
                    return pingouin
                else:
                    print(f"Aucun pingouin trouvé avec l'id {id_pingouin}.")
                    return None
    except pymssql.Error as e:
        print("Erreur lors de la récupération :", e)
        return None