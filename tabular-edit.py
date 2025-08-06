import pandas as pd

# Parametre
categorie = ["Alimentation","Revenu", "Transport", "Loisirs", "Épargne", "Cadeau"] 

"""for i in range(len(categorie)) : 
    print(i, categorie[i])"""

mois = ["" ,"janvier", "fevrier", "mars", "avril", "mai", "juin", "juillet", "aout", "septembre", "octrobre", "novembre", "decembre"]

#données
data = [
    {"Date": "2025-01-05", "Description": "McDo", "Montant": -8.50, "Catégorie": "Alimentation"},
    {"Date": "2025-01-06", "Description": "Bourse CROUS", "Montant": 450.00, "Catégorie": "Revenu"},
    {"Date": "2025-01-10", "Description": "Passe Navigo", "Montant": -42.00, "Catégorie": "Transport"},
    {"Date": "2025-01-15", "Description": "Cinéma", "Montant": -12.00, "Catégorie": "Loisirs"},
    {"Date": "2025-01-20", "Description": "Épargne", "Montant": -50.00, "Catégorie": "Épargne"},
]

# Convertir en DataFrame
df = pd.DataFrame(data)

# Calculs
total_depenses = df[df["Montant"] < 0]["Montant"].sum()
total_revenus = df[df["Montant"] > 0]["Montant"].sum()
solde = total_revenus + total_depenses

# Regrouper les dépenses par catégorie
depenses_par_categorie = df[df["Montant"] < 0].groupby("Catégorie")["Montant"].sum().reset_index()

# Statistiques
stats = pd.DataFrame({
    "Type": ["Total Revenus", "Total Dépenses", "Solde"],
    "Montant": [total_revenus, total_depenses, solde]
})

# Écriture dans un fichier Excel
with pd.ExcelWriter("suivi_comptes.xlsx", engine="openpyxl") as writer:
    df.to_excel(writer, sheet_name="Toutes les dépenses", index=False)
    depenses_par_categorie.to_excel(writer, sheet_name="Par catégorie", index=False)
    stats.to_excel(writer, sheet_name="Statistiques", index=False)

print("✅ Fichier Excel 'suivi_comptes.xlsx' généré.")