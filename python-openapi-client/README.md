# openapi-client
<h1 style=\"border:4px solid #004785;color:#004785; font-family: 'Open Sans', sans-serif; font-size: 32px;\">API de Pagos</h1> <br /><br /> <h1 style=\"border:4px solid #004785;color:#004785; font-family: 'Open Sans', sans-serif; font-size: 24px;\">Descripción del Servicio</h1> <p style=\"color:#004785;\"><b><u>Documentación en formato OpenAPI 3.0</b></u></p> <br/> Contrato especificado según especificaciones https://www.openapis.org/ y https://swagger.io/.<br /><br />  En el site https://editor.swagger.io/ se dispone de un  Viewer, Editor y  Generar de Código ( SDK ) para varios lenguajes de programación; incluyendo JAVA, C#, C++, Perl, Node.js, GO, PHP, Ruby y otros.<br/><br/> Para <b>ver</b> la documentación o <b>generar</b> código de la librería cliente o SDK  se deberá selecciónar en el menú horizontal  la opción <b>File</b>, en el menú vertical que se depliega la opción <b>Import File</b> y luego se deberá selecciónar el archivo del contrato deseado, ya sea  extensión <b>.json</b> o <b>.yaml</b>. <br/><br/> Además se puede generar el código de la librería cliente desde la línea de comandos a través de la herramienta  <b>CLI</b>  de  <b>OpenAPI Generator</b>. Esta presenta generadores de SDK en mayor variedad de lenguajes de programación.  En el site https://openapi-generator.tech/docs/installation se documenta cómo  <b>instalar</b> la herramienta CLI.<br/><br/> Los clientes generados contienen, adicionalmente al código,  la documentación de uso del mismo en <b>README.md</b>, como también en el subdirectorio <b>docs</b> toda la documentación del API o servicio y sus operaciones, con el detalle de los  campos o elementos y su dominio.<br /><br /><br /><br /> <h1 style=\"border:4px solid #004785;color:#004785; font-family: 'Open Sans', sans-serif; font-size: 24px;\">Notas a tener en cuenta para realizar la Integración</h1><br/> <p style=\"color:#004785;\"><b><u>Conceptos y/ Mecanismos relevantes Soportados por el Protocolo de Integración</u></b></p> <br/><br/> <span>&#8226;</span> <b>Interpretración de las Respuesta</b>,<br /><br/> El único campo que indica si la transacción fue aprobada, rechazada, o tienen algun error, es el elemento de las respuestas llamado <b>ResponseActions</b>, el  cual es un <b>ARRAY</b> de valores. Cada uno de estos indica una acción a realizar. Los elementos <b>ResponseCode</b>  y <b>ResponseMessage</b> son solamente informativos y por lo tanto no deben usarse para tomar acciones y los mismos pueden cambiar en base a la configuración de la Plataforma.<br/><br/> <span>&#8226;</span> <b>Bloque de transacciones</b>, permite Confirmar o Cancelar/Revertir todas las transacciones que forman parte de un bloque. <br/><br/> El POS puede definir un bloque o conjunto de transacciones simplemente indicando en todas ellas el mismo valor en el atributo/elemento/campo opcional llamado <b>Block</b>.<br/> 
La operación <b>BlockCancel</b>, permite que el POS pueda solicitar a la plataforma la reversión y/o cancelación de todo el bloque de transacciones .<br/> La operación <b>BlockClose</b>, confirma todas las transacciones que forman parte del bloque especificado.<br/>
Si el POS no posee un identificador unívoco de la transacción de venta, al momento de interactuar contra la plataforma podrá obtener uno con la operación  <b>BlockCreate</b>. Si el elemento o campo <b>Block</b>  existe y su contenido es Vacío o Nulo la plataforma realiza un <b>BlockCreate</b> automáticamente.<br /><br/>
<span>&#8226;</span> <b>Reversas por Ruptura de Secuencia</b>. Evita la necesidad de persistir datos de la reversa y ahorra una transacción en el flujo.<br/>
  El método llamado de ruptura de secuencia es utilizado para detectar los casos en los cuales el POS o Caja no pudo recibir una respuesta del mismo o no pudo procesarla adecuadamente. De esta forma permite a la misma reversar la transacción que no pudo procesar el POS o recibir la respuesta si fuese necesario. 

  En todo requerimiento el POS debe enviar el campo/elemento Sequence, con el valor recibido en el anterior requerimiento o vacío en el primero.

  La plataforma  genera una nueva secuencia solamente cuando el requerimiento realizado es reversible o cuando se produce una ruptura.  Por lo tanto los comandos en los cuales la plataforma  genera una nueva secuencia son <b>Sale</b>, <b>Void</b>, <b>Authorize*</b>, <b>DebtPayment</b>, <b>VoidDebtPayment</b>, <b>Confirm</b>, <b>Close</b> y <b>Cancel</b>.

  En caso de que la plataforma reverse el requerimiento previo retornará en la respuesta los siguiente campos o elementos.
  <blockquote><b>WasReversePrevious</b>, con valor <b>1</b><br/>
  <b>ReversedAnswerKey</b> conteniendo el <b>AnswerKey</b> de la transacción reversada<br/>
  <b>ReversedSequence</b> conteniendo el <b>Sequence </b>de la transacción reversada</blockquote>
  
En caso de que la plataforma no reverse el requerimiento previo retornará los siguientes campos o elementos <blockquote><b>WasReversePrevious</b>, con valor <b>0</b></blockquote> <br/> <span>&#8226;</span> <b>Reversas Tradicionales</b>. El POS debe repetir el mismo requerimiento adicionando el atributo/elemento <b>IsReverse</b> con valor <b>1</b>.  Se debe tener en cuenta que en esta modalidad la plataforma no retorna los siguientes atributos/elementos.

  <blockquote>
  <b>WasReversePrevious</b><br/>
  <b>ReversedAnswerKey</b><br/>
  <b>ReversedSequence</b>
  </blockquote>
  
<span>&#8226;</span> <b>Transacción Opcional de Confirmación</b>, ya que el mecanismo anterior permite que cada transacción Reverse o Confirme la anterior.<br/><br/> <span>&#8226;</span> <b>La Plataforma indica siempre las acciones que se deben realizar</b><br/><br/> <span>&#8226;</span><span>&#8226;</span> <b>Solicitar datos adicionales</b> ( <b>RequiredInformation</b> ), indicando no sólo cuáles son, sino también de qué tipo, valor  inicial, patrón de validación, si son mandatorios o no, qué Label se presenta al usuario, qué ayuda se presenta al usuario, etc.<br/> <span>&#8226;</span><span>&#8226;</span> <b>Mostrar Mensajes en Pantalla</b>. <span>&#8226;</span><span>&#8226;</span> <b>Imprimir Tickets</b>, ya sea en papel o capturar digitalmente el mismo, como así también el Layout de los mismos.<br/><br/><br/> <span>&#8226;</span> <b>Compresión de la trama</b> en base a codificación de los campos numéricos, string siempre de longitud variable, uso de sinónimos en los  campos, para que el programador programe usando los nombres largos y en el transporte se usen sus sinónimos cortos. <br/> <br/> <span>&#8226;</span> <b>Seguridad de los Datos Sensibles y de la Transaccion</b>, El elemento <b>Security</b> debera estar presente solo si los datos sensibles <b>CardNumber</b>, <b>ExpDate</b>, <b>PIN</b>, <b>Track1</b>, <b>Track2</b>, <b>SecurityCode</b> y  <b>CardCryptogram</b> deban ser envidos encriptados y por lo tanto este le elemento nos permite indicar el metodo de encriptacion utilizado y los datos adicionales que sean requeridos por la encriptacion. Si por ejemplo fuese el elemento PIN usando DUKPT y el resto de los datos sencible Track1, Track2 y SecurityCode, se deberian enviar  de la siguiente forma: </br>

      \"Security” :  [
        {
          \"Type\": \"PIN\",
          \"Values\":  [
              { 
                  \"Name\": \"Method\",
                  \"Value\": \"DUKPT\"
              },
              { 
                  \"Name\": \"KSN\",
                  \"Value\": \"1234567890ABCDEF\"
              },
              { 
                  \"Name\": \"CRC32\",
                  \"Value\": \"12345\"
              },
              { 
                  \"Name\": \"PlainTextLength\",
                  \"Value\": \"4\"
              },
              { 
                  \"Name\": \"CipherCounter\",
                  \"Value\": \"123\"
              },
              { 
                  \"Name\": \"ConsecutiveFailedCiphersCounter\",
                  \"Value\": \"123\"
              },
              { 
                  \"Name\": \"Data\",
                  \"Value\": \"01234567890123456\"
              }
          ] 
        },
        {
          \"Type\": \"SensitiveData\",
          \"Values\":  [
              { 
                  \"Name\": \"Method\",
                  \"Value\": \"DUKPT-eGlobal\"
              },
              { 
                  \"Name\": \"KSN\",
                  \"Value\": \"1234567890ABCDEF\"
              },
              { 
                  \"Name\": \"Track1CRC32\",
                  \"Value\": \"12345\"
              },
              { 
                  \"Name\": \"Track2CRC32\",
                  \"Value\": \"12345\"
              },
              { 
                  \"Name\": \"Track1Length\",
                  \"Value\": \"79\"
              },
              { 
                  \"Name\": \"Track2Length\",
                  \"Value\": \"37\"
              },
              { 
                  \"Name\": \"SecurityCodeLength\",
                  \"Value\": \"3\"
              },
              { 
                  \"Name\": \"CipherCounter\",
                  \"Value\": \"123\"
              },
              { 
                  \"Name\": \"ConsecutiveFailedCiphersCounter\",
                  \"Value\": \"123\"
              },
              { 
                  \"Name\": \"Data\",
                  \"Value\": \"1ahbcd23412345123412b213b1324b1234b2134b2134132b4123b23\"
              }
          ] 
        },
        {
          \"Type\": \"3DSecure\",
          \"Values\":  [
              { 
                  \"Name\": \"Method\",
                  \"Value\": \"3DS-SNAP\"
              },
              { 
                      
                  \"Name\":  \"TransactionStatus\",
                  \"Value\": \"SuccessfullyAuthenticated\"
              },
              { 
                      
                  \"Name\":  \"AuthenticationECI\",
                  \"Value\": \"05\"
              },
              { 
                      
                  \"Name\":  \"IsChallengeMandated\",
                  \"Value\": \"false\"
              },
              ...
              { 
                      
                  \"Name\":  \"AcsReferenceNumber\",
                  \"Value\": \"3DS_LOA_ACS_PPFU_020100_00009\"
              },
              { 
                  \"Name\":  \"ProcessedAsDataOnly\",
                  \"Value\": \"false\"
              }
          ] 
        }        
      ]
