# OrderInitialObjectOrderInitial


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**system_identification** | **str** | ID que identifica el sistema desde donde proviene la petición. | 
**company_identification** | **str** | ID que identifica la companía desde donde proviene la petición. | 
**branch_identification** | **str** | ID que identifica la sucursal desde donde proviene la petición. Esta sucursal pertenece a una determinada companía. | [optional] 
**pos_identification** | **str** | ID que identifica la caja o punto de venta desde donde proviene la petición. Este punto de venta pertenece a una determinada sucursal y companía. | [optional] 
**required_information** | [**[DebtPaymentObjectDebtPaymentRequiredInformation]**](DebtPaymentObjectDebtPaymentRequiredInformation.md) | En caso de que se requiera información adicional para poder completar la operación, como podrían ser ciertos datos ingresados por el vendedor para realizar verificaciones especificas (como los últimos 4 digitos), el código de seguridad de la tarjeta o la fecha de vencimiento, este elemento estará presente. | [optional] 
**service_version** | **str** | Versión del Servicio de la Plataforma con la cual se quiere transaccionar, en caso de no ser especificado será atendido por la última versión del servicio disponible. | [optional] 
**sequence** | **str** | Retornado en todas las respuesta que el POS/PINPAD debe enviar en el próximo requerimiento. En caso de que el POS no lo envíe, envíe vacío o con un valor que no corresponde se produce “La Ruptura de Secuencia” y la plataforma si la última transacción que realizó el POS no esta confirmada y esta Aprobada genera entonces una reversa de la misma. | [optional] 
**security** | [**[SaleObjectSaleSecurity]**](SaleObjectSaleSecurity.md) | Datos asociados a la seguridad de la transacción o de elementos sensibles. | [optional] 
**merchant_notify_url** | **str** | URL para notificación del comercio | [optional] 
**merchant_redirect_url** | **str** | . | [optional] 
**date_time** | **datetime** | Fecha y Hora de la transacción generada por el Punto de Venta - RFC3339 https://xml2rfc.tools.ietf.org/public/rfc/html/rfc3339.html#anchor14 | [optional] 
**transaction_identification** | **str** | ID de la operación a realizar, generado por el sistema externo | [optional] 
**transaction_description** | **str** | Descripción del tipo de operación que se realizará | [optional] 
**merchant_identification** | **str** | ID del comercio que el para el cual se estara realizando la operación. Este valor puede ser enviado en lugar del SystemIdentification y CompanyIdentification, para luego ser traducido por el propio Plataforma a los valores configurados para ello. Ademas, puede relaciónarse el valor de BranchIdentification y/o POSIdentification de la misma forma. Si ello no se realiza, estos elementos tomaran valores genericos (por default) igual a 0. | [optional] 
**installments** | **int** | Cantidad de cuotas que permite este plan | [optional] 
**facility_type** | **int** | Tipo de plan utilizado para para realizar la operación | [optional] 
**currency_code** | **str** | código de Moneda - ISO 4217 &lt;https://en.wikipedia.org/wiki/ISO_4217 Se puede utilizar la Codificación Alfabética o Numérica &lt;br /&gt;   * Num   - Alpha - Description &lt;br /&gt;   * &#39;032&#39; - &#39;ARS&#39; - Pesos Argentinos &lt;br /&gt;   * &#39;152&#39; - &#39;CLP&#39; - Pesos Chilenos &lt;br/&gt;   * &#39;484&#39; - &#39;MXN&#39; - Pesos Mexicanos &lt;br/&gt;   * &#39;840&#39; - &#39;USD&#39; - dólares Americanos &lt;br/&gt;   * &#39;878&#39; - &#39;EUR&#39; - Euros &lt;br/&gt;   * &#39;858&#39; - &#39;UYU&#39; - Pesos Uruguayos &lt;br/&gt;   * &#39;878&#39; - &#39;EUR&#39; - Euros &lt;br/&gt;   * &#39;986&#39; - &#39;BRL&#39; - Real Brasileño | [optional] 
**amount** | **float** | Monto con la que se realizó transacción. Si este valor es recibido, la búsqueda de los planes será limitada con este criterio. | [optional] 
**net_amount** | **str** | . | [optional] 
**payer** | [**SaleObjectSalePayer**](SaleObjectSalePayer.md) |  | [optional] 
**customer** | [**SaleObjectSaleCustomer**](SaleObjectSaleCustomer.md) |  | [optional] 
**seller** | [**SaleObjectSaleSeller**](SaleObjectSaleSeller.md) |  | [optional] 
**products** | [**[SaleResponseObjectSaleResponseProducts]**](SaleResponseObjectSaleResponseProducts.md) | Detalle de Productos de la Operación. | [optional] 
**tax_refund_type** | **str** | Esquema de Devolución de Impuestos a utilizar en la transacción | [optional] 
**valid_thru** | **datetime** | Fecha y Hora de fin de validez de La transacción - RFC3339 https://xml2rfc.tools.ietf.org/public/rfc/html/rfc3339.html#anchor14 | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


