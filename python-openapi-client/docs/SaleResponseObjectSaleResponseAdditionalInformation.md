# SaleResponseObjectSaleResponseAdditionalInformation


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Nombre del dato a solicitar | [optional] 
**type** | **str** | Tipo de dato a solicitar | [optional] 
**interpret_for** | **str** | Este elemento se le solicita al POS o el dispositivo de venta/ReadingDevice.  En caso de que se requiera RequieredInformation y no esté definida esta propiedad  se debe asumir que es para el POS. | [optional] 
**ui_type** | **str** | Tipo de elemento a utilizar para su representación en la Interfaz de Usuario ( Button, etc ) | [optional] 
**ui_attributes** | **str** | Atributos de Forma, font, color, etc necesarios por el aplicativo | [optional] 
**value** | **str** | Valor del Elemento Adicional Solicitado | [optional] 
**label** | **str** | Leyenda a mostrar en pantalla para el dato a solicitar | [optional] 
**min_length** | **int** | Longitud mínima del dato a solicitar | [optional] 
**max_length** | **int** | Longitud máxima del dato a solicitar | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


