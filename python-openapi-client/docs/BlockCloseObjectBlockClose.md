# BlockCloseObjectBlockClose


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_identification** | **str** | Identificador de la Compañía para la Plataforma de Integración. | 
**system_identification** | **str** | Identificador de Aplicativo para la Plataforma de Integración que usa la Compañía especificada. | 
**block** | **str** | ID que identifica a un grupo de transacciones que serán confirmadas o canceladas | 
**branch_identification** | **str** | Identificador de Aplicativo para la Plataforma de Integración que usa la Compañía especificada. | [optional] 
**pos_identification** | **bool, date, datetime, dict, float, int, list, str, none_type** | Identificador del Punto de Venta/POS/Caja que pertenece a la sucursal y companía especificada. | [optional] 
**request_type** | **str** | Tipo de Operación que se está requiriendo, solo necesario sobre formatos que no soportan elementos complejos o compuestos. | [optional] 
**service_version** | **str** | Versión del Servicio de la Plataforma con la cual se quiere transaccionar, en caso de no ser especificado será atendido por la última versión del servicio disponible. | [optional] 
**sequence** | **str** | Retornado en todas las respuesta que el POS/PINPAD debe enviar en el próximo requerimiento. En caso de que el POS no lo envíe, envíe vacío o con un valor que no corresponde se produce “La Ruptura de Secuencia” y la plataforma si la última transacción que realizó el POS no esta confirmada y esta Aprobada genera entonces una reversa de la misma. | [optional] 
**security** | [**[SaleObjectSaleSecurity]**](SaleObjectSaleSecurity.md) | Datos asociados a la seguridad de la transacción o de elementos sensibles. | [optional] 
**ticket** | **str** | Ticket Digitalizado ( Total o parte del mismo por ejemplo la Firma Digitalizada )    codificado en Base64. | [optional] 
**ticket_answer_key** | **str** | Identificador Unívoco de la Transacción que se quiere Referenciar a la cual pertenece el Ticket Digitalizado. El valor fue obtenido en el campo o elemento AnswerKey de la Respuesta de la transacción referenciada. Si firma fue capturada previamente y se envía en el requerimiento de la misma Operación Sale, Authorize*, Void, Return, Adjustment, DebtPayment o VoidDebtPayment no es necesario que se envíe este elemento o campo. | [optional] 
**request_key** | **str** | Identificador del Requermiento obtenido en la respuesta de la operación WalletRequest.             | [optional] 
**reason_sequence_break** | **str** | Motivo por el cual se requiere romper la secuencia. | [optional] 
**pos_type** | **str** | Tipo de punto de venta. | [optional] 
**pos_version** | **str** | Versión del Aplicativo del punto de Venta. | [optional] 
**pos_address** | **str** | Dirección IP de la Caja o POS. | [optional] 
**pos_serial** | **str** | Número de serie o identificador unívoco del punto de venta. | [optional] 
**posgeo** | **str** | Coordenadas Geográficas del aplicativo de punto de venta | [optional] 
**reading_device_version** | **str** | Versión del dispositivo. | [optional] 
**reading_device_type** | **str** | Tipo de dispositivo utilizado para ingresar los datos de la tarjeta. En función al dispositivo usado, serán realizadas ciertas verificaciones, por lo que ciertos datos serán requeridos. CustomerKeyboard, utilizado para ingreso manual de tarjeta a través de un portal web, por ejemplo - Keyboard, utilizado para ingreso manual de la tarjeta por parte del vendedor - MagneticStripReader, lector de banda de tarjetas por emulación de teclado, u otro valor configurado  que indentifique el dispositivo que se esta utilizando. | [optional] 
**reading_device_operating_from** | **datetime** | Indica desde cuando se encuentra operativo o encendido el dispositivo | [optional] 
**reading_device_serial** | **str** | Número de serie o identificador unívoco del dispositivo. | [optional] 
**reading_device_geo** | **str** | Coordenadas Geograficas del dispositivo de lectura | [optional] 
**reading_device_address** | **str** | Dirección IP o MAC Address del dispositivo. | [optional] 
**user_id** | **str** | Identificador del usuario que está realizando la Transacción. | [optional] 
**user_name** | **str** | Nombre del usuario que está realizando la Transacción. | [optional] 
**foreign_block** | **str** | Identificador Alternativo de un  Bloque Que se informa en las operaciones BlockCancel o BlockClose. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


