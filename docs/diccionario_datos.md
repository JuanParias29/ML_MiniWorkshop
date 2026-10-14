# Diccionario de datos de Olist

Los cinco CSV usados están incluidos en [`data/`](../data/). Se descargaron de
la versión 2 del dataset y se conservaron sus filas, seleccionando únicamente
las columnas descritas abajo. Se omitieron geolocalización, vendedores, pagos,
reseñas y campos no utilizados como ubicación y entrega. Las cantidades de
filas y encabezados se verificaron en los archivos incluidos; los tipos
indicados son tipos lógicos: pandas infiere los identificadores como texto,
las marcas de tiempo como texto ISO hasta convertirlas explícitamente en los
notebooks y el precio como numérico.

La ficha de Kaggle anuncia nueve CSV y aproximadamente 100.000 pedidos. La
selección incluida contiene 99.441 pedidos, 99.441 registros de clientes,
112.650 líneas de artículo, 32.951 productos y 71 traducciones de categorías.
Los identificadores son seudónimos anonimizados por Olist. Las relaciones
indicadas derivan del esquema y se usan para enlazar las tablas.

| Archivo / tabla | Columnas incluidas (tipo lógico) | Claves y relaciones principales | Uso en las rutas |
| --- | --- | --- | --- |
| `olist_orders_dataset.csv` | `order_id` (texto), `customer_id` (texto), `order_status` (texto), `order_purchase_timestamp` (fecha/hora ISO como texto) | `order_id` identifica pedido; `customer_id` referencia `customers.customer_id`. | Las tres rutas; fecha de compra y estado. |
| `olist_customers_dataset.csv` | `customer_id`, `customer_unique_id` (texto seudónimo) | `customer_id` se enlaza con pedidos; `customer_unique_id` agrupa pedidos asociados al mismo cliente seudónimo. | Recompra y segmentación para agrupar. |
| `olist_order_items_dataset.csv` | `order_id`, `product_id` (texto), `price` (numérico) | `order_id` enlaza pedidos y `product_id` productos; el original permite varias líneas por pedido. | Pronóstico, recompra y segmentación. |
| `olist_products_dataset.csv` | `product_id`, `product_category_name` (texto; puede faltar categoría) | `product_id` enlaza líneas de pedido. | Categoría para las tres rutas. |
| `product_category_name_translation.csv` | `product_category_name`, `product_category_name_english` (texto) | `product_category_name` enlaza el nombre de categoría del producto. | Traducción usada como etiqueta legible. |
| `olist_order_payments_dataset.csv` | No incluido | Tabla original no copiada al repositorio. | No se requiere. |
| `olist_order_reviews_dataset.csv` | No incluido | Tabla original no copiada al repositorio. | No se requiere. |
| `olist_sellers_dataset.csv` | No incluido | Tabla original no copiada al repositorio. | No se requiere. |
| `olist_geolocation_dataset.csv` | No incluido | Tabla original no copiada al repositorio. | No se requiere. |

## Relaciones usadas

```text
customers.customer_id 1 ── * orders.customer_id
orders.order_id       1 ── * order_items.order_id
products.product_id   1 ── * order_items.product_id
products.product_category_name  * ── 1 product_category_name_translation.product_category_name
customers.customer_unique_id    agrupa pedidos asociados a customer_id
```

Las relaciones describen enlaces esperados. La tabla de traducción puede no
cubrir todas las categorías; en ese caso se conserva el nombre original o se
etiqueta como `sin_categoria`.

## Límites de interpretación y privacidad

- No hay columnas publicadas de inventario, disponibilidad, quiebre de stock,
  unidades pedidas no satisfechas ni intención de compra.
- No aparece una columna explícita `quantity`. El número de filas de
  `order_items` mide líneas de artículos observadas, no necesariamente unidades.
- `customer_unique_id` es un identificador seudónimo y se usa solo para
  agrupar. No se muestra en tablas, gráficos o interfaz; no se usan nombres,
  ubicaciones ni coordenadas.
- El texto de reseñas y los campos geográficos no se necesitan para estas
  prácticas; no se incluyen en los CSV de este repositorio.
- La ficha de Kaggle muestra CC BY-NC-SA 4.0. Los CSV seleccionados se
  redistribuyen con atribución en [`data/README.md`](../data/README.md); la
  reducción de columnas es una adaptación sujeta a las mismas condiciones.
