# Datos de práctica

Estos CSV son una selección de columnas del **Brazilian E-Commerce Public
Dataset by Olist**, versión 2, descargado de
<https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce>.
Se mantuvieron los registros y se omitieron las columnas no utilizadas en el
taller. Las tablas contienen:

- pedidos: `order_id`, `customer_id`, `order_status`,
  `order_purchase_timestamp`;
- clientes: `customer_id`, `customer_unique_id`;
- líneas: `order_id`, `product_id`, `price`;
- productos: `product_id`, `product_category_name`;
- traducción: `product_category_name`, `product_category_name_english`.

Se excluyeron códigos postales, ciudades, estados, datos de vendedores,
reseñas, pagos y geolocalización. Los identificadores de cliente incluidos
son seudónimos ya anonimizados por la fuente y solo se necesitan para agrupar
pedidos; no representan nombres ni datos de contacto.

**Atribución:** Olist, *Brazilian E-Commerce Public Dataset by Olist*,
<https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce>, licencia
[CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).
Esta selección conserva las filas originales y contiene una adaptación por
reducción de columnas. Su redistribución debe mantener la atribución, ser para
uso no comercial y respetar ShareAlike. La licencia MIT del código no se aplica
a estos archivos de datos.

Los notebooks leen estos CSV directamente desde la carpeta `data/` en la rama
`main` del repositorio; no se necesita descargar el ZIP de Kaggle.
