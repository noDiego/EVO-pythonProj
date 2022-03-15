# KeysRenewalObjectKeysRenewal


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_identification** | **str** | Identificador de la Compañía para la Plataforma de Integración. | 
**system_identification** | **str** | Identificador de Aplicativo para la Plataforma de Integración que usa la Compañía especificada. | 
**branch_identification** | **str** | Identificador de Aplicativo para la Plataforma de Integración que usa la Compañía especificada. | [optional] 
**pos_identification** | **str** | Identificador del Punto de Venta/POS/Caja que pertenece a la sucursal y companía especificada. | [optional] 
**request_type** | **str** | Tipo de Operación que se está requiriendo, solo necesario sobre formatos que no soportan elementos complejos o compuestos. | [optional] 
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
**reading_device_geo** | **str** | Coordenadas Geográficas del dispositivo de lectura | [optional] 
**user_id** | **str** | Identificador del usuario que está realizando la Transacción. | [optional] 
**user_name** | **str** | Nombre del usuario que está realizando la Transacción. | [optional] 
**timeout** | **float** | Tiempo de espera que el POS espera al PINPAD para obtener la respuesta al requerimiento.  | [optional] 
**ticket** | **str** | Ticket Digitalizado ( Total o parte del mismo por ejemplo la Firma Digitalizada )    codificado en Base64. | [optional] 
**ticket_answer_key** | **str** | Identificador Unívoco de la Transacción que se quiere Referenciar a la cual pertenece el Ticket Digitalizado. El valor fue obtenido en el campo o elemento AnswerKey de la Respuesta de la transacción referenciada. Si la firma fue capturada previamente y se envía en el requerimiento de la misma Operación Sale, Authorize*, Void, Return, Adjustment, DebtPayment, VoidDebtPayment o Enrollment no es necesario que se envíe este elemento o campo. | [optional] 
**service_version** | **str** | Versión del Servicio de la Plataforma con la cual se quiere transaccionar, en caso de no ser especificado será atendido por la última versión del servicio disponible. | [optional] 
**sequence** | **str** | Retornado en todas las respuesta que el POS/PINPAD debe enviar en el próximo requerimiento. En caso de que el POS no lo envíe, envíe vacío o con un valor que no corresponde se produce “La Ruptura de Secuencia” y la plataforma, si la última transacción que realizó el POS no está confirmada y está aprobada, genera una reversa de la misma. | [optional] 
**required_information** | [**[SaleObjectSaleRequiredInformation]**](SaleObjectSaleRequiredInformation.md) | En caso de que se requiera información adicional para poder completar la operación, como podrían ser ciertos datos ingresados por el vendedor para realizar verificaciones especificas (como los últimos 4 digitos), el código de seguridad de la tarjeta o la fecha de vencimiento, este elemento estará presente. | [optional] 
**block** | **str** | ID que identifica a un grupo de transacciones que serán confirmadas o canceladas. | [optional] 
**products** | [**[SaleObjectSaleProducts]**](SaleObjectSaleProducts.md) | Detalle de Productos de la Operación. | [optional] 
**payment_facilitator_id** | **str** | Identificador de facilitador de pagos o Payfac. | [optional] 
**merchant_id** | **str** | Número de comercio utilizado para realizar la transacción. Este Número es asignado por el host, y parametrizado en la BD, relacionado a cada uno de los planes disponibles. | [optional] 
**terminal_id** | **str** | Identificador de Terminal por el cual se envía la Transacción al Host. | [optional] 
**terminal_trace** | **int** | Número de Trace/Secuencia que genera la plataforma para la transacción asociado al TerminalID. | [optional] 
**configuration** | [**SaleResponseObjectSaleResponseConfiguration**](SaleResponseObjectSaleResponseConfiguration.md) |  | [optional] 
**settlement_batch_number** | **int** | Para aquellos host que exista el concepto de lote, es el número de lote al cual pertenece la transacción. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


