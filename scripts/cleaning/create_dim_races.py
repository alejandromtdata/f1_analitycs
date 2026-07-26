import fastf1
import pandas as pd
import os

# Obtener calendario oficial 2025
schedule = fastf1.get_event_schedule(2025)

# Eliminar test de pretemporada
schedule = schedule[
    schedule["EventFormat"] != "testing"
]

# Seleccionar columnas útiles
races = schedule[
    [
        "RoundNumber",
        "Country",
        "Location",
        "EventName",
        "EventDate"
    ]
]

# Renombrar columnas
races = races.rename(
    columns={
        "EventName": "RaceName",
        "Location": "CircuitName"
    }
)

# Añadir columnas manuales
races["LengthKm"] = ""
races["LeftTurns"] = ""
races["RightTurns"] = ""

# Diccionario imágenes circuitos
circuit_images = {
    "Australian Grand Prix": "australia.png",
    "Chinese Grand Prix": "china.png",
    "Japanese Grand Prix": "japan.png",
    "Bahrain Grand Prix": "bahrain.png",
    "Saudi Arabian Grand Prix": "arabia_saudi.png",
    "Miami Grand Prix": "miami.png",
    "Emilia Romagna Grand Prix": "emilia_romagna.png",
    "Monaco Grand Prix": "monaco.png",
    "Spanish Grand Prix": "spain.png",
    "Canadian Grand Prix": "canada.png",
    "Austrian Grand Prix": "austria.png",
    "British Grand Prix": "great_britain.png",
    "Belgian Grand Prix": "belgium.png",
    "Hungarian Grand Prix": "hungary.png",
    "Dutch Grand Prix": "netherlands.png",
    "Italian Grand Prix": "italy.png",
    "Azerbaijan Grand Prix": "baku.png",
    "Singapore Grand Prix": "singapore.png",
    "United States Grand Prix": "usa.png",
    "Mexico City Grand Prix": "mexico.png",
    "São Paulo Grand Prix": "brasil.png",
    "Las Vegas Grand Prix": "las_vegas.png",
    "Qatar Grand Prix": "qatar.png",
    "Abu Dhabi Grand Prix": "abu_dhabi.png"
}

github_assets = (
    "https://raw.githubusercontent.com/"
    "alejandromtdata/f1_analytics/main/"
    "assets/"
)

races["CircuitImagePath"] = (
    github_assets
    + "circuits/"
    + races["RaceName"].map(circuit_images)
)

# Reordenar columnas
races = races[
    [
        "RoundNumber",
        "RaceName",
        "Country",
        "CircuitName",
        "EventDate",
        "LengthKm",
        "LeftTurns",
        "RightTurns",
        "CircuitImagePath"
    ]
]

# Crear carpeta clean
os.makedirs(
    "data/clean",
    exist_ok=True
)

# Exportar CSV
races.to_csv(
    "data/clean/dim_races.csv",
    index=False
)

print("\ndim_races creada correctamente")
print(races.head())