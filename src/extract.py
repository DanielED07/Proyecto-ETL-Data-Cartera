from config.settings import QUERY_TIPO_ENTIDAD, QUERY_CUENTAS
from src.utils import setup_logger
import pandas as pd
import requests

logger = setup_logger()

def extract(API1, API2, FECHA_CORTE):
    logger.info("Iniciando extracción de datos desde datos.gov.co...")
    try:
        QUERY1 = {
        "FECHA_CORTE":FECHA_CORTE,
        '$WHERE': QUERY_TIPO_ENTIDAD,
        "RENGLON":"5"
        }

        QUERY2 = {
            "FECHA_CORTE":FECHA_CORTE,
            '$WHERE':QUERY_CUENTAS
        }
        #-------------------#
        # REQUEST DATOS GOV #
        #-------------------#
        request1 = requests.get(API1, params = QUERY1)
        request2 = requests.get(API2, params = QUERY2)

        #-----------------#
        # EXTRACCIÓN DATA #
        #-----------------#

        if request1.status_code == 200 and request2.status_code == 200:
            contenido1_json = request1.json()
            contenido2_json = request2.json()

            df1 = pd.json_normalize(contenido1_json)
            df2 = pd.json_normalize(contenido2_json)

            logger.info("Extracción completada exitosamente.")
            return [df1, df2]
    except Exception as e:
        logger.error(f"Error en la extracción: {e}")
        raise