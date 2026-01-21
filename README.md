# Pipeline de Indicadores Financieros - SFC (Colombia)

Este proyecto es un pipeline de ingeniería de datos (ETL) que automatiza la extracción, transformación y carga de datos de cartera de las compañías de financiamiento y bancos en Colombia, utilizando la API de **Datos Abiertos (datos.gov.co)**.

## 1. Estructura del Proyecto

* **`config/`**: Parámetros estáticos y queries de la API.
* **`data/`**: Almacenamiento de la base de datos procesada (SQLite).
* **`logs/`**: Registros de ejecución para auditoría y errores.
* **`src/`**: Código fuente modular (Extract, Transform, Load, Utils).
* **`main.py`**: Orquestador principal del pipeline.

## 2. Requisitos Previos

* Python 3.8 o superior.
* Conexión a internet (para llamadas a la API).

## 3. Instalación y Ejecución

1. Clona este repositorio:
   ```bash
   git clone [https://github.com/DanielED07/Proyecto-ETL-Data-Cartera.git](https://github.com/DanielED07/Proyecto-ETL-Data-Cartera.git)
   cd nombre-del-proyecto
   ```

2. Ejecutar ETL (main.py):
   ```bash
   python main.py --fecha 2024-05-31
   ```