</br> Para el caso de DUKPT-eGlobal, <b>Track2</b>, <b>SecurityCode</b> y <b>Track1</b> se cifraran formando parte del mismo Bloque, El mismo se debera formar con el Track2 ( reemplazando el signo = por el digito D ) completandolo hasta los 38 digitos con el digito F, luego el  SecurityCode completandolo hasta 10 digitos y por ultimo el Track1 padeado completando el bloque  de los 208 digitos.  </br> Este elemento <b>Security</b> sera utilizado para enviar cualquier dato de autenticacion del pagador por ejemplo 3DSecure, para el caso de que el proveedor de la Autenticacion sea SNAP se deberan contener como valores todos los elementos definidos en el objeto <b>ThreeDSInformation</b>.     </br> Este mecanismo podra utilizarse en el futuro para encriptar otros datos que sean sensibles pero no del medio de pago, si no de las personas.
</br> <h1 style=\"border:4px solid #004785;color:#004785; font-family: 'Open Sans', sans-serif; font-size: 24px;\">Log de Cambios</h1></br>
<span>&#8226;</span> <b>Versión 5.6.1</b>
<span>&#8226;</span><span>&#8226;</span> Se añade el campo <b>MerchantCategory</b> en las respuestas de todas las transacciones. Sólo se enviará en caso de que la categoría de la compañia exista.</br>
<span>&#8226;</span> <b>Versión 5.6.0</b>
<span>&#8226;</span><span>&#8226;</span> Los campos <b>ResponseCode</b>, <b>ResponseMessage</b> y <b>ResponseActions</b> son <b>obligatorios</b> en las respuestas de todas las transacciones.</br>
<span>&#8226;</span> <b>Versión 5.5.7</b>
<span>&#8226;</span><span>&#8226;</span> Se añade el elemento <b>Notification</b>. El mismo se encuentra dentro de <b>SaleResponse</b> y <b>AuthorizeSaleResponse</b>. Notificación a generar alertas vía e-mail.</br>
<span>&#8226;</span> <b>Versión 5.5.6</b>
<span>&#8226;</span><span>&#8226;</span> Se añaden los elementos <b>CardAppLabel</b>, <b>CardAuthRequestCryptogram</b> y <b>CardAuthResponseCryptogram</b>, para facilitar el analisis de los POS y ReadingDevices, el contenido de dichos elementos se encontraba en Tag de los elementos CardCryptogram y CardCryptogramResponse.</br>
<span>&#8226;</span>  <b>Versión 5.5.5</b>
<span>&#8226;</span><span>&#8226;</span> Se modifican los elementos <b>AuthorizeSale</b> y <b>AuthorizeSaleResponse</b> para su correcta documentación. Además, se añade el campo <b>ReadingDeviceOperatingFrom</b> el cual indica desde cuando se encuentra operativo o encendido el dispositivo</br>
<span>&#8226;</span> <b>Versión 5.5.4</b>
<span>&#8226;</span><span>&#8226;</span> Se renombra el atributo <b>ReasonReverse</b> a <b>ReverseReason</b>. Dicho campo permite notificar en las Reversas la razón por la cual fue necesario generarla.</br>
<span>&#8226;</span> <b>Versión 5.5.3</b>
<span>&#8226;</span><span>&#8226;</span> Se agregan atributos al elemento <b>Configuration</b> para la operación <b>PaymentMethod</b>. Por otra parte, se añade el mismo en todas las operaciones donde no se encontraba documentado. </br><b>• Versión 5.5.2</b>
<span>&#8226;</span><span>&#8226;</span> Se Agrega el elemento <b>Payer</b> con los datos del Pagador. Originalmente hasta esta version se envian los mismos en el elemento <b>Customer</b>, pero desde ahora se permite que se informen personas ( fisicas y juridicas ) como cliente comprador y como pagador. Si el elemento <b>Payer</b> no esta presente se tomaran los datos del elemento <b>Customer</b>. Se da soporte al Tipo de Ticket Payer.</br>
<span>&#8226;</span> <b>Versión 5.5.1</b> </br>
<span>&#8226;</span><span>&#8226;</span> Se completa la documentacion de los Elementos <b>Seller</b> y <b>Customer</b>, agregandose los atributos <b>City</b> y  <b>AbbreviatedName</b>.<br/>   <span>&#8226;</span><span>&#8226;</span> Se unifica la definicion del Elemento  <b>Customer</b> .<br/>   <span>&#8226;</span><span>&#8226;</span> Se agrega el Elemento <b>PaymentFacilitatorID</b> para indicar el Identificador de Facilitador de pagos o Payfac.</br>
<span>&#8226;</span> <b>Versión 5.5.0</b> </br>
<span>&#8226;</span><span>&#8226;</span> El elemento <b>ResponseActions</b> y <b>PosOrDeviceAction</b> de todas las operaciones deja de ser una lista.<br/>  de elementos en un string y se convierte en un array de string. Cada valor de la lista anterior está representada por un elemento del array.<br/>   <span>&#8226;</span><span>&#8226;</span> Se agregan los campos <b>ForeignIdentifier</b>, <b>SmallImage</b> y <b>LargeImage</b> en el campo <b>Wallets</b> de la operación <b>WalletsResponse</b>.<br/> <span>&#8226;</span><span>&#8226;</span> En el campo <b>PaymentMethods</b> de la operación <b>PaymentMethodsResponse</b> se agregan las properties <b>Imag</b>, <b>SmallImage</b> y <b>LargeImage</b>. Además se adiciona el campo <b>ID</b> en <b>Category</b> y el campo <b>ForeignIdentifier</b> en <b>Type</b>. <br/> <span>&#8226;</span><span>&#8226;</span> Se agrupan los campos relacionados con los datos del cliente y del vendedor en dos únicos campos de tipo objeto denominados <b>Customer</b> y <b>Seller</b>, respectivamente.<br/> <span>&#8226;</span><span>&#8226;</span> El elemento Layout del campo <b>Tickets</b> se convierte en un array de objetos que contiene elementos que permiten describir, dar formato y codificar los datos a imprimir. <br/> <span>&#8226;</span><span>&#8226;</span> Se documenta la operación <b>OrderStatus</b>.</br> <span>&#8226;</span><span>&#8226;</span> Los campos que refieren a tiempo y fecha se convierten en formato date-time. </br> <span>&#8226;</span><span>&#8226;</span> Se agrega el campo <b>ForeignResponseCode</b> en todas las respuestas de las operaciones, como un código de para el sistema externo, es decir, para la aplicación cliente que se comunica con el TEF.</br> <span>&#8226;</span><span>&#8226;</span> Se adiciona el campo <b>CardGetMode</b> que permite indicar por cada elemento que contiene los datos sensibles, si están encriptados y también el algoritmo usado. En caso de no estar especificado se asume PLAIN.</br> <span>&#8226;</span><span>&#8226;</span> Se agrega el campo <b>OrigReference</b> en aquellas operaciones que pueden referenciar a una transacción previa, como <b>Void</b>, <b>Return</b> y <b>GetTransaction</b>.</br> <span>&#8226;</span><span>&#8226;</span> Se cambia la estrutura de la respuesta de la Operacion <b>GetTransacion</b> por errores. </br> <span>&#8226;</span><span>&#8226;</span> Se agregan las acciones Ok, Error y Retry en los campos <b>ResponseActions</b>.</br> <span>&#8226;</span><span>&#8226;</span> En aquellas operaciones financieras en las que se especifica la tarjeta se agrega en el requerimiento el campo <b>Pin</b>y en la respuesta el campo <b>WorkingKeys</b>.</br> <span>&#8226;</span><span>&#8226;</span> Se agrega el campo <b>Security</b> con el objetivo de indicar los datos sensibles de seguridad de una transacción tanto en los requerimientos como en las respuestas de las operaciones disponibles.</br> <span>&#8226;</span><span>&#8226;</span> Se agrega la operacion <b>KeysRenewal</b> Las claves podran ser retornadas en el elemento <b>Security</b> y en caso de obtener como accion de respuesta <b>KeysRenewal</b> se esta indicando que esta nueva operacion debe ser ejecutada.<br/>      <span>&#8226;</span><span>&#8226;</span> Se agrega la opcion <b>Signature</b>  .<br/>     <span>&#8226;</span><span>&#8226;</span> Se agrega el elemento  <b>CategoryCode</b> para especificar el MCC del Vendedor y/o del Cliente  .<br/>     <span>&#8226;</span><span>&#8226;</span> Se agregan los Elementos <b>MerchantID</b>, <b>TerminalID</b>, <b>TraceNumber</b> y <b>SettlementBatchNumber</b> En los requerimientos, en caso que los mismos contengan valor los mismos seran utilizados para enviar al Host Resolutor de la Transaccion.</br>  <span>&#8226;</span><span>&#8226;</span> Se agregan los valores para pagos recurrentes a  los Elementos  <b>CardReadMode</b> y  <b>CardReadModeDescription</b> <span>&#8226;</span> <b>Versión 5.4.0</b> </br> <span>&#8226;</span><span>&#8226;</span> Se cambia la dirección IP por el nombre.</br> <span>&#8226;</span><span>&#8226;</span> Se contemplan los Datos del <b>Vendedor/Seller</b> y del <b>Cliente/Customer</b> en las operaciones  <b>WalletRequest</b>, <b>Sale</b>, <b>AuthorizeSale</b>, <b>DebtPayment</b>,  <b>Deposit</b>,  <b>Settlement</b>,  <b>Capture</b>.</br> <span>&#8226;</span><span>&#8226;</span> Se Agregan los elementos <b>POSGEO</b> y <b>ReadingDeviceGEO</b> para que el dispositivo de lectura y el Punto de venta Notifiquen su coordenadas georefenciales en el momento de que se realiza la transacción.</br> <span>&#8226;</span><span>&#8226;</span> Se unifica y amplía el elemento <b>RequiredInformation</b>  tanto en los requerimientos como en las respuestas</br>  <span>&#8226;</span><span>&#8226;</span> Se cambia el tipo el elemento <b>CurrencyCode</b> a string para permitir cualquieras de la notaciones posibles.</br> <span>&#8226;</span><span>&#8226;</span> Se cambia el  elemento <b>Currency</b> por <b>CurrencyCode</b>  en el elemento <b>Plans</b>.</br> <span>&#8226;</span><span>&#8226;</span> Se contemplan del detalle ( elemento <b>Products</b> ) de la venta en las operaciones  <b>WalletRequest</b>, <b>Sale</b>, <b>Void</b>, <b>Return</b>, <b>AuthorizeSale</b>, <b>DebtPayment</b>,  <b>VoidDebtPayment</b>, <b>Deposit</b>,  <b>Settlement</b>,  <b>Capture</b>.</br> <span>&#8226;</span><span>&#8226;</span> Agregamos la operación <b>DebtInquiry</b> que actua como sinónimo de <b>BalanceInquery</b>, la cual podía ser usada para consulta de Saldo y también de deuda.</br> <span>&#8226;</span><span>&#8226;</span> Se corrigen los tipos de Datos de Varios campos <b>Amount</b> que en lugar de string debían ser number.</br> <span>&#8226;</span><span>&#8226;</span> Se agregan las operaciones <b>QueryCompanies</b> y <b>QueryLineOfBusiness</b> para la consulta de Rubros y Empresas que se pueden utilizar para pagar Servicios/Deuda/Facturas con la operación <b>DebtPayment</b>.</br> <span>&#8226;</span><span>&#8226;</span> Se adiciona el elemento <b>Companies</b> en la Operacion <b>BalanceInquiry</b> para el caso de que existan mas de una Compania para el mismo codigo o identificador de la deuda o factura a pagar y adicionalmente se agrega para ese caso la posibilidad de especificar a que compania corrende el Pago en el elemento <b>DebtCompanyIdentification</b> en la operación <b>DebtPayment</b>.</br> <span>&#8226;</span><span>&#8226;</span> Se adiciona el elemento <b>BaseAmonut</b> en los requerimientos de las operación <b>Return</b>, el elemento <b>Reference</b>  en las operaciones <b>Sale</b>, <b>AuthorizeSale</b>, <b>Void</b>, <b>Return</b>, <b>DebtPayment</b>, <b>VoidDebtPayment</b>, <b>GetTransaction</b> y <b>WalletRequest</b>.  Además, se agregan los elementos <b>TaxFinancialCostAmount</b>, <b>TaxFinancialCostPercentage</b>, <b>FinancialCostAmount</b>, <b>FinancialCostPercentage</b> y <b>RequestAmount</b>  en las respuestas de dichas operaciones.</br> <span>&#8226;</span><span>&#8226;</span> En cada plan que se devuelve a través del <b>PaymentMethodResponse</b> estarán presentes <b>TaxFinancialCostAmount</b>,  <b>TaxFinancialCostPercentage</b>, <b>FinancialCostAmount</b> y <b>FinancialCostPercentage</b>. </br> <span>&#8226;</span><span>&#8226;</span> Se agregan los elementos  <b>CardAppName</b> y <b>CardAppIdentifier</b> en las peticiones de las operaciones <b>Sale</b>, <b>AuthorizeSale</b>,  <b>Void</b>, <b>Return</b>, <b>PaymentMethods</b>, <b>GetCard</b>, <b>Validate</b>, <b>DebtInquiery</b>, <b>BalanceInquiry</b>, <b>DebtPayment</b> y <b>VoidDebtPayment</b>.  Además, se agregan en las respuestas de algunas de ellas.</br> <span>&#8226;</span><span>&#8226;</span> Se cambia la estructura del elemento <b>Tickets</b> de las respuestas donde el elemento <b>Action</b>  hace referencia a las acciones que debe ejecutar el punto de venta, el elemento <b>DeviceAction</b> a las acciones que debe ejecutar el dispositivo y <b>ExecutedAction</b> a las acciones  que ejecutó la plataforma para sus <b>Tickets</b>.</br> <span>&#8226;</span><span>&#8226;</span> Se adicionan los elementos <b>POSOrDeviceAction</b>, <b>OperationMode</b> y <b>OperationModeDescription</b> a la operación <b>Configure</b>.</br> <span>&#8226;</span><span>&#8226;</span> Se agrega el elemento <b>RemainderAmount</b> a la operación <b>GetBlockResponse</b> que hace referencia a la diferencia entre el monto total de la transacción y las devoluciones parciales realizadas.</br> <span>&#8226;</span><span>&#8226;</span> Se corrijen errores en la definición de varios campos, como <b>ReadingDeviceType</b> y <b>CardReadMode</b>.</br> <span>&#8226;</span><span>&#8226;</span> Se reemplaza el campo <b>ApplicationIdentification</b> por <b>SystemIdentification</b> en las operaciones <b>EnableService</b>, <b>Wallets</b>, <b>QueryCompanies</b>,  <b>QueryLineOfBusiness</b> y sus respectivas respuestas. </br> <span>&#8226;</span><span>&#8226;</span> Se agregan el identifidor Tributario en <b>Sale</b>, <b>AuthorizeSale</b>, <b>Void</b>,  <b>Return</b>, <b>DebtPayment</b>, <b>VoidDebtPayment</b> y <b>Debtinquery</b> que permite transacciones con <b>Token</b> ( <b>CredentialToken</b> y  <b>CredentialIssuerToken</b> ). En estas operaciones se elimina de mandatorias al campo <b>BranchIdentification</b> y <b>POSIdentification</b><br/> <span>&#8226;</span><span>&#8226;</span> Se agrega la operación <b>Enrollment</b>, la cual permite transacciones con <b>Token</b> ( <b>CredentialToken</b> y  <b>CredentialIssuerToken</b> ) y pagos recurrentes.</br> <span>&#8226;</span><span>&#8226;</span> El campo <b>ResponseAction</b> deja de ser un enum y se convierte en string. Se indica en la descripción los posibles actions.</br> <span>&#8226;</span><span>&#8226;</span> Se agregan los campos <b>SellerIdentification</b> y <b>SellerIdentificationType</b> en aquellas operaciones en las que se especifican con los datos del vendedor.</br> <span>&#8226;</span><span>&#8226;</span> El campo <b>FacilityPayments</b> deja de ser mandatario en las operaciones <b>Enrollment</b> y <b>Sale</b>. </br> <span>&#8226;</span><span>&#8226;</span> Se elimina la posibilidad de envío en el header HTTP.<br/> <span>&#8226;</span><span>&#8226;</span> Se agregan los campos <b>CashbackAmount</b> y <b>TipAmount</b> en la operación <b>WalletRequest</b>.<br/> <span>&#8226;</span><span>&#8226;</span> Se adiciona en el campo <b>CardReadMode</b> la opción K de Token.<br/> <span>&#8226;</span><span>&#8226;</span> Se corrige el campo <b>Answertype</b> y se modifica por <b>AnswerType</b>.<br/> <span>&#8226;</span><span>&#8226;</span> Se agregan los campos referidos al vendedor en las operaciones <b>Void</b> y <b>Return</b>. <br/> <span>&#8226;</span><span>&#8226;</span> Se crea un primer nivel para cada operación de tipo objeto. <br/>  <span>&#8226;</span><span>&#8226;</span> Se crea el campo <b>InputTokens</b> como un array de objetos que contienen Name y Value como properties en las operaciones <b>Sale</b>, <b>AuthorizeSale</b>, <b>Void</b>, <b>Return</b>, <b>DebtPayment</b>, <b>VoidDebtPayment</b> y <b>DebtInquiry</b>.<br/> <span>&#8226;</span><span>&#8226;</span> Los elementos <b>Action</b>, <b>DeviceAction</b> y <b>ExecutedAction</b> del campo <b>Tickets</b> dejan de ser de tipo string y se convierten en arrays.<br/>     <span>&#8226;</span><span>&#8226;</span> Se agrega el elemento <b>AdditionalInformation</b> en las respuestas de todas las operaciones.<br/>    
</br>
<span>&#8226;</span> <b>Versión 5.3.0</b> Se amplía la definición de la Operación <b>Configure</b> permitiendo tanto en la respuesta como en el requerimiento los elementos <b>Operations</b>, <b>Tables</b> y <b>Files</b></br></br> Se agregan los elementos <b>VoidSupport</b>, <b>ReturnSupport</b>, <b>WalletUseInVoidTransaction</b> y <b>WalletUseInReturnTransaction</b> en las caracteristicas de un Wallet.<br/><br/> Se agrega el Valor <b>Display</b> en el elemento <b>ResponseActions</b> indicando que se debe mostrar en el Display del Dispositivo o Aplicativo el contenido del elemento <b>DisplayResponseMessage</b>.  En la respuesta de la operación  <b>BalanceInquery</b> se agregan los elementos <b>AmountAvailable</b> y <b>PointsAvailable</b> para indicar los saldos.</br> Se especifica en la documentación que el Cancel puede ser usado para Cancelar un Pago con Wallets en Curso.</br></br> Se agregan elementos en los Requerimientos y en las respuestas opcionales entre los POS* que permiten describir las características del punto de venta, los Device* que permiten especificar las características del Dispositivo de Lectura.<br/>   Se cambió el elemento <b>AnswerIdentification</b> por <b>AnswerKey</b>  para compatibilizar con el servicio de Pagos.<br/><br/>     Se agregaron <b>AccountNumber</b>, <b>AccountType</b> y <b>Balance</b> en las operaciones <b>BalanceInquiry</b> y <b>DebtPayment</b> .<br/><br/>     Se agregaron las Operaciones <b>Confirm</b> y  <b>Cancel</b>, donde la Operación <b>Confirm</b> es usada para confirmar un pago recibido por el POS o Aplicativo del comercio. Existen Wallets en los que la confirmación es automática y se indica en el Elemento  <b>AutoConfirm</b> de la respuesta del comando <b>Wallets</b>. La operación <b>Cancel</b> puede ser utilizada a partir de que la Plataforma retorne la acción <b>PaymentFlowIsCancelable</b> en la respuesta de una operación <b>WalletRequest</b>. El Wallet soporta Cancelación de Requerimiento lo cual está indicado con el Elemento <b>SupportRequestCancel</b> dentro de las propiedades de  los Wallets que son retornados por la Operación <b>Wallets</b>.<br/> Se agregó como carasterística de los Wallets también el elemento <b>SupportValidityOfTheRequest</b> que indica si en el primer requerimiento de la Operación <b>WalletRequest</b> se puede enviar el elemento <b>TransactionTimeout</b> que especifica el tiempo de vida de la intención de pago. Superado ese tiempo no se podrá pagar y el ciclo de reintento será detenido por la plataforma, indicado por las siguientes acciones: <b>Completed</b> y <b>Error</b>.<br/> Se agrega el Elemento <b>Tickets</b> en la respuesta de una Operación <b>WalletRequest</b>. El elemento estará presente si como acción está presente el Valor <b>Tickets</b>, indicando que los mismos deberán ser Impresos, capturados digitalmente, etc. según se indique. <br/><br/> Se permite en la Operación <b>PaymentMethod</b> la búsqueda por el Id o el ForeignIdentification<br/><br/>
<span>&#8226;</span> <b>Versión 5.2.6</b> Se cambia el nombre del elemento <b>DateTime</b> por <b>TransactionDateTime</b> en la operación <b>WalletRequest</b>.<br/><br/> <span>&#8226;</span> <b>Versión 5.2.5</b> Se agregan en los Planes el atributo <b>POSOrDeviceActions</b> que permite indecarle al Dispositivo que debe solicitar  PIN para esa transacción y eso lo indica enviando la acción <b>RequestPIN</b>.<br/> <span>&#8226;</span><span>&#8226;</span> Se agrega el <b>ResponseActions</b> <b>Configure</b> que indica que se debe ejecutar una reconfiguración para obtener  parámetros nuevos ya que hay alguna actualización. <span>&#8226;</span><span>&#8226;</span> Se agregan las Operaciones <b>Wallets</b>, <b>WalletRequest</b> y <b>EnableService</b>, las mismas pueden formar parte  de un Block y forman parte de la ruptura de Secuencia.<br/><br/> <span>&#8226;</span> <b>Versión 5.2.4</b> Se agrega el identifidor Tributario en <b>OrderInitial</b>, que permite transacciones con <b>Token</b> ( <b>CredentialToken</b> y  <b>CredentialIssuerToken</b> ).<br/> <span>&#8226;</span><span>&#8226;</span> Se completa el <b>GetCardResponse</b> para que contenga los  elementos <b>PaymentMethod</b> y <b>Plans</b>.<br/> <span>&#8226;</span><span>&#8226;</span> Se completa el <b>PaymentMethodResponse</b> para que contenga los elementos <b>PaymentMethod</b> y <b>Plans</b>.<br/> <span>&#8226;</span><span>&#8226;</span> Se agrega en el <b>GetCard</b>: permite forzar un modo de lectura y permite solicitar los datos leídos al POS <b>CardGetMode</b>. <br/><br/> <span>&#8226;</span><span>&#8226;</span> Se permite el envío de datos del cliente <b>Customer*</b> en las operaciones Financieras.<br/><br/> <span>&#8226;</span> <b>Versión 5.2.3</b> Se cambian los valores posibles para <b>ResponseActionCancel</b> en las operaciones <b>GetBlock</b> y <b>GetTransaction</b>.<br/>   <br/> <span>&#8226;</span> <b>Versión 5.2.2</b> Se agrega el Atributo <b>ReasonReverse</b> que permite notificar en las Reversas la razón por la cual fue necesario  generarla, el atributo <b>ReasonSequenceBreak</b> que permite indicar la razón por la cual se produce la ruptura de secuencia que podrá generar una reversa si  fuese necesario, y el atributo </b>Reason</b> en la operación <b>Cancel</b>.<br/>   <br/> <span>&#8226;</span> <b>Versión 5.2.1</b> Se agrega el Atributo <b>IsReverse</b> en todos las operaciones reversables.<br/>   <br/><br/> <br/><br/> <br/><p style=\"color:Blue;\">&copy;2019-2021 EVO Payments Inc. All rights reserved.</p>The EVO Payments name, logo and related trademarks and service marks, owned<br /> by EVO Payments, are registered and/or used in the<br /> United States and many foreign countries. All other trademarks,<br /> service marks and trade names referenced in this site are the property<br /> of their respective owners.<br /> <br /> <br /> ANY USE, COPYING OR REPRODUCTION OF THE TRADEMARKS, LOGOS, INFORMATION,<br />  IMAGES OR DESIGNS CONTAINED IN THIS SITE IS STRICTLY<br />  PROHIBITED WITHOUT THE PRIOR WRITTEN PERMISSION OF EVO Payments Inc.<br /> <br /> 

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 5.6.1
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://integrationsevopayments.mx](https://integrationsevopayments.mx)

