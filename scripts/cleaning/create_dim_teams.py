import pandas as pd
import os

# Cargar CSV RAW
df = pd.read_csv(
    "data/raw/fact_laps_2025.csv"
)

# Seleccionar columna Team
teams = df[
    [
        "Team"
    ]
]

# Eliminar duplicados
teams = teams.drop_duplicates()

# Ordenar alfabéticamente
teams = teams.sort_values(
    by="Team"
)

# Diccionario colores equipos
team_colors = {
    "Red Bull Racing": "#0600EF",
    "Ferrari": "#DC0000",
    "Mercedes": "#00D2BE",
    "McLaren": "#FF8700",
    "Aston Martin": "#006F62",
    "Alpine": "#FB00FF",
    "Williams": "#005AFF",
    "Racing Bulls": "#1E5BC6",
    "Kick Sauber": "#52E252",
    "Haas F1 Team": "#FFFFFF"
}

# Mapear colores
teams["TeamColor"] = teams[
    "Team"
].map(team_colors)

# Diccionario logos equipos
team_logos = {
    "Alpine": "alpine.jpg",
    "Aston Martin": "aston_martin.jpg",
    "Ferrari": "ferrari.jpg",
    "Haas F1 Team": "haas.jpg",
    "Kick Sauber": "kick_sauber.png",
    "McLaren": "mc_laren.jpg",
    "Mercedes": "mercedes.jpg",
    "Racing Bulls": "racing_bulls.png",
    "Red Bull Racing": "red_bull.jpg",
    "Williams": "williams.jpg"
}
github_assets = (
    "https://raw.githubusercontent.com/"
    "alejandromtdata/f1_analytics/main/"
    "assets/"
)

teams["TeamLogoPath"] = (
    github_assets
    + "teams/"
    + teams["Team"].map(team_logos)
)

# Reordenar columnas
teams = teams[
    [
        "Team",
        "TeamColor",
        "TeamLogoPath"
    ]
]

# Crear carpeta clean
os.makedirs(
    "data/clean",
    exist_ok=True
)

# Exportar CSV
teams.to_csv(
    "data/clean/dim_teams.csv",
    index=False
)

print("\ndim_teams creada correctamente")
print(teams.head())