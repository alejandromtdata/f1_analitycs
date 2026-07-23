import pandas as pd
import os

# =========================
# Cargar CSV RAW
# =========================

df = pd.read_csv(
    "data/raw/fact_laps_2025.csv"
)

# =========================
# Seleccionar columnas útiles
# =========================

laps = df[
    [
        "Driver",
        "DriverNumber",
        "RaceName",
        "LapNumber",
        "Sector1Time",
        "Sector2Time",
        "Sector3Time",
        "LapTime",
        "Position",
        "Stint",
        "Compound",
        "TyreLife",
        "SpeedST",
        "IsPersonalBest",
        "Team"
    ]
]

# =========================
# Convertir columnas numéricas
# =========================

laps["LapNumber"] = laps["LapNumber"].fillna(0).astype(int)

laps["Position"] = laps["Position"].fillna(0).astype(int)

laps["Stint"] = laps["Stint"].fillna(0).astype(int)

laps["TyreLife"] = laps["TyreLife"].fillna(0).astype(int)

laps["SpeedST"] = laps["SpeedST"].fillna(0).astype(int)

# =========================
# Función formatear tiempos
# =========================

def format_lap_time(time_str):

    if pd.isnull(time_str):
        return None

    td = pd.to_timedelta(time_str)

    total_seconds = td.total_seconds()

    minutes = int(total_seconds // 60)

    seconds = total_seconds % 60

    return f"{minutes}:{seconds:06.3f}"

# =========================
# Crear columnas numéricas para cálculos BI
# =========================

laps["Sector1Seconds"] = pd.to_timedelta(
    laps["Sector1Time"]
).dt.total_seconds()

laps["Sector2Seconds"] = pd.to_timedelta(
    laps["Sector2Time"]
).dt.total_seconds()

laps["Sector3Seconds"] = pd.to_timedelta(
    laps["Sector3Time"]
).dt.total_seconds()

laps["LapTimeSeconds"] = pd.to_timedelta(
    laps["LapTime"]
).dt.total_seconds()


# =========================
# Formatear tiempos
# =========================

laps["Sector1Time"] = laps[
    "Sector1Time"
].apply(format_lap_time)

laps["Sector2Time"] = laps[
    "Sector2Time"
].apply(format_lap_time)

laps["Sector3Time"] = laps[
    "Sector3Time"
].apply(format_lap_time)

laps["LapTime"] = laps[
    "LapTime"
].apply(format_lap_time)

# =========================
# Ordenar datos
# =========================

laps = laps.sort_values(
    by=[
        "RaceName",
        "DriverNumber",
        "LapNumber"
    ]
)

# =========================
# Crear carpeta clean
# =========================

os.makedirs(
    "data/clean",
    exist_ok=True
)

# =========================
# Exportar CSV limpio
# =========================

laps.to_csv(
    "data/clean/fact_laps_clean.csv",
    index=False
)

# =========================
# Preview
# =========================

print("\nfact_laps_clean creada correctamente")

print(laps.head())