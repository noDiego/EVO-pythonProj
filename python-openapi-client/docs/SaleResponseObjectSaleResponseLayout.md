# SaleResponseObjectSaleResponseLayout


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute** | **[str]** | Posibles atributos de impresión que se aplicarán en el Data. En caso de no estar presente el elemento se imprime el texto en el tamaño predefinido como normal y con justificación a la izquierda (LeftJustified). | [optional] 
**content_type** | **str** | En caso de no estar presente el elemento se asume que el elemento Data contiene texto plano (Text). Para el caso de Template los TAG o  elementos a tratar estan deliminatos por _$ y $_ quedando de la siguiente forma _$ElementName$_. Donde ElementName es el nombre del campo/elemento que deben incluir en el mismo. Ejemplo: Si el dispositivo recibe _$Ticket$_, reemplazara este indicaror por la Firma o Ticket Digitalizado. | [optional] 
**encode_type** | **str** | Tipo de codificación de los datos. En caso de no estar presente el elemento se asume que el elemento Data está codificado como Plain. | [optional] 
**data** | **str** | Dato a imprimir codificado según los valores presentes en ContentType y EncodeType. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


