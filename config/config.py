import os
import sys
from pathlib import Path

if getattr(sys, "frozen", False):
    BASE_DIR = Path(sys.executable).resolve().parent
    RESOURCE_DIR = Path(getattr(sys, "_MEIPASS", BASE_DIR))
else:
    BASE_DIR = Path(__file__).resolve().parents[1]
    RESOURCE_DIR = BASE_DIR

# Un solo archivo; se crea solo. (MESA_DB permite otra ruta, p. ej. en pruebas.)
DB_PATH = Path(os.environ.get("MESA_DB", BASE_DIR / "data" / "mesa_compartida.db"))
SCHEMA_PATH = RESOURCE_DIR / "database" / "mesa_compartida.sql"

APP_NAME = "Mesa Compartida"
SCHEMA_VERSION = 2

# ---------------------------------------------------------------- CATÁLOGO DE ALIMENTOS
# tipo -> (requiere refrigeración, raciones por kg, valor estimado por kg en pesos)
ALIMENTOS = {
    "Pan y tortilla": (False, 5.0, 35.0),
    "Frutas y verduras": (False, 4.0, 25.0),
    "Abarrotes (latas, granos, pasta)": (False, 4.5, 40.0),
    "Comida preparada": (False, 3.0, 80.0),
    "Lácteos y huevo": (True, 4.0, 60.0),
    "Carnes y embutidos": (True, 3.5, 110.0),
}
HORAS_LIMITE = [2, 4, 8, 12, 24, 48]     # tiempo disponible para recoger antes de que se eche a perder
URGENTE_HORAS = 4                        # <= esto se marca prioridad ALTA

# Tipos de vehículo y capacidades sugeridas (en kg)
VEHICULOS_INFO = {
    "Bicicleta": {"max_sugerido": 20, "default": 10, "desc": "Canastilla o mochila: máx. sugerido 20 kg (ej. 10 kg)"},
    "Motocicleta": {"max_sugerido": 50, "default": 25, "desc": "Caja trasera o parrilla: máx. sugerido 50 kg (ej. 15 a 40 kg)"},
    "Automóvil / Carro": {"max_sugerido": 150, "default": 130, "desc": "Cajuela y asientos: alrededor de 80 a 130-150 kg"},
    "Camioneta / SUV": {"max_sugerido": 600, "default": 350, "desc": "Batea o cajuela amplia: de 200 a 600 kg"},
    "Camión de carga": {"max_sugerido": 3000, "default": 1000, "desc": "Carga pesada: especifica la capacidad en kg"},
    "Otro": {"max_sugerido": 3000, "default": 50, "desc": "Especifica la capacidad real de tu vehículo"},
}
CAPACIDADES_KG = (10, 25, 50, 130, 150)   # Capacidades de referencia
CAPACIDAD_MAXIMA_DONACION = 150           # Límite por viaje individual
GASOLINA_PRECIO = 24.50
KM_POR_LITRO = 11.0
FACTOR_RUTA = 1.30                       # km reales ≈ línea recta × 1.30 (sin internet)

# ---------------------------------------------------------------- PUNTOS FIJOS (EJEMPLOS: editar)
BASE = {"nombre": "Centro de acopio", "lat": 16.7531, "lng": -93.1156}
COMEDORES = [
    {"nombre": "Comedor San Roque", "lat": 16.7600, "lng": -93.1250, "personas": 80},
    {"nombre": "Comedor Albergue Esperanza", "lat": 16.7300, "lng": -93.0900, "personas": 120},
    {"nombre": "Casa Hogar Los Pinos", "lat": 16.7800, "lng": -93.1000, "personas": 45},
    {"nombre": "Comedor Comunitario Santa María", "lat": 16.7620, "lng": -93.1350, "personas": 90},
    {"nombre": "Asilo San Vicente de Paúl", "lat": 16.7450, "lng": -93.1250, "personas": 60},
]
ZONAS = [
    {"nombre": "Centro", "lat": 16.7528, "lng": -93.1152},
    {"nombre": "Terán", "lat": 16.7430, "lng": -93.1330},
    {"nombre": "Las Granjas", "lat": 16.7350, "lng": -93.0930},
    {"nombre": "Plan de Ayala", "lat": 16.7690, "lng": -93.1000},
    {"nombre": "Albania", "lat": 16.7800, "lng": -93.1400},
]
