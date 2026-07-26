import pandas as pd
import os

# Cargar CSV RAW
df = pd.read_csv(
    "data/raw/fact_laps_2025.csv"
)

# Seleccionar columnas
drivers = df[
    [
        "DriverNumber",
        "Driver",
        "Team"
    ]
]

# Eliminar duplicados iniciales
drivers = drivers.drop_duplicates()

# Renombrar columnas
drivers = drivers.rename(
    columns={
        "Driver": "DriverCode"
    }
)

# Limpiar espacios
drivers["DriverCode"] = drivers[
    "DriverCode"
].str.strip()

# Mantener Tsunoda en Red Bull
drivers = drivers[
    ~(
        (drivers["DriverCode"] == "TSU")
        & (drivers["Team"] == "Racing Bulls")
    )
]

# Mantener Lawson en Racing Bulls
drivers = drivers[
    ~(
        (drivers["DriverCode"] == "LAW")
        & (drivers["Team"] == "Red Bull Racing")
    )
]

# Diccionario nombres completos
driver_names = {
    "VER": "Max Verstappen",
    "NOR": "Lando Norris",
    "LEC": "Charles Leclerc",
    "HAM": "Lewis Hamilton",
    "ALO": "Fernando Alonso",
    "SAI": "Carlos Sainz",
    "RUS": "George Russell",
    "ANT": "Kimi Antonelli",
    "PIA": "Oscar Piastri",
    "TSU": "Yuki Tsunoda",
    "LAW": "Liam Lawson",
    "HAD": "Isack Hadjar",
    "ALB": "Alexander Albon",
    "COL": "Franco Colapinto",
    "DOO": "Jack Doohan",
    "GAS": "Pierre Gasly",
    "OCO": "Esteban Ocon",
    "BEA": "Oliver Bearman",
    "HUL": "Nico Hulkenberg",
    "BOR": "Gabriel Bortoleto",
    "STR": "Lance Stroll"
}

# Mapear nombres completos
drivers["FullName"] = drivers[
    "DriverCode"
].map(driver_names)

# Un piloto por dorsal
drivers = drivers.drop_duplicates(
    subset=["DriverNumber"]
)

# Ordenar por dorsal
drivers = drivers.sort_values(
    by="DriverNumber"
)

# Columnas auxiliares
drivers["TeamColor"] = ""


github_assets = (
    "https://raw.githubusercontent.com/"
    "alejandromtdata/f1_analytics/main/"
    "assets/drivers"
)

drivers["PhotoPath"] = (
    github_assets
    + "drivers/"
    + drivers["FullName"]
        .str.lower()
        .str.replace(" ", "_")
    + ".webp"
)
drivers["TeamLogoPath"] = ""

# Reordenar columnas
drivers = drivers[
    [
        "DriverNumber",
        "FullName",
        "DriverCode",
        "Team",
        "TeamColor",
        "PhotoPath",
        "TeamLogoPath"
    ]
]

# Crear carpeta clean
os.makedirs(
    "data/clean",
    exist_ok=True
)

# Exportar CSV limpio
drivers.to_csv(
    "data/clean/dim_drivers.csv",
    index=False
)

print("\ndim_drivers creada correctamente")
print(drivers.head())


