## Implementacion

- Requiere Python >=3.6
- Se generó el cliente utilizando openapi-generator-5.4.0.
- Para su instalación se ejecutó el siguiente comando desde el directorio del codigo generado
  - "python setup.py install --user"
- Una vez hecho esto solo se agregó "import openapi_client" al codigo de ejemplo
- Se agrega en codigo generado el tipo de autenticacion necesario para uso de token (Oauth en Configuration, L402)
- Se agrega variable para guardar default authentication en api_client de codigo generado. (L76, L119)
  - Ademas se modifica funcion "update_params_for_auth" en api_client donde se maneja el uso del tipo de autenticacion (L616)
- Se arregla response_code para que permita str e int

## Uso

- Para la ejecución del codigo de ejemplo debe ejecutarse el siguiente comando:
  "python main.py"
- Puede agregarse el parametro hostname para especificar un host distinto de la siguiente manera.
  "python main.py --hostname=http://www.page.com"

