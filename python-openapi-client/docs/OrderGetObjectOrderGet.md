# OrderGetObjectOrderGet


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**initial_token** | **str** | . | 
**service_version** | **str** | Versión del Servicio de la Plataforma con la cual se quiere transaccionar, en caso de no ser especificado será atendido por la última versión del servicio disponible. | [optional] 
**sequence** | **str** | Retornado en todas las respuesta que el POS/PINPAD debe enviar en el próximo requerimiento. En caso de que el POS no lo envíe, envíe vacío o con un valor que no corresponde se produce “La Ruptura de Secuencia” y la plataforma si la última transacción que realizó el POS no esta confirmada y esta Aprobada genera entonces una reversa de la misma. | [optional] 
**security** | [**[SaleObjectSaleSecurity]**](SaleObjectSaleSecurity.md) | Datos asociados a la seguridad de la transacción o de elementos sensibles. | [optional] 
**payment_facilitator_id** | **str** | Identificador de facilitador de pagos o Payfac. | [optional] 
**merchant_id** | **str** | Número de comercio utilizado para realizar la transacción. Este Número es asignado por el host, y parametrizado en la BD, relacionado a cada uno de los planes disponibles. | [optional] 
**terminal_id** | **str** | Identificador de Terminal por el cual se envía la Transacción al Host. | [optional] 
**terminal_trace** | **int** | Número de Trace/Secuencia que genera la plataforma para la transacción asociado al TerminalID. | [optional] 
**settlement_batch_number** | **int** | Para aquellos host que exista el concepto de lote, es el número de lote al cual pertenece la transacción. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


