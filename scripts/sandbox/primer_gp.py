import fastf1
import os

# Cache local
fastf1.Cache.enable_cache("cache")

print("Cargando GP...")

# España 2025 - Carrera
session = fastf1.get_session(2025, "Spain", "R")

session.load()

laps = session.laps

print("\nColumnas disponibles:")
print(laps.columns.tolist())

print("\nPrimeras filas:")
print(laps.head())

os.makedirs("data", exist_ok=True)

laps.to_csv(
    "data/spain_2025_laps.csv",
    index=False
)

print("\nCSV generado en data/spain_2025_laps.csv")

