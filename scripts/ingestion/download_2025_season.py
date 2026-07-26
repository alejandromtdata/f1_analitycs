import fastf1
import pandas as pd
import os

# Activar cache
fastf1.Cache.enable_cache("cache")

# Calendario 2025
races = [
    "Australia",
    "China",
    "Japan",
    "Bahrain",
    "Saudi Arabia",
    "Miami",
    "Emilia Romagna",
    "Monaco",
    "Spain",
    "Canada",
    "Austria",
    "Great Britain",
    "Belgium",
    "Hungary",
    "Netherlands",
    "Italy",
    "Azerbaijan",
    "Singapore",
    "United States",
    "Mexico",
    "Brazil",
    "Las Vegas",
    "Qatar",
    "Abu Dhabi"
]

all_laps = []

for race in races:

    print(f"\nCargando {race}...")

    try:
        session = fastf1.get_session(2025, race, "R")
        session.load()

        event = session.event

        laps["RaceName"] = event["EventName"]
        laps["Country"] = event["Country"]
        laps["CircuitName"] = event["Location"]
        laps["RoundNumber"] = event["RoundNumber"]

        laps = session.laps.copy()

        # Añadir nombre GP
        laps["RaceName"] = race

        # Seleccionar columnas útiles
        laps = laps[
            [
                "RaceName",
                "Driver",
                "DriverNumber",
                "Team",
                "LapNumber",
                "LapTime",
                "Sector1Time",
                "Sector2Time",
                "Sector3Time",
                "Compound",
                "TyreLife",
                "Stint",
                "Position",
                "SpeedST",
                "IsPersonalBest"
            ]
        ]

        all_laps.append(laps)

        print(f"{race} OK")

    except Exception as e:
        print(f"Error en {race}: {e}")

# Unir todo
final_df = pd.concat(all_laps)

# Crear carpeta data
os.makedirs("data", exist_ok=True)

# Exportar CSV
final_df.to_csv(
    "data/fact_laps_2025.csv",
    index=False
)

print("\nCSV final generado:")
print("data/fact_laps_2025.csv")

print("\nFilas totales:")
print(len(final_df))
