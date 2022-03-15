# WalletRequestObjectWalletRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**system_identification** | **str** | Identificación  del sistema o Aplicativo. | 
**company_identification** | **str** | Identificador de la Compañía para la Plataforma de Integración. | 
**branch_identification** | **str** | ID de la sucursal, en caso de no existir ese concepto y ser un dispotivo que tiene posiciónamiento, deberá ser el mismo en caso contrario el mismo valor que el elemento &lt;b&gt;CompanyIdentification&lt;/b&gt; | [optional] 
**pos_identification** | **str** | ID de la caja perteneciente a la sucursal indicada, en caso de no existir ese concepto y ser un dispotivo que tiene un identificador unico como por ejemplo el IMEI deberá viajar este. | [optional] 
**request_type** | **str** | Tipo de Requerimiento. Solo requerido para protocolos de transporte donde el tipo no se este especificando o en el PATH o en el tipo complejo que contiene al mismo | [optional] 
**service_version** | **str** | Versión del Servicio de la Plataforma con la cual se quiere transaccionar, en caso de no ser especificado será atendido por la última versión del servicio disponible. | [optional] 
**sequence** | **str** | Retornado en todas las respuesta que el POS/PINPAD debe enviar en el próximo requerimiento. En caso de que el POS no lo envíe, envíe vacío o con un valor que no corresponde se produce “La Ruptura de Secuencia” y la plataforma si la última transacción que realizó el POS no esta confirmada y esta Aprobada genera entonces una reversa de la misma. | [optional] 
**security** | [**[SaleObjectSaleSecurity]**](SaleObjectSaleSecurity.md) | Datos asociados a la seguridad de la transacción o de elementos sensibles. | [optional] 
**block** | **str** | ID que identifica a un grupo de transacciones que serán confirmadas o canceladas | [optional] 
**ticket** | **str** | Ticket Digitalizado ( Total o parte del mismo por ejemplo la Firma Digitalizada )    codificado en Base64. | [optional] 
**ticket_answer_key** | **str** | Identificador Unívoco de la Transacción que se quiere Referenciar a la cual pertenece el Ticket Digitalizado. El valor fue obtenido en el campo o elemento AnswerKey de la Respuesta de la transacción referenciada. Si firma fue capturada previamente y se envía en el requerimiento de la misma Operación Sale, Authorize*, Void, Return, Adjustment, DebtPayment o VoidDebtPayment no es necesario que se envíe este elemento o campo. | [optional] 
**required_information** | [**[DebtPaymentObjectDebtPaymentRequiredInformation]**](DebtPaymentObjectDebtPaymentRequiredInformation.md) | En caso de que se requiera información adicional para poder completar la operación, como podrían ser ciertos datos ingresados por el vendedor para realizar verificaciones especificas (como los últimos 4 digitos), el código de seguridad de la tarjeta o la fecha de vencimiento, este elemento estará presente. | [optional] 
**additional_information** | [**[SaleResponseObjectSaleResponseAdditionalInformation]**](SaleResponseObjectSaleResponseAdditionalInformation.md) | En caso de que se requiera información adicional para poder completar la operación, como podrían ser ciertos datos ingresados por el vendedor para realizar verificaciones especificas (como los últimos 4 digitos), el código de seguridad de la tarjeta o la fecha de vencimiento, este elemento estará presente. | [optional] 
**request_key** | **str** | Identificador Privado para ser identificar la transacción a realizar, normalmente es un código a Presentar, solo sera enviado si ya fue creado por un WalletRequest previo y solamente queremos obtener los datos que pudo el Pagador Selecciónar, como el Medio de Pago para poder aplicar una promoción | [optional] 
**merchant_notify_url** | **str** | URL para notificación del comercio | [optional] 
**reference** | **str** | Referencia de la transacción para el punto de venta | [optional] 
**transaction_type** | **str** | Tipo de Transacción (Sale, Void, Return, Authorize,...) por la cual se está realizado el requerimiento (Usado en WalletRequest) | [optional] 
**transaction_description** | **str** | Descripción del tipo de operación que se realizará | [optional] 
**transaction_identification** | **str** | ID de La transacción UNIVOCO para el Punto de venta | [optional] 
**trasaction_date_time** | **str** | Fecha y Hora de la transacción generada por el Punto de Venta - RFC3339 https://xml2rfc.tools.ietf.org/public/rfc/html/rfc3339.html#anchor14 | [optional] 
**transaction_timeout** | **float** | Tiempo en segúndos que la transacción permanecera vigente | [optional] 
**pos_type** | **str** | Tipo de punto de venta. | [optional] 
**pos_version** | **str** | Versión del Aplicativo del punto de Venta. | [optional] 
**pos_address** | **str** | Dirección IP de la Caja o POS. | [optional] 
**pos_serial** | **str** | Número de serie o identificador unívoco del punto de venta. | [optional] 
**posgeo** | **str** | Coordenadas Geográficas del aplicativo de punto de venta | [optional] 
**reading_device_type** | **str** | Tipo de dispositivo utilizado para ingresar los datos de la tarjeta. En función al dispositivo usado, serán realizadas ciertas verificaciones, por lo que ciertos datos serán requeridos. CustomerKeyboard, utilizado para ingreso manual de tarjeta a través de un portal web, por ejemplo - Keyboard, utilizado para ingreso manual de la tarjeta por parte del vendedor - MagneticStripReader, lector de banda de tarjetas por emulación de teclado, u otro valor configurado  que indentifique el dispositivo que se esta utilizando. | [optional] 
**reading_device_operating_from** | **datetime** | Indica desde cuando se encuentra operativo o encendido el dispositivo | [optional] 
**reading_device_version** | **str** | Versión del dispositivo. | [optional] 
**reading_device_address** | **str** | Dirección IP o MAC Address del dispositivo. | [optional] 
**reading_device_serial** | **str** | Número de serie o identificador unívoco del dispositivo. | [optional] 
**reading_device_geo** | **str** | Coordenadas Geograficas del dispositivo de lectura | [optional] 
**user_id** | **str** | Identificador del usuario que está realizando la Transacción. | [optional] 
**user_name** | **str** | Nombre del usuario que está realizando la Transacción. | [optional] 
**currency_code** | **str** | código de Moneda - ISO 4217 &lt;https://en.wikipedia.org/wiki/ISO_4217 Se puede utilizar la Codificación Alfabética o Numérica &lt;br /&gt;   * Num   - Alpha - Description &lt;br /&gt;   * &#39;032&#39; - &#39;ARS&#39; - Pesos Argentinos &lt;br /&gt;   * &#39;152&#39; - &#39;CLP&#39; - Pesos Chilenos &lt;br/&gt;   * &#39;484&#39; - &#39;MXN&#39; - Pesos Mexicanos &lt;br/&gt;   * &#39;840&#39; - &#39;USD&#39; - dólares Americanos &lt;br/&gt;   * &#39;878&#39; - &#39;EUR&#39; - Euros &lt;br/&gt;   * &#39;858&#39; - &#39;UYU&#39; - Pesos Uruguayos &lt;br/&gt;   * &#39;878&#39; - &#39;EUR&#39; - Euros &lt;br/&gt;   * &#39;986&#39; - &#39;BRL&#39; - Real Brasileño | [optional] 
**amount** | **float** | Monto de la transacción a ser enviada | [optional] 
**cashback_amount** | **float** | Monto del dinero en efectivo (cashback). | [optional] 
**tip_amount** | **float** | Importe o Monto de la Propina. | [optional] 
**wallet_identification** | **str** | Identificador del Wallet Retornado por la Operación Wallets | [optional] 
**payer** | [**SaleObjectSalePayer**](SaleObjectSalePayer.md) |  | [optional] 
**customer** | [**SaleObjectSaleCustomer**](SaleObjectSaleCustomer.md) |  | [optional] 
**seller** | [**SaleObjectSaleSeller**](SaleObjectSaleSeller.md) |  | [optional] 
**products** | [**[SaleResponseObjectSaleResponseProducts]**](SaleResponseObjectSaleResponseProducts.md) | Detalle de Productos de la Operación. | [optional] 
**tax_refund_type** | **str** | Esquema de Devolución de Impuestos a utilizar en la transacción | [optional] 
**valid_thru** | **datetime** | Fecha y Hora de fin de validez de La transacción - RFC3339 https://xml2rfc.tools.ietf.org/public/rfc/html/rfc3339.html#anchor14 | [optional] 
**payment_facilitator_id** | **str** | Identificador de facilitador de pagos o Payfac. | [optional] 
**merchant_id** | **str** | Número de comercio utilizado para realizar la transacción. Este Número es asignado por el host, y parametrizado en la BD, relacionado a cada uno de los planes disponibles. | [optional] 
**terminal_id** | **str** | Identificador de Terminal por el cual se envía la Transacción al Host. | [optional] 
**terminal_trace** | **int** | Número de Trace/Secuencia que genera la plataforma para la transacción asociado al TerminalID. | [optional] 
**settlement_batch_number** | **int** | Para aquellos host que exista el concepto de lote, es el número de lote al cual pertenece la transacción. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


