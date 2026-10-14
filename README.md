# Taller de Machine Learning aplicado a comercio electrónico

<p align="center">
  <img
    src="./docs/banner_taller_ml.png"
    alt="Taller de Machine Learning aplicado a comercio electrónico"
    width="100%"
  >
</p>


## Descripción

Este repositorio contiene un taller educativo en español para introducir conceptos y técnicas de **Machine Learning aplicados al comercio electrónico**, utilizando el conjunto de datos público de Olist como caso de estudio. Este taller fue diseñado y desarrollado como material educativo para las actividades de formación de **Jarvis Lab**, en el marco de la **Semana de la Ingeniería 2026** de la Pontificia Universidad Javeriana.

El taller se organiza en tres rutas de aprendizaje progresivas que abordan el pronóstico de compras observadas, la predicción de recompra y la segmentación de clientes. Las tres siguen las seis fases de **CRISP-DM** (*Cross-Industry Standard Process for Data Mining*).

## Objetivos

- Comprender el flujo de trabajo de un proyecto de Machine Learning a partir de un problema de negocio.
- Aplicar las seis fases de CRISP-DM en problemas de análisis de datos.
- Explorar técnicas de pronóstico de series temporales, clasificación binaria y aprendizaje no supervisado.
- Construir variables a partir de datos transaccionales de comercio electrónico.
- Interpretar métricas y resultados, reconociendo las limitaciones de los datos y los modelos.
- Experimentar con interfaces interactivas para explorar el comportamiento de los modelos entrenados.

## Rutas de aprendizaje

| Notebook                                                             | Pregunta orientadora                                                            | Alcance                                                                                                                        |
| -------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| [`01_pronostico_demanda.ipynb`](./01_pronostico_demanda.ipynb)       | ¿Cuántas líneas de artículos compradas podrían observarse en próximos periodos? | Ruta principal presencial (\~1 hora). Permite seleccionar una categoría, una agregación temporal y un horizonte de pronóstico. |
| [`02_prediccion_recompra.ipynb`](./02_prediccion_recompra.ipynb)     | ¿Volverá a comprar un cliente durante una ventana futura de 90 días?            | Continuación: clasificación binaria con separación temporal para definir la variable objetivo.                                 |
| [`03_segmentacion_clientes.ipynb`](./03_segmentacion_clientes.ipynb) | ¿Qué patrones de compra similares aparecen entre clientes?                      | Continuación: análisis RFM, escalado de variables, K-Means e interpretación exploratoria de segmentos.                         |

Cada notebook desarrolla un problema específico y concluye con una interfaz pequeña de Gradio para experimentar con el modelo.

> **Nota:** en Google Colab, las interfaces son temporales. No constituyen servicios persistentes, despliegues de producción ni recomendaciones para tomar decisiones comerciales reales.

## Metodología: CRISP-DM

Las tres rutas se estructuran alrededor de las seis fases de CRISP-DM:

1. **Comprensión del negocio:** definición del problema y de la pregunta que se busca responder.
2. **Comprensión de los datos:** exploración de las tablas, las variables y la información disponible.
3. **Preparación de los datos:** selección, transformación y construcción de variables.
4. **Modelado:** aplicación de técnicas de Machine Learning adecuadas al problema.
5. **Evaluación:** análisis de métricas, resultados y limitaciones.
6. **Despliegue:** interacción con el modelo mediante una interfaz demostrativa.

Estas fases constituyen una guía de trabajo y no un proceso estrictamente lineal. En proyectos reales, es habitual regresar a etapas anteriores cuando los resultados, la calidad de los datos o los objetivos del negocio lo requieren.

## Datos y atribución

El taller utiliza el [Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce), publicado en Kaggle por Olist y distribuido mediante la ficha mantenida por `olistbr`.

Según la ficha de Kaggle, el conjunto contiene aproximadamente 100.000 pedidos de 2016 a 2018, distribuidos en nueve archivos CSV, con un tamaño total cercano a 126 MB.

La licencia indicada en Kaggle es [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). Sus condiciones incluyen atribuir la fuente, limitar el uso a fines no comerciales y compartir las adaptaciones bajo la misma licencia, además de cumplir los demás términos aplicables.

Antes de redistribuir los datos o utilizar derivados, se debe verificar la ficha original y las condiciones legales vigentes.

**La licencia del código no modifica la licencia de los datos.** El código educativo de este repositorio se distribuye bajo MIT, mientras que el conjunto de datos conserva las condiciones establecidas por sus titulares.

## Instalación y preparación de los datos

### 1. Descargar el conjunto de datos

Descargue el dataset desde la [página oficial de Kaggle](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce). Inicie sesión y acepte las condiciones que solicite la plataforma. También puede utilizar la CLI oficial de Kaggle.

No incluya `kaggle.json`, tokens ni credenciales dentro del repositorio. En local, utilice la ubicación segura documentada por Kaggle; en Google Colab, utilice Secrets o cargue manualmente el archivo ZIP desde su equipo.

