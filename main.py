import argparse
from datetime import datetime
from src.extract import extract
from src.load import load_to_sqlite
from src.transform import transform
from config.settings import API_KEY1, API_KEY2
from src.utils import setup_logger, validar_formato_fecha

logger = setup_logger()

def run_pipeline():
    parser = argparse.ArgumentParser(description="Pipeline de Indicadores SFC")
    parser.add_argument(
        "--fecha", 
        type=str, 
        help="Fecha de corte en formato YYYY-MM-DD",
        default=datetime.now().strftime("%Y-%m-%d") # Por defecto usa hoy
    )
    
    args = parser.parse_args()
    fecha_corte = args.fecha if args.fecha else datetime.now().strftime("%Y-%m-%d")

    logger.info("--- INICIANDO PIPELINE DE INDICADORES SFC ---")
    try:
        validar_formato_fecha(fecha_corte)
        #------------#
        # Extracción #
        #------------#
        data_raw = extract(API_KEY1, API_KEY2, fecha_corte)
        
        #----------------#
        # Transformación #
        #----------------#
        data_final = transform(data_raw[0], data_raw[1])
        
        #-------#
        # Carga #
        #-------#
        load_to_sqlite(data_final)
        logger.info("--- PIPELINE FINALIZADO CON ÉXITO ---")
    except Exception as e:
        logger.critical(f"EL PIPELINE FALLÓ: {e}")

if __name__ == "__main__":
    run_pipeline()