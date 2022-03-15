# ConfigureObjectConfigureFiles

Cada objetorepresenta un archivo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identificador del archivo | [optional] 
**description** | **str** | Decripción | [optional] 
**type** | **str** | Tipo de archivo | [optional] 
**path** | **str** | Lugar donde el archivo se encuentra o sebe alojarse | [optional] 
**version** | **str** | Version del archivo | [optional] 
**attributes** | **str** | Atributos del archivo | [optional] 
**data** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | contenido del archivo, codificado en Base64 | [optional] 
**effective_from** | **datetime** | Fecha y hora de a partir de la cual este archivo entra en vigencia - RFC3339 https://xml2rfc.tools.ietf.org/public/rfc/html/rfc3339.html#anchor14 | [optional] 
**effective_to** | **datetime** | Fecha y hora de a partir de la cual este archivo entra en vigencia - RFC3339 https://xml2rfc.tools.ietf.org/public/rfc/html/rfc3339.html#anchor14 | [optional] 
**time_of_life** | **int** | Timeout de vida  para dicha tabla expresado en milisegúndos | [optional] 
**time_of_life_offline** | **int** | Timeout de vida  para dicha tabla expresado en milisegúndos para el caso de que el POS o dispositivo se encuentre fuera de línea de la plataforma | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