### 2. Organizar los archivos

Descomprima los CSV originales, sin modificarlos, dentro de `data/raw/`.

Las tablas requeridas incluyen:

- `olist_orders_dataset.csv`
- `olist_customers_dataset.csv`
- `olist_order_items_dataset.csv`
- `olist_products_dataset.csv`
- `product_category_name_translation.csv`

El conjunto original contiene otras tablas que no son necesarias para estos ejercicios.

La carpeta `data/raw/` está excluida de Git.

### 3. Instalar dependencias y preparar las tablas

Desde la raíz del repositorio, ejecute:

```bash
python -m pip install -r requirements.txt
python scripts/prepare_data.py
```

El script valida los encabezados, conserva los CSV originales y genera los archivos Parquet requeridos en `data/processed/`, carpeta también excluida de Git.

Solo se convierten las tablas necesarias para los ejercicios: pedidos, clientes, líneas de pedido, productos y traducción de categorías.

### 4. Ejecutar los notebooks

Abra los notebooks desde la raíz del repositorio y ejecute sus celdas en orden.

Si falta algún archivo Parquet requerido, el notebook se detendrá y mostrará instrucciones para preparar los datos. No se generan resultados ficticios para sustituir los resultados del conjunto de datos.

## Ejecución en Google Colab

Puede abrir cada notebook desde GitHub y seleccionar **Open in Colab**, o clonar el repositorio directamente en una sesión de Colab.

Pasos generales:

1. Abra el repositorio en Google Colab.
2. Instale las dependencias de `requirements.txt`.
3. Descargue y descomprima los datos en `data/raw/`.
4. Ejecute `scripts/prepare_data.py`.
5. Ejecute las celdas del notebook seleccionado en orden.

La sesión de Colab y las interfaces de Gradio desaparecen al cerrar o reiniciar el entorno. Si desea conservar los resultados, guarde los archivos necesarios por separado.

## Ejecución local

**Requisitos:** Python 3.10–3.13 y JupyterLab o Jupyter Notebook.

Cree un entorno virtual, instale las dependencias, prepare los datos y abra Jupyter desde la raíz del repositorio.

```bash
python -m venv .venv

# Windows PowerShell
.venv\Scripts\Activate.ps1

# macOS/Linux
source .venv/bin/activate

python -m pip install -r requirements.txt
python scripts/prepare_data.py
jupyter lab
```

Las visualizaciones y las interfaces de Gradio requieren un navegador.

## Alcance y limitaciones

Es importante distinguir entre las compras observadas y la demanda real del mercado.

El conjunto de datos registra pedidos y artículos comprados, pero no contiene información sobre inventario, disponibilidad, quiebres de stock ni demanda no satisfecha. Por tanto, los notebooks no permiten medir directamente ventas perdidas ni reconstruir la demanda que no llegó a convertirse en una compra.

Los modelos y las métricas obtenidos deben interpretarse dentro de estas limitaciones. Este material no constituye una herramienta validada para decisiones comerciales reales.

## Estructura del repositorio

```text
.
├── notebooks/
│   ├── 01_pronostico_demanda.ipynb
│   ├── 02_prediccion_recompra.ipynb
│   └── 03_segmentacion_clientes.ipynb
├── docs/
│   ├── diccionario_datos.md
│   └── banner_taller_ml.png
├── data/
│   ├── raw/          # Datos originales
│   └── processed/    # Datos procesados
├── requirements.txt
├── LICENSE
└── README.md
```

## Tecnologías utilizadas

- **Python:** procesamiento de datos y desarrollo de modelos.
- **Pandas:** manipulación y transformación de tablas.
- **Parquet:** almacenamiento de datos procesados.
- **Jupyter:** desarrollo y ejecución interactiva.
- **Scikit-learn:** herramientas de Machine Learning.
- **Gradio:** construcción de interfaces demostrativas.
- **CRISP-DM:** marco metodológico para estructurar el proceso analítico.

Las versiones principales de las dependencias están definidas en [`requirements.txt`](./requirements.txt).

## Autor · Juan Pablo Arias Buitrago

Científico de Datos & Presidente de Jarvis Lab · IEEE CIS

## Organización

**Jarvis Lab** es un semillero de investigación vinculado al Departamento de Ingeniería de Sistemas de la Pontificia Universidad Javeriana, relacionado con el ecosistema de IEEE Computational Intelligence Society (IEEE CIS).

El semillero promueve el aprendizaje, la investigación y el desarrollo de soluciones basadas en inteligencia artificial y disciplinas relacionadas. Este taller contribuye a sus actividades de formación mediante un recurso práctico para explorar técnicas de Machine Learning y sus aplicaciones.

## Licencia

El código fuente de este repositorio se distribuye bajo la licencia [MIT](./LICENSE).

El conjunto de datos de Olist está sujeto a sus propias condiciones de uso y licencia, descritas en la sección [Datos y atribución](#datos-y-atribucion). La licencia MIT del código no modifica ni reemplaza las condiciones aplicables a los datos.