## Requirements.

Python >=3.6

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import openapi_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import openapi_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import openapi_client
from pprint import pprint
from openapi_client.api import payment_api
from openapi_client.model.authorize_sale_object import AuthorizeSaleObject
from openapi_client.model.authorize_sale_response_object import AuthorizeSaleResponseObject
from openapi_client.model.balance_inquiry_object import BalanceInquiryObject
from openapi_client.model.balance_inquiry_response_object import BalanceInquiryResponseObject
from openapi_client.model.block_cancel_object import BlockCancelObject
from openapi_client.model.block_cancel_response_object import BlockCancelResponseObject
from openapi_client.model.block_close_object import BlockCloseObject
from openapi_client.model.block_close_response_object import BlockCloseResponseObject
from openapi_client.model.block_create_object import BlockCreateObject
from openapi_client.model.block_create_response_object import BlockCreateResponseObject
from openapi_client.model.cancel_object import CancelObject
from openapi_client.model.cancel_response_object import CancelResponseObject
from openapi_client.model.capture_object import CaptureObject
from openapi_client.model.capture_response_object import CaptureResponseObject
from openapi_client.model.close_object import CloseObject
from openapi_client.model.close_response_object import CloseResponseObject
from openapi_client.model.configure_object import ConfigureObject
from openapi_client.model.configure_response_object import ConfigureResponseObject
from openapi_client.model.confirm_object import ConfirmObject
from openapi_client.model.confirm_response_object import ConfirmResponseObject
from openapi_client.model.debt_inquiry_object import DebtInquiryObject
from openapi_client.model.debt_inquiry_response_object import DebtInquiryResponseObject
from openapi_client.model.debt_payment_object import DebtPaymentObject
from openapi_client.model.debt_payment_response_object import DebtPaymentResponseObject
from openapi_client.model.deposit_object import DepositObject
from openapi_client.model.deposit_response_object import DepositResponseObject
from openapi_client.model.enable_service_object import EnableServiceObject
from openapi_client.model.enable_service_response_object import EnableServiceResponseObject
from openapi_client.model.enrollment_object import EnrollmentObject
from openapi_client.model.enrollment_response_object import EnrollmentResponseObject
from openapi_client.model.get_block_object import GetBlockObject
from openapi_client.model.get_block_response_object import GetBlockResponseObject
from openapi_client.model.get_card_object import GetCardObject
from openapi_client.model.get_card_response_object import GetCardResponseObject
from openapi_client.model.get_transaction_object import GetTransactionObject
from openapi_client.model.get_transaction_response_object import GetTransactionResponseObject
from openapi_client.model.keep_alive_object import KeepAliveObject
from openapi_client.model.keep_alive_response_object import KeepAliveResponseObject
from openapi_client.model.keys_renewal_object import KeysRenewalObject
from openapi_client.model.order_final_object import OrderFinalObject
from openapi_client.model.order_final_response_object import OrderFinalResponseObject
from openapi_client.model.order_get_object import OrderGetObject
from openapi_client.model.order_get_response_object import OrderGetResponseObject
from openapi_client.model.order_initial_object import OrderInitialObject
from openapi_client.model.order_initial_response_object import OrderInitialResponseObject
from openapi_client.model.order_status_object import OrderStatusObject
from openapi_client.model.order_status_response_object import OrderStatusResponseObject
from openapi_client.model.payment_method_object import PaymentMethodObject
from openapi_client.model.payment_method_response_object import PaymentMethodResponseObject
from openapi_client.model.payment_methods_object import PaymentMethodsObject
from openapi_client.model.payment_methods_response_object import PaymentMethodsResponseObject
from openapi_client.model.query_companies_object import QueryCompaniesObject
from openapi_client.model.query_companies_response_object import QueryCompaniesResponseObject
from openapi_client.model.query_line_of_business_object import QueryLineOfBusinessObject
from openapi_client.model.query_line_of_business_response_object import QueryLineOfBusinessResponseObject
from openapi_client.model.return_object import ReturnObject
from openapi_client.model.return_response_object import ReturnResponseObject
from openapi_client.model.sale_object import SaleObject
from openapi_client.model.sale_response_object import SaleResponseObject
from openapi_client.model.settlement_object import SettlementObject
from openapi_client.model.settlement_response_object import SettlementResponseObject
from openapi_client.model.validate_object import ValidateObject
from openapi_client.model.validate_response_object import ValidateResponseObject
from openapi_client.model.void_debt_payment_object import VoidDebtPaymentObject
from openapi_client.model.void_debt_payment_response_object import VoidDebtPaymentResponseObject
from openapi_client.model.void_object import VoidObject
from openapi_client.model.void_response_object import VoidResponseObject
from openapi_client.model.wallet_request_object import WalletRequestObject
from openapi_client.model.wallet_request_response_object import WalletRequestResponseObject
from openapi_client.model.wallets_object import WalletsObject
from openapi_client.model.wallets_response_object import WalletsResponseObject
# Defining the host is optional and defaults to https://testcodi.multipay.mx:30801/Payments/Authorize/5.6.1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://testcodi.multipay.mx:30801/Payments/Authorize/5.6.1"
)



# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
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

    try:
        # Autorización de Venta sin Captura o Pre Autorización
        api_response = api_instance.authorize_sale_post(authorize_sale_object)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PaymentApi->authorize_sale_post: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://testcodi.multipay.mx:30801/Payments/Authorize/5.6.1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*PaymentApi* | [**authorize_sale_post**](docs/PaymentApi.md#authorize_sale_post) | **POST** /AuthorizeSale | Autorización de Venta sin Captura o Pre Autorización
*PaymentApi* | [**balance_inquiry_post**](docs/PaymentApi.md#balance_inquiry_post) | **POST** /BalanceInquiry | Consulta de Saldo/Deuda de cuenta/Credencial
*PaymentApi* | [**block_cancel_post**](docs/PaymentApi.md#block_cancel_post) | **POST** /BlockCancel | Cancelación del último bloque de transacciones realizadas.
*PaymentApi* | [**block_close_post**](docs/PaymentApi.md#block_close_post) | **POST** /BlockClose | Confirmación del último bloque de transacciones realizadas.
*PaymentApi* | [**block_create_post**](docs/PaymentApi.md#block_create_post) | **POST** /BlockCreate | Crea un Identificador de Bloque-Block de transacciones.
*PaymentApi* | [**cancel_post**](docs/PaymentApi.md#cancel_post) | **POST** /Cancel | Cancela una Transacción en Curso, Inciada con un GetCard/WalletRequest.
*PaymentApi* | [**capture_post**](docs/PaymentApi.md#capture_post) | **POST** /Capture | Confirmación de un consumo previo.
*PaymentApi* | [**close_post**](docs/PaymentApi.md#close_post) | **POST** /Close | Utilizada por el POS para indicar que finalizo su sesion.
*PaymentApi* | [**configure_post**](docs/PaymentApi.md#configure_post) | **POST** /Configure | Permite crear configuración en Plataforma
*PaymentApi* | [**confirm_post**](docs/PaymentApi.md#confirm_post) | **POST** /Confirm | Confirmación de la última operación realizada.
*PaymentApi* | [**debt_inquiry_post**](docs/PaymentApi.md#debt_inquiry_post) | **POST** /DebtInquiry | Consulta de Deuda de cuenta/credencial
*PaymentApi* | [**debt_payment_post**](docs/PaymentApi.md#debt_payment_post) | **POST** /DebtPayment | Pago de Deuda, Resumen de Cuenta o Saldo.
*PaymentApi* | [**deposit_post**](docs/PaymentApi.md#deposit_post) | **POST** /Deposit | Confirmación de un consumo previo.
*PaymentApi* | [**enable_service_post**](docs/PaymentApi.md#enable_service_post) | **POST** /EnableService | Permite Habilitar el uso de un Servicio
*PaymentApi* | [**enrollment_post**](docs/PaymentApi.md#enrollment_post) | **POST** /Enrollment | Suscripción al servicio de pagos Tokenizados y pagos recurrentes.
*PaymentApi* | [**get_block_post**](docs/PaymentApi.md#get_block_post) | **POST** /GetBlock | Recupera los identificadores de las transacciones que  lo componen.
*PaymentApi* | [**get_card_post**](docs/PaymentApi.md#get_card_post) | **POST** /GetCard | Solicitud de Lectura del Medio de Pago
*PaymentApi* | [**get_transaction_post**](docs/PaymentApi.md#get_transaction_post) | **POST** /GetTransaction | Recupera los datos de la transacción especificada. 
*PaymentApi* | [**keep_alive_post**](docs/PaymentApi.md#keep_alive_post) | **POST** /KeepAlive | Mensaje que informa si está disponible el Servicio Authorize.
*PaymentApi* | [**keys_renewal_post**](docs/PaymentApi.md#keys_renewal_post) | **POST** /KeysRenewal | Renovacion de Llaves
*PaymentApi* | [**order_final_post**](docs/PaymentApi.md#order_final_post) | **POST** /OrderFinal | Reclamar el estatus de la operación de compra.
*PaymentApi* | [**order_get_post**](docs/PaymentApi.md#order_get_post) | **POST** /OrderGet | Recuperar la operación iniciada por el comercio, para su compra.
*PaymentApi* | [**order_initial_post**](docs/PaymentApi.md#order_initial_post) | **POST** /OrderInitial | Indica el inicio de una operación de venta.
*PaymentApi* | [**order_status_post**](docs/PaymentApi.md#order_status_post) | **POST** /OrderStatus | Recuperación del Estado de una Transacción Iniciada por el OrderInitial.
*PaymentApi* | [**payment_method_post**](docs/PaymentApi.md#payment_method_post) | **POST** /PaymentMethod | Consulta de  \&quot;planes\&quot; financieros para un Medio de Pago.
*PaymentApi* | [**payment_methods_post**](docs/PaymentApi.md#payment_methods_post) | **POST** /PaymentMethods | Consulta de los Medios de Pago  disponibles.
*PaymentApi* | [**query_companies_post**](docs/PaymentApi.md#query_companies_post) | **POST** /QueryCompanies | Consulta de Empresas para el Pago de Servicios o Deuda
*PaymentApi* | [**query_line_of_business_post**](docs/PaymentApi.md#query_line_of_business_post) | **POST** /QueryLineOfBusiness | Consulta de Rubros de Empresas para el Pago de Servicios o Deuda
*PaymentApi* | [**return_post**](docs/PaymentApi.md#return_post) | **POST** /Return | Realización de una devolución de operación de compra/autorización.
*PaymentApi* | [**sale_post**](docs/PaymentApi.md#sale_post) | **POST** /Sale | Realización de una compra/Autorización de compra
*PaymentApi* | [**settlement_post**](docs/PaymentApi.md#settlement_post) | **POST** /Settlement | Confirmación de un consumo previo.
*PaymentApi* | [**validate_post**](docs/PaymentApi.md#validate_post) | **POST** /Validate | Realización de una Validación
*PaymentApi* | [**void_debt_payment_post**](docs/PaymentApi.md#void_debt_payment_post) | **POST** /VoidDebtPayment | Cancelación de  Pago de Deuda, Saldo o Resumen.
*PaymentApi* | [**void_post**](docs/PaymentApi.md#void_post) | **POST** /Void | Operación de Cancelación/Anulación.
*PaymentApi* | [**wallet_request_post**](docs/PaymentApi.md#wallet_request_post) | **POST** /WalletRequest | Inicia un transacción contra el Wallet
*PaymentApi* | [**wallets_post**](docs/PaymentApi.md#wallets_post) | **POST** /Wallets | Obtiene la Lista de Wallets Disponibles


## Documentation For Models

 - [AuthorizeSaleObject](docs/AuthorizeSaleObject.md)
 - [AuthorizeSaleObjectAuthorizeSale](docs/AuthorizeSaleObjectAuthorizeSale.md)
 - [AuthorizeSaleResponseObject](docs/AuthorizeSaleResponseObject.md)
 - [BalanceInquiryObject](docs/BalanceInquiryObject.md)
 - [BalanceInquiryObjectBalanceInquiry](docs/BalanceInquiryObjectBalanceInquiry.md)
 - [BalanceInquiryResponseObject](docs/BalanceInquiryResponseObject.md)
 - [BlockCancelObject](docs/BlockCancelObject.md)
 - [BlockCancelObjectBlockCancel](docs/BlockCancelObjectBlockCancel.md)
 - [BlockCancelResponseObject](docs/BlockCancelResponseObject.md)
 - [BlockCancelResponseObjectBlockCancelResponse](docs/BlockCancelResponseObjectBlockCancelResponse.md)
 - [BlockCloseObject](docs/BlockCloseObject.md)
 - [BlockCloseObjectBlockClose](docs/BlockCloseObjectBlockClose.md)
 - [BlockCloseResponseObject](docs/BlockCloseResponseObject.md)
 - [BlockCloseResponseObjectBlockCloseResponse](docs/BlockCloseResponseObjectBlockCloseResponse.md)
 - [BlockCreateObject](docs/BlockCreateObject.md)
 - [BlockCreateObjectBlockCreate](docs/BlockCreateObjectBlockCreate.md)
 - [BlockCreateResponseObject](docs/BlockCreateResponseObject.md)
 - [BlockCreateResponseObjectBlockCreateResponse](docs/BlockCreateResponseObjectBlockCreateResponse.md)
 - [CancelObject](docs/CancelObject.md)
 - [CancelObjectCancel](docs/CancelObjectCancel.md)
 - [CancelResponseObject](docs/CancelResponseObject.md)
 - [CancelResponseObjectCancelResponse](docs/CancelResponseObjectCancelResponse.md)
 - [CaptureObject](docs/CaptureObject.md)
 - [CaptureObjectCapture](docs/CaptureObjectCapture.md)
 - [CaptureResponseObject](docs/CaptureResponseObject.md)
 - [CloseObject](docs/CloseObject.md)
 - [CloseObjectClose](docs/CloseObjectClose.md)
 - [CloseResponseObject](docs/CloseResponseObject.md)
 - [CloseResponseObjectCloseResponse](docs/CloseResponseObjectCloseResponse.md)
 - [ConfigureObject](docs/ConfigureObject.md)
 - [ConfigureObjectConfigure](docs/ConfigureObjectConfigure.md)
 - [ConfigureObjectConfigureFiles](docs/ConfigureObjectConfigureFiles.md)
 - [ConfigureObjectConfigureOperations](docs/ConfigureObjectConfigureOperations.md)
 - [ConfigureObjectConfigureTables](docs/ConfigureObjectConfigureTables.md)
 - [ConfigureResponseObject](docs/ConfigureResponseObject.md)
 - [ConfigureResponseObjectConfigureResponse](docs/ConfigureResponseObjectConfigureResponse.md)
 - [ConfirmObject](docs/ConfirmObject.md)
 - [ConfirmObjectConfirm](docs/ConfirmObjectConfirm.md)
 - [ConfirmResponseObject](docs/ConfirmResponseObject.md)
 - [ConfirmResponseObjectConfirmResponse](docs/ConfirmResponseObjectConfirmResponse.md)
 - [DebtInquiryObject](docs/DebtInquiryObject.md)
 - [DebtInquiryObjectDebtInquiry](docs/DebtInquiryObjectDebtInquiry.md)
 - [DebtInquiryResponseObject](docs/DebtInquiryResponseObject.md)
 - [DebtInquiryResponseObjectDebtInquiryResponse](docs/DebtInquiryResponseObjectDebtInquiryResponse.md)
 - [DebtInquiryResponseObjectDebtInquiryResponseAccountSummary](docs/DebtInquiryResponseObjectDebtInquiryResponseAccountSummary.md)
 - [DebtInquiryResponseObjectDebtInquiryResponseAccountSummaryAccountStatus](docs/DebtInquiryResponseObjectDebtInquiryResponseAccountSummaryAccountStatus.md)
 - [DebtInquiryResponseObjectDebtInquiryResponseCompanies](docs/DebtInquiryResponseObjectDebtInquiryResponseCompanies.md)
 - [DebtPaymentObject](docs/DebtPaymentObject.md)
 - [DebtPaymentObjectDebtPayment](docs/DebtPaymentObjectDebtPayment.md)
 - [DebtPaymentObjectDebtPaymentRequiredInformation](docs/DebtPaymentObjectDebtPaymentRequiredInformation.md)
 - [DebtPaymentResponseObject](docs/DebtPaymentResponseObject.md)
 - [DebtPaymentResponseObjectDebtPaymentResponse](docs/DebtPaymentResponseObjectDebtPaymentResponse.md)
 - [DepositObject](docs/DepositObject.md)
 - [DepositObjectDeposit](docs/DepositObjectDeposit.md)
 - [DepositResponseObject](docs/DepositResponseObject.md)
 - [DepositResponseObjectDepositResponse](docs/DepositResponseObjectDepositResponse.md)
 - [EnableServiceObject](docs/EnableServiceObject.md)
 - [EnableServiceObjectEnableService](docs/EnableServiceObjectEnableService.md)
 - [EnableServiceResponseObject](docs/EnableServiceResponseObject.md)
 - [EnableServiceResponseObjectEnableServiceResponse](docs/EnableServiceResponseObjectEnableServiceResponse.md)
 - [EnrollmentObject](docs/EnrollmentObject.md)
 - [EnrollmentObjectEnrollment](docs/EnrollmentObjectEnrollment.md)
 - [EnrollmentObjectEnrollmentRecurrence](docs/EnrollmentObjectEnrollmentRecurrence.md)
 - [EnrollmentResponseObject](docs/EnrollmentResponseObject.md)
 - [EnrollmentResponseObjectEnrollmentResponse](docs/EnrollmentResponseObjectEnrollmentResponse.md)
 - [GetBlockObject](docs/GetBlockObject.md)
 - [GetBlockObjectGetBlock](docs/GetBlockObjectGetBlock.md)
 - [GetBlockObjectGetBlockTransactionsRequired](docs/GetBlockObjectGetBlockTransactionsRequired.md)
 - [GetBlockResponseObject](docs/GetBlockResponseObject.md)
 - [GetBlockResponseObjectGetBlockResponse](docs/GetBlockResponseObjectGetBlockResponse.md)
 - [GetCardObject](docs/GetCardObject.md)
 - [GetCardObjectGetCard](docs/GetCardObjectGetCard.md)
 - [GetCardResponseObject](docs/GetCardResponseObject.md)
 - [GetCardResponseObjectGetCardResponse](docs/GetCardResponseObjectGetCardResponse.md)
 - [GetTransactionObject](docs/GetTransactionObject.md)
 - [GetTransactionObjectGetTransaction](docs/GetTransactionObjectGetTransaction.md)
 - [GetTransactionResponseObject](docs/GetTransactionResponseObject.md)
 - [GetTransactionResponseObjectGetTransactionResponse](docs/GetTransactionResponseObjectGetTransactionResponse.md)
 - [GetTransactionResponseObjectGetTransactionResponsePayer](docs/GetTransactionResponseObjectGetTransactionResponsePayer.md)
 - [GetTransactionResponseObjectGetTransactionResponseTransaction](docs/GetTransactionResponseObjectGetTransactionResponseTransaction.md)
 - [KeepAliveObject](docs/KeepAliveObject.md)
 - [KeepAliveResponseObject](docs/KeepAliveResponseObject.md)
 - [KeepAliveResponseObjectKeepAliveResponse](docs/KeepAliveResponseObjectKeepAliveResponse.md)
 - [KeysRenewalObject](docs/KeysRenewalObject.md)
 - [KeysRenewalObjectKeysRenewal](docs/KeysRenewalObjectKeysRenewal.md)
 - [KeysRenewalResponseObject](docs/KeysRenewalResponseObject.md)
 - [KeysRenewalResponseObjectKeysRenewalResponse](docs/KeysRenewalResponseObjectKeysRenewalResponse.md)
 - [OrderFinalObject](docs/OrderFinalObject.md)
 - [OrderFinalObjectOrderFinal](docs/OrderFinalObjectOrderFinal.md)
 - [OrderFinalResponseObject](docs/OrderFinalResponseObject.md)
 - [OrderFinalResponseObjectOrderFinalResponse](docs/OrderFinalResponseObjectOrderFinalResponse.md)
 - [OrderGetObject](docs/OrderGetObject.md)
 - [OrderGetObjectOrderGet](docs/OrderGetObjectOrderGet.md)
 - [OrderGetResponseObject](docs/OrderGetResponseObject.md)
 - [OrderGetResponseObjectOrderGetResponse](docs/OrderGetResponseObjectOrderGetResponse.md)
 - [OrderInitialObject](docs/OrderInitialObject.md)
 - [OrderInitialObjectOrderInitial](docs/OrderInitialObjectOrderInitial.md)
 - [OrderInitialResponseObject](docs/OrderInitialResponseObject.md)
 - [OrderInitialResponseObjectOrderInitialResponse](docs/OrderInitialResponseObjectOrderInitialResponse.md)
 - [OrderStatusObject](docs/OrderStatusObject.md)
 - [OrderStatusObjectOrderStatus](docs/OrderStatusObjectOrderStatus.md)
 - [OrderStatusResponseObject](docs/OrderStatusResponseObject.md)
 - [OrderStatusResponseObjectOrderStatusResponse](docs/OrderStatusResponseObjectOrderStatusResponse.md)
 - [PaymentMethodObject](docs/PaymentMethodObject.md)
 - [PaymentMethodObjectPaymentMethod](docs/PaymentMethodObjectPaymentMethod.md)
 - [PaymentMethodResponseObject](docs/PaymentMethodResponseObject.md)
 - [PaymentMethodResponseObjectPaymentMethodResponse](docs/PaymentMethodResponseObjectPaymentMethodResponse.md)
 - [PaymentMethodResponseObjectPaymentMethodResponseConfiguration](docs/PaymentMethodResponseObjectPaymentMethodResponseConfiguration.md)
 - [PaymentMethodResponseObjectPaymentMethodResponseConfigurationCompany](docs/PaymentMethodResponseObjectPaymentMethodResponseConfigurationCompany.md)
 - [PaymentMethodsObject](docs/PaymentMethodsObject.md)
 - [PaymentMethodsObjectPaymentMethods](docs/PaymentMethodsObjectPaymentMethods.md)
 - [PaymentMethodsResponseObject](docs/PaymentMethodsResponseObject.md)
 - [PaymentMethodsResponseObjectPaymentMethodsResponse](docs/PaymentMethodsResponseObjectPaymentMethodsResponse.md)
 - [PaymentMethodsResponseObjectPaymentMethodsResponseCategory](docs/PaymentMethodsResponseObjectPaymentMethodsResponseCategory.md)
 - [PaymentMethodsResponseObjectPaymentMethodsResponsePaymentMethods](docs/PaymentMethodsResponseObjectPaymentMethodsResponsePaymentMethods.md)
 - [PaymentMethodsResponseObjectPaymentMethodsResponseType](docs/PaymentMethodsResponseObjectPaymentMethodsResponseType.md)
 - [QueryCompaniesObject](docs/QueryCompaniesObject.md)
 - [QueryCompaniesObjectQueryCompanies](docs/QueryCompaniesObjectQueryCompanies.md)
 - [QueryCompaniesResponseObject](docs/QueryCompaniesResponseObject.md)
 - [QueryCompaniesResponseObjectQueryCompaniesResponse](docs/QueryCompaniesResponseObjectQueryCompaniesResponse.md)
 - [QueryCompaniesResponseObjectQueryCompaniesResponseAdditionalInformation](docs/QueryCompaniesResponseObjectQueryCompaniesResponseAdditionalInformation.md)
 - [QueryCompaniesResponseObjectQueryCompaniesResponseCompanies](docs/QueryCompaniesResponseObjectQueryCompaniesResponseCompanies.md)
 - [QueryLineOfBusinessObject](docs/QueryLineOfBusinessObject.md)
 - [QueryLineOfBusinessObjectQueryLineOfBusiness](docs/QueryLineOfBusinessObjectQueryLineOfBusiness.md)
 - [QueryLineOfBusinessResponseObject](docs/QueryLineOfBusinessResponseObject.md)
 - [QueryLineOfBusinessResponseObjectQueryLineOfBusinessResponse](docs/QueryLineOfBusinessResponseObjectQueryLineOfBusinessResponse.md)
 - [QueryLineOfBusinessResponseObjectQueryLineOfBusinessResponseLineOfBusiness](docs/QueryLineOfBusinessResponseObjectQueryLineOfBusinessResponseLineOfBusiness.md)
 - [ReturnObject](docs/ReturnObject.md)
 - [ReturnObjectReturn](docs/ReturnObjectReturn.md)
 - [ReturnResponseObject](docs/ReturnResponseObject.md)
 - [SaleObject](docs/SaleObject.md)
 - [SaleObjectSale](docs/SaleObjectSale.md)
 - [SaleObjectSaleCustomer](docs/SaleObjectSaleCustomer.md)
 - [SaleObjectSaleInputTokens](docs/SaleObjectSaleInputTokens.md)
 - [SaleObjectSalePayer](docs/SaleObjectSalePayer.md)
 - [SaleObjectSaleProducts](docs/SaleObjectSaleProducts.md)
 - [SaleObjectSaleRequiredInformation](docs/SaleObjectSaleRequiredInformation.md)
 - [SaleObjectSaleSecurity](docs/SaleObjectSaleSecurity.md)
 - [SaleObjectSaleSeller](docs/SaleObjectSaleSeller.md)
 - [SaleObjectSaleValues](docs/SaleObjectSaleValues.md)
 - [SaleResponseObject](docs/SaleResponseObject.md)
 - [SaleResponseObjectSaleResponse](docs/SaleResponseObjectSaleResponse.md)
 - [SaleResponseObjectSaleResponseAdditionalInformation](docs/SaleResponseObjectSaleResponseAdditionalInformation.md)
 - [SaleResponseObjectSaleResponseCardCategory](docs/SaleResponseObjectSaleResponseCardCategory.md)
 - [SaleResponseObjectSaleResponseConfiguration](docs/SaleResponseObjectSaleResponseConfiguration.md)
 - [SaleResponseObjectSaleResponseConfigurationBranch](docs/SaleResponseObjectSaleResponseConfigurationBranch.md)
 - [SaleResponseObjectSaleResponseConfigurationCompany](docs/SaleResponseObjectSaleResponseConfigurationCompany.md)
 - [SaleResponseObjectSaleResponseLayout](docs/SaleResponseObjectSaleResponseLayout.md)
 - [SaleResponseObjectSaleResponseMerchantCategory](docs/SaleResponseObjectSaleResponseMerchantCategory.md)
 - [SaleResponseObjectSaleResponseNotification](docs/SaleResponseObjectSaleResponseNotification.md)
 - [SaleResponseObjectSaleResponseNotificationControlUseRule](docs/SaleResponseObjectSaleResponseNotificationControlUseRule.md)
 - [SaleResponseObjectSaleResponseNotificationDistributionList](docs/SaleResponseObjectSaleResponseNotificationDistributionList.md)
 - [SaleResponseObjectSaleResponsePaymentMethod](docs/SaleResponseObjectSaleResponsePaymentMethod.md)
 - [SaleResponseObjectSaleResponsePaymentMethodCategory](docs/SaleResponseObjectSaleResponsePaymentMethodCategory.md)
 - [SaleResponseObjectSaleResponsePaymentMethodDebitAccount](docs/SaleResponseObjectSaleResponsePaymentMethodDebitAccount.md)
 - [SaleResponseObjectSaleResponsePaymentMethodIssuers](docs/SaleResponseObjectSaleResponsePaymentMethodIssuers.md)
 - [SaleResponseObjectSaleResponsePaymentMethodType](docs/SaleResponseObjectSaleResponsePaymentMethodType.md)
 - [SaleResponseObjectSaleResponsePlans](docs/SaleResponseObjectSaleResponsePlans.md)
 - [SaleResponseObjectSaleResponsePlansCashback](docs/SaleResponseObjectSaleResponsePlansCashback.md)
 - [SaleResponseObjectSaleResponsePlansDeferral](docs/SaleResponseObjectSaleResponsePlansDeferral.md)
 - [SaleResponseObjectSaleResponseProducts](docs/SaleResponseObjectSaleResponseProducts.md)
 - [SaleResponseObjectSaleResponseRequiredInformation](docs/SaleResponseObjectSaleResponseRequiredInformation.md)
 - [SaleResponseObjectSaleResponseTickets](docs/SaleResponseObjectSaleResponseTickets.md)
 - [SaleResponseObjectSaleResponseWorkingKeys](docs/SaleResponseObjectSaleResponseWorkingKeys.md)
 - [SettlementObject](docs/SettlementObject.md)
 - [SettlementObjectSettlement](docs/SettlementObjectSettlement.md)
 - [SettlementResponseObject](docs/SettlementResponseObject.md)
 - [ValidateObject](docs/ValidateObject.md)
 - [ValidateObjectValidate](docs/ValidateObjectValidate.md)
 - [ValidateResponseObject](docs/ValidateResponseObject.md)
 - [ValidateResponseObjectValidateResponse](docs/ValidateResponseObjectValidateResponse.md)
 - [VoidDebtPaymentObject](docs/VoidDebtPaymentObject.md)
 - [VoidDebtPaymentObjectVoidDebtPayment](docs/VoidDebtPaymentObjectVoidDebtPayment.md)
 - [VoidDebtPaymentObjectVoidDebtPaymentProducts](docs/VoidDebtPaymentObjectVoidDebtPaymentProducts.md)
 - [VoidDebtPaymentResponseObject](docs/VoidDebtPaymentResponseObject.md)
 - [VoidObject](docs/VoidObject.md)
 - [VoidObjectVoid](docs/VoidObjectVoid.md)
 - [VoidResponseObject](docs/VoidResponseObject.md)
 - [VoidResponseObjectVoidResponse](docs/VoidResponseObjectVoidResponse.md)
 - [WalletRequestObject](docs/WalletRequestObject.md)
 - [WalletRequestObjectWalletRequest](docs/WalletRequestObjectWalletRequest.md)
 - [WalletRequestResponseObject](docs/WalletRequestResponseObject.md)
 - [WalletRequestResponseObjectWalletRequestResponse](docs/WalletRequestResponseObjectWalletRequestResponse.md)
 - [WalletsObject](docs/WalletsObject.md)
 - [WalletsObjectWallets](docs/WalletsObjectWallets.md)
 - [WalletsResponseObject](docs/WalletsResponseObject.md)
 - [WalletsResponseObjectWalletsResponse](docs/WalletsResponseObjectWalletsResponse.md)
 - [WalletsResponseObjectWalletsResponseWallets](docs/WalletsResponseObjectWalletsResponseWallets.md)


## Documentation For Authorization


## ApiKeyHeaderAuth

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author

integrations@evopayments.mx


## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in openapi_client.apis and openapi_client.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from openapi_client.api.default_api import DefaultApi`
- `from openapi_client.model.pet import Pet`

Solution 2:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import openapi_client
from openapi_client.apis import *
from openapi_client.models import *
```

