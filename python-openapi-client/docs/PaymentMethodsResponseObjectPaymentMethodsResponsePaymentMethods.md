# PaymentMethodsResponseObjectPaymentMethodsResponsePaymentMethods


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID interno en la base de datos para este metodo de pago | [optional] 
**foreign_identifier** | **str** | ID externo de este metodo de pago, utilizado por el punto de venta para reconocer al medio de pago en su base de datos | [optional] 
**image** | **str** | Nombre de la Imagen o Logo o la imagen codificado en base64 | [optional] 
**large_image** | **str** | Nombre de la Imagen o Logo o la imagen codificado en base64 | [optional] 
**small_image** | **str** | Nombre de la Imagen o Logo o la imagen codificado en base64 | [optional] 
**card_number_max_length** | **int** | Longitud máxima del Número de tarjeta de este medio de pago | [optional] 
**card_number_min_length** | **int** | Longitud mínima del Número de tarjeta de este medio de pago | [optional] 
**security_code_max_length** | **int** | Longitud máxima del código de seguridad de tarjeta de este medio de pago | [optional] 
**security_code_min_length** | **int** | Longitud mínima del código de seguridad de tarjeta de este medio de pago | [optional] 
**description** | **str** | LIena que describe al metodo de pago | [optional] 
**type** | [**PaymentMethodsResponseObjectPaymentMethodsResponseType**](PaymentMethodsResponseObjectPaymentMethodsResponseType.md) |  | [optional] 
**category** | [**PaymentMethodsResponseObjectPaymentMethodsResponseCategory**](PaymentMethodsResponseObjectPaymentMethodsResponseCategory.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


