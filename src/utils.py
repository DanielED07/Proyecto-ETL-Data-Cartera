from datetime import datetime
import logging
import os

def setup_logger(name="pipeline_sfc"):
    """Configura el logger para el proyecto."""
    
    # Crear carpeta de logs si no existe
    if not os.path.exists('logs'):
        os.makedirs('logs')

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Evitar duplicados si se llama varias veces
    if not logger.handlers:
        # Formato del mensaje: Fecha - Nivel - Mensaje
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

        # Handler para consola
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        # Handler para archivo (se guarda en logs/pipeline.log)
        file_handler = logging.FileHandler('logs/pipeline.log')
        file_handler.setFormatter(formatter)

        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

    return logger

def validar_formato_fecha(fecha_str):
    """
    Verifica si una cadena de texto tiene el formato YYYY-MM-DD.
    Retorna True si es válido, lanza ValueError si no.
    """
    try:
        datetime.strptime(fecha_str, '%Y-%m-%d')
        return True
    except ValueError:
        raise ValueError(f"Formato de fecha inválido: '{fecha_str}'. Debe ser YYYY-MM-DD.")