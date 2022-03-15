# openapi_client.PaymentApi

All URIs are relative to *https://testcodi.multipay.mx:30801/Payments/Authorize/5.6.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authorize_sale_post**](PaymentApi.md#authorize_sale_post) | **POST** /AuthorizeSale | Autorización de Venta sin Captura o Pre Autorización
[**balance_inquiry_post**](PaymentApi.md#balance_inquiry_post) | **POST** /BalanceInquiry | Consulta de Saldo/Deuda de cuenta/Credencial
[**block_cancel_post**](PaymentApi.md#block_cancel_post) | **POST** /BlockCancel | Cancelación del último bloque de transacciones realizadas.
[**block_close_post**](PaymentApi.md#block_close_post) | **POST** /BlockClose | Confirmación del último bloque de transacciones realizadas.
[**block_create_post**](PaymentApi.md#block_create_post) | **POST** /BlockCreate | Crea un Identificador de Bloque-Block de transacciones.
[**cancel_post**](PaymentApi.md#cancel_post) | **POST** /Cancel | Cancela una Transacción en Curso, Inciada con un GetCard/WalletRequest.
[**capture_post**](PaymentApi.md#capture_post) | **POST** /Capture | Confirmación de un consumo previo.
[**close_post**](PaymentApi.md#close_post) | **POST** /Close | Utilizada por el POS para indicar que finalizo su sesion.
[**configure_post**](PaymentApi.md#configure_post) | **POST** /Configure | Permite crear configuración en Plataforma
[**confirm_post**](PaymentApi.md#confirm_post) | **POST** /Confirm | Confirmación de la última operación realizada.
[**debt_inquiry_post**](PaymentApi.md#debt_inquiry_post) | **POST** /DebtInquiry | Consulta de Deuda de cuenta/credencial
[**debt_payment_post**](PaymentApi.md#debt_payment_post) | **POST** /DebtPayment | Pago de Deuda, Resumen de Cuenta o Saldo.
[**deposit_post**](PaymentApi.md#deposit_post) | **POST** /Deposit | Confirmación de un consumo previo.
[**enable_service_post**](PaymentApi.md#enable_service_post) | **POST** /EnableService | Permite Habilitar el uso de un Servicio
[**enrollment_post**](PaymentApi.md#enrollment_post) | **POST** /Enrollment | Suscripción al servicio de pagos Tokenizados y pagos recurrentes.
[**get_block_post**](PaymentApi.md#get_block_post) | **POST** /GetBlock | Recupera los identificadores de las transacciones que  lo componen.
[**get_card_post**](PaymentApi.md#get_card_post) | **POST** /GetCard | Solicitud de Lectura del Medio de Pago
[**get_transaction_post**](PaymentApi.md#get_transaction_post) | **POST** /GetTransaction | Recupera los datos de la transacción especificada. 
[**keep_alive_post**](PaymentApi.md#keep_alive_post) | **POST** /KeepAlive | Mensaje que informa si está disponible el Servicio Authorize.
[**keys_renewal_post**](PaymentApi.md#keys_renewal_post) | **POST** /KeysRenewal | Renovacion de Llaves
[**order_final_post**](PaymentApi.md#order_final_post) | **POST** /OrderFinal | Reclamar el estatus de la operación de compra.
[**order_get_post**](PaymentApi.md#order_get_post) | **POST** /OrderGet | Recuperar la operación iniciada por el comercio, para su compra.
[**order_initial_post**](PaymentApi.md#order_initial_post) | **POST** /OrderInitial | Indica el inicio de una operación de venta.
[**order_status_post**](PaymentApi.md#order_status_post) | **POST** /OrderStatus | Recuperación del Estado de una Transacción Iniciada por el OrderInitial.
[**payment_method_post**](PaymentApi.md#payment_method_post) | **POST** /PaymentMethod | Consulta de  \&quot;planes\&quot; financieros para un Medio de Pago.
[**payment_methods_post**](PaymentApi.md#payment_methods_post) | **POST** /PaymentMethods | Consulta de los Medios de Pago  disponibles.
[**query_companies_post**](PaymentApi.md#query_companies_post) | **POST** /QueryCompanies | Consulta de Empresas para el Pago de Servicios o Deuda
[**query_line_of_business_post**](PaymentApi.md#query_line_of_business_post) | **POST** /QueryLineOfBusiness | Consulta de Rubros de Empresas para el Pago de Servicios o Deuda
[**return_post**](PaymentApi.md#return_post) | **POST** /Return | Realización de una devolución de operación de compra/autorización.
[**sale_post**](PaymentApi.md#sale_post) | **POST** /Sale | Realización de una compra/Autorización de compra
[**settlement_post**](PaymentApi.md#settlement_post) | **POST** /Settlement | Confirmación de un consumo previo.
[**validate_post**](PaymentApi.md#validate_post) | **POST** /Validate | Realización de una Validación
[**void_debt_payment_post**](PaymentApi.md#void_debt_payment_post) | **POST** /VoidDebtPayment | Cancelación de  Pago de Deuda, Saldo o Resumen.
[**void_post**](PaymentApi.md#void_post) | **POST** /Void | Operación de Cancelación/Anulación.
[**wallet_request_post**](PaymentApi.md#wallet_request_post) | **POST** /WalletRequest | Inicia un transacción contra el Wallet
[**wallets_post**](PaymentApi.md#wallets_post) | **POST** /Wallets | Obtiene la Lista de Wallets Disponibles


# **authorize_sale_post**
> AuthorizeSaleResponseObject authorize_sale_post(authorize_sale_object)

Autorización de Venta sin Captura o Pre Autorización

Si se desea enviar una compra/autorización, se deberá enviar una petición a este endpoint con los datos requeridos a continuación.

### Example


```python
import time
import openapi_client
from openapi_client.api import payment_api
from openapi_client.model.authorize_sale_response_object import AuthorizeSaleResponseObject
from openapi_client.model.authorize_sale_object import AuthorizeSaleObject
from pprint import pprint
# Defining the host is optional and defaults to https://testcodi.multipay.mx:30801/Payments/Authorize/5.6.1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://testcodi.multipay.mx:30801/Payments/Authorize/5.6.1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = payment_api.PaymentApi(api_client)
    authorize_sale_object = AuthorizeSaleObject(
        authorize_sale=AuthorizeSaleObjectAuthorizeSale(
            company_identification="company_identification_example",
            system_identification="system_identification_example",
            branch_identification="branch_identification_example",
            pos_identification="pos_identification_example",
            request_type="request_type_example",
            request_key="request_key_example",
            service_version="service_version_example",
            sequence="sequence_example",
            security=[
                SaleObjectSaleSecurity(
                    type="type_example",
                    values=[
                        SaleObjectSaleValues(
                            name="name_example",
                            value=None,
                        ),
                    ],
                ),
            ],
            block="block_example",
            required_information=[
                SaleObjectSaleRequiredInformation(
                    name="name_example",
                    type="STRING",
                    interpret_for="POS",
                    it_is_defined=True,
                    ui_type="ui_type_example",
                    ui_attributes="ui_attributes_example",
                    value="value_example",
                    label="label_example",
                    min_length=1,
                    max_length=1,
                    validation_expression_type="regex",
                    validation_expression="validation_expression_example",
                    mandatory=True,
                ),
            ],
            ticket="ticket_example",
            ticket_answer_key="ticket_answer_key_example",
            timeout=3.14,
            merchant_notify_url="merchant_notify_url_example",
            is_reverse=3.14,
            reason_reverse="TIMEOUT",
            reason_sequence_break="TIMEOUT",
            reference="reference_example",
            transaction_description="transaction_description_example",
            pos_type="pos_type_example",
            pos_version="pos_version_example",
            pos_address="pos_address_example",
            pos_serial="pos_serial_example",
            posgeo="posgeo_example",
            reading_device_type="reading_device_type_example",
            reading_device_operating_from=dateutil_parser('1970-01-01T00:00:00.00Z'),
            reading_device_version="reading_device_version_example",
            reading_device_address="reading_device_address_example",
            reading_device_serial="reading_device_serial_example",
            reading_device_geo="reading_device_geo_example",
            user_id="user_id_example",
            user_name="user_name_example",
            amount=3.14,
            alternative_amount=3.14,
            cashback_amount=3.14,
            tip_amount=3.14,
            promoted_amount=3.14,
            currency_code="484",
            facility_payments=3.14,
            facility_type="facility_type_example",
            plan="plan_example",
            card_read_mode="B",
            card_get_mode="card_get_mode_example",
            card_number="card_number_example",
            card_number_masked="card_number_masked_example",
            card_number_encrypted="card_number_encrypted_example",
            card_exp="card_exp_example",
            card_cryptogram="card_cryptogram_example",
            card_app_name="card_app_name_example",
            card_app_identifier="card_app_identifier_example",
            card_app_label="card_app_label_example",
            card_auth_request_cryptogram="card_auth_request_cryptogram_example",
            card_auth_response_cryptogram="card_auth_response_cryptogram_example",
            track1="track1_example",
            track2="track2_example",
            input_tokens=[
                SaleObjectSaleInputTokens(
                    name="name_example",
                    value="value_example",
                ),
            ],
            security_code="security_code_example",
            pin="pin_example",
            credential_token="credential_token_example",
            credential_issuer_token="credential_issuer_token_example",
            payer=SaleObjectSalePayer(
                identification="identification_example",
                identification_type="PAS",
                email="email_example",
                document_type="PAS",
                document_number="document_number_example",
                first_name="first_name_example",
                last_name="last_name_example",
                middle_name="middle_name_example",
                abbreviated_name="abbreviated_name_example",
                phone="phone_example",
                zip_code="zip_code_example",
                address_street="address_street_example",
                address_number="address_number_example",
                address_internal="address_internal_example",
                address_suburb="address_suburb_example",
                address_delegation="address_delegation_example",
                city="city_example",
                state="state_example",
                country="country_example",
                category_code=1,
                tax_category_type="tax_category_type_example",
                tax_identification_type="tax_identification_type_example",
                tax_identification="tax_identification_example",
                notify_url="notify_url_example",
            ),
            customer=SaleObjectSaleCustomer(
                identification="identification_example",
                identification_type="PAS",
                email="email_example",
                document_type="PAS",
                document_number="document_number_example",
                first_name="first_name_example",
                last_name="last_name_example",
                middle_name="middle_name_example",
                abbreviated_name="abbreviated_name_example",
                phone="phone_example",
                zip_code="zip_code_example",
                address_street="address_street_example",
                address_number="address_number_example",
                address_internal="address_internal_example",
                address_suburb="address_suburb_example",
                address_delegation="address_delegation_example",
                city="city_example",
                state="state_example",
                country="country_example",
                category_code=1,
                tax_category_type="tax_category_type_example",
                tax_identification_type="tax_identification_type_example",
                tax_identification="tax_identification_example",
                notify_url="notify_url_example",
            ),
            seller=SaleObjectSaleSeller(
                identification="identification_example",
                identification_type="PAS",
                email="email_example",
                document_type="PAS",
                document_number="document_number_example",
                first_name="first_name_example",
                last_name="last_name_example",
                middle_name="middle_name_example",
                abbreviated_name="abbreviated_name_example",
                phone="phone_example",
                zip_code="zip_code_example",
                address_street="address_street_example",
                address_number="address_number_example",
                address_internal="address_internal_example",
                address_suburb="address_suburb_example",
                address_delegation="address_delegation_example",
                city="city_example",
                state="state_example",
                country="country_example",
                category_code=1,
                tax_category_type="tax_category_type_example",
                tax_identification_type="tax_identification_type_example",
                tax_identification="tax_identification_example",
                notify_url="notify_url_example",
            ),
            products=[
                SaleObjectSaleProducts(
                    item=1,
                    name="name_example",
                    code="code_example",
                    quantity=3.14,
                    unit="unit_example",
                    unit_amount=3.14,
                    net_amount=3.14,
                    tax_amount=3.14,
                    total_amount=3.14,
                ),
            ],
            tax_refund_type="tax_refund_type_example",
            auth_code="auth_code_example",
            payment_facilitator_id="payment_facilitator_id_example",
            merchant_id="merchant_id_example",
            terminal_id="terminal_id_example",
            terminal_trace=1,
            settlement_batch_number=1,
        ),
    ) # AuthorizeSaleObject | Elementos o Atributos que componen el requerimiento de una transacción, los atributos condicionales y/o opcionales que no sean requeridos para esta transacción no deberán ser enviados.

    # example passing only required values which don't have defaults set
    try:
        # Autorización de Venta sin Captura o Pre Autorización
        api_response = api_instance.authorize_sale_post(authorize_sale_object)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PaymentApi->authorize_sale_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorize_sale_object** | [**AuthorizeSaleObject**](AuthorizeSaleObject.md)| Elementos o Atributos que componen el requerimiento de una transacción, los atributos condicionales y/o opcionales que no sean requeridos para esta transacción no deberán ser enviados. |

### Return type

[**AuthorizeSaleResponseObject**](AuthorizeSaleResponseObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Elementos o Atributos que componen la respuesta a la transacción requerida.  |  -  |
**400** | Bad request. |  -  |
**401** | Authorization information is missing or invalid. |  -  |
**404** | Not Found. |  -  |
**405** | Invalid Method. |  -  |
**500** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **balance_inquiry_post**
> BalanceInquiryResponseObject balance_inquiry_post(balance_inquiry_object)

Consulta de Saldo/Deuda de cuenta/Credencial

Consulta de saldo, deuda de la cuenta asociada a la credencial o método de identificación utilizado.

### Example


```python
import time
import openapi_client
from openapi_client.api import payment_api
from openapi_client.model.balance_inquiry_response_object import BalanceInquiryResponseObject
from openapi_client.model.balance_inquiry_object import BalanceInquiryObject
from pprint import pprint
# Defining the host is optional and defaults to https://testcodi.multipay.mx:30801/Payments/Authorize/5.6.1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://testcodi.multipay.mx:30801/Payments/Authorize/5.6.1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = payment_api.PaymentApi(api_client)
    balance_inquiry_object = BalanceInquiryObject(
        balance_inquiry=BalanceInquiryObjectBalanceInquiry(
            company_identification="company_identification_example",
            system_identification="system_identification_example",
            branch_identification="branch_identification_example",
            pos_identification="pos_identification_example",
            service_version="service_version_example",
            sequence="sequence_example",
            security=[
                SaleObjectSaleSecurity(
                    type="type_example",
                    values=[
                        SaleObjectSaleValues(
                            name="name_example",
                            value=None,
                        ),
                    ],
                ),
            ],
            block="block_example",
            reason_sequence_break="TIMEOUT",
            reading_device_type="reading_device_type_example",
            card_app_name="card_app_name_example",
            card_app_identifier="card_app_identifier_example",
            card_app_label="card_app_label_example",
            card_auth_request_cryptogram="card_auth_request_cryptogram_example",
            card_auth_response_cryptogram="card_auth_response_cryptogram_example",
            card_read_mode="B",
            card_get_mode="card_get_mode_example",
            card_number="card_number_example",
            card_number_masked="card_number_masked_example",
            card_exp="card_exp_example",
            track1="track1_example",
            track2="track2_example",
            input_tokens=[
                SaleObjectSaleInputTokens(
                    name="name_example",
                    value="value_example",
                ),
            ],
            security_code="security_code_example",
            pin="pin_example",
            card_last_four_digits="card_last_four_digits_example",
            payer=SaleObjectSalePayer(
                identification="identification_example",
                identification_type="PAS",
                email="email_example",
                document_type="PAS",
                document_number="document_number_example",
                first_name="first_name_example",
                last_name="last_name_example",
                middle_name="middle_name_example",
                abbreviated_name="abbreviated_name_example",
                phone="phone_example",
                zip_code="zip_code_example",
                address_street="address_street_example",
                address_number="address_number_example",
                address_internal="address_internal_example",
                address_suburb="address_suburb_example",
                address_delegation="address_delegation_example",
                city="city_example",
                state="state_example",
                country="country_example",
                category_code=1,
                tax_category_type="tax_category_type_example",
                tax_identification_type="tax_identification_type_example",
                tax_identification="tax_identification_example",
                notify_url="notify_url_example",
            ),
            customer=SaleObjectSaleCustomer(
                identification="identification_example",
                identification_type="PAS",
                email="email_example",
                document_type="PAS",
                document_number="document_number_example",
                first_name="first_name_example",
                last_name="last_name_example",
                middle_name="middle_name_example",
                abbreviated_name="abbreviated_name_example",
                phone="phone_example",
                zip_code="zip_code_example",
                address_street="address_street_example",
                address_number="address_number_example",
                address_internal="address_internal_example",
                address_suburb="address_suburb_example",
                address_delegation="address_delegation_example",
                city="city_example",
                state="state_example",
                country="country_example",
                category_code=1,
                tax_category_type="tax_category_type_example",
                tax_identification_type="tax_identification_type_example",
                tax_identification="tax_identification_example",
                notify_url="notify_url_example",
            ),
            payment_facilitator_id="payment_facilitator_id_example",
            merchant_id="merchant_id_example",
            terminal_id="terminal_id_example",
            terminal_trace=1,
            settlement_batch_number=1,
        ),
    ) # BalanceInquiryObject | Elementos o Atributos que componen el requerimiento de una transacción, los atributos condicionales y/o opcionales que no sean requeridos para esta transacción no deberán ser enviados.

    # example passing only required values which don't have defaults set
    try:
        # Consulta de Saldo/Deuda de cuenta/Credencial
        api_response = api_instance.balance_inquiry_post(balance_inquiry_object)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PaymentApi->balance_inquiry_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **balance_inquiry_object** | [**BalanceInquiryObject**](BalanceInquiryObject.md)| Elementos o Atributos que componen el requerimiento de una transacción, los atributos condicionales y/o opcionales que no sean requeridos para esta transacción no deberán ser enviados. |

### Return type

[**BalanceInquiryResponseObject**](BalanceInquiryResponseObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Elementos o Atributos que componen la respuesta a la transacción requerida.  |  -  |
**400** | Bad request. |  -  |
**401** | Authorization information is missing or invalid. |  -  |
**404** | Not Found. |  -  |
**405** | Invalid Method. |  -  |
**500** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **block_cancel_post**
> BlockCancelResponseObject block_cancel_post(block_cancel_object)

Cancelación del último bloque de transacciones realizadas.

Luego de realizar una serie de operaciones de compra/autorización, anulación y/o devolución, y haber procesado correctamente cada una de las respuestas, estas operaciones se realizaron con esta funcionalidad activada (es decir, enviando un Número de bloque a la cual asociar estas operaciones), se debe enviar una confirmación, para asi eliminar las reversas que se encuentran pendientes de envio en caso de que el punto de venta decida deshacer la venta completa por el motivo que sea, o una cancelación, para asi enviar esas reversas pendientes y asi deshacerlas por completo. Si el punto de venta envia un nuevo Número de bloque confirmar o cancelar previamente el anterior, la Plataforma procederá a confirmar o cancelar automaticamente el bloque de transacciones pendientes, según como haya sido configurado para actuar en este escenario.

### Example


```python
import time
import openapi_client
from openapi_client.api import payment_api
from openapi_client.model.block_cancel_response_object import BlockCancelResponseObject
from openapi_client.model.block_cancel_object import BlockCancelObject
from pprint import pprint
# Defining the host is optional and defaults to https://testcodi.multipay.mx:30801/Payments/Authorize/5.6.1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://testcodi.multipay.mx:30801/Payments/Authorize/5.6.1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = payment_api.PaymentApi(api_client)
    block_cancel_object = BlockCancelObject(
        block_cancel=BlockCancelObjectBlockCancel(
            company_identification="company_identification_example",
            system_identification="system_identification_example",
            branch_identification="branch_identification_example",
            pos_identification=None,
            request_type="request_type_example",
            service_version="service_version_example",
            sequence="sequence_example",
            security=[
                SaleObjectSaleSecurity(
                    type="type_example",
                    values=[
                        SaleObjectSaleValues(
                            name="name_example",
                            value=None,
                        ),
                    ],
                ),
            ],
            block="block_example",
            ticket="ticket_example",
            ticket_answer_key="ticket_answer_key_example",
            request_key="request_key_example",
            reason_sequence_break="TIMEOUT",
            pos_type="pos_type_example",
            pos_version="pos_version_example",
            pos_address="pos_address_example",
            pos_serial="pos_serial_example",
            posgeo="posgeo_example",
            reading_device_version="reading_device_version_example",
            reading_device_type=None,
            reading_device_operating_from=dateutil_parser('1970-01-01T00:00:00.00Z'),
            reading_device_serial="reading_device_serial_example",
            reading_device_geo="reading_device_geo_example",
            reading_device_address="reading_device_address_example",
            user_id="user_id_example",
            user_name="user_name_example",
            foreign_block="foreign_block_example",
        ),
    ) # BlockCancelObject | Elementos o Atributos que componen el requerimiento de una transacción, los atributos condicionales y/o opcionales que no sean requeridos para esta transacción no deberán ser enviados.

    # example passing only required values which don't have defaults set
    try:
        # Cancelación del último bloque de transacciones realizadas.
        api_response = api_instance.block_cancel_post(block_cancel_object)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PaymentApi->block_cancel_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **block_cancel_object** | [**BlockCancelObject**](BlockCancelObject.md)| Elementos o Atributos que componen el requerimiento de una transacción, los atributos condicionales y/o opcionales que no sean requeridos para esta transacción no deberán ser enviados. |

### Return type

[**BlockCancelResponseObject**](BlockCancelResponseObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Elementos o Atributos que componen la respuesta a la transacción requerida.  |  -  |
**400** | Bad request. |  -  |
**401** | Authorization information is missing or invalid. |  -  |
**404** | Not Found. |  -  |
**405** | Invalid Method. |  -  |
**500** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **block_close_post**
> BlockCloseResponseObject block_close_post(block_close_object)

Confirmación del último bloque de transacciones realizadas.

Luego de realizar una serie de operaciones de compra/autorización, anulación y/o devolución, y haber procesado correctamente cada una de las respuestas, estas operaciones se realizaron con esta funcionalidad activada (es decir, enviando un número de bloque a la cual asociar estas operaciones), se debe enviar una confirmación, para asi eliminar las reversas que se encuentran pendientes de envío en caso de que el punto de venta decida deshacer la venta completa por el motivo que sea, o una cancelación, para así enviar esas reversas pendientes y deshacerlas por completo. Si el punto de venta envía un nuevo número de bloque confirmar o cancelar previamente el anterior, la Plataforma procederá a confirmar o cancelar automáticamente el bloque de transacciones pendientes, segín como haya sido configurado para actuar en este escenario.

### Example


```python
import time
import openapi_client
from openapi_client.api import payment_api
from openapi_client.model.block_close_object import BlockCloseObject
from openapi_client.model.block_close_response_object import BlockCloseResponseObject
from pprint import pprint
# Defining the host is optional and defaults to https://testcodi.multipay.mx:30801/Payments/Authorize/5.6.1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://testcodi.multipay.mx:30801/Payments/Authorize/5.6.1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = payment_api.PaymentApi(api_client)
    block_close_object = BlockCloseObject(
        block_close=BlockCloseObjectBlockClose(
            company_identification="company_identification_example",
            system_identification="system_identification_example",
            branch_identification="branch_identification_example",
            pos_identification=None,
            request_type="request_type_example",
            service_version="service_version_example",
            sequence="sequence_example",
            security=[
                SaleObjectSaleSecurity(
                    type="type_example",
                    values=[
                        SaleObjectSaleValues(
                            name="name_example",
                            value=None,
                        ),
                    ],
                ),
            ],
            block="block_example",
            ticket="ticket_example",
            ticket_answer_key="ticket_answer_key_example",
            request_key="request_key_example",
            reason_sequence_break="TIMEOUT",
            pos_type="pos_type_example",
            pos_version="pos_version_example",
            pos_address="pos_address_example",
            pos_serial="pos_serial_example",
            posgeo="posgeo_example",
            reading_device_version="reading_device_version_example",
            reading_device_type="reading_device_type_example",
            reading_device_operating_from=dateutil_parser('1970-01-01T00:00:00.00Z'),
            reading_device_serial="reading_device_serial_example",
            reading_device_geo="reading_device_geo_example",
            reading_device_address="reading_device_address_example",
            user_id="user_id_example",
            user_name="user_name_example",
            foreign_block="foreign_block_example",
        ),
    ) # BlockCloseObject | Elementos o Atributos que componen el requerimiento de una transacción, los atributos condicionales y/o opcionales que no sean requeridos para esta transacción no deberán ser enviados.

    # example passing only required values which don't have defaults set
    try:
        # Confirmación del último bloque de transacciones realizadas.
        api_response = api_instance.block_close_post(block_close_object)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PaymentApi->block_close_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **block_close_object** | [**BlockCloseObject**](BlockCloseObject.md)| Elementos o Atributos que componen el requerimiento de una transacción, los atributos condicionales y/o opcionales que no sean requeridos para esta transacción no deberán ser enviados. |

### Return type

[**BlockCloseResponseObject**](BlockCloseResponseObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Elementos o Atributos que componen la respuesta a la transacción requerida.  |  -  |
**400** | Bad request. |  -  |
**401** | Authorization information is missing or invalid. |  -  |
**404** | Not Found. |  -  |
**405** | Invalid Method. |  -  |
**500** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **block_create_post**
> BlockCreateResponseObject block_create_post(block_create_object)

Crea un Identificador de Bloque-Block de transacciones.

Operación utilizada para crear un Bloque de transacciones, esta operación se ejecuta en forma implícita en cualquier operación que Contenga el atributo <b>Block</b> sin valor en el requirimiento. Utilizado por sistemas que no poseen un identificador único de su operación.

### Example


```python
import time
import openapi_client
from openapi_client.api import payment_api
from openapi_client.model.block_create_response_object import BlockCreateResponseObject
from openapi_client.model.block_create_object import BlockCreateObject
from pprint import pprint
# Defining the host is optional and defaults to https://testcodi.multipay.mx:30801/Payments/Authorize/5.6.1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://testcodi.multipay.mx:30801/Payments/Authorize/5.6.1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = payment_api.PaymentApi(api_client)
    block_create_object = BlockCreateObject(
        block_create=BlockCreateObjectBlockCreate(
            company_identification="company_identification_example",
            system_identification="system_identification_example",
            branch_identification="branch_identification_example",
            pos_identification=None,
            request_type="request_type_example",
            service_version="service_version_example",
            sequence="sequence_example",
            security=[
                SaleObjectSaleSecurity(
                    type="type_example",
                    values=[
                        SaleObjectSaleValues(
                            name="name_example",
                            value=None,
                        ),
                    ],
                ),
            ],
            block="block_example",
            ticket="ticket_example",
            ticket_answer_key="ticket_answer_key_example",
            request_key="request_key_example",
            reason_sequence_break="TIMEOUT",
            pos_type="pos_type_example",
            pos_version="pos_version_example",
            pos_address="pos_address_example",
            pos_serial="pos_serial_example",
            posgeo="posgeo_example",
            reading_device_version="reading_device_version_example",
            reading_device_type="reading_device_type_example",
            reading_device_operating_from=dateutil_parser('1970-01-01T00:00:00.00Z'),
            reading_device_serial="reading_device_serial_example",
            reading_device_geo="reading_device_geo_example",
            reading_device_address="reading_device_address_example",
            user_id="user_id_example",
            user_name="user_name_example",
        ),
    ) # BlockCreateObject | Elementos o Atributos que componen el requerimiento de una transacción, los atributos condicionales y/o opcionales que no sean requeridos para esta transacción no deberán ser enviados.

    # example passing only required values which don't have defaults set
    try:
        # Crea un Identificador de Bloque-Block de transacciones.
        api_response = api_instance.block_create_post(block_create_object)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PaymentApi->block_create_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **block_create_object** | [**BlockCreateObject**](BlockCreateObject.md)| Elementos o Atributos que componen el requerimiento de una transacción, los atributos condicionales y/o opcionales que no sean requeridos para esta transacción no deberán ser enviados. |

### Return type

[**BlockCreateResponseObject**](BlockCreateResponseObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Elementos o Atributos que componen la respuesta a la transacción requerida.  |  -  |
**400** | Bad request. |  -  |
**401** | Authorization information is missing or invalid. |  -  |
**404** | Not Found. |  -  |
**405** | Invalid Method. |  -  |
**500** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_post**
> CancelResponseObject cancel_post(cancel_object)

Cancela una Transacción en Curso, Inciada con un GetCard/WalletRequest.

Se utiliza para cancelar una Operación en la cual la Plataforma posee el control del dispositivo de lectura, y ya no desea continuar con la transacción. Utilizado despúes de ejecutar GetCard.

### Example


```python
import time
import openapi_client
from openapi_client.api import payment_api
from openapi_client.model.cancel_response_object import CancelResponseObject
from openapi_client.model.cancel_object import CancelObject
from pprint import pprint
# Defining the host is optional and defaults to https://testcodi.multipay.mx:30801/Payments/Authorize/5.6.1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://testcodi.multipay.mx:30801/Payments/Authorize/5.6.1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = payment_api.PaymentApi(api_client)
    cancel_object = CancelObject(
        cancel=CancelObjectCancel(
            company_identification="company_identification_example",
            system_identification="system_identification_example",
            branch_identification="branch_identification_example",
            pos_identification=None,
            service_version="service_version_example",
            sequence="sequence_example",
            security=[
                SaleObjectSaleSecurity(
                    type="type_example",
                    values=[
                        SaleObjectSaleValues(
                            name="name_example",
                            value=None,
                        ),
                    ],
                ),
            ],
            block="block_example",
            ticket="ticket_example",
            ticket_answer_key="ticket_answer_key_example",
            request_key="request_key_example",
            reason="TIMEOUT",
            pos_type="pos_type_example",
            pos_version="pos_version_example",
            pos_address="pos_address_example",
            pos_serial="pos_serial_example",
            posgeo="posgeo_example",
            reading_device_type="reading_device_type_example",
            reading_device_operating_from=dateutil_parser('1970-01-01T00:00:00.00Z'),
            reading_device_version="reading_device_version_example",
            reading_device_address="reading_device_address_example",
            reading_device_serial="reading_device_serial_example",
            reading_device_geo="reading_device_geo_example",
            user_id="user_id_example",
            user_name="user_name_example",
        ),
    ) # CancelObject | Elementos o Atributos que componen el requerimiento de una transacción, los atributos condicionales y/o opcionales que no sean requeridos para esta transacción no deberán ser enviados.

    # example passing only required values which don't have defaults set
    try:
        # Cancela una Transacción en Curso, Inciada con un GetCard/WalletRequest.
        api_response = api_instance.cancel_post(cancel_object)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PaymentApi->cancel_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cancel_object** | [**CancelObject**](CancelObject.md)| Elementos o Atributos que componen el requerimiento de una transacción, los atributos condicionales y/o opcionales que no sean requeridos para esta transacción no deberán ser enviados. |

### Return type

[**CancelResponseObject**](CancelResponseObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Elementos o Atributos que componen la respuesta a la transacción requerida.  |  -  |
**400** | Bad request. |  -  |
**401** | Authorization information is missing or invalid. |  -  |
**404** | Not Found. |  -  |
**405** | Invalid Method. |  -  |
**500** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **capture_post**
> CaptureResponseObject capture_post(capture_object)

Confirmación de un consumo previo.

Operación de confirmación de una autorización sin Captura del tipo Authorize realizada previamente (normalmente en Operaciones de Checking-Checkout).

### Example


```python
import time
import openapi_client
from openapi_client.api import payment_api
from openapi_client.model.capture_response_object import CaptureResponseObject
from openapi_client.model.capture_object import CaptureObject
from pprint import pprint
# Defining the host is optional and defaults to https://testcodi.multipay.mx:30801/Payments/Authorize/5.6.1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://testcodi.multipay.mx:30801/Payments/Authorize/5.6.1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = payment_api.PaymentApi(api_client)
    capture_object = CaptureObject(
        capture=CaptureObjectCapture(
            company_identification="company_identification_example",
            system_identification="system_identification_example",
            branch_identification="branch_identification_example",
            pos_identification="pos_identification_example",
            request_type="request_type_example",
            service_version="service_version_example",
            sequence="sequence_example",
            security=[
                SaleObjectSaleSecurity(
                    type="type_example",
                    values=[
                        SaleObjectSaleValues(
                            name="name_example",
                            value=None,
                        ),
                    ],
                ),
            ],
            block="block_example",
            required_information=[
                SaleObjectSaleRequiredInformation(
                    name="name_example",
                    type="STRING",
                    interpret_for="POS",
                    it_is_defined=True,
                    ui_type="ui_type_example",
                    ui_attributes="ui_attributes_example",
                    value="value_example",
                    label="label_example",
                    min_length=1,
                    max_length=1,
                    validation_expression_type="regex",
                    validation_expression="validation_expression_example",
                    mandatory=True,
                ),
            ],
            ticket="ticket_example",
            ticket_answer_key="ticket_answer_key_example",
            timeout=3.14,
            merchant_notify_url="merchant_notify_url_example",
            is_reverse=3.14,
            reverse_reason="TIMEOUT",
            reason_sequence_break="TIMEOUT",
            pos_type="pos_type_example",
            pos_version="pos_version_example",
            pos_address="pos_address_example",
            pos_serial="pos_serial_example",
            posgeo="posgeo_example",
            reading_device_type="reading_device_type_example",
            reading_device_operating_from=dateutil_parser('1970-01-01T00:00:00.00Z'),
            reading_device_version="reading_device_version_example",
            reading_device_address="reading_device_address_example",
            reading_device_serial="reading_device_serial_example",
            reading_device_geo="reading_device_geo_example",
            user_id="user_id_example",
            user_name="user_name_example",
            amount=3.14,
            amount_charged=3.14,
            card_read_mode="B",
            card_get_mode="card_get_mode_example",
            card_number="card_number_example",
            card_number_masked="card_number_masked_example",
            card_number_encrypted="card_number_encrypted_example",
            card_exp="card_exp_example",
            track1="track1_example",
            track2="track2_example",
            security_code="security_code_example",
            pin="pin_example",
            card_cryptogram="card_cryptogram_example",
            credential_token="credential_token_example",
            credential_issuer_token="credential_issuer_token_example",
            card_app_name="card_app_name_example",
            card_app_identifier="card_app_identifier_example",
            card_app_label="card_app_label_example",
            card_auth_request_cryptogram="card_auth_request_cryptogram_example",
            card_auth_response_cryptogram="card_auth_response_cryptogram_example",
            payer=SaleObjectSalePayer(
                identification="identification_example",
                identification_type="PAS",
                email="email_example",
                document_type="PAS",
                document_number="document_number_example",
                first_name="first_name_example",
                last_name="last_name_example",
                middle_name="middle_name_example",
                abbreviated_name="abbreviated_name_example",
                phone="phone_example",
                zip_code="zip_code_example",
                address_street="address_street_example",
                address_number="address_number_example",
                address_internal="address_internal_example",
                address_suburb="address_suburb_example",
                address_delegation="address_delegation_example",
                city="city_example",
                state="state_example",
                country="country_example",
                category_code=1,
                tax_category_type="tax_category_type_example",
                tax_identification_type="tax_identification_type_example",
                tax_identification="tax_identification_example",
                notify_url="notify_url_example",
            ),
            customer=SaleObjectSaleCustomer(
                identification="identification_example",
                identification_type="PAS",
                email="email_example",
                document_type="PAS",
                document_number="document_number_example",
                first_name="first_name_example",
                last_name="last_name_example",
                middle_name="middle_name_example",
                abbreviated_name="abbreviated_name_example",
                phone="phone_example",
                zip_code="zip_code_example",
                address_street="address_street_example",
                address_number="address_number_example",
                address_internal="address_internal_example",
                address_suburb="address_suburb_example",
                address_delegation="address_delegation_example",
                city="city_example",
                state="state_example",
                country="country_example",
                category_code=1,
                tax_category_type="tax_category_type_example",
                tax_identification_type="tax_identification_type_example",
                tax_identification="tax_identification_example",
                notify_url="notify_url_example",
            ),
            seller=SaleObjectSaleSeller(
                identification="identification_example",
                identification_type="PAS",
                email="email_example",
                document_type="PAS",
                document_number="document_number_example",
                first_name="first_name_example",
                last_name="last_name_example",
                middle_name="middle_name_example",
                abbreviated_name="abbreviated_name_example",
                phone="phone_example",
                zip_code="zip_code_example",
                address_street="address_street_example",
                address_number="address_number_example",
                address_internal="address_internal_example",
                address_suburb="address_suburb_example",
                address_delegation="address_delegation_example",
                city="city_example",
                state="state_example",
                country="country_example",
                category_code=1,
                tax_category_type="tax_category_type_example",
                tax_identification_type="tax_identification_type_example",
                tax_identification="tax_identification_example",
                notify_url="notify_url_example",
            ),
            products=[
                SaleObjectSaleProducts(
                    item=1,
                    name="name_example",
                    code="code_example",
                    quantity=3.14,
                    unit="unit_example",
                    unit_amount=3.14,
                    net_amount=3.14,
                    tax_amount=3.14,
                    total_amount=3.14,
                ),
            ],
            orig_answer_key="orig_answer_key_example",
            orig_block="orig_block_example",
            orig_foreign_block="orig_foreign_block_example",
            tax_refund_type="tax_refund_type_example",
            payment_facilitator_id="payment_facilitator_id_example",
            merchant_id="merchant_id_example",
            terminal_id="terminal_id_example",
            terminal_trace=1,
            settlement_batch_number=1,
        ),
    ) # CaptureObject | Elementos o Atributos que componen el requerimiento de una transacción, los atributos condicionales y/o opcionales que no sean requeridos para esta transacción no deberán ser enviados.

    # example passing only required values which don't have defaults set
    try:
        # Confirmación de un consumo previo.
        api_response = api_instance.capture_post(capture_object)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PaymentApi->capture_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **capture_object** | [**CaptureObject**](CaptureObject.md)| Elementos o Atributos que componen el requerimiento de una transacción, los atributos condicionales y/o opcionales que no sean requeridos para esta transacción no deberán ser enviados. |

### Return type

[**CaptureResponseObject**](CaptureResponseObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Elementos o Atributos que componen la respuesta a la transacción requerida.  |  -  |
**400** | Bad request. |  -  |
**401** | Authorization information is missing or invalid. |  -  |
**404** | Not Found. |  -  |
**405** | Invalid Method. |  -  |
**500** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **close_post**
> CloseResponseObject close_post(close_object)

Utilizada por el POS para indicar que finalizo su sesion.

Con esta operación el POS esta indicando a la plataforma que finaliza su session de Trabajo, la misma se reinicia con cuialquier nueva operación enviada por el POS. 

### Example


```python
import time
import openapi_client
from openapi_client.api import payment_api
from openapi_client.model.close_object import CloseObject
from openapi_client.model.close_response_object import CloseResponseObject
from pprint import pprint
# Defining the host is optional and defaults to https://testcodi.multipay.mx:30801/Payments/Authorize/5.6.1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://testcodi.multipay.mx:30801/Payments/Authorize/5.6.1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = payment_api.PaymentApi(api_client)
    close_object = CloseObject(
        close=CloseObjectClose(
            company_identification="company_identification_example",
            system_identification="system_identification_example",
            branch_identification="branch_identification_example",
            pos_identification="pos_identification_example",
            request_type="request_type_example",
            service_version="service_version_example",
            sequence="sequence_example",
            security=[
                SaleObjectSaleSecurity(
                    type="type_example",
                    values=[
                        SaleObjectSaleValues(
                            name="name_example",
                            value=None,
                        ),
                    ],
                ),
            ],
            block="block_example",
            ticket="ticket_example",
            ticket_answer_key="ticket_answer_key_example",
            timeout=3.14,
            reason_sequence_break="TIMEOUT",
            pos_type="pos_type_example",
            pos_version="pos_version_example",
            pos_address="pos_address_example",
            pos_serial="pos_serial_example",
            posgeo="posgeo_example",
            reading_device_type="reading_device_type_example",
            reading_device_operating_from=dateutil_parser('1970-01-01T00:00:00.00Z'),
            reading_device_version="reading_device_version_example",
            reading_device_address="reading_device_address_example",
            reading_device_serial="reading_device_serial_example",
            reading_device_geo="reading_device_geo_example",
            user_id="user_id_example",
            user_name="user_name_example",
        ),
    ) # CloseObject | Elementos o Atributos que componen el requerimiento de una transacción, los atributos condicionales y/o opcionales que no sean requeridos para esta transacción no deberán ser enviados.

    # example passing only required values which don't have defaults set
    try:
        # Utilizada por el POS para indicar que finalizo su sesion.
        api_response = api_instance.close_post(close_object)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PaymentApi->close_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **close_object** | [**CloseObject**](CloseObject.md)| Elementos o Atributos que componen el requerimiento de una transacción, los atributos condicionales y/o opcionales que no sean requeridos para esta transacción no deberán ser enviados. |

### Return type

[**CloseResponseObject**](CloseResponseObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Elementos o Atributos que componen la respuesta a la transacción requerida.  |  -  |
**400** | Bad request. |  -  |
**401** | Authorization information is missing or invalid. |  -  |
**404** | Not Found. |  -  |
**405** | Invalid Method. |  -  |
**500** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configure_post**
> ConfigureResponseObject configure_post(configure_object)

Permite crear configuración en Plataforma

Al ejecutar esta operación se permite que Plataforma cree el Dispositivo físico ( PINPAD ) en sus tablas de configuración y lo asocie al Aplicativo-Empresa-Sucursal-Caja.

### Example


```python
import time
import openapi_client
from openapi_client.api import payment_api
from openapi_client.model.configure_response_object import ConfigureResponseObject
from openapi_client.model.configure_object import ConfigureObject
from pprint import pprint
# Defining the host is optional and defaults to https://testcodi.multipay.mx:30801/Payments/Authorize/5.6.1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://testcodi.multipay.mx:30801/Payments/Authorize/5.6.1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = payment_api.PaymentApi(api_client)
    configure_object = ConfigureObject(
        configure=ConfigureObjectConfigure(
            company_identification="company_identification_example",
            system_identification="system_identification_example",
            branch_identification="branch_identification_example",
            pos_identification=None,
            request_type="request_type_example",
            service_version="service_version_example",
            sequence="sequence_example",
            security=[
                SaleObjectSaleSecurity(
                    type="type_example",
                    values=[
                        SaleObjectSaleValues(
                            name="name_example",
                            value=None,
                        ),
                    ],
                ),
            ],
            block="block_example",
            ticket="ticket_example",
            ticket_answer_key="ticket_answer_key_example",
            reason_sequence_break="TIMEOUT",
            pos_type="pos_type_example",
            pos_version="pos_version_example",
            pos_address="pos_address_example",
            pos_serial="pos_serial_example",
            posgeo="posgeo_example",
            reading_device_version="reading_device_version_example",
            reading_device_type="reading_device_type_example",
            reading_device_operating_from=dateutil_parser('1970-01-01T00:00:00.00Z'),
            reading_device_serial="reading_device_serial_example",
            reading_device_geo="reading_device_geo_example",
            reading_device_address="reading_device_address_example",
            user_id="user_id_example",
            user_name="user_name_example",
            posor_device_actions=[
                "RequestPIN",
            ],
            operation_mode="operation_mode_example",
            operation_mode_description="operation_mode_description_example",
            operations=[
                ConfigureObjectConfigureOperations(
                    id="id_example",
                    description="description_example",
                    request={},
                    answer={},
                    default_timeout=1,
                    version="version_example",
                    effective_from=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    effective_to=dateutil_parser('1970-01-01T00:00:00.00Z'),
                ),
            ],
            tables=[
                ConfigureObjectConfigureTables(
                    id="id_example",
                    description="description_example",
                    version="version_example",
                    data={},
                    effective_from=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    effective_to=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    time_of_life=1,
                    time_of_life_offline=1,
                ),
            ],
            files=[
                ConfigureObjectConfigureFiles(
                    id="id_example",
                    description="description_example",
                    type="type_example",
                    path="path_example",
                    version="version_example",
                    attributes="attributes_example",
                    data={},
                    effective_from=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    effective_to=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    time_of_life=1,
                    time_of_life_offline=1,
                ),
            ],
        ),
    ) # ConfigureObject | Elementos o Atributos que componen el requerimiento de una transacción, los atributos condicionales y/o opcionales que no sean requeridos para esta transacción no deberán ser enviados.

    # example passing only required values which don't have defaults set
    try:
        # Permite crear configuración en Plataforma
        api_response = api_instance.configure_post(configure_object)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PaymentApi->configure_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **configure_object** | [**ConfigureObject**](ConfigureObject.md)| Elementos o Atributos que componen el requerimiento de una transacción, los atributos condicionales y/o opcionales que no sean requeridos para esta transacción no deberán ser enviados. |

### Return type

[**ConfigureResponseObject**](ConfigureResponseObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Elementos o Atributos que componen la respuesta a la transacción requerida.  |  -  |
**400** | Bad request. |  -  |
**401** | Authorization information is missing or invalid. |  -  |
**404** | Not Found. |  -  |
**405** | Invalid Method. |  -  |
**500** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **confirm_post**
> ConfirmResponseObject confirm_post(confirm_object)

Confirmación de la última operación realizada.

Luego de realizar una operación de compra/autorización, anulación o devolución, y haber procesado correctamente la respuesta, se debe enviar una confirmación, de forma de eliminar la reversa que se encuentra pendiente de envío en caso de que esa respuesta no sea procesada por el punto de venta o no llegue a su destino. 

### Example


```python
import time
import openapi_client
from openapi_client.api import payment_api
from openapi_client.model.confirm_response_object import ConfirmResponseObject
from openapi_client.model.confirm_object import ConfirmObject
from pprint import pprint
# Defining the host is optional and defaults to https://testcodi.multipay.mx:30801/Payments/Authorize/5.6.1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://testcodi.multipay.mx:30801/Payments/Authorize/5.6.1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = payment_api.PaymentApi(api_client)
    confirm_object = ConfirmObject(
        confirm=ConfirmObjectConfirm(
            company_identification="company_identification_example",
            system_identification="system_identification_example",
            branch_identification="branch_identification_example",
            pos_identification=None,
            request_type="request_type_example",
            service_version="service_version_example",
            sequence="sequence_example",
            security=[
                SaleObjectSaleSecurity(
                    type="type_example",
                    values=[
                        SaleObjectSaleValues(
                            name="name_example",
                            value=None,
                        ),
                    ],
                ),
            ],
            block="block_example",
            ticket="ticket_example",
            ticket_answer_key="ticket_answer_key_example",
            request_key="request_key_example",
            reason_sequence_break="TIMEOUT",
            pos_type="pos_type_example",
            pos_version="pos_version_example",
            pos_address="pos_address_example",
            pos_serial="pos_serial_example",
            posgeo="posgeo_example",
            reading_device_version="reading_device_version_example",
            reading_device_type="reading_device_type_example",
            reading_device_operating_from=dateutil_parser('1970-01-01T00:00:00.00Z'),
            reading_device_serial="reading_device_serial_example",
            reading_device_geo="reading_device_geo_example",
            reading_device_address="reading_device_address_example",
            user_id="user_id_example",
            user_name="user_name_example",
        ),
    ) # ConfirmObject | Elementos o Atributos que componen el requerimiento de una transacción, los atributos condicionales y/o opcionales que no sean requeridos para esta transacción no deberán ser enviados.

    # example passing only required values which don't have defaults set
    try:
        # Confirmación de la última operación realizada.
        api_response = api_instance.confirm_post(confirm_object)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PaymentApi->confirm_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **confirm_object** | [**ConfirmObject**](ConfirmObject.md)| Elementos o Atributos que componen el requerimiento de una transacción, los atributos condicionales y/o opcionales que no sean requeridos para esta transacción no deberán ser enviados. |

### Return type

[**ConfirmResponseObject**](ConfirmResponseObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Elementos o Atributos que componen la respuesta a la transacción requerida.  |  -  |
**400** | Bad request. |  -  |
**401** | Authorization information is missing or invalid. |  -  |
**404** | Not Found. |  -  |
**405** | Invalid Method. |  -  |
**500** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **debt_inquiry_post**
> DebtInquiryResponseObject debt_inquiry_post(debt_inquiry_object)

Consulta de Deuda de cuenta/credencial

Consulta de saldo, deuda de la cuenta asociada a la credencial o método de identificación utilizado.

### Example


```python
import time
import openapi_client
from openapi_client.api import payment_api
from openapi_client.model.debt_inquiry_response_object import DebtInquiryResponseObject
from openapi_client.model.debt_inquiry_object import DebtInquiryObject
from pprint import pprint
# Defining the host is optional and defaults to https://testcodi.multipay.mx:30801/Payments/Authorize/5.6.1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://testcodi.multipay.mx:30801/Payments/Authorize/5.6.1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = payment_api.PaymentApi(api_client)
    debt_inquiry_object = DebtInquiryObject(
        debt_inquiry=DebtInquiryObjectDebtInquiry(
            company_identification="company_identification_example",
            system_identification="system_identification_example",
            branch_identification="branch_identification_example",
            pos_identification="pos_identification_example",
            service_version="service_version_example",
            sequence="sequence_example",
            security=[
                SaleObjectSaleSecurity(
                    type="type_example",
                    values=[
                        SaleObjectSaleValues(
                            name="name_example",
                            value=None,
                        ),
                    ],
                ),
            ],
            block="block_example",
            reason_sequence_break="TIMEOUT",
            reading_device_type="reading_device_type_example",
            reading_device_operating_from=dateutil_parser('1970-01-01T00:00:00.00Z'),
            card_app_name="card_app_name_example",
            card_app_identifier="card_app_identifier_example",
            card_app_label="card_app_label_example",
            card_auth_request_cryptogram="card_auth_request_cryptogram_example",
            card_auth_response_cryptogram="card_auth_response_cryptogram_example",
            card_read_mode="B",
            card_get_mode="card_get_mode_example",
            card_number="card_number_example",
            card_number_masked="card_number_masked_example",
            card_number_encrypted="card_number_encrypted_example",
            card_exp="card_exp_example",
            track1="track1_example",
            track2="track2_example",
            input_tokens=[
                SaleObjectSaleInputTokens(
                    name="name_example",
                    value="value_example",
                ),
            ],
            security_code="security_code_example",
            pin="pin_example",
            card_last_four_digits="card_last_four_digits_example",
            credential_token="credential_token_example",
            credential_issuer_token="credential_issuer_token_example",
            payer=SaleObjectSalePayer(
                identification="identification_example",
                identification_type="PAS",
                email="email_example",
                document_type="PAS",
                document_number="document_number_example",
                first_name="first_name_example",
                last_name="last_name_example",
                middle_name="middle_name_example",
                abbreviated_name="abbreviated_name_example",
                phone="phone_example",
                zip_code="zip_code_example",
                address_street="address_street_example",
                address_number="address_number_example",
                address_internal="address_internal_example",
                address_suburb="address_suburb_example",
                address_delegation="address_delegation_example",
                city="city_example",
                state="state_example",
                country="country_example",
                category_code=1,
                tax_category_type="tax_category_type_example",
                tax_identification_type="tax_identification_type_example",
                tax_identification="tax_identification_example",
                notify_url="notify_url_example",
            ),
            customer=SaleObjectSaleCustomer(
                identification="identification_example",
                identification_type="PAS",
                email="email_example",
                document_type="PAS",
                document_number="document_number_example",
                first_name="first_name_example",
                last_name="last_name_example",
                middle_name="middle_name_example",
                abbreviated_name="abbreviated_name_example",
                phone="phone_example",
                zip_code="zip_code_example",
                address_street="address_street_example",
                address_number="address_number_example",
                address_internal="address_internal_example",
                address_suburb="address_suburb_example",
                address_delegation="address_delegation_example",
                city="city_example",
                state="state_example",
                country="country_example",
                category_code=1,
                tax_category_type="tax_category_type_example",
                tax_identification_type="tax_identification_type_example",
                tax_identification="tax_identification_example",
                notify_url="notify_url_example",
            ),
            payment_facilitator_id="payment_facilitator_id_example",
            merchant_id="merchant_id_example",
            terminal_id="terminal_id_example",
            terminal_trace=1,
            settlement_batch_number=1,
        ),
    ) # DebtInquiryObject | Elementos o Atributos que componen el requerimiento de una transacción, los atributos condicionales y/o opcionales que no sean requeridos para esta transacción no deberán ser enviados.

    # example passing only required values which don't have defaults set
    try:
        # Consulta de Deuda de cuenta/credencial
        api_response = api_instance.debt_inquiry_post(debt_inquiry_object)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PaymentApi->debt_inquiry_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **debt_inquiry_object** | [**DebtInquiryObject**](DebtInquiryObject.md)| Elementos o Atributos que componen el requerimiento de una transacción, los atributos condicionales y/o opcionales que no sean requeridos para esta transacción no deberán ser enviados. |

### Return type

[**DebtInquiryResponseObject**](DebtInquiryResponseObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Elementos o Atributos que componen la respuesta a la transacción requerida.  |  -  |
**400** | Bad request. |  -  |
**401** | Authorization information is missing or invalid. |  -  |
**404** | Not Found. |  -  |
**405** | Invalid Method. |  -  |
**500** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **debt_payment_post**
> DebtPaymentResponseObject debt_payment_post(debt_payment_object)

Pago de Deuda, Resumen de Cuenta o Saldo.

Pago de Deuda, Resumen de Cuenta o Saldo.

### Example


```python
import time
import openapi_client
from openapi_client.api import payment_api
from openapi_client.model.debt_payment_response_object import DebtPaymentResponseObject
from openapi_client.model.debt_payment_object import DebtPaymentObject
from pprint import pprint
# Defining the host is optional and defaults to https://testcodi.multipay.mx:30801/Payments/Authorize/5.6.1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://testcodi.multipay.mx:30801/Payments/Authorize/5.6.1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = payment_api.PaymentApi(api_client)
    debt_payment_object = DebtPaymentObject(
        debt_payment=DebtPaymentObjectDebtPayment(
            company_identification="company_identification_example",
            system_identification="system_identification_example",
            branch_identification="branch_identification_example",
            pos_identification="pos_identification_example",
            request_type="request_type_example",
            service_version="service_version_example",
            sequence="sequence_example",
            security=[
                SaleObjectSaleSecurity(
                    type="type_example",
                    values=[
                        SaleObjectSaleValues(
                            name="name_example",
                            value=None,
                        ),
                    ],
                ),
            ],
            block="block_example",
            required_information=[
                DebtPaymentObjectDebtPaymentRequiredInformation(
                    name="name_example",
                    type="STRING",
                    interpret_for="POS",
                    it_is_defined=True,
                    ui_type="ui_type_example",
                    ui_attributes="ui_attributes_example",
                    value="value_example",
                    label="label_example",
                    min_length=1,
                    max_length=1,
                    validation_expression_type="regex",
                    validation_expression="validation_expression_example",
                    mandatory=True,
                ),
            ],
            ticket="ticket_example",
            ticket_answer_key="ticket_answer_key_example",
            timeout=3.14,
            request_key="request_key_example",
            merchant_notify_url="merchant_notify_url_example",
            is_reverse=3.14,
            reverse_reason="TIMEOUT",
            reason_sequence_break="TIMEOUT",
            reference="reference_example",
            pos_type="pos_type_example",
            pos_version="pos_version_example",
            pos_address="pos_address_example",
            pos_serial="pos_serial_example",
            posgeo="posgeo_example",
            reading_device_type="reading_device_type_example",
            reading_device_operating_from=dateutil_parser('1970-01-01T00:00:00.00Z'),
            reading_device_version="reading_device_version_example",
            reading_device_address="reading_device_address_example",
            reading_device_serial="reading_device_serial_example",
            reading_device_geo="reading_device_geo_example",
            user_id="user_id_example",
            user_name="user_name_example",
            amount=3.14,
            facility_payments=3.14,
            facility_type="facility_type_example",
            card_read_mode="B",
            card_get_mode="card_get_mode_example",
            card_number="card_number_example",
            card_number_masked="card_number_masked_example",
            card_number_encrypted="card_number_encrypted_example",
            card_exp="card_exp_example",
            track1="track1_example",
            track2="track2_example",
            security_code="security_code_example",
            pin="pin_example",
            card_cryptogram="card_cryptogram_example",
            card_app_name="card_app_name_example",
            card_app_identifier="card_app_identifier_example",
            card_app_label="card_app_label_example",
            card_auth_request_cryptogram="card_auth_request_cryptogram_example",
            card_auth_response_cryptogram="card_auth_response_cryptogram_example",
            credential_token="credential_token_example",
            credential_issuer_token="credential_issuer_token_example",
            input_tokens=[
                SaleObjectSaleInputTokens(
                    name="name_example",
                    value="value_example",
                ),
            ],
            payer=SaleObjectSalePayer(
                identification="identification_example",
                identification_type="PAS",
                email="email_example",
                document_type="PAS",
                document_number="document_number_example",
                first_name="first_name_example",
                last_name="last_name_example",
                middle_name="middle_name_example",
                abbreviated_name="abbreviated_name_example",
                phone="phone_example",
                zip_code="zip_code_example",
                address_street="address_street_example",
                address_number="address_number_example",
                address_internal="address_internal_example",
                address_suburb="address_suburb_example",
                address_delegation="address_delegation_example",
                city="city_example",
                state="state_example",
                country="country_example",
                category_code=1,
                tax_category_type="tax_category_type_example",
                tax_identification_type="tax_identification_type_example",
                tax_identification="tax_identification_example",
                notify_url="notify_url_example",
            ),
            customer=SaleObjectSaleCustomer(
                identification="identification_example",
                identification_type="PAS",
                email="email_example",
                document_type="PAS",
                document_number="document_number_example",
                first_name="first_name_example",
                last_name="last_name_example",
                middle_name="middle_name_example",
                abbreviated_name="abbreviated_name_example",
                phone="phone_example",
                zip_code="zip_code_example",
                address_street="address_street_example",
                address_number="address_number_example",
                address_internal="address_internal_example",
                address_suburb="address_suburb_example",
                address_delegation="address_delegation_example",
                city="city_example",
                state="state_example",
                country="country_example",
                category_code=1,
                tax_category_type="tax_category_type_example",
                tax_identification_type="tax_identification_type_example",
                tax_identification="tax_identification_example",
                notify_url="notify_url_example",
            ),
            seller=SaleObjectSaleSeller(
                identification="identification_example",
                identification_type="PAS",
                email="email_example",
                document_type="PAS",
                document_number="document_number_example",
                first_name="first_name_example",
                last_name="last_name_example",
                middle_name="middle_name_example",
                abbreviated_name="abbreviated_name_example",
                phone="phone_example",
                zip_code="zip_code_example",
                address_street="address_street_example",
                address_number="address_number_example",
                address_internal="address_internal_example",
                address_suburb="address_suburb_example",
                address_delegation="address_delegation_example",
                city="city_example",
                state="state_example",
                country="country_example",
                category_code=1,
                tax_category_type="tax_category_type_example",
                tax_identification_type="tax_identification_type_example",
                tax_identification="tax_identification_example",
                notify_url="notify_url_example",
            ),
            tax_refund_type="tax_refund_type_example",
            debt_company_identification="debt_company_identification_example",
            products=[
                SaleResponseObjectSaleResponseProducts(
                    item=1,
                    name="name_example",
                    code="code_example",
                    quantity=3.14,
                    unit="unit_example",
                    unit_amount=3.14,
                    net_amount=3.14,
                    tax_amount=3.14,
                    total_amount=3.14,
                ),
            ],
            payment_facilitator_id="payment_facilitator_id_example",
            merchant_id="merchant_id_example",
            terminal_id="terminal_id_example",
            terminal_trace=1,
            settlement_batch_number=1,
        ),
    ) # DebtPaymentObject | Elementos o Atributos que componen el requerimiento de una transacción, los atributos condicionales y/o opcionales que no sean requeridos para esta transacción no deberán ser enviados.

    # example passing only required values which don't have defaults set
    try:
        # Pago de Deuda, Resumen de Cuenta o Saldo.
        api_response = api_instance.debt_payment_post(debt_payment_object)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PaymentApi->debt_payment_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **debt_payment_object** | [**DebtPaymentObject**](DebtPaymentObject.md)| Elementos o Atributos que componen el requerimiento de una transacción, los atributos condicionales y/o opcionales que no sean requeridos para esta transacción no deberán ser enviados. |

### Return type

[**DebtPaymentResponseObject**](DebtPaymentResponseObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Elementos o Atributos que componen la respuesta a la transacción requerida.  |  -  |
**400** | Bad request. |  -  |
**401** | Authorization information is missing or invalid. |  -  |
**404** | Not Found. |  -  |
**405** | Invalid Method. |  -  |
**500** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deposit_post**
> DepositResponseObject deposit_post(deposit_object)

Confirmación de un consumo previo.

Operación de confirmación de una autorización sin Captura del tipo Authorize realizada previamente (normalmente en Operaciones de Checking-Checkout ).

### Example


```python
import time
import openapi_client
from openapi_client.api import payment_api
from openapi_client.model.deposit_response_object import DepositResponseObject
from openapi_client.model.deposit_object import DepositObject
from pprint import pprint
# Defining the host is optional and defaults to https://testcodi.multipay.mx:30801/Payments/Authorize/5.6.1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://testcodi.multipay.mx:30801/Payments/Authorize/5.6.1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = payment_api.PaymentApi(api_client)
    deposit_object = DepositObject(
        deposit=DepositObjectDeposit(
            company_identification="company_identification_example",
            system_identification="system_identification_example",
            branch_identification="branch_identification_example",
            pos_identification="pos_identification_example",
            request_type="request_type_example",
            service_version="service_version_example",
            sequence="sequence_example",
            security=[
                SaleObjectSaleSecurity(
                    type="type_example",
                    values=[
                        SaleObjectSaleValues(
                            name="name_example",
                            value=None,
                        ),
                    ],
                ),
            ],
            block="block_example",
            required_information=[
                SaleObjectSaleRequiredInformation(
                    name="name_example",
                    type="STRING",
                    interpret_for="POS",
                    it_is_defined=True,
                    ui_type="ui_type_example",
                    ui_attributes="ui_attributes_example",
                    value="value_example",
                    label="label_example",
                    min_length=1,
                    max_length=1,
                    validation_expression_type="regex",
                    validation_expression="validation_expression_example",
                    mandatory=True,
                ),
            ],
            ticket="ticket_example",
            ticket_answer_key="ticket_answer_key_example",
            timeout=3.14,
            merchant_notify_url="merchant_notify_url_example",
            is_reverse=3.14,
            reverse_reason="TIMEOUT",
            reason_sequence_break="TIMEOUT",
            pos_type="pos_type_example",
            pos_version="pos_version_example",
            pos_address="pos_address_example",
            pos_serial="pos_serial_example",
            posgeo="posgeo_example",
            reading_device_type="reading_device_type_example",
            reading_device_operating_from=dateutil_parser('1970-01-01T00:00:00.00Z'),
            reading_device_version="reading_device_version_example",
            reading_device_address="reading_device_address_example",
            reading_device_serial="reading_device_serial_example",
            reading_device_geo="reading_device_geo_example",
            user_id="user_id_example",
            user_name="user_name_example",
            amount=3.14,
            amount_charged=3.14,
            card_read_mode="B",
            card_get_mode="card_get_mode_example",
            card_number="card_number_example",
            card_number_masked="card_number_masked_example",
            card_number_encrypted="card_number_encrypted_example",
            card_exp="card_exp_example",
            track1="track1_example",
            track2="track2_example",
            security_code="security_code_example",
            pin="pin_example",
            card_cryptogram="card_cryptogram_example",
            credential_token="credential_token_example",
            credential_issuer_token="credential_issuer_token_example",
            card_app_name="card_app_name_example",
            card_app_identifier="card_app_identifier_example",
            card_app_label="card_app_label_example",
            card_auth_request_cryptogram="card_auth_request_cryptogram_example",
            card_auth_response_cryptogram="card_auth_response_cryptogram_example",
            payer=SaleObjectSalePayer(
                identification="identification_example",
                identification_type="PAS",
                email="email_example",
                document_type="PAS",
                document_number="document_number_example",
                first_name="first_name_example",
                last_name="last_name_example",
                middle_name="middle_name_example",
                abbreviated_name="abbreviated_name_example",
                phone="phone_example",
                zip_code="zip_code_example",
                address_street="address_street_example",
                address_number="address_number_example",
                address_internal="address_internal_example",
                address_suburb="address_suburb_example",
                address_delegation="address_delegation_example",
                city="city_example",
                state="state_example",
                country="country_example",
                category_code=1,
                tax_category_type="tax_category_type_example",
                tax_identification_type="tax_identification_type_example",
                tax_identification="tax_identification_example",
                notify_url="notify_url_example",
            ),
            customer=SaleObjectSaleCustomer(
                identification="identification_example",
                identification_type="PAS",
                email="email_example",
                document_type="PAS",
                document_number="document_number_example",
                first_name="first_name_example",
                last_name="last_name_example",
                middle_name="middle_name_example",
                abbreviated_name="abbreviated_name_example",
                phone="phone_example",
                zip_code="zip_code_example",
                address_street="address_street_example",
                address_number="address_number_example",
                address_internal="address_internal_example",
                address_suburb="address_suburb_example",
                address_delegation="address_delegation_example",
                city="city_example",
                state="state_example",
                country="country_example",
                category_code=1,
                tax_category_type="tax_category_type_example",
                tax_identification_type="tax_identification_type_example",
                tax_identification="tax_identification_example",
                notify_url="notify_url_example",
            ),
            seller=SaleObjectSaleSeller(
                identification="identification_example",
                identification_type="PAS",
                email="email_example",
                document_type="PAS",
                document_number="document_number_example",
                first_name="first_name_example",
                last_name="last_name_example",
                middle_name="middle_name_example",
                abbreviated_name="abbreviated_name_example",
                phone="phone_example",
                zip_code="zip_code_example",
                address_street="address_street_example",
                address_number="address_number_example",
                address_internal="address_internal_example",
                address_suburb="address_suburb_example",
                address_delegation="address_delegation_example",
                city="city_example",
                state="state_example",
                country="country_example",
                category_code=1,
                tax_category_type="tax_category_type_example",
                tax_identification_type="tax_identification_type_example",
                tax_identification="tax_identification_example",
                notify_url="notify_url_example",
            ),
            products=[
                SaleObjectSaleProducts(
                    item=1,
                    name="name_example",
                    code="code_example",
                    quantity=3.14,
                    unit="unit_example",
                    unit_amount=3.14,
                    net_amount=3.14,
                    tax_amount=3.14,
                    total_amount=3.14,
                ),
            ],
            orig_answer_key="orig_answer_key_example",
            orig_block="orig_block_example",
            orig_foreign_block="orig_foreign_block_example",
            tax_refund_type="tax_refund_type_example",
            payment_facilitator_id="payment_facilitator_id_example",
            merchant_id="merchant_id_example",
            terminal_id="terminal_id_example",
            terminal_trace=1,
            settlement_batch_number=1,
        ),
    ) # DepositObject | Elementos o Atributos que componen el requerimiento de una transacción, los atributos condicionales y/o opcionales que no sean requeridos para esta transacción no deberán ser enviados.

    # example passing only required values which don't have defaults set
    try:
        # Confirmación de un consumo previo.
        api_response = api_instance.deposit_post(deposit_object)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PaymentApi->deposit_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deposit_object** | [**DepositObject**](DepositObject.md)| Elementos o Atributos que componen el requerimiento de una transacción, los atributos condicionales y/o opcionales que no sean requeridos para esta transacción no deberán ser enviados. |

### Return type

[**DepositResponseObject**](DepositResponseObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Elementos o Atributos que componen la respuesta a la transacción requerida.  |  -  |
**400** | Bad request. |  -  |
**401** | Authorization information is missing or invalid. |  -  |
**404** | Not Found. |  -  |
**405** | Invalid Method. |  -  |
**500** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_service_post**
> EnableServiceResponseObject enable_service_post(enable_service_object)

Permite Habilitar el uso de un Servicio

Esta operación es solamente utilizada para habilitar un Servicio  para la cadena Comercial, la Sucursal o la Terminal.

### Example


```python
import time
import openapi_client
from openapi_client.api import payment_api
from openapi_client.model.enable_service_response_object import EnableServiceResponseObject
from openapi_client.model.enable_service_object import EnableServiceObject
from pprint import pprint
# Defining the host is optional and defaults to https://testcodi.multipay.mx:30801/Payments/Authorize/5.6.1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://testcodi.multipay.mx:30801/Payments/Authorize/5.6.1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = payment_api.PaymentApi(api_client)
    enable_service_object = EnableServiceObject(
        enable_service=EnableServiceObjectEnableService(
            system_identification="system_identification_example",
            company_identification="company_identification_example",
            branch_identification="branch_identification_example",
            pos_identification="pos_identification_example",
            request_type="request_type_example",
            service_version="service_version_example",
            sequence="sequence_example",
            security=[
                SaleObjectSaleSecurity(
                    type="type_example",
                    values=[
                        SaleObjectSaleValues(
                            name="name_example",
                            value=None,
                        ),
                    ],
                ),
            ],
            block="block_example",
            required_information=[
                DebtPaymentObjectDebtPaymentRequiredInformation(
                    name="name_example",
                    type="STRING",
                    interpret_for="POS",
                    it_is_defined=True,
                    ui_type="ui_type_example",
                    ui_attributes="ui_attributes_example",
                    value="value_example",
                    label="label_example",
                    min_length=1,
                    max_length=1,
                    validation_expression_type="regex",
                    validation_expression="validation_expression_example",
                    mandatory=True,
                ),
            ],
            ticket="ticket_example",
            ticket_answer_key="ticket_answer_key_example",
            transaction_identification="transaction_identification_example",
            transaction_description="transaction_description_example",
            trasaction_date_time="trasaction_date_time_example",
            pos_type="pos_type_example",
            pos_version="pos_version_example",
            pos_address="pos_address_example",
            pos_serial="pos_serial_example",
            posgeo="posgeo_example",
            reading_device_type="reading_device_type_example",
            reading_device_operating_from=dateutil_parser('1970-01-01T00:00:00.00Z'),
            reading_device_version="reading_device_version_example",
            reading_device_address="reading_device_address_example",
            reading_device_serial="reading_device_serial_example",
            reading_device_geo="reading_device_geo_example",
            user_id="user_id_example",
            user_name="user_name_example",
            authentication_information="authentication_information_example",
            payment_facilitator_id="payment_facilitator_id_example",
            merchant_id="merchant_id_example",
            terminal_id="terminal_id_example",
            terminal_trace=1,
            settlement_batch_number=1,
        ),
    ) # EnableServiceObject | Objeto que contendrá los datos del Requerimiento para Habilitar un Servicio.

    # example passing only required values which don't have defaults set
    try:
        # Permite Habilitar el uso de un Servicio
        api_response = api_instance.enable_service_post(enable_service_object)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PaymentApi->enable_service_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enable_service_object** | [**EnableServiceObject**](EnableServiceObject.md)| Objeto que contendrá los datos del Requerimiento para Habilitar un Servicio. |

### Return type

[**EnableServiceResponseObject**](EnableServiceResponseObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Un objeto con un nodo principal llamado \&quot;EnableServicesResponse\&quot;. Dentro de él, estará presente toda la información con el resultado que nos informa el host sobre la operación que intentamos realizar. |  -  |
**400** | Bad request. |  -  |
**401** | Authorization information is missing or invalid. |  -  |
**404** | Not Found. |  -  |
**405** | Invalid Method. |  -  |
**500** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enrollment_post**
> EnrollmentResponseObject enrollment_post(enrollment_object)

Suscripción al servicio de pagos Tokenizados y pagos recurrentes.

Si se desea enviar una compra/autorización, se deberá enviar una petición a este endpoint con los datos requeridos a continuación.

### Example


```python
import time
import openapi_client
from openapi_client.api import payment_api
from openapi_client.model.enrollment_response_object import EnrollmentResponseObject
from openapi_client.model.enrollment_object import EnrollmentObject
from pprint import pprint
# Defining the host is optional and defaults to https://testcodi.multipay.mx:30801/Payments/Authorize/5.6.1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://testcodi.multipay.mx:30801/Payments/Authorize/5.6.1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = payment_api.PaymentApi(api_client)
    enrollment_object = EnrollmentObject(
        enrollment=EnrollmentObjectEnrollment(
            company_identification="company_identification_example",
            system_identification="system_identification_example",
            branch_identification="branch_identification_example",
            pos_identification="pos_identification_example",
            recurrence=[
                EnrollmentObjectEnrollmentRecurrence(
                    interval_type="0",
                    interval_value=1,
                    number_of_recurrences="number_of_recurrences_example",
                ),
            ],
            credential_issuer_token="credential_issuer_token_example",
            card_app_name="card_app_name_example",
            card_app_identifier="card_app_identifier_example",
            card_app_label="card_app_label_example",
            card_auth_request_cryptogram="card_auth_request_cryptogram_example",
            card_auth_response_cryptogram="card_auth_response_cryptogram_example",
            card_read_mode="B",
            card_number="card_number_example",
            card_number_masked="card_number_masked_example",
            card_number_encrypted="card_number_encrypted_example",
            card_exp="card_exp_example",
            track1="track1_example",
            track2="track2_example",
            security_code="security_code_example",
            pin="pin_example",
            card_cryptogram="card_cryptogram_example",
            amount=3.14,
            alternative_amount=3.14,
            request_type="request_type_example",
            pos_type="pos_type_example",
            pos_version="pos_version_example",
            pos_address="pos_address_example",
            pos_serial="pos_serial_example",
            posgeo="posgeo_example",
            reading_device_type="reading_device_type_example",
            reading_device_operating_from=dateutil_parser('1970-01-01T00:00:00.00Z'),
            reading_device_version="reading_device_version_example",
            reading_device_address="reading_device_address_example",
            reading_device_serial="reading_device_serial_example",
            reading_device_geo="reading_device_geo_example",
            user_id="user_id_example",
            user_name="user_name_example",
            timeout=3.14,
            ticket="ticket_example",
            ticket_answer_key="ticket_answer_key_example",
            service_version="service_version_example",
            sequence="sequence_example",
            security=[
                SaleObjectSaleSecurity(
                    type="type_example",
                    values=[
                        SaleObjectSaleValues(
                            name="name_example",
                            value=None,
                        ),
                    ],
                ),
            ],
            plan="plan_example",
            currency_code="484",
            facility_payments=3.14,
            facility_type="facility_type_example",
            transaction_description="transaction_description_example",
            required_information=[
                SaleObjectSaleRequiredInformation(
                    name="name_example",
                    type="STRING",
                    interpret_for="POS",
                    it_is_defined=True,
                    ui_type="ui_type_example",
                    ui_attributes="ui_attributes_example",
                    value="value_example",
                    label="label_example",
                    min_length=1,
                    max_length=1,
                    validation_expression_type="regex",
                    validation_expression="validation_expression_example",
                    mandatory=True,
                ),
            ],
            payer=SaleObjectSalePayer(
                identification="identification_example",
                identification_type="PAS",
                email="email_example",
                document_type="PAS",
                document_number="document_number_example",
                first_name="first_name_example",
                last_name="last_name_example",
                middle_name="middle_name_example",
                abbreviated_name="abbreviated_name_example",
                phone="phone_example",
                zip_code="zip_code_example",
                address_street="address_street_example",
                address_number="address_number_example",
                address_internal="address_internal_example",
                address_suburb="address_suburb_example",
                address_delegation="address_delegation_example",
                city="city_example",
                state="state_example",
                country="country_example",
                category_code=1,
                tax_category_type="tax_category_type_example",
                tax_identification_type="tax_identification_type_example",
                tax_identification="tax_identification_example",
                notify_url="notify_url_example",
            ),
            customer=SaleObjectSaleCustomer(
                identification="identification_example",
                identification_type="PAS",
                email="email_example",
                document_type="PAS",
                document_number="document_number_example",
                first_name="first_name_example",
                last_name="last_name_example",
                middle_name="middle_name_example",
                abbreviated_name="abbreviated_name_example",
                phone="phone_example",
                zip_code="zip_code_example",
                address_street="address_street_example",
                address_number="address_number_example",
                address_internal="address_internal_example",
                address_suburb="address_suburb_example",
                address_delegation="address_delegation_example",
                city="city_example",
                state="state_example",
                country="country_example",
                category_code=1,
                tax_category_type="tax_category_type_example",
                tax_identification_type="tax_identification_type_example",
                tax_identification="tax_identification_example",
                notify_url="notify_url_example",
            ),
            seller=SaleObjectSaleSeller(
                identification="identification_example",
                identification_type="PAS",
                email="email_example",
                document_type="PAS",
                document_number="document_number_example",
                first_name="first_name_example",
                last_name="last_name_example",
                middle_name="middle_name_example",
                abbreviated_name="abbreviated_name_example",
                phone="phone_example",
                zip_code="zip_code_example",
                address_street="address_street_example",
                address_number="address_number_example",
                address_internal="address_internal_example",
                address_suburb="address_suburb_example",
                address_delegation="address_delegation_example",
                city="city_example",
                state="state_example",
                country="country_example",
                category_code=1,
                tax_category_type="tax_category_type_example",
                tax_identification_type="tax_identification_type_example",
                tax_identification="tax_identification_example",
                notify_url="notify_url_example",
            ),
            merchant_notify_url="merchant_notify_url_example",
            block="block_example",
            request_key="request_key_example",
            is_reverse=3.14,
            reverse_reason="TIMEOUT",
            reason_sequence_break="TIMEOUT",
            products=[
                SaleObjectSaleProducts(
                    item=1,
                    name="name_example",
                    code="code_example",
                    quantity=3.14,
                    unit="unit_example",
                    unit_amount=3.14,
                    net_amount=3.14,
                    tax_amount=3.14,
                    total_amount=3.14,
                ),
            ],
            reference="reference_example",
            payment_facilitator_id="payment_facilitator_id_example",
            merchant_id="merchant_id_example",
            terminal_id="terminal_id_example",
            terminal_trace=1,
            settlement_batch_number=1,
        ),
    ) # EnrollmentObject | Elementos o Atributos que componen el requerimiento de una transacción, los atributos condicionales y/o opcionales que no sean requeridos para esta transacción no deberán ser enviados.

    # example passing only required values which don't have defaults set
    try:
        # Suscripción al servicio de pagos Tokenizados y pagos recurrentes.
        api_response = api_instance.enrollment_post(enrollment_object)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PaymentApi->enrollment_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enrollment_object** | [**EnrollmentObject**](EnrollmentObject.md)| Elementos o Atributos que componen el requerimiento de una transacción, los atributos condicionales y/o opcionales que no sean requeridos para esta transacción no deberán ser enviados. |

### Return type

[**EnrollmentResponseObject**](EnrollmentResponseObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Elementos o Atributos que componen la respuesta a la transacción requerida.  |  -  |
**400** | Bad request. |  -  |
**401** | Authorization information is missing or invalid. |  -  |
**404** | Not Found. |  -  |
**405** | Invalid Method. |  -  |
**500** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_block_post**
> GetBlockResponseObject get_block_post(get_block_object)

Recupera los identificadores de las transacciones que  lo componen.

Luego de realizar una serie de operaciones de compra/autorización, anulación y/o devolución, y haber procesado correctamente cada una de las respuestas, estas operaciones se realizaron con esta funcionalidad activada (es decir, enviando un Número de bloque a la cual asociar estas operaciones), se debe enviar una confirmación, para asi eliminar las reversas que se encuentran pendientes de envio en caso de que el punto de venta decida deshacer la venta completa por el motivo que sea, o una cancelación, para asi enviar esas reversas pendientes y asi deshacerlas por completo. Si el punto de venta envía un nuevo Número de bloque confirmar o cancelar previamente el anterior, La Plataforma procederá a confirmar o cancelar automáticamente el bloque de transacciones pendientes, según como haya sido configurado para actuar en este escenario.

### Example


```python
import time
import openapi_client
from openapi_client.api import payment_api
from openapi_client.model.get_block_response_object import GetBlockResponseObject
from openapi_client.model.get_block_object import GetBlockObject
from pprint import pprint
# Defining the host is optional and defaults to https://testcodi.multipay.mx:30801/Payments/Authorize/5.6.1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://testcodi.multipay.mx:30801/Payments/Authorize/5.6.1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = payment_api.PaymentApi(api_client)
    get_block_object = GetBlockObject(
        get_block=GetBlockObjectGetBlock(
            company_identification="company_identification_example",
            system_identification="system_identification_example",
            branch_identification="branch_identification_example",
            pos_identification=None,
            request_type="request_type_example",
            service_version="service_version_example",
            sequence="sequence_example",
            security=[
                SaleObjectSaleSecurity(
                    type="type_example",
                    values=[
                        SaleObjectSaleValues(
                            name="name_example",
                            value=None,
                        ),
                    ],
                ),
            ],
            block="block_example",
            ticket="ticket_example",
            ticket_answer_key="ticket_answer_key_example",
            request_key="request_key_example",
            reason_sequence_break="TIMEOUT",
            pos_type="pos_type_example",
            pos_version="pos_version_example",
            pos_address="pos_address_example",
            pos_serial="pos_serial_example",
            posgeo="posgeo_example",
            reading_device_version="reading_device_version_example",
            reading_device_type="reading_device_type_example",
            reading_device_operating_from=dateutil_parser('1970-01-01T00:00:00.00Z'),
            reading_device_serial="reading_device_serial_example",
            reading_device_geo="reading_device_geo_example",
            reading_device_address="reading_device_address_example",
            user_id="user_id_example",
            user_name="user_name_example",
            orig_block="orig_block_example",
            orig_foreign_block="orig_foreign_block_example",
            transactions_required=[
                GetBlockObjectGetBlockTransactionsRequired(
                    transaction_type="All",
                    state=[
                        "Returned",
                    ],
                ),
            ],
        ),
    ) # GetBlockObject | Elementos o Atributos que componen el requerimiento de una transacción, los atributos condicionales y/o opcionales que no sean requeridos para esta transacción no deberán ser enviados.

    # example passing only required values which don't have defaults set
    try:
        # Recupera los identificadores de las transacciones que  lo componen.
        api_response = api_instance.get_block_post(get_block_object)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PaymentApi->get_block_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_block_object** | [**GetBlockObject**](GetBlockObject.md)| Elementos o Atributos que componen el requerimiento de una transacción, los atributos condicionales y/o opcionales que no sean requeridos para esta transacción no deberán ser enviados. |

### Return type

[**GetBlockResponseObject**](GetBlockResponseObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Elementos o Atributos que componen la respuesta a la transacción requerida.  |  -  |
**400** | Bad request. |  -  |
**401** | Authorization information is missing or invalid. |  -  |
**404** | Not Found. |  -  |
**405** | Invalid Method. |  -  |
**500** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_card_post**
> GetCardResponseObject get_card_post(get_card_object)

Solicitud de Lectura del Medio de Pago

Utilizada solamente en el caso de que el Aplicativo Integrado no tenga el control  del Lector y el mismo esté en control de la Plataforma.

### Example


```python
import time
import openapi_client
from openapi_client.api import payment_api
from openapi_client.model.get_card_response_object import GetCardResponseObject
from openapi_client.model.get_card_object import GetCardObject
from pprint import pprint
# Defining the host is optional and defaults to https://testcodi.multipay.mx:30801/Payments/Authorize/5.6.1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://testcodi.multipay.mx:30801/Payments/Authorize/5.6.1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = payment_api.PaymentApi(api_client)
    get_card_object = GetCardObject(
        get_card=GetCardObjectGetCard(
            company_identification="company_identification_example",
            system_identification="system_identification_example",
            branch_identification="branch_identification_example",
            pos_identification="pos_identification_example",
            request_type="request_type_example",
            service_version="service_version_example",
            sequence="sequence_example",
            security=[
                SaleObjectSaleSecurity(
                    type="type_example",
                    values=[
                        SaleObjectSaleValues(
                            name="name_example",
                            value=None,
                        ),
                    ],
                ),
            ],
            block="block_example",
            ticket="ticket_example",
            ticket_answer_key="ticket_answer_key_example",
            timeout=3.14,
            reason_sequence_break="TIMEOUT",
            transaction_type="transaction_type_example",
            pos_type="pos_type_example",
            pos_version="pos_version_example",
            pos_address="pos_address_example",
            pos_serial="pos_serial_example",
            posgeo="posgeo_example",
            reading_device_type="reading_device_type_example",
            reading_device_operating_from=dateutil_parser('1970-01-01T00:00:00.00Z'),
            reading_device_version="reading_device_version_example",
            reading_device_address="reading_device_address_example",
            reading_device_serial="reading_device_serial_example",
            reading_device_geo="reading_device_geo_example",
            user_id="user_id_example",
            user_name="user_name_example",
            currency_code="484",
            amount=3.14,
            alternative_amount=3.14,
            card_read_mode="B",
            card_app_name="card_app_name_example",
            card_app_identifier="card_app_identifier_example",
            card_app_label="card_app_label_example",
            card_auth_request_cryptogram="card_auth_request_cryptogram_example",
            card_auth_response_cryptogram="card_auth_response_cryptogram_example",
            card_get_mode="card_get_mode_example",
            payment_facilitator_id="payment_facilitator_id_example",
            merchant_id="merchant_id_example",
        ),
    ) # GetCardObject | Elementos o Atributos que componen el requerimiento de una transacción, los atributos condicionales y/o opcionales que no sean requeridos para esta transacción no deberán ser enviados.

    # example passing only required values which don't have defaults set
    try:
        # Solicitud de Lectura del Medio de Pago
        api_response = api_instance.get_card_post(get_card_object)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PaymentApi->get_card_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_card_object** | [**GetCardObject**](GetCardObject.md)| Elementos o Atributos que componen el requerimiento de una transacción, los atributos condicionales y/o opcionales que no sean requeridos para esta transacción no deberán ser enviados. |

### Return type

[**GetCardResponseObject**](GetCardResponseObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Elementos o Atributos que componen la respuesta a la transacción requerida.  |  -  |
**400** | Bad request. |  -  |
**401** | Authorization information is missing or invalid. |  -  |
**404** | Not Found. |  -  |
**405** | Invalid Method. |  -  |
**500** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transaction_post**
> GetTransactionResponseObject get_transaction_post(get_transaction_object)

Recupera los datos de la transacción especificada. 

Recupera todos los datos de la transacción referenciada por el elemento OrigAnswerKey.

### Example


```python
import time
import openapi_client
from openapi_client.api import payment_api
from openapi_client.model.get_transaction_response_object import GetTransactionResponseObject
from openapi_client.model.get_transaction_object import GetTransactionObject
from pprint import pprint
# Defining the host is optional and defaults to https://testcodi.multipay.mx:30801/Payments/Authorize/5.6.1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://testcodi.multipay.mx:30801/Payments/Authorize/5.6.1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = payment_api.PaymentApi(api_client)
    get_transaction_object = GetTransactionObject(
        get_transaction=GetTransactionObjectGetTransaction(
            company_identification="company_identification_example",
            system_identification="system_identification_example",
            branch_identification="branch_identification_example",
            pos_identification=None,
            request_type="request_type_example",
            service_version="service_version_example",
            sequence="sequence_example",
            security=[
                SaleObjectSaleSecurity(
                    type="type_example",
                    values=[
                        SaleObjectSaleValues(
                            name="name_example",
                            value=None,
                        ),
                    ],
                ),
            ],
            block="block_example",
            ticket="ticket_example",
            ticket_answer_key="ticket_answer_key_example",
            request_key="request_key_example",
            reason_sequence_break="TIMEOUT",
            reference="reference_example",
            orig_reference="orig_reference_example",
            pos_type="pos_type_example",
            pos_version="pos_version_example",
            pos_address="pos_address_example",
            pos_serial="pos_serial_example",
            posgeo="posgeo_example",
            reading_device_version="reading_device_version_example",
            reading_device_type="reading_device_type_example",
            reading_device_operating_from=dateutil_parser('1970-01-01T00:00:00.00Z'),
            reading_device_serial="reading_device_serial_example",
            reading_device_geo="reading_device_geo_example",
            reading_device_address="reading_device_address_example",
            user_id="user_id_example",
            user_name="user_name_example",
            answer_key="answer_key_example",
        ),
    ) # GetTransactionObject | Elementos o Atributos que componen el requerimiento de una transacción, los atributos condicionales y/o opcionales que no sean requeridos para esta transacción no deberán ser enviados.

    # example passing only required values which don't have defaults set
    try:
        # Recupera los datos de la transacción especificada. 
        api_response = api_instance.get_transaction_post(get_transaction_object)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PaymentApi->get_transaction_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_transaction_object** | [**GetTransactionObject**](GetTransactionObject.md)| Elementos o Atributos que componen el requerimiento de una transacción, los atributos condicionales y/o opcionales que no sean requeridos para esta transacción no deberán ser enviados. |

### Return type

[**GetTransactionResponseObject**](GetTransactionResponseObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Elementos o Atributos que componen la respuesta a la transacción requerida.  |  -  |
**400** | Bad request. |  -  |
**401** | Authorization information is missing or invalid. |  -  |
**404** | Not Found. |  -  |
**405** | Invalid Method. |  -  |
**500** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **keep_alive_post**
> KeepAliveResponseObject keep_alive_post(keep_alive_object)

Mensaje que informa si está disponible el Servicio Authorize.

Luego de realizar una serie de operaciones de compra/autorización, anulación y/o devolución, y haber procesado correctamente cada una de las respuestas, estas operaciones se realizaron con esta funcionalidad activada (es decir, enviando un Número de bloque a la cual asociar estas operaciones), se debe enviar una confirmación, para asi eliminar las reversas que se encuentran pendientes de envío en caso de que el punto de venta decida deshacer la venta completa por el motivo que sea, o una cancelación, para así enviar esas reversas pendientes y deshacerlas por completo. Si el punto de venta envía un nuevo Número de bloque confirmar o cancelar previamente el anterior, el Plataforma procederá a confirmar o cancelar automáticamente el bloque de transacciones pendientes, según como haya sido configurado para actuar en este escenario.

### Example


```python
import time
import openapi_client
from openapi_client.api import payment_api
from openapi_client.model.keep_alive_object import KeepAliveObject
from openapi_client.model.keep_alive_response_object import KeepAliveResponseObject
from pprint import pprint
# Defining the host is optional and defaults to https://testcodi.multipay.mx:30801/Payments/Authorize/5.6.1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://testcodi.multipay.mx:30801/Payments/Authorize/5.6.1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = payment_api.PaymentApi(api_client)
    keep_alive_object = KeepAliveObject(
        keep_alive=BlockCreateObjectBlockCreate(
            company_identification="company_identification_example",
            system_identification="system_identification_example",
            branch_identification="branch_identification_example",
            pos_identification=None,
            request_type="request_type_example",
            service_version="service_version_example",
            sequence="sequence_example",
            security=[
                SaleObjectSaleSecurity(
                    type="type_example",
                    values=[
                        SaleObjectSaleValues(
                            name="name_example",
                            value=None,
                        ),
                    ],
                ),
            ],
            block="block_example",
            ticket="ticket_example",
            ticket_answer_key="ticket_answer_key_example",
            request_key="request_key_example",
            reason_sequence_break="TIMEOUT",
            pos_type="pos_type_example",
            pos_version="pos_version_example",
            pos_address="pos_address_example",
            pos_serial="pos_serial_example",
            posgeo="posgeo_example",
            reading_device_version="reading_device_version_example",
            reading_device_type="reading_device_type_example",
            reading_device_operating_from=dateutil_parser('1970-01-01T00:00:00.00Z'),
            reading_device_serial="reading_device_serial_example",
            reading_device_geo="reading_device_geo_example",
            reading_device_address="reading_device_address_example",
            user_id="user_id_example",
            user_name="user_name_example",
        ),
    ) # KeepAliveObject | Elementos o Atributos que componen el requerimiento de una transacción, los atributos condicionales y/o opcionales que no sean requeridos para esta transacción no deberán ser enviados.

    # example passing only required values which don't have defaults set
    try:
        # Mensaje que informa si está disponible el Servicio Authorize.
        api_response = api_instance.keep_alive_post(keep_alive_object)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PaymentApi->keep_alive_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **keep_alive_object** | [**KeepAliveObject**](KeepAliveObject.md)| Elementos o Atributos que componen el requerimiento de una transacción, los atributos condicionales y/o opcionales que no sean requeridos para esta transacción no deberán ser enviados. |

### Return type

[**KeepAliveResponseObject**](KeepAliveResponseObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Elementos o Atributos que componen la respuesta a la transacción requerida.  |  -  |
**400** | Bad request. |  -  |
**401** | Authorization information is missing or invalid. |  -  |
**404** | Not Found. |  -  |
**405** | Invalid Method. |  -  |
**500** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **keys_renewal_post**
> KeysRenewalObject keys_renewal_post(keys_renewal_object)

Renovacion de Llaves

Renovacion de llaves

### Example


```python
import time
import openapi_client
from openapi_client.api import payment_api
from openapi_client.model.keys_renewal_object import KeysRenewalObject
from pprint import pprint
# Defining the host is optional and defaults to https://testcodi.multipay.mx:30801/Payments/Authorize/5.6.1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://testcodi.multipay.mx:30801/Payments/Authorize/5.6.1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = payment_api.PaymentApi(api_client)
    keys_renewal_object = KeysRenewalObject(
        keys_renewal=KeysRenewalObjectKeysRenewal(
            company_identification="company_identification_example",
            system_identification="system_identification_example",
            branch_identification="branch_identification_example",
            pos_identification="pos_identification_example",
            request_type="request_type_example",
            pos_type="pos_type_example",
            pos_version="pos_version_example",
            pos_address="pos_address_example",
            pos_serial="pos_serial_example",
            posgeo="posgeo_example",
            reading_device_type="reading_device_type_example",
            reading_device_operating_from=dateutil_parser('1970-01-01T00:00:00.00Z'),
            reading_device_version="reading_device_version_example",
            reading_device_address="reading_device_address_example",
            reading_device_serial="reading_device_serial_example",
            reading_device_geo="reading_device_geo_example",
            user_id="user_id_example",
            user_name="user_name_example",
            timeout=3.14,
            ticket="ticket_example",
            ticket_answer_key="ticket_answer_key_example",
            service_version="service_version_example",
            sequence="sequence_example",
            required_information=[
                SaleObjectSaleRequiredInformation(
                    name="name_example",
                    type="STRING",
                    interpret_for="POS",
                    it_is_defined=True,
                    ui_type="ui_type_example",
                    ui_attributes="ui_attributes_example",
                    value="value_example",
                    label="label_example",
                    min_length=1,
                    max_length=1,
                    validation_expression_type="regex",
                    validation_expression="validation_expression_example",
                    mandatory=True,
                ),
            ],
            block="block_example",
            products=[
                SaleObjectSaleProducts(
                    item=1,
                    name="name_example",
                    code="code_example",
                    quantity=3.14,
                    unit="unit_example",
                    unit_amount=3.14,
                    net_amount=3.14,
                    tax_amount=3.14,
                    total_amount=3.14,
                ),
            ],
            payment_facilitator_id="payment_facilitator_id_example",
            merchant_id="merchant_id_example",
            terminal_id="terminal_id_example",
            terminal_trace=1,
            configuration=SaleResponseObjectSaleResponseConfiguration(
                company=SaleResponseObjectSaleResponseConfigurationCompany(
                    id="id_example",
                    address="address_example",
                    tax_code="tax_code_example",
                    description="description_example",
                    additional_config={},
                ),
                branch=SaleResponseObjectSaleResponseConfigurationBranch(
                    id="id_example",
                    name="name_example",
                    foreign_identifier="foreign_identifier_example",
                    description="description_example",
                    address="address_example",
                    city="city_example",
                    state="state_example",
                    region_code="region_code_example",
                    zip_code="zip_code_example",
                    country_code="country_code_example",
                    category=1,
                    additional_config={},
                ),
            ),
            settlement_batch_number=1,
        ),
    ) # KeysRenewalObject | Elementos o Atributos que componen el requerimiento de una transacción, los atributos condicionales y/o opcionales que no sean requeridos para esta transacción no deberán ser enviados.

    # example passing only required values which don't have defaults set
    try:
        # Renovacion de Llaves
        api_response = api_instance.keys_renewal_post(keys_renewal_object)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PaymentApi->keys_renewal_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **keys_renewal_object** | [**KeysRenewalObject**](KeysRenewalObject.md)| Elementos o Atributos que componen el requerimiento de una transacción, los atributos condicionales y/o opcionales que no sean requeridos para esta transacción no deberán ser enviados. |

### Return type

[**KeysRenewalObject**](KeysRenewalObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Elementos o Atributos que componen la respuesta a la transacción requerida.  |  -  |
**400** | Bad request. |  -  |
**401** | Authorization information is missing or invalid. |  -  |
**404** | Not Found. |  -  |
**405** | Invalid Method. |  -  |
**500** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **order_final_post**
> OrderFinalResponseObject order_final_post(order_final_object)

Reclamar el estatus de la operación de compra.

Con está operación se puede obtener el status de la operación de compra iniciada con PaymentInital. Si la compra ya ha sido liquidada por el cliente o no.

### Example


```python
import time
import openapi_client
from openapi_client.api import payment_api
from openapi_client.model.order_final_response_object import OrderFinalResponseObject
from openapi_client.model.order_final_object import OrderFinalObject
from pprint import pprint
# Defining the host is optional and defaults to https://testcodi.multipay.mx:30801/Payments/Authorize/5.6.1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://testcodi.multipay.mx:30801/Payments/Authorize/5.6.1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = payment_api.PaymentApi(api_client)
    order_final_object = OrderFinalObject(
        order_final=OrderFinalObjectOrderFinal(
            system_identification="system_identification_example",
            company_identification="company_identification_example",
            branch_identification="branch_identification_example",
            pos_identification="pos_identification_example",
            service_version="service_version_example",
            sequence="sequence_example",
            security=[
                SaleObjectSaleSecurity(
                    type="type_example",
                    values=[
                        SaleObjectSaleValues(
                            name="name_example",
                            value=None,
                        ),
                    ],
                ),
            ],
            merchant_identification="merchant_identification_example",
            transaction_identification="transaction_identification_example",
            transaction_description="transaction_description_example",
            payment_token="payment_token_example",
            initial_identification="initial_identification_example",
        ),
    ) # OrderFinalObject | Elementos o Atributos que componen el requerimiento de una transacción, los atributos condicionales y/o opcionales que no sean requeridos para esta transacción no deberán ser enviados.

    # example passing only required values which don't have defaults set
    try:
        # Reclamar el estatus de la operación de compra.
        api_response = api_instance.order_final_post(order_final_object)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PaymentApi->order_final_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_final_object** | [**OrderFinalObject**](OrderFinalObject.md)| Elementos o Atributos que componen el requerimiento de una transacción, los atributos condicionales y/o opcionales que no sean requeridos para esta transacción no deberán ser enviados. |

### Return type

[**OrderFinalResponseObject**](OrderFinalResponseObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Elementos o Atributos que componen la respuesta a la transacción requerida.  |  -  |
**400** | Bad request. |  -  |
**401** | Authorization information is missing or invalid. |  -  |
**404** | Not Found. |  -  |
**405** | Invalid Method. |  -  |
**500** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **order_get_post**
> OrderGetResponseObject order_get_post(order_get_object)

Recuperar la operación iniciada por el comercio, para su compra.

Con este método el cliente podrá recuperar los datos para realizar la compra de un producto o servicio y posteriormente ejecutar la compra con la operación Sale.

### Example


```python
import time
import openapi_client
from openapi_client.api import payment_api
from openapi_client.model.order_get_object import OrderGetObject
from openapi_client.model.order_get_response_object import OrderGetResponseObject
from pprint import pprint
# Defining the host is optional and defaults to https://testcodi.multipay.mx:30801/Payments/Authorize/5.6.1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://testcodi.multipay.mx:30801/Payments/Authorize/5.6.1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = payment_api.PaymentApi(api_client)
    order_get_object = OrderGetObject(
        order_get=OrderGetObjectOrderGet(
            initial_token="initial_token_example",
            service_version="service_version_example",
            sequence="sequence_example",
            security=[
                SaleObjectSaleSecurity(
                    type="type_example",
                    values=[
                        SaleObjectSaleValues(
                            name="name_example",
                            value=None,
                        ),
                    ],
                ),
            ],
            payment_facilitator_id="payment_facilitator_id_example",
            merchant_id="merchant_id_example",
            terminal_id="terminal_id_example",
            terminal_trace=1,
            settlement_batch_number=1,
        ),
    ) # OrderGetObject | Elementos o Atributos que componen el requerimiento de una transacción, los atributos condicionales y/o opcionales que no sean requeridos para esta transacción no deberán ser enviados.

    # example passing only required values which don't have defaults set
    try:
        # Recuperar la operación iniciada por el comercio, para su compra.
        api_response = api_instance.order_get_post(order_get_object)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PaymentApi->order_get_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_get_object** | [**OrderGetObject**](OrderGetObject.md)| Elementos o Atributos que componen el requerimiento de una transacción, los atributos condicionales y/o opcionales que no sean requeridos para esta transacción no deberán ser enviados. |

### Return type

[**OrderGetResponseObject**](OrderGetResponseObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Elementos o Atributos que componen la respuesta a la transacción requerida.  |  -  |
**400** | Bad request. |  -  |
**401** | Authorization information is missing or invalid. |  -  |
**404** | Not Found. |  -  |
**405** | Invalid Method. |  -  |
**500** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **order_initial_post**
> OrderInitialResponseObject order_initial_post(order_initial_object)

Indica el inicio de una operación de venta.

Con esta operación el comercio deberá indicar un inicio de transación de venta, mandando toda la información al switch, donde posteriormente el cliente deberá recuperar para realizar la compra.

### Example


```python
import time
import openapi_client
from openapi_client.api import payment_api
from openapi_client.model.order_initial_response_object import OrderInitialResponseObject
from openapi_client.model.order_initial_object import OrderInitialObject
from pprint import pprint
# Defining the host is optional and defaults to https://testcodi.multipay.mx:30801/Payments/Authorize/5.6.1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://testcodi.multipay.mx:30801/Payments/Authorize/5.6.1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = payment_api.PaymentApi(api_client)
    order_initial_object = OrderInitialObject(
        order_initial=OrderInitialObjectOrderInitial(
            system_identification="system_identification_example",
            company_identification="company_identification_example",
            branch_identification="branch_identification_example",
            pos_identification="pos_identification_example",
            required_information=[
                DebtPaymentObjectDebtPaymentRequiredInformation(
                    name="name_example",
                    type="STRING",
                    interpret_for="POS",
                    it_is_defined=True,
                    ui_type="ui_type_example",
                    ui_attributes="ui_attributes_example",
                    value="value_example",
                    label="label_example",
                    min_length=1,
                    max_length=1,
                    validation_expression_type="regex",
                    validation_expression="validation_expression_example",
                    mandatory=True,
                ),
            ],
            service_version="service_version_example",
            sequence="sequence_example",
            security=[
                SaleObjectSaleSecurity(
                    type="type_example",
                    values=[
                        SaleObjectSaleValues(
                            name="name_example",
                            value=None,
                        ),
                    ],
                ),
            ],
            merchant_notify_url="merchant_notify_url_example",
            merchant_redirect_url="merchant_redirect_url_example",
            date_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            transaction_identification="transaction_identification_example",
            transaction_description="transaction_description_example",
            merchant_identification="merchant_identification_example",
            installments=1,
            facility_type=1,
            currency_code="484",
            amount=3.14,
            net_amount="net_amount_example",
            payer=SaleObjectSalePayer(
                identification="identification_example",
                identification_type="PAS",
                email="email_example",
                document_type="PAS",
                document_number="document_number_example",
                first_name="first_name_example",
                last_name="last_name_example",
                middle_name="middle_name_example",
                abbreviated_name="abbreviated_name_example",
                phone="phone_example",
                zip_code="zip_code_example",
                address_street="address_street_example",
                address_number="address_number_example",
                address_internal="address_internal_example",
                address_suburb="address_suburb_example",
                address_delegation="address_delegation_example",
                city="city_example",
                state="state_example",
                country="country_example",
                category_code=1,
                tax_category_type="tax_category_type_example",
                tax_identification_type="tax_identification_type_example",
                tax_identification="tax_identification_example",
                notify_url="notify_url_example",
            ),
            customer=SaleObjectSaleCustomer(
                identification="identification_example",
                identification_type="PAS",
                email="email_example",
                document_type="PAS",
                document_number="document_number_example",
                first_name="first_name_example",
                last_name="last_name_example",
                middle_name="middle_name_example",
                abbreviated_name="abbreviated_name_example",
                phone="phone_example",
                zip_code="zip_code_example",
                address_street="address_street_example",
                address_number="address_number_example",
                address_internal="address_internal_example",
                address_suburb="address_suburb_example",
                address_delegation="address_delegation_example",
                city="city_example",
                state="state_example",
                country="country_example",
                category_code=1,
                tax_category_type="tax_category_type_example",
                tax_identification_type="tax_identification_type_example",
                tax_identification="tax_identification_example",
                notify_url="notify_url_example",
            ),
            seller=SaleObjectSaleSeller(
                identification="identification_example",
                identification_type="PAS",
                email="email_example",
                document_type="PAS",
                document_number="document_number_example",
                first_name="first_name_example",
                last_name="last_name_example",
                middle_name="middle_name_example",
                abbreviated_name="abbreviated_name_example",
                phone="phone_example",
                zip_code="zip_code_example",
                address_street="address_street_example",
                address_number="address_number_example",
                address_internal="address_internal_example",
                address_suburb="address_suburb_example",
                address_delegation="address_delegation_example",
                city="city_example",
                state="state_example",
                country="country_example",
                category_code=1,
                tax_category_type="tax_category_type_example",
                tax_identification_type="tax_identification_type_example",
                tax_identification="tax_identification_example",
                notify_url="notify_url_example",
            ),
            products=[
                SaleResponseObjectSaleResponseProducts(
                    item=1,
                    name="name_example",
                    code="code_example",
                    quantity=3.14,
                    unit="unit_example",
                    unit_amount=3.14,
                    net_amount=3.14,
                    tax_amount=3.14,
                    total_amount=3.14,
                ),
            ],
            tax_refund_type="tax_refund_type_example",
            valid_thru=dateutil_parser('1970-01-01T00:00:00.00Z'),
        ),
    ) # OrderInitialObject | Elementos o Atributos que componen el requerimiento de una transacción, los atributos condicionales y/o opcionales que no sean requeridos para esta transacción no deberán ser enviados.

    # example passing only required values which don't have defaults set
    try:
        # Indica el inicio de una operación de venta.
        api_response = api_instance.order_initial_post(order_initial_object)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PaymentApi->order_initial_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_initial_object** | [**OrderInitialObject**](OrderInitialObject.md)| Elementos o Atributos que componen el requerimiento de una transacción, los atributos condicionales y/o opcionales que no sean requeridos para esta transacción no deberán ser enviados. |

### Return type

[**OrderInitialResponseObject**](OrderInitialResponseObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Elementos o Atributos que componen la respuesta a la transacción requerida.  |  -  |
**400** | Bad request. |  -  |
**401** | Authorization information is missing or invalid. |  -  |
**404** | Not Found. |  -  |
**405** | Invalid Method. |  -  |
**500** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **order_status_post**
> OrderStatusResponseObject order_status_post(order_status_object)

Recuperación del Estado de una Transacción Iniciada por el OrderInitial.

Si se desea recuperar el estado de una transacción iniciada, se deberá enviar una petición a este endpoint con los datos requeridos a continuación.

### Example


```python
import time
import openapi_client
from openapi_client.api import payment_api
from openapi_client.model.order_status_response_object import OrderStatusResponseObject
from openapi_client.model.order_status_object import OrderStatusObject
from pprint import pprint
# Defining the host is optional and defaults to https://testcodi.multipay.mx:30801/Payments/Authorize/5.6.1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://testcodi.multipay.mx:30801/Payments/Authorize/5.6.1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = payment_api.PaymentApi(api_client)
    order_status_object = OrderStatusObject(
        order_status=OrderStatusObjectOrderStatus(
            company_identification="company_identification_example",
            system_identification="system_identification_example",
            branch_identification="branch_identification_example",
            pos_identification="pos_identification_example",
            request_type="request_type_example",
            service_version="service_version_example",
            sequence="sequence_example",
            security=[
                SaleObjectSaleSecurity(
                    type="type_example",
                    values=[
                        SaleObjectSaleValues(
                            name="name_example",
                            value=None,
                        ),
                    ],
                ),
            ],
            block="block_example",
            required_information=[
                SaleObjectSaleRequiredInformation(
                    name="name_example",
                    type="STRING",
                    interpret_for="POS",
                    it_is_defined=True,
                    ui_type="ui_type_example",
                    ui_attributes="ui_attributes_example",
                    value="value_example",
                    label="label_example",
                    min_length=1,
                    max_length=1,
                    validation_expression_type="regex",
                    validation_expression="validation_expression_example",
                    mandatory=True,
                ),
            ],
            input_tokens=[
                SaleObjectSaleInputTokens(
                    name="name_example",
                    value="value_example",
                ),
            ],
            ticket="ticket_example",
            ticket_answer_key="ticket_answer_key_example",
            timeout=3.14,
            request_key="request_key_example",
            merchant_notify_url="merchant_notify_url_example",
            is_reverse=3.14,
            reverse_reason="TIMEOUT",
            reason_sequence_break="TIMEOUT",
            reference="reference_example",
            transaction_description="transaction_description_example",
            pos_type="pos_type_example",
            pos_version="pos_version_example",
            pos_address="pos_address_example",
            pos_serial="pos_serial_example",
            posgeo="posgeo_example",
            reading_device_type="reading_device_type_example",
            reading_device_operating_from=dateutil_parser('1970-01-01T00:00:00.00Z'),
            reading_device_version="reading_device_version_example",
            reading_device_address="reading_device_address_example",
            reading_device_serial="reading_device_serial_example",
            reading_device_geo="reading_device_geo_example",
            user_id="user_id_example",
            user_name="user_name_example",
            amount=3.14,
            alternative_amount=3.14,
            cashback_amount=3.14,
            tip_amount=3.14,
            promoted_amount=3.14,
            currency_code="484",
            facility_payments=3.14,
            facility_type="facility_type_example",
            plan="plan_example",
            card_read_mode="B",
            card_number="card_number_example",
            card_number_masked="card_number_masked_example",
            card_number_encrypted="card_number_encrypted_example",
            card_exp="card_exp_example",
            track1="track1_example",
            track2="track2_example",
            security_code="security_code_example",
            pin="pin_example",
            card_cryptogram="card_cryptogram_example",
            credential_token="credential_token_example",
            credential_issuer_token="credential_issuer_token_example",
            card_app_name="card_app_name_example",
            card_app_identifier="card_app_identifier_example",
            card_app_label="card_app_label_example",
            card_auth_request_cryptogram="card_auth_request_cryptogram_example",
            card_auth_response_cryptogram="card_auth_response_cryptogram_example",
            payer=SaleObjectSalePayer(
                identification="identification_example",
                identification_type="PAS",
                email="email_example",
                document_type="PAS",
                document_number="document_number_example",
                first_name="first_name_example",
                last_name="last_name_example",
                middle_name="middle_name_example",
                abbreviated_name="abbreviated_name_example",
                phone="phone_example",
                zip_code="zip_code_example",
                address_street="address_street_example",
                address_number="address_number_example",
                address_internal="address_internal_example",
                address_suburb="address_suburb_example",
                address_delegation="address_delegation_example",
                city="city_example",
                state="state_example",
                country="country_example",
                category_code=1,
                tax_category_type="tax_category_type_example",
                tax_identification_type="tax_identification_type_example",
                tax_identification="tax_identification_example",
                notify_url="notify_url_example",
            ),
            customer=SaleObjectSaleCustomer(
                identification="identification_example",
                identification_type="PAS",
                email="email_example",
                document_type="PAS",
                document_number="document_number_example",
                first_name="first_name_example",
                last_name="last_name_example",
                middle_name="middle_name_example",
                abbreviated_name="abbreviated_name_example",
                phone="phone_example",
                zip_code="zip_code_example",
                address_street="address_street_example",
                address_number="address_number_example",
                address_internal="address_internal_example",
                address_suburb="address_suburb_example",
                address_delegation="address_delegation_example",
                city="city_example",
                state="state_example",
                country="country_example",
                category_code=1,
                tax_category_type="tax_category_type_example",
                tax_identification_type="tax_identification_type_example",
                tax_identification="tax_identification_example",
                notify_url="notify_url_example",
            ),
            seller=SaleObjectSaleSeller(
                identification="identification_example",
                identification_type="PAS",
                email="email_example",
                document_type="PAS",
                document_number="document_number_example",
                first_name="first_name_example",
                last_name="last_name_example",
                middle_name="middle_name_example",
                abbreviated_name="abbreviated_name_example",
                phone="phone_example",
                zip_code="zip_code_example",
                address_street="address_street_example",
                address_number="address_number_example",
                address_internal="address_internal_example",
                address_suburb="address_suburb_example",
                address_delegation="address_delegation_example",
                city="city_example",
                state="state_example",
                country="country_example",
                category_code=1,
                tax_category_type="tax_category_type_example",
                tax_identification_type="tax_identification_type_example",
                tax_identification="tax_identification_example",
                notify_url="notify_url_example",
            ),
            products=[
                SaleObjectSaleProducts(
                    item=1,
                    name="name_example",
                    code="code_example",
                    quantity=3.14,
                    unit="unit_example",
                    unit_amount=3.14,
                    net_amount=3.14,
                    tax_amount=3.14,
                    total_amount=3.14,
                ),
            ],
            tax_refund_type="tax_refund_type_example",
            auth_code="auth_code_example",
        ),
    ) # OrderStatusObject | Elementos o Atributos que componen el requerimiento de una transacción, los atributos condicionales y/o opcionales que no sean requeridos para esta transacción no deberán ser enviados.

    # example passing only required values which don't have defaults set
    try:
        # Recuperación del Estado de una Transacción Iniciada por el OrderInitial.
        api_response = api_instance.order_status_post(order_status_object)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PaymentApi->order_status_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_status_object** | [**OrderStatusObject**](OrderStatusObject.md)| Elementos o Atributos que componen el requerimiento de una transacción, los atributos condicionales y/o opcionales que no sean requeridos para esta transacción no deberán ser enviados. |

### Return type

[**OrderStatusResponseObject**](OrderStatusResponseObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Elementos o Atributos que componen la respuesta a la transacción requerida.  |  -  |
**400** | Bad request. |  -  |
**401** | Authorization information is missing or invalid. |  -  |
**404** | Not Found. |  -  |
**405** | Invalid Method. |  -  |
**500** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payment_method_post**
> PaymentMethodResponseObject payment_method_post(payment_method_object)

Consulta de  \"planes\" financieros para un Medio de Pago.

Los Planes financieros indican cuotas, diferimiento, monedas, rangos de importe, modos de ingreso y otros atributos de configuración permitidos. Utilizado si se desea conocer los planes financieros relaciónados a un número de tarjeta/Token/Identificador Alternativo especificado. Si es un número de Tarjeta, el mismo podrá estar enmascarado.

### Example


```python
import time
import openapi_client
from openapi_client.api import payment_api
from openapi_client.model.payment_method_response_object import PaymentMethodResponseObject
from openapi_client.model.payment_method_object import PaymentMethodObject
from pprint import pprint
# Defining the host is optional and defaults to https://testcodi.multipay.mx:30801/Payments/Authorize/5.6.1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://testcodi.multipay.mx:30801/Payments/Authorize/5.6.1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = payment_api.PaymentApi(api_client)
    payment_method_object = PaymentMethodObject(
        payment_method=PaymentMethodObjectPaymentMethod(
            company_identification="company_identification_example",
            system_identification="system_identification_example",
            branch_identification="branch_identification_example",
            pos_identification="pos_identification_example",
            request_type="request_type_example",
            service_version="service_version_example",
            sequence="sequence_example",
            security=[
                SaleObjectSaleSecurity(
                    type="type_example",
                    values=[
                        SaleObjectSaleValues(
                            name="name_example",
                            value=None,
                        ),
                    ],
                ),
            ],
            block="block_example",
            ticket="ticket_example",
            ticket_answer_key="ticket_answer_key_example",
            timeout=3.14,
            request_key="request_key_example",
            reason_sequence_break="reason_sequence_break_example",
            transaction_type="transaction_type_example",
            pos_type="pos_type_example",
            pos_version="pos_version_example",
            pos_address="pos_address_example",
            pos_serial="pos_serial_example",
            posgeo="posgeo_example",
            reading_device_type="reading_device_type_example",
            reading_device_operating_from=dateutil_parser('1970-01-01T00:00:00.00Z'),
            reading_device_version="reading_device_version_example",
            reading_device_address="reading_device_address_example",
            reading_device_serial="reading_device_serial_example",
            reading_device_geo="reading_device_geo_example",
            user_id="user_id_example",
            user_name="user_name_example",
            amount=3.14,
            alternative_amount=3.14,
            currency_code="484",
            facility_payments=3.14,
            facility_type="facility_type_example",
            card_app_name="card_app_name_example",
            card_app_identifier="card_app_identifier_example",
            card_app_label="card_app_label_example",
            card_auth_request_cryptogram="card_auth_request_cryptogram_example",
            card_auth_response_cryptogram="card_auth_response_cryptogram_example",
            card_read_mode="B",
            card_number="card_number_example",
            card_number_masked="card_number_masked_example",
            payment_method_id=1,
            payment_method_foreign_identifier=1,
            orig_transaction_type="Return",
            issuer="issuer_example",
            get_dinamic_plans=3.14,
            payment_facilitator_id="payment_facilitator_id_example",
            merchant_id="merchant_id_example",
        ),
    ) # PaymentMethodObject | Elementos o Atributos que componen el requerimiento de una transacción, los atributos condicionales y/o opcionales que no sean requeridos para esta transacción no deberán ser enviados.

    # example passing only required values which don't have defaults set
    try:
        # Consulta de  \"planes\" financieros para un Medio de Pago.
        api_response = api_instance.payment_method_post(payment_method_object)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PaymentApi->payment_method_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_method_object** | [**PaymentMethodObject**](PaymentMethodObject.md)| Elementos o Atributos que componen el requerimiento de una transacción, los atributos condicionales y/o opcionales que no sean requeridos para esta transacción no deberán ser enviados. |

### Return type

[**PaymentMethodResponseObject**](PaymentMethodResponseObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Elementos o Atributos que componen la respuesta a la transacción requerida.  |  -  |
**400** | Bad request. |  -  |
**401** | Authorization information is missing or invalid. |  -  |
**404** | Not Found. |  -  |
**405** | Invalid Method. |  -  |
**500** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payment_methods_post**
> PaymentMethodsResponseObject payment_methods_post(payment_methods_object)

Consulta de los Medios de Pago  disponibles.

Utilizado para obtener la lista de los medios de pagos disponibles, para quien está realizando el requerimiento.

### Example


```python
import time
import openapi_client
from openapi_client.api import payment_api
from openapi_client.model.payment_methods_response_object import PaymentMethodsResponseObject
from openapi_client.model.payment_methods_object import PaymentMethodsObject
from pprint import pprint
# Defining the host is optional and defaults to https://testcodi.multipay.mx:30801/Payments/Authorize/5.6.1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://testcodi.multipay.mx:30801/Payments/Authorize/5.6.1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = payment_api.PaymentApi(api_client)
    payment_methods_object = PaymentMethodsObject(
        payment_methods=PaymentMethodsObjectPaymentMethods(
            company_identification="company_identification_example",
            system_identification="system_identification_example",
            branch_identification="branch_identification_example",
            pos_identification="pos_identification_example",
            service_version="service_version_example",
            sequence="sequence_example",
            security=[
                SaleObjectSaleSecurity(
                    type="type_example",
                    values=[
                        SaleObjectSaleValues(
                            name="name_example",
                            value=None,
                        ),
                    ],
                ),
            ],
        ),
    ) # PaymentMethodsObject | Elementos o Atributos que componen el requerimiento de una transacción, los atributos condicionales y/o opcionales que no sean requeridos para esta transacción no deberán ser enviados.

    # example passing only required values which don't have defaults set
    try:
        # Consulta de los Medios de Pago  disponibles.
        api_response = api_instance.payment_methods_post(payment_methods_object)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PaymentApi->payment_methods_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_methods_object** | [**PaymentMethodsObject**](PaymentMethodsObject.md)| Elementos o Atributos que componen el requerimiento de una transacción, los atributos condicionales y/o opcionales que no sean requeridos para esta transacción no deberán ser enviados. |

### Return type

[**PaymentMethodsResponseObject**](PaymentMethodsResponseObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Elementos o Atributos que componen la respuesta a la transacción requerida.  |  -  |
**400** | Bad request. |  -  |
**401** | Authorization information is missing or invalid. |  -  |
**404** | Not Found. |  -  |
**405** | Invalid Method. |  -  |
**500** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_companies_post**
> QueryCompaniesResponseObject query_companies_post(query_companies_object)

Consulta de Empresas para el Pago de Servicios o Deuda

Esta operación Entrega la Lista de Empresas o Servicios que pueden ser pagados por la plataforma.

### Example


```python
import time
import openapi_client
from openapi_client.api import payment_api
from openapi_client.model.query_companies_response_object import QueryCompaniesResponseObject
from openapi_client.model.query_companies_object import QueryCompaniesObject
from pprint import pprint
# Defining the host is optional and defaults to https://testcodi.multipay.mx:30801/Payments/Authorize/5.6.1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://testcodi.multipay.mx:30801/Payments/Authorize/5.6.1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = payment_api.PaymentApi(api_client)
    query_companies_object = QueryCompaniesObject(
        query_companies=QueryCompaniesObjectQueryCompanies(
            system_identification="system_identification_example",
            company_identification="company_identification_example",
            branch_identification="branch_identification_example",
            pos_identification="pos_identification_example",
            request_type="request_type_example",
            service_version="service_version_example",
            sequence="sequence_example",
            security=[
                SaleObjectSaleSecurity(
                    type="type_example",
                    values=[
                        SaleObjectSaleValues(
                            name="name_example",
                            value=None,
                        ),
                    ],
                ),
            ],
            block="block_example",
            required_information=[
                DebtPaymentObjectDebtPaymentRequiredInformation(
                    name="name_example",
                    type="STRING",
                    interpret_for="POS",
                    it_is_defined=True,
                    ui_type="ui_type_example",
                    ui_attributes="ui_attributes_example",
                    value="value_example",
                    label="label_example",
                    min_length=1,
                    max_length=1,
                    validation_expression_type="regex",
                    validation_expression="validation_expression_example",
                    mandatory=True,
                ),
            ],
            ticket="ticket_example",
            ticket_answer_key="ticket_answer_key_example",
            transaction_identification="transaction_identification_example",
            transaction_description="transaction_description_example",
            trasaction_date_time="trasaction_date_time_example",
            pos_type="pos_type_example",
            pos_version="pos_version_example",
            pos_address="pos_address_example",
            pos_serial="pos_serial_example",
            posgeo="posgeo_example",
            reading_device_type="reading_device_type_example",
            reading_device_operating_from=dateutil_parser('1970-01-01T00:00:00.00Z'),
            reading_device_version="reading_device_version_example",
            reading_device_address="reading_device_address_example",
            reading_device_serial="reading_device_serial_example",
            reading_device_geo="reading_device_geo_example",
            user_id="user_id_example",
            user_name="user_name_example",
            line_of_business_identification="line_of_business_identification_example",
            payment_facilitator_id="payment_facilitator_id_example",
            merchant_id="merchant_id_example",
            terminal_id="terminal_id_example",
            terminal_trace=1,
            settlement_batch_number=1,
        ),
    ) # QueryCompaniesObject | Objeto que contendrá los datos del Requerimiento para obtener la lista de Empresas.

    # example passing only required values which don't have defaults set
    try:
        # Consulta de Empresas para el Pago de Servicios o Deuda
        api_response = api_instance.query_companies_post(query_companies_object)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PaymentApi->query_companies_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_companies_object** | [**QueryCompaniesObject**](QueryCompaniesObject.md)| Objeto que contendrá los datos del Requerimiento para obtener la lista de Empresas. |

### Return type

[**QueryCompaniesResponseObject**](QueryCompaniesResponseObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Un objeto con un nodo principal llamado \&quot;QueryCompaniesResponse\&quot;. Dentro de él, estará presente toda la información con el resultado que nos informa el host sobre la operación que intentamos realizar. |  -  |
**400** | Bad request. |  -  |
**401** | Authorization information is missing or invalid. |  -  |
**404** | Not Found. |  -  |
**405** | Invalid Method. |  -  |
**500** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_line_of_business_post**
> QueryLineOfBusinessResponseObject query_line_of_business_post(query_line_of_business_object)

Consulta de Rubros de Empresas para el Pago de Servicios o Deuda

Esta operación entrega la Lista de Rubros que pueden ser pagados por la plataforma.

### Example


```python
import time
import openapi_client
from openapi_client.api import payment_api
from openapi_client.model.query_line_of_business_response_object import QueryLineOfBusinessResponseObject
from openapi_client.model.query_line_of_business_object import QueryLineOfBusinessObject
from pprint import pprint
# Defining the host is optional and defaults to https://testcodi.multipay.mx:30801/Payments/Authorize/5.6.1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://testcodi.multipay.mx:30801/Payments/Authorize/5.6.1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = payment_api.PaymentApi(api_client)
    query_line_of_business_object = QueryLineOfBusinessObject(
        query_line_of_business=QueryLineOfBusinessObjectQueryLineOfBusiness(
            company_identification="company_identification_example",
            system_identification="system_identification_example",
            branch_identification="branch_identification_example",
            pos_identification="pos_identification_example",
            request_type="request_type_example",
            service_version="service_version_example",
            sequence="sequence_example",
            security=[
                SaleObjectSaleSecurity(
                    type="type_example",
                    values=[
                        SaleObjectSaleValues(
                            name="name_example",
                            value=None,
                        ),
                    ],
                ),
            ],
            block="block_example",
            required_information=[
                SaleObjectSaleRequiredInformation(
                    name="name_example",
                    type="STRING",
                    interpret_for="POS",
                    it_is_defined=True,
                    ui_type="ui_type_example",
                    ui_attributes="ui_attributes_example",
                    value="value_example",
                    label="label_example",
                    min_length=1,
                    max_length=1,
                    validation_expression_type="regex",
                    validation_expression="validation_expression_example",
                    mandatory=True,
                ),
            ],
            ticket="ticket_example",
            ticket_answer_key="ticket_answer_key_example",
            transaction_identification="transaction_identification_example",
            transaction_description="transaction_description_example",
            trasaction_date_time="trasaction_date_time_example",
            pos_type="pos_type_example",
            pos_version="pos_version_example",
            pos_address="pos_address_example",
            pos_serial="pos_serial_example",
            posgeo="posgeo_example",
            reading_device_type="reading_device_type_example",
            reading_device_operating_from=dateutil_parser('1970-01-01T00:00:00.00Z'),
            reading_device_version="reading_device_version_example",
            reading_device_address="reading_device_address_example",
            reading_device_serial="reading_device_serial_example",
            reading_device_geo="reading_device_geo_example",
            user_id="user_id_example",
            user_name="user_name_example",
            payment_facilitator_id="payment_facilitator_id_example",
            merchant_id="merchant_id_example",
            terminal_id="terminal_id_example",
            terminal_trace=1,
            settlement_batch_number=1,
        ),
    ) # QueryLineOfBusinessObject | Objeto que contendrá los datos del Requerimiento para obtener la lista de Rubros.

    # example passing only required values which don't have defaults set
    try:
        # Consulta de Rubros de Empresas para el Pago de Servicios o Deuda
        api_response = api_instance.query_line_of_business_post(query_line_of_business_object)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PaymentApi->query_line_of_business_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_line_of_business_object** | [**QueryLineOfBusinessObject**](QueryLineOfBusinessObject.md)| Objeto que contendrá los datos del Requerimiento para obtener la lista de Rubros. |

### Return type

[**QueryLineOfBusinessResponseObject**](QueryLineOfBusinessResponseObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Un objeto con un nodo principal llamado \&quot;QueryLineOfBusinessResponse\&quot;. Dentro de eé, estará presente toda la información con el resultado que nos informa el host sobre la operación que intentamos realizar. |  -  |
**400** | Bad request. |  -  |
**401** | Authorization information is missing or invalid. |  -  |
**404** | Not Found. |  -  |
**405** | Invalid Method. |  -  |
**500** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **return_post**
> ReturnResponseObject return_post(return_object)

Realización de una devolución de operación de compra/autorización.

Si se desea enviar una devolución de compra/autorización, se deberá enviar una petición a este endpoint con los datos requeridos a continuación.

### Example


```python
import time
import openapi_client
from openapi_client.api import payment_api
from openapi_client.model.return_object import ReturnObject
from openapi_client.model.return_response_object import ReturnResponseObject
from pprint import pprint
# Defining the host is optional and defaults to https://testcodi.multipay.mx:30801/Payments/Authorize/5.6.1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://testcodi.multipay.mx:30801/Payments/Authorize/5.6.1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = payment_api.PaymentApi(api_client)
    return_object = ReturnObject(
        _return=ReturnObjectReturn(
            company_identification="company_identification_example",
            system_identification="system_identification_example",
            branch_identification="branch_identification_example",
            pos_identification="pos_identification_example",
            request_type="request_type_example",
            request_key="request_key_example",
            service_version="service_version_example",
            sequence="sequence_example",
            security=[
                SaleObjectSaleSecurity(
                    type="type_example",
                    values=[
                        SaleObjectSaleValues(
                            name="name_example",
                            value=None,
                        ),
                    ],
                ),
            ],
            block="block_example",
            required_information=[
                SaleObjectSaleRequiredInformation(
                    name="name_example",
                    type="STRING",
                    interpret_for="POS",
                    it_is_defined=True,
                    ui_type="ui_type_example",
                    ui_attributes="ui_attributes_example",
                    value="value_example",
                    label="label_example",
                    min_length=1,
                    max_length=1,
                    validation_expression_type="regex",
                    validation_expression="validation_expression_example",
                    mandatory=True,
                ),
            ],
            ticket="ticket_example",
            ticket_answer_key="ticket_answer_key_example",
            timeout=3.14,
            merchant_notify_url="merchant_notify_url_example",
            is_reverse=3.14,
            reverse_reason="TIMEOUT",
            reason_sequence_break="TIMEOUT",
            reference="reference_example",
            transaction_description="transaction_description_example",
            pos_type="pos_type_example",
            pos_version="pos_version_example",
            pos_address="pos_address_example",
            pos_serial="pos_serial_example",
            posgeo="posgeo_example",
            reading_device_type="reading_device_type_example",
            reading_device_operating_from=dateutil_parser('1970-01-01T00:00:00.00Z'),
            reading_device_version="reading_device_version_example",
            reading_device_address="reading_device_address_example",
            reading_device_serial="reading_device_serial_example",
            reading_device_geo="reading_device_geo_example",
            user_id="user_id_example",
            user_name="user_name_example",
            amount=3.14,
            alternative_amount=3.14,
            cashback_amount=3.14,
            tip_amount=3.14,
            promoted_amount=3.14,
            currency_code="484",
            facility_payments=3.14,
            facility_type="facility_type_example",
            plan="plan_example",
            card_read_mode="B",
            card_get_mode="card_get_mode_example",
            card_number="card_number_example",
            card_number_masked="card_number_masked_example",
            card_number_encrypted="card_number_encrypted_example",
            card_exp="card_exp_example",
            card_cryptogram="card_cryptogram_example",
            card_app_name="card_app_name_example",
            card_app_identifier="card_app_identifier_example",
            card_app_label="card_app_label_example",
            card_auth_request_cryptogram="card_auth_request_cryptogram_example",
            card_auth_response_cryptogram="card_auth_response_cryptogram_example",
            track1="track1_example",
            track2="track2_example",
            input_tokens=[
                SaleObjectSaleInputTokens(
                    name="name_example",
                    value="value_example",
                ),
            ],
            security_code="security_code_example",
            pin="pin_example",
            credential_token="credential_token_example",
            credential_issuer_token="credential_issuer_token_example",
            payer=SaleObjectSalePayer(
                identification="identification_example",
                identification_type="PAS",
                email="email_example",
                document_type="PAS",
                document_number="document_number_example",
                first_name="first_name_example",
                last_name="last_name_example",
                middle_name="middle_name_example",
                abbreviated_name="abbreviated_name_example",
                phone="phone_example",
                zip_code="zip_code_example",
                address_street="address_street_example",
                address_number="address_number_example",
                address_internal="address_internal_example",
                address_suburb="address_suburb_example",
                address_delegation="address_delegation_example",
                city="city_example",
                state="state_example",
                country="country_example",
                category_code=1,
                tax_category_type="tax_category_type_example",
                tax_identification_type="tax_identification_type_example",
                tax_identification="tax_identification_example",
                notify_url="notify_url_example",
            ),
            customer=SaleObjectSaleCustomer(
                identification="identification_example",
                identification_type="PAS",
                email="email_example",
                document_type="PAS",
                document_number="document_number_example",
                first_name="first_name_example",
                last_name="last_name_example",
                middle_name="middle_name_example",
                abbreviated_name="abbreviated_name_example",
                phone="phone_example",
                zip_code="zip_code_example",
                address_street="address_street_example",
                address_number="address_number_example",
                address_internal="address_internal_example",
                address_suburb="address_suburb_example",
                address_delegation="address_delegation_example",
                city="city_example",
                state="state_example",
                country="country_example",
                category_code=1,
                tax_category_type="tax_category_type_example",
                tax_identification_type="tax_identification_type_example",
                tax_identification="tax_identification_example",
                notify_url="notify_url_example",
            ),
            seller=SaleObjectSaleSeller(
                identification="identification_example",
                identification_type="PAS",
                email="email_example",
                document_type="PAS",
                document_number="document_number_example",
                first_name="first_name_example",
                last_name="last_name_example",
                middle_name="middle_name_example",
                abbreviated_name="abbreviated_name_example",
                phone="phone_example",
                zip_code="zip_code_example",
                address_street="address_street_example",
                address_number="address_number_example",
                address_internal="address_internal_example",
                address_suburb="address_suburb_example",
                address_delegation="address_delegation_example",
                city="city_example",
                state="state_example",
                country="country_example",
                category_code=1,
                tax_category_type="tax_category_type_example",
                tax_identification_type="tax_identification_type_example",
                tax_identification="tax_identification_example",
                notify_url="notify_url_example",
            ),
            products=[
                SaleObjectSaleProducts(
                    item=1,
                    name="name_example",
                    code="code_example",
                    quantity=3.14,
                    unit="unit_example",
                    unit_amount=3.14,
                    net_amount=3.14,
                    tax_amount=3.14,
                    total_amount=3.14,
                ),
            ],
            orig_answer_key="orig_answer_key_example",
            orig_reference="orig_reference_example",
            orig_foreign_block="orig_foreign_block_example",
            orig_auth_date_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            orig_auth_ticket=1,
            orig_merchant_id="orig_merchant_id_example",
            orig_terminal_id=1,
            tax_refund_type="tax_refund_type_example",
            auth_code="auth_code_example",
            payment_facilitator_id="payment_facilitator_id_example",
            merchant_id="merchant_id_example",
            terminal_id="terminal_id_example",
            terminal_trace=1,
            settlement_batch_number=1,
        ),
    ) # ReturnObject | Elementos o Atributos que componen el requerimiento de una transacción, los atributos condicionales y/o opcionales que no sean requeridos para esta transacción no deberán ser enviados.

    # example passing only required values which don't have defaults set
    try:
        # Realización de una devolución de operación de compra/autorización.
        api_response = api_instance.return_post(return_object)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PaymentApi->return_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **return_object** | [**ReturnObject**](ReturnObject.md)| Elementos o Atributos que componen el requerimiento de una transacción, los atributos condicionales y/o opcionales que no sean requeridos para esta transacción no deberán ser enviados. |

### Return type

[**ReturnResponseObject**](ReturnResponseObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Elementos o Atributos que componen la respuesta a la transacción requerida.  |  -  |
**400** | Bad request. |  -  |
**401** | Authorization information is missing or invalid. |  -  |
**404** | Not Found. |  -  |
**405** | Invalid Method. |  -  |
**500** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sale_post**
> SaleResponseObject sale_post(sale_object)

Realización de una compra/Autorización de compra

Si se desea enviar una compra/autorización, se deberá enviar una petición a este endpoint con los datos requeridos a continuación.

### Example


```python
import time
import openapi_client
from openapi_client.api import payment_api
from openapi_client.model.sale_object import SaleObject
from openapi_client.model.sale_response_object import SaleResponseObject
from pprint import pprint
# Defining the host is optional and defaults to https://testcodi.multipay.mx:30801/Payments/Authorize/5.6.1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://testcodi.multipay.mx:30801/Payments/Authorize/5.6.1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = payment_api.PaymentApi(api_client)
    sale_object = SaleObject(
        sale=SaleObjectSale(
            company_identification="company_identification_example",
            system_identification="system_identification_example",
            branch_identification="branch_identification_example",
            pos_identification="pos_identification_example",
            request_type="request_type_example",
            request_key="request_key_example",
            service_version="service_version_example",
            sequence="sequence_example",
            security=[
                SaleObjectSaleSecurity(
                    type="type_example",
                    values=[
                        SaleObjectSaleValues(
                            name="name_example",
                            value=None,
                        ),
                    ],
                ),
            ],
            block="block_example",
            required_information=[
                SaleObjectSaleRequiredInformation(
                    name="name_example",
                    type="STRING",
                    interpret_for="POS",
                    it_is_defined=True,
                    ui_type="ui_type_example",
                    ui_attributes="ui_attributes_example",
                    value="value_example",
                    label="label_example",
                    min_length=1,
                    max_length=1,
                    validation_expression_type="regex",
                    validation_expression="validation_expression_example",
                    mandatory=True,
                ),
            ],
            ticket="ticket_example",
            ticket_answer_key="ticket_answer_key_example",
            timeout=3.14,
            merchant_notify_url="merchant_notify_url_example",
            is_reverse=3.14,
            reverse_reason="TIMEOUT",
            reason_sequence_break="TIMEOUT",
            reference="reference_example",
            transaction_description="transaction_description_example",
            pos_type="pos_type_example",
            pos_version="pos_version_example",
            pos_address="pos_address_example",
            pos_serial="pos_serial_example",
            posgeo="posgeo_example",
            reading_device_type="reading_device_type_example",
            reading_device_operating_from=dateutil_parser('1970-01-01T00:00:00.00Z'),
            reading_device_version="reading_device_version_example",
            reading_device_address="reading_device_address_example",
            reading_device_serial="reading_device_serial_example",
            reading_device_geo="reading_device_geo_example",
            user_id="user_id_example",
            user_name="user_name_example",
            amount=3.14,
            alternative_amount=3.14,
            cashback_amount=3.14,
            tip_amount=3.14,
            promoted_amount=3.14,
            currency_code="484",
            facility_payments=3.14,
            facility_type="facility_type_example",
            plan="plan_example",
            card_read_mode="B",
            card_get_mode="card_get_mode_example",
            card_number="card_number_example",
            card_number_masked="card_number_masked_example",
            card_number_encrypted="card_number_encrypted_example",
            card_exp="card_exp_example",
            card_cryptogram="card_cryptogram_example",
            card_app_name="card_app_name_example",
            card_app_identifier="card_app_identifier_example",
            card_app_label="card_app_label_example",
            card_auth_request_cryptogram="card_auth_request_cryptogram_example",
            card_auth_response_cryptogram="card_auth_response_cryptogram_example",
            track1="track1_example",
            track2="track2_example",
            input_tokens=[
                SaleObjectSaleInputTokens(
                    name="name_example",
                    value="value_example",
                ),
            ],
            security_code="security_code_example",
            pin="pin_example",
            credential_token="credential_token_example",
            credential_issuer_token="credential_issuer_token_example",
            payer=SaleObjectSalePayer(
                identification="identification_example",
                identification_type="PAS",
                email="email_example",
                document_type="PAS",
                document_number="document_number_example",
                first_name="first_name_example",
                last_name="last_name_example",
                middle_name="middle_name_example",
                abbreviated_name="abbreviated_name_example",
                phone="phone_example",
                zip_code="zip_code_example",
                address_street="address_street_example",
                address_number="address_number_example",
                address_internal="address_internal_example",
                address_suburb="address_suburb_example",
                address_delegation="address_delegation_example",
                city="city_example",
                state="state_example",
                country="country_example",
                category_code=1,
                tax_category_type="tax_category_type_example",
                tax_identification_type="tax_identification_type_example",
                tax_identification="tax_identification_example",
                notify_url="notify_url_example",
            ),
            customer=SaleObjectSaleCustomer(
                identification="identification_example",
                identification_type="PAS",
                email="email_example",
                document_type="PAS",
                document_number="document_number_example",
                first_name="first_name_example",
                last_name="last_name_example",
                middle_name="middle_name_example",
                abbreviated_name="abbreviated_name_example",
                phone="phone_example",
                zip_code="zip_code_example",
                address_street="address_street_example",
                address_number="address_number_example",
                address_internal="address_internal_example",
                address_suburb="address_suburb_example",
                address_delegation="address_delegation_example",
                city="city_example",
                state="state_example",
                country="country_example",
                category_code=1,
                tax_category_type="tax_category_type_example",
                tax_identification_type="tax_identification_type_example",
                tax_identification="tax_identification_example",
                notify_url="notify_url_example",
            ),
            seller=SaleObjectSaleSeller(
                identification="identification_example",
                identification_type="PAS",
                email="email_example",
                document_type="PAS",
                document_number="document_number_example",
                first_name="first_name_example",
                last_name="last_name_example",
                middle_name="middle_name_example",
                abbreviated_name="abbreviated_name_example",
                phone="phone_example",
                zip_code="zip_code_example",
                address_street="address_street_example",
                address_number="address_number_example",
                address_internal="address_internal_example",
                address_suburb="address_suburb_example",
                address_delegation="address_delegation_example",
                city="city_example",
                state="state_example",
                country="country_example",
                category_code=1,
                tax_category_type="tax_category_type_example",
                tax_identification_type="tax_identification_type_example",
                tax_identification="tax_identification_example",
                notify_url="notify_url_example",
            ),
            products=[
                SaleObjectSaleProducts(
                    item=1,
                    name="name_example",
                    code="code_example",
                    quantity=3.14,
                    unit="unit_example",
                    unit_amount=3.14,
                    net_amount=3.14,
                    tax_amount=3.14,
                    total_amount=3.14,
                ),
            ],
            tax_refund_type="tax_refund_type_example",
            auth_code="auth_code_example",
            payment_facilitator_id="payment_facilitator_id_example",
            merchant_id="merchant_id_example",
            terminal_id="terminal_id_example",
            terminal_trace=1,
            settlement_batch_number=1,
        ),
    ) # SaleObject | Elementos o Atributos que componen el requerimiento de una transacción, los atributos condicionales y/o opcionales que no sean requeridos para esta transacción no deberán ser enviados.

    # example passing only required values which don't have defaults set
    try:
        # Realización de una compra/Autorización de compra
        api_response = api_instance.sale_post(sale_object)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PaymentApi->sale_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sale_object** | [**SaleObject**](SaleObject.md)| Elementos o Atributos que componen el requerimiento de una transacción, los atributos condicionales y/o opcionales que no sean requeridos para esta transacción no deberán ser enviados. |

### Return type

[**SaleResponseObject**](SaleResponseObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Elementos o Atributos que componen la respuesta a la transacción requerida.  |  -  |
**400** | Bad request. |  -  |
**401** | Authorization information is missing or invalid. |  -  |
**404** | Not Found. |  -  |
**405** | Invalid Method. |  -  |
**500** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settlement_post**
> SettlementResponseObject settlement_post(settlement_object)

Confirmación de un consumo previo.

Operación de confirmación de una autorización sin Captura realizada previamente por la Operación Authorize/AuthorizeSale realizada. (Normalmente en Operaciones de Checking-Checkout). Las Operaciones Settlement, Deposit y Capure son sinómimos, pueden usarse cualquiera de ellas.

### Example


```python
import time
import openapi_client
from openapi_client.api import payment_api
from openapi_client.model.settlement_object import SettlementObject
from openapi_client.model.settlement_response_object import SettlementResponseObject
from pprint import pprint
# Defining the host is optional and defaults to https://testcodi.multipay.mx:30801/Payments/Authorize/5.6.1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://testcodi.multipay.mx:30801/Payments/Authorize/5.6.1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = payment_api.PaymentApi(api_client)
    settlement_object = SettlementObject(
        settlement=SettlementObjectSettlement(
            company_identification="company_identification_example",
            system_identification="system_identification_example",
            branch_identification="branch_identification_example",
            pos_identification="pos_identification_example",
            request_type="request_type_example",
            service_version="service_version_example",
            sequence="sequence_example",
            security=[
                SaleObjectSaleSecurity(
                    type="type_example",
                    values=[
                        SaleObjectSaleValues(
                            name="name_example",
                            value=None,
                        ),
                    ],
                ),
            ],
            block="block_example",
            required_information=[
                SaleObjectSaleRequiredInformation(
                    name="name_example",
                    type="STRING",
                    interpret_for="POS",
                    it_is_defined=True,
                    ui_type="ui_type_example",
                    ui_attributes="ui_attributes_example",
                    value="value_example",
                    label="label_example",
                    min_length=1,
                    max_length=1,
                    validation_expression_type="regex",
                    validation_expression="validation_expression_example",
                    mandatory=True,
                ),
            ],
            ticket="ticket_example",
            ticket_answer_key="ticket_answer_key_example",
            timeout=3.14,
            merchant_notify_url="merchant_notify_url_example",
            is_reverse=3.14,
            reverse_reason="TIMEOUT",
            reason_sequence_break="TIMEOUT",
            pos_type="pos_type_example",
            pos_version="pos_version_example",
            pos_address="pos_address_example",
            pos_serial="pos_serial_example",
            posgeo="posgeo_example",
            reading_device_type="reading_device_type_example",
            reading_device_operating_from=dateutil_parser('1970-01-01T00:00:00.00Z'),
            reading_device_version="reading_device_version_example",
            reading_device_address="reading_device_address_example",
            reading_device_serial="reading_device_serial_example",
            reading_device_geo="reading_device_geo_example",
            user_id="user_id_example",
            user_name="user_name_example",
            amount=3.14,
            amount_charged=3.14,
            card_read_mode="B",
            card_get_mode="B",
            card_number="card_number_example",
            card_number_masked="card_number_masked_example",
            card_number_encrypted="card_number_encrypted_example",
            card_exp="card_exp_example",
            track1="track1_example",
            track2="track2_example",
            security_code="security_code_example",
            pin="pin_example",
            card_cryptogram="card_cryptogram_example",
            credential_token="credential_token_example",
            credential_issuer_token="credential_issuer_token_example",
            card_app_name="card_app_name_example",
            card_app_identifier="card_app_identifier_example",
            card_app_label="card_app_label_example",
            card_auth_request_cryptogram="card_auth_request_cryptogram_example",
            card_auth_response_cryptogram="card_auth_response_cryptogram_example",
            payer=SaleObjectSalePayer(
                identification="identification_example",
                identification_type="PAS",
                email="email_example",
                document_type="PAS",
                document_number="document_number_example",
                first_name="first_name_example",
                last_name="last_name_example",
                middle_name="middle_name_example",
                abbreviated_name="abbreviated_name_example",
                phone="phone_example",
                zip_code="zip_code_example",
                address_street="address_street_example",
                address_number="address_number_example",
                address_internal="address_internal_example",
                address_suburb="address_suburb_example",
                address_delegation="address_delegation_example",
                city="city_example",
                state="state_example",
                country="country_example",
                category_code=1,
                tax_category_type="tax_category_type_example",
                tax_identification_type="tax_identification_type_example",
                tax_identification="tax_identification_example",
                notify_url="notify_url_example",
            ),
            customer=SaleObjectSaleCustomer(
                identification="identification_example",
                identification_type="PAS",
                email="email_example",
                document_type="PAS",
                document_number="document_number_example",
                first_name="first_name_example",
                last_name="last_name_example",
                middle_name="middle_name_example",
                abbreviated_name="abbreviated_name_example",
                phone="phone_example",
                zip_code="zip_code_example",
                address_street="address_street_example",
                address_number="address_number_example",
                address_internal="address_internal_example",
                address_suburb="address_suburb_example",
                address_delegation="address_delegation_example",
                city="city_example",
                state="state_example",
                country="country_example",
                category_code=1,
                tax_category_type="tax_category_type_example",
                tax_identification_type="tax_identification_type_example",
                tax_identification="tax_identification_example",
                notify_url="notify_url_example",
            ),
            seller=SaleObjectSaleSeller(
                identification="identification_example",
                identification_type="PAS",
                email="email_example",
                document_type="PAS",
                document_number="document_number_example",
                first_name="first_name_example",
                last_name="last_name_example",
                middle_name="middle_name_example",
                abbreviated_name="abbreviated_name_example",
                phone="phone_example",
                zip_code="zip_code_example",
                address_street="address_street_example",
                address_number="address_number_example",
                address_internal="address_internal_example",
                address_suburb="address_suburb_example",
                address_delegation="address_delegation_example",
                city="city_example",
                state="state_example",
                country="country_example",
                category_code=1,
                tax_category_type="tax_category_type_example",
                tax_identification_type="tax_identification_type_example",
                tax_identification="tax_identification_example",
                notify_url="notify_url_example",
            ),
            products=[
                SaleObjectSaleProducts(
                    item=1,
                    name="name_example",
                    code="code_example",
                    quantity=3.14,
                    unit="unit_example",
                    unit_amount=3.14,
                    net_amount=3.14,
                    tax_amount=3.14,
                    total_amount=3.14,
                ),
            ],
            tax_refund_type="tax_refund_type_example",
            orig_answer_key="orig_answer_key_example",
            orig_block="orig_block_example",
            orig_foreign_block="orig_foreign_block_example",
            payment_facilitator_id="payment_facilitator_id_example",
            merchant_id="merchant_id_example",
            terminal_id="terminal_id_example",
            terminal_trace=1,
            settlement_batch_number=1,
        ),
    ) # SettlementObject | Elementos o Atributos que componen el requerimiento de una transacción, los atributos condicionales y/o opcionales que no sean requeridos para esta transacción no deberán ser enviados.

    # example passing only required values which don't have defaults set
    try:
        # Confirmación de un consumo previo.
        api_response = api_instance.settlement_post(settlement_object)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PaymentApi->settlement_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settlement_object** | [**SettlementObject**](SettlementObject.md)| Elementos o Atributos que componen el requerimiento de una transacción, los atributos condicionales y/o opcionales que no sean requeridos para esta transacción no deberán ser enviados. |

### Return type

[**SettlementResponseObject**](SettlementResponseObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Cuerpo de la respuesta. Alli se encuentra el resultado de la operación, junto con toda la información relevante. |  -  |
**400** | Bad request. |  -  |
**401** | Authorization information is missing or invalid. |  -  |
**404** | Not Found. |  -  |
**405** | Invalid Method. |  -  |
**500** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_post**
> ValidateResponseObject validate_post(validate_object)

Realización de una Validación

Si se desea enviar una compra/autorización, se deberá enviar una petición a este endpoint con los datos requeridos a continuación.

### Example


```python
import time
import openapi_client
from openapi_client.api import payment_api
from openapi_client.model.validate_object import ValidateObject
from openapi_client.model.validate_response_object import ValidateResponseObject
from pprint import pprint
# Defining the host is optional and defaults to https://testcodi.multipay.mx:30801/Payments/Authorize/5.6.1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://testcodi.multipay.mx:30801/Payments/Authorize/5.6.1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = payment_api.PaymentApi(api_client)
    validate_object = ValidateObject(
        validate=ValidateObjectValidate(
            company_identification="company_identification_example",
            system_identification="system_identification_example",
            branch_identification="branch_identification_example",
            pos_identification="pos_identification_example",
            service_version="service_version_example",
            sequence="sequence_example",
            security=[
                SaleObjectSaleSecurity(
                    type="type_example",
                    values=[
                        SaleObjectSaleValues(
                            name="name_example",
                            value=None,
                        ),
                    ],
                ),
            ],
            block="block_example",
            reason_sequence_break="TIMEOUT",
            reading_device_type="reading_device_type_example",
            reading_device_operating_from=dateutil_parser('1970-01-01T00:00:00.00Z'),
            card_app_name="card_app_name_example",
            card_app_identifier="card_app_identifier_example",
            card_app_label="card_app_label_example",
            card_auth_request_cryptogram="card_auth_request_cryptogram_example",
            card_auth_response_cryptogram="card_auth_response_cryptogram_example",
            card_read_mode="B",
            card_get_mode="card_get_mode_example",
            card_number="card_number_example",
            card_number_masked="card_number_masked_example",
            card_number_encrypted="card_number_encrypted_example",
            card_exp="card_exp_example",
            track1="track1_example",
            track2="track2_example",
            security_code="security_code_example",
            pin="pin_example",
            card_last_four_digits="card_last_four_digits_example",
            payer=SaleObjectSalePayer(
                identification="identification_example",
                identification_type="PAS",
                email="email_example",
                document_type="PAS",
                document_number="document_number_example",
                first_name="first_name_example",
                last_name="last_name_example",
                middle_name="middle_name_example",
                abbreviated_name="abbreviated_name_example",
                phone="phone_example",
                zip_code="zip_code_example",
                address_street="address_street_example",
                address_number="address_number_example",
                address_internal="address_internal_example",
                address_suburb="address_suburb_example",
                address_delegation="address_delegation_example",
                city="city_example",
                state="state_example",
                country="country_example",
                category_code=1,
                tax_category_type="tax_category_type_example",
                tax_identification_type="tax_identification_type_example",
                tax_identification="tax_identification_example",
                notify_url="notify_url_example",
            ),
            customer=SaleObjectSaleCustomer(
                identification="identification_example",
                identification_type="PAS",
                email="email_example",
                document_type="PAS",
                document_number="document_number_example",
                first_name="first_name_example",
                last_name="last_name_example",
                middle_name="middle_name_example",
                abbreviated_name="abbreviated_name_example",
                phone="phone_example",
                zip_code="zip_code_example",
                address_street="address_street_example",
                address_number="address_number_example",
                address_internal="address_internal_example",
                address_suburb="address_suburb_example",
                address_delegation="address_delegation_example",
                city="city_example",
                state="state_example",
                country="country_example",
                category_code=1,
                tax_category_type="tax_category_type_example",
                tax_identification_type="tax_identification_type_example",
                tax_identification="tax_identification_example",
                notify_url="notify_url_example",
            ),
            payment_facilitator_id="payment_facilitator_id_example",
            merchant_id="merchant_id_example",
            terminal_id="terminal_id_example",
            terminal_trace=1,
            settlement_batch_number=1,
        ),
    ) # ValidateObject | Elementos o Atributos que componen el requerimiento de una transacción, los atributos condicionales y/o opcionales que no sean requeridos para esta transacción no deberán ser enviados.

    # example passing only required values which don't have defaults set
    try:
        # Realización de una Validación
        api_response = api_instance.validate_post(validate_object)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PaymentApi->validate_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **validate_object** | [**ValidateObject**](ValidateObject.md)| Elementos o Atributos que componen el requerimiento de una transacción, los atributos condicionales y/o opcionales que no sean requeridos para esta transacción no deberán ser enviados. |

### Return type

[**ValidateResponseObject**](ValidateResponseObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Elementos o Atributos que componen la respuesta a la transacción requerida.  |  -  |
**400** | Bad request. |  -  |
**401** | Authorization information is missing or invalid. |  -  |
**404** | Not Found. |  -  |
**405** | Invalid Method. |  -  |
**500** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **void_debt_payment_post**
> VoidDebtPaymentResponseObject void_debt_payment_post(void_debt_payment_object)

Cancelación de  Pago de Deuda, Saldo o Resumen.

Operación utilizada para anular un Pago de Deuda realizado previamente.

### Example


```python
import time
import openapi_client
from openapi_client.api import payment_api
from openapi_client.model.void_debt_payment_object import VoidDebtPaymentObject
from openapi_client.model.void_debt_payment_response_object import VoidDebtPaymentResponseObject
from pprint import pprint
# Defining the host is optional and defaults to https://testcodi.multipay.mx:30801/Payments/Authorize/5.6.1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://testcodi.multipay.mx:30801/Payments/Authorize/5.6.1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = payment_api.PaymentApi(api_client)
    void_debt_payment_object = VoidDebtPaymentObject(
        void_debt_payment=VoidDebtPaymentObjectVoidDebtPayment(
            company_identification="company_identification_example",
            system_identification="system_identification_example",
            branch_identification="branch_identification_example",
            pos_identification="pos_identification_example",
            request_type="request_type_example",
            service_version="service_version_example",
            sequence="sequence_example",
            security=[
                SaleObjectSaleSecurity(
                    type="type_example",
                    values=[
                        SaleObjectSaleValues(
                            name="name_example",
                            value=None,
                        ),
                    ],
                ),
            ],
            block="block_example",
            required_information=[
                DebtPaymentObjectDebtPaymentRequiredInformation(
                    name="name_example",
                    type="STRING",
                    interpret_for="POS",
                    it_is_defined=True,
                    ui_type="ui_type_example",
                    ui_attributes="ui_attributes_example",
                    value="value_example",
                    label="label_example",
                    min_length=1,
                    max_length=1,
                    validation_expression_type="regex",
                    validation_expression="validation_expression_example",
                    mandatory=True,
                ),
            ],
            ticket="ticket_example",
            ticket_answer_key="ticket_answer_key_example",
            timeout=3.14,
            request_key="request_key_example",
            is_reverse=3.14,
            reverse_reason="TIMEOUT",
            reason_sequence_break="TIMEOUT",
            reference="reference_example",
            orig_reference="orig_reference_example",
            pos_type="pos_type_example",
            pos_version="pos_version_example",
            pos_address="pos_address_example",
            pos_serial="pos_serial_example",
            posgeo="posgeo_example",
            reading_device_type="reading_device_type_example",
            reading_device_operating_from=dateutil_parser('1970-01-01T00:00:00.00Z'),
            reading_device_version="reading_device_version_example",
            reading_device_address="reading_device_address_example",
            reading_device_serial="reading_device_serial_example",
            reading_device_geo="reading_device_geo_example",
            user_id="user_id_example",
            user_name="user_name_example",
            card_read_mode="B",
            card_get_mode="card_get_mode_example",
            card_number="card_number_example",
            card_number_masked="card_number_masked_example",
            card_number_encrypted="card_number_encrypted_example",
            card_exp="card_exp_example",
            track1="track1_example",
            track2="track2_example",
            security_code="security_code_example",
            pin="pin_example",
            card_cryptogram="card_cryptogram_example",
            card_app_name="card_app_name_example",
            card_app_identifier="card_app_identifier_example",
            card_app_label="card_app_label_example",
            card_auth_request_cryptogram="card_auth_request_cryptogram_example",
            card_auth_response_cryptogram="card_auth_response_cryptogram_example",
            credential_token="credential_token_example",
            credential_issuer_token="credential_issuer_token_example",
            input_tokens=[
                SaleObjectSaleInputTokens(
                    name="name_example",
                    value="value_example",
                ),
            ],
            products=[
                VoidDebtPaymentObjectVoidDebtPaymentProducts(
                    item=1,
                    name="name_example",
                    code="code_example",
                    quantity=3.14,
                    unit="unit_example",
                    unit_amount=3.14,
                    net_amount=3.14,
                    tax_amount=3.14,
                    total_amount=3.14,
                ),
            ],
            payment_facilitator_id="payment_facilitator_id_example",
            merchant_id="merchant_id_example",
            terminal_id="terminal_id_example",
            terminal_trace=1,
            settlement_batch_number=1,
        ),
    ) # VoidDebtPaymentObject | Elementos o Atributos que componen el requerimiento de una transacción, los atributos condicionales y/o opcionales que no sean requeridos para esta transacción no deberán ser enviados.

    # example passing only required values which don't have defaults set
    try:
        # Cancelación de  Pago de Deuda, Saldo o Resumen.
        api_response = api_instance.void_debt_payment_post(void_debt_payment_object)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PaymentApi->void_debt_payment_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **void_debt_payment_object** | [**VoidDebtPaymentObject**](VoidDebtPaymentObject.md)| Elementos o Atributos que componen el requerimiento de una transacción, los atributos condicionales y/o opcionales que no sean requeridos para esta transacción no deberán ser enviados. |

### Return type

[**VoidDebtPaymentResponseObject**](VoidDebtPaymentResponseObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Elementos o Atributos que componen la respuesta a la transacción requerida.  |  -  |
**400** | Bad request. |  -  |
**401** | Authorization information is missing or invalid. |  -  |
**404** | Not Found. |  -  |
**405** | Invalid Method. |  -  |
**500** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **void_post**
> VoidResponseObject void_post(void_object)

Operación de Cancelación/Anulación.

Esta operación actúa como un comodín. Cuando el Plataforma procesa un requerimiento de este tipo, dependiendo del tipo de operación original a la que se refiera, del estado de ella, y algunos parámetros más, se enviará finalmente una devolución o una anulación. La forma en la que este tipo de requerimiento opera es la siguiente: si la operación se encuentra abierta (sin haber sido enviado el cierre de lote) y la operación proviene del mismo número de terminal con la cual se realizó la operación original, finalmente la transacción financiera que se enviará al host será una anulación. Por el contrario, si alguna de las condiciones anteriores no se cumple, se realizará una devolución total de la operación original. En ese caso, se debe cumplir que no haya sido devuelta de forma parcial anteriormente. Vale aclarar también que si se el resultado es una anulación, la transacción original podrá ser una compra/autorización, una devolución o un pago de resumen. Sin embargo, si es una devolución, la original solo podrá ser una compra/autorización. Para cualquier otro escenario donde algo de ello no se cumpla, la petición será rechazada.

### Example


```python
import time
import openapi_client
from openapi_client.api import payment_api
from openapi_client.model.void_response_object import VoidResponseObject
from openapi_client.model.void_object import VoidObject
from pprint import pprint
# Defining the host is optional and defaults to https://testcodi.multipay.mx:30801/Payments/Authorize/5.6.1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://testcodi.multipay.mx:30801/Payments/Authorize/5.6.1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = payment_api.PaymentApi(api_client)
    void_object = VoidObject(
        void=VoidObjectVoid(
            company_identification="company_identification_example",
            system_identification="system_identification_example",
            branch_identification="branch_identification_example",
            pos_identification="pos_identification_example",
            request_type="request_type_example",
            request_key="request_key_example",
            orig_answer_key="orig_answer_key_example",
            orig_reference="orig_reference_example",
            service_version="service_version_example",
            sequence="sequence_example",
            security=[
                SaleObjectSaleSecurity(
                    type="type_example",
                    values=[
                        SaleObjectSaleValues(
                            name="name_example",
                            value=None,
                        ),
                    ],
                ),
            ],
            block="block_example",
            required_information=[
                SaleObjectSaleRequiredInformation(
                    name="name_example",
                    type="STRING",
                    interpret_for="POS",
                    it_is_defined=True,
                    ui_type="ui_type_example",
                    ui_attributes="ui_attributes_example",
                    value="value_example",
                    label="label_example",
                    min_length=1,
                    max_length=1,
                    validation_expression_type="regex",
                    validation_expression="validation_expression_example",
                    mandatory=True,
                ),
            ],
            ticket="ticket_example",
            ticket_answer_key="ticket_answer_key_example",
            timeout=3.14,
            merchant_notify_url="merchant_notify_url_example",
            is_reverse=3.14,
            reverse_reason="TIMEOUT",
            reason_sequence_break="TIMEOUT",
            reference="reference_example",
            transaction_description="transaction_description_example",
            pos_type="pos_type_example",
            pos_version="pos_version_example",
            pos_address="pos_address_example",
            pos_serial="pos_serial_example",
            posgeo="posgeo_example",
            reading_device_type="reading_device_type_example",
            reading_device_operating_from=dateutil_parser('1970-01-01T00:00:00.00Z'),
            reading_device_version="reading_device_version_example",
            reading_device_address="reading_device_address_example",
            reading_device_serial="reading_device_serial_example",
            reading_device_geo="reading_device_geo_example",
            user_id="user_id_example",
            user_name="user_name_example",
            amount=3.14,
            alternative_amount=3.14,
            cashback_amount=3.14,
            tip_amount=3.14,
            promoted_amount=3.14,
            currency_code="484",
            facility_payments=3.14,
            facility_type="facility_type_example",
            plan="plan_example",
            card_read_mode="B",
            card_get_mode="card_get_mode_example",
            card_number="card_number_example",
            card_number_masked="card_number_masked_example",
            card_number_encrypted="card_number_encrypted_example",
            card_exp="card_exp_example",
            card_cryptogram="card_cryptogram_example",
            card_app_name="card_app_name_example",
            card_app_identifier="card_app_identifier_example",
            card_app_label="card_app_label_example",
            card_auth_request_cryptogram="card_auth_request_cryptogram_example",
            card_auth_response_cryptogram="card_auth_response_cryptogram_example",
            track1="track1_example",
            track2="track2_example",
            input_tokens=[
                SaleObjectSaleInputTokens(
                    name="name_example",
                    value="value_example",
                ),
            ],
            security_code="security_code_example",
            pin="pin_example",
            credential_token="credential_token_example",
            credential_issuer_token="credential_issuer_token_example",
            payer=SaleObjectSalePayer(
                identification="identification_example",
                identification_type="PAS",
                email="email_example",
                document_type="PAS",
                document_number="document_number_example",
                first_name="first_name_example",
                last_name="last_name_example",
                middle_name="middle_name_example",
                abbreviated_name="abbreviated_name_example",
                phone="phone_example",
                zip_code="zip_code_example",
                address_street="address_street_example",
                address_number="address_number_example",
                address_internal="address_internal_example",
                address_suburb="address_suburb_example",
                address_delegation="address_delegation_example",
                city="city_example",
                state="state_example",
                country="country_example",
                category_code=1,
                tax_category_type="tax_category_type_example",
                tax_identification_type="tax_identification_type_example",
                tax_identification="tax_identification_example",
                notify_url="notify_url_example",
            ),
            customer=SaleObjectSaleCustomer(
                identification="identification_example",
                identification_type="PAS",
                email="email_example",
                document_type="PAS",
                document_number="document_number_example",
                first_name="first_name_example",
                last_name="last_name_example",
                middle_name="middle_name_example",
                abbreviated_name="abbreviated_name_example",
                phone="phone_example",
                zip_code="zip_code_example",
                address_street="address_street_example",
                address_number="address_number_example",
                address_internal="address_internal_example",
                address_suburb="address_suburb_example",
                address_delegation="address_delegation_example",
                city="city_example",
                state="state_example",
                country="country_example",
                category_code=1,
                tax_category_type="tax_category_type_example",
                tax_identification_type="tax_identification_type_example",
                tax_identification="tax_identification_example",
                notify_url="notify_url_example",
            ),
            seller=SaleObjectSaleSeller(
                identification="identification_example",
                identification_type="PAS",
                email="email_example",
                document_type="PAS",
                document_number="document_number_example",
                first_name="first_name_example",
                last_name="last_name_example",
                middle_name="middle_name_example",
                abbreviated_name="abbreviated_name_example",
                phone="phone_example",
                zip_code="zip_code_example",
                address_street="address_street_example",
                address_number="address_number_example",
                address_internal="address_internal_example",
                address_suburb="address_suburb_example",
                address_delegation="address_delegation_example",
                city="city_example",
                state="state_example",
                country="country_example",
                category_code=1,
                tax_category_type="tax_category_type_example",
                tax_identification_type="tax_identification_type_example",
                tax_identification="tax_identification_example",
                notify_url="notify_url_example",
            ),
            products=[
                SaleObjectSaleProducts(
                    item=1,
                    name="name_example",
                    code="code_example",
                    quantity=3.14,
                    unit="unit_example",
                    unit_amount=3.14,
                    net_amount=3.14,
                    tax_amount=3.14,
                    total_amount=3.14,
                ),
            ],
            tax_refund_type="tax_refund_type_example",
            auth_code="auth_code_example",
            payment_facilitator_id="payment_facilitator_id_example",
            merchant_id="merchant_id_example",
            terminal_id="terminal_id_example",
            terminal_trace=1,
            settlement_batch_number=1,
        ),
    ) # VoidObject | Elementos o Atributos que componen el requerimiento de una transacción, los atributos condicionales y/o opcionales que no sean requeridos para esta transacción no deberán ser enviados.

    # example passing only required values which don't have defaults set
    try:
        # Operación de Cancelación/Anulación.
        api_response = api_instance.void_post(void_object)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PaymentApi->void_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **void_object** | [**VoidObject**](VoidObject.md)| Elementos o Atributos que componen el requerimiento de una transacción, los atributos condicionales y/o opcionales que no sean requeridos para esta transacción no deberán ser enviados. |

### Return type

[**VoidResponseObject**](VoidResponseObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Elementos o Atributos que componen la respuesta a la transacción requerida.  |  -  |
**400** | Bad request. |  -  |
**401** | Authorization information is missing or invalid. |  -  |
**404** | Not Found. |  -  |
**405** | Invalid Method. |  -  |
**500** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wallet_request_post**
> WalletRequestResponseObject wallet_request_post(wallet_request_object)

Inicia un transacción contra el Wallet

Esta operación sera utilizada para obtener el código o método de identificación del Wallet.

### Example


```python
import time
import openapi_client
from openapi_client.api import payment_api
from openapi_client.model.wallet_request_object import WalletRequestObject
from openapi_client.model.wallet_request_response_object import WalletRequestResponseObject
from pprint import pprint
# Defining the host is optional and defaults to https://testcodi.multipay.mx:30801/Payments/Authorize/5.6.1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://testcodi.multipay.mx:30801/Payments/Authorize/5.6.1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = payment_api.PaymentApi(api_client)
    wallet_request_object = WalletRequestObject(
        wallet_request=WalletRequestObjectWalletRequest(
            system_identification="system_identification_example",
            company_identification="company_identification_example",
            branch_identification="branch_identification_example",
            pos_identification="pos_identification_example",
            request_type="request_type_example",
            service_version="service_version_example",
            sequence="sequence_example",
            security=[
                SaleObjectSaleSecurity(
                    type="type_example",
                    values=[
                        SaleObjectSaleValues(
                            name="name_example",
                            value=None,
                        ),
                    ],
                ),
            ],
            block="block_example",
            ticket="ticket_example",
            ticket_answer_key="ticket_answer_key_example",
            required_information=[
                DebtPaymentObjectDebtPaymentRequiredInformation(
                    name="name_example",
                    type="STRING",
                    interpret_for="POS",
                    it_is_defined=True,
                    ui_type="ui_type_example",
                    ui_attributes="ui_attributes_example",
                    value="value_example",
                    label="label_example",
                    min_length=1,
                    max_length=1,
                    validation_expression_type="regex",
                    validation_expression="validation_expression_example",
                    mandatory=True,
                ),
            ],
            additional_information=[
                SaleResponseObjectSaleResponseAdditionalInformation(
                    name="name_example",
                    type="STRING",
                    interpret_for="POS",
                    ui_type="ui_type_example",
                    ui_attributes="ui_attributes_example",
                    value="value_example",
                    label="label_example",
                    min_length=1,
                    max_length=1,
                ),
            ],
            request_key="request_key_example",
            merchant_notify_url="merchant_notify_url_example",
            reference="reference_example",
            transaction_type="transaction_type_example",
            transaction_description="transaction_description_example",
            transaction_identification="transaction_identification_example",
            trasaction_date_time="trasaction_date_time_example",
            transaction_timeout=60,
            pos_type="pos_type_example",
            pos_version="pos_version_example",
            pos_address="pos_address_example",
            pos_serial="pos_serial_example",
            posgeo="posgeo_example",
            reading_device_type="reading_device_type_example",
            reading_device_operating_from=dateutil_parser('1970-01-01T00:00:00.00Z'),
            reading_device_version="reading_device_version_example",
            reading_device_address="reading_device_address_example",
            reading_device_serial="reading_device_serial_example",
            reading_device_geo="reading_device_geo_example",
            user_id="user_id_example",
            user_name="user_name_example",
            currency_code="484",
            amount=1.23,
            cashback_amount=3.14,
            tip_amount=3.14,
            wallet_identification="wallet_identification_example",
            payer=SaleObjectSalePayer(
                identification="identification_example",
                identification_type="PAS",
                email="email_example",
                document_type="PAS",
                document_number="document_number_example",
                first_name="first_name_example",
                last_name="last_name_example",
                middle_name="middle_name_example",
                abbreviated_name="abbreviated_name_example",
                phone="phone_example",
                zip_code="zip_code_example",
                address_street="address_street_example",
                address_number="address_number_example",
                address_internal="address_internal_example",
                address_suburb="address_suburb_example",
                address_delegation="address_delegation_example",
                city="city_example",
                state="state_example",
                country="country_example",
                category_code=1,
                tax_category_type="tax_category_type_example",
                tax_identification_type="tax_identification_type_example",
                tax_identification="tax_identification_example",
                notify_url="notify_url_example",
            ),
            customer=SaleObjectSaleCustomer(
                identification="identification_example",
                identification_type="PAS",
                email="email_example",
                document_type="PAS",
                document_number="document_number_example",
                first_name="first_name_example",
                last_name="last_name_example",
                middle_name="middle_name_example",
                abbreviated_name="abbreviated_name_example",
                phone="phone_example",
                zip_code="zip_code_example",
                address_street="address_street_example",
                address_number="address_number_example",
                address_internal="address_internal_example",
                address_suburb="address_suburb_example",
                address_delegation="address_delegation_example",
                city="city_example",
                state="state_example",
                country="country_example",
                category_code=1,
                tax_category_type="tax_category_type_example",
                tax_identification_type="tax_identification_type_example",
                tax_identification="tax_identification_example",
                notify_url="notify_url_example",
            ),
            seller=SaleObjectSaleSeller(
                identification="identification_example",
                identification_type="PAS",
                email="email_example",
                document_type="PAS",
                document_number="document_number_example",
                first_name="first_name_example",
                last_name="last_name_example",
                middle_name="middle_name_example",
                abbreviated_name="abbreviated_name_example",
                phone="phone_example",
                zip_code="zip_code_example",
                address_street="address_street_example",
                address_number="address_number_example",
                address_internal="address_internal_example",
                address_suburb="address_suburb_example",
                address_delegation="address_delegation_example",
                city="city_example",
                state="state_example",
                country="country_example",
                category_code=1,
                tax_category_type="tax_category_type_example",
                tax_identification_type="tax_identification_type_example",
                tax_identification="tax_identification_example",
                notify_url="notify_url_example",
            ),
            products=[
                SaleResponseObjectSaleResponseProducts(
                    item=1,
                    name="name_example",
                    code="code_example",
                    quantity=3.14,
                    unit="unit_example",
                    unit_amount=3.14,
                    net_amount=3.14,
                    tax_amount=3.14,
                    total_amount=3.14,
                ),
            ],
            tax_refund_type="tax_refund_type_example",
            valid_thru=dateutil_parser('1970-01-01T00:00:00.00Z'),
            payment_facilitator_id="payment_facilitator_id_example",
            merchant_id="merchant_id_example",
            terminal_id="terminal_id_example",
            terminal_trace=1,
            settlement_batch_number=1,
        ),
    ) # WalletRequestObject | Objeto que contendrá los datos del Requerimiento para obtener el Requerimeinto del Wallet.

    # example passing only required values which don't have defaults set
    try:
        # Inicia un transacción contra el Wallet
        api_response = api_instance.wallet_request_post(wallet_request_object)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PaymentApi->wallet_request_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_request_object** | [**WalletRequestObject**](WalletRequestObject.md)| Objeto que contendrá los datos del Requerimiento para obtener el Requerimeinto del Wallet. |

### Return type

[**WalletRequestResponseObject**](WalletRequestResponseObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Un objeto con un nodo principal llamado \&quot;WalletRequestResponse\&quot;. Dentro de él, estará presente toda la información con el resultado que nos informa el host sobre la operación que intentamos realizar. |  -  |
**400** | Bad request. |  -  |
**401** | Authorization information is missing or invalid. |  -  |
**404** | Not Found. |  -  |
**405** | Invalid Method. |  -  |
**500** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wallets_post**
> WalletsResponseObject wallets_post(wallets_object)

Obtiene la Lista de Wallets Disponibles

Esta operación es solamente utilizada para obtener la lista de Wallets con las cuales el sistema puede operar.

### Example


```python
import time
import openapi_client
from openapi_client.api import payment_api
from openapi_client.model.wallets_object import WalletsObject
from openapi_client.model.wallets_response_object import WalletsResponseObject
from pprint import pprint
# Defining the host is optional and defaults to https://testcodi.multipay.mx:30801/Payments/Authorize/5.6.1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://testcodi.multipay.mx:30801/Payments/Authorize/5.6.1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = payment_api.PaymentApi(api_client)
    wallets_object = WalletsObject(
        wallets=WalletsObjectWallets(
            system_identification="system_identification_example",
            company_identification="company_identification_example",
            branch_identification="branch_identification_example",
            pos_identification="pos_identification_example",
            request_type="request_type_example",
            service_version="service_version_example",
            sequence="sequence_example",
            security=[
                SaleObjectSaleSecurity(
                    type="type_example",
                    values=[
                        SaleObjectSaleValues(
                            name="name_example",
                            value=None,
                        ),
                    ],
                ),
            ],
            block="block_example",
            ticket="ticket_example",
            ticket_answer_key="ticket_answer_key_example",
            transaction_description="transaction_description_example",
            transaction_identification="transaction_identification_example",
            trasaction_date_time="trasaction_date_time_example",
            pos_type="pos_type_example",
            pos_version="pos_version_example",
            pos_address="pos_address_example",
            pos_serial="pos_serial_example",
            posgeo="posgeo_example",
            reading_device_type="reading_device_type_example",
            reading_device_operating_from=dateutil_parser('1970-01-01T00:00:00.00Z'),
            reading_device_version="reading_device_version_example",
            reading_device_address="reading_device_address_example",
            reading_device_serial="reading_device_serial_example",
            reading_device_geo="reading_device_geo_example",
            user_id="user_id_example",
            user_name="user_name_example",
            payment_facilitator_id="payment_facilitator_id_example",
            merchant_id="merchant_id_example",
            terminal_id="terminal_id_example",
            terminal_trace=1,
            settlement_batch_number=1,
        ),
    ) # WalletsObject | Objeto que contendrá los datos del Requerimiento para obtener los Wallets disponibles.

    # example passing only required values which don't have defaults set
    try:
        # Obtiene la Lista de Wallets Disponibles
        api_response = api_instance.wallets_post(wallets_object)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PaymentApi->wallets_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallets_object** | [**WalletsObject**](WalletsObject.md)| Objeto que contendrá los datos del Requerimiento para obtener los Wallets disponibles. |

### Return type

[**WalletsResponseObject**](WalletsResponseObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Un objeto con un nodo principal llamado \&quot;WalletsResponse\&quot;. Dentro de él, estará presente toda la información con el resultado que nos informa el host sobre la operación que intentamos realizar. |  -  |
**400** | Bad request. |  -  |
**401** | Authorization information is missing or invalid. |  -  |
**404** | Not Found. |  -  |
**405** | Invalid Method. |  -  |
**500** | Unexpected error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

