# ConfigureObjectConfigureOperations

Cada objetorepresenta un tipo de Operación/transacción

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identificador de tipo de Operación, Ej Sale | [optional] 
**description** | **str** | Descripción de la Operación | [optional] 
**request** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Especificación del requerimiento | [optional] 
**answer** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Especificación de la respuesta | [optional] 
**default_timeout** | **int** | Timeout por default para dicha operación expresado en milisegúndos | [optional] 
**version** | **str** | Versión de la transacción | [optional] 
**effective_from** | **datetime** | Fecha y hora de a partir de la cual este archivo entra en vigencia - RFC3339 https://xml2rfc.tools.ietf.org/public/rfc/html/rfc3339.html#anchor14 | [optional] 
**effective_to** | **datetime** | Fecha y hora de a partir de la cual este archivo entra en vigencia - RFC3339 https://xml2rfc.tools.ietf.org/public/rfc/html/rfc3339.html#anchor14 | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


