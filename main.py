import argparse
from openapi_client import ApiClient, Configuration
from openapi_client.api.payment_api import PaymentApi
from openapi_client.model.block_create_object_block_create import BlockCreateObjectBlockCreate
from openapi_client.model.keep_alive_object import KeepAliveObject

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--hostname', help='set basepath hostname')

args = parser.parse_args()
hostname = args.hostname


def start():
    if not hostname:
        api_configuration = Configuration('https://testcodi.multipay.mx:30801/token/CL/Payments/Authorize/5.6.1')
    else:
        api_configuration = Configuration(hostname)

    api_configuration.api_key_prefix = {'OAuth': 'Bearer'}
    api_configuration.api_key = {"OAuth": "1e7a1e55-5df4-3d80-959a-b8528f68d785"}
    api_client = ApiClient(api_configuration)
    api_client.default_authentication = "OAuth"

    print(f'Utilizando hostname: {api_client.configuration.host}')

    payment_api = PaymentApi(api_client)
    payment_api.__init__(api_client)

    keepalive_object = KeepAliveObject()

    system_identification = 'BciPagos1.0.0'
    company_identification = '2000001'
    keepalive_data = BlockCreateObjectBlockCreate(company_identification, system_identification)
    setattr(keepalive_data, 'branch_identification', '2100001')
    setattr(keepalive_data, 'pos_identification', '2110004')

    setattr(keepalive_object, 'keep_alive', keepalive_data)

    print('Llamando a KeepAlive...')
    try:
        response = payment_api.keep_alive_post(keepalive_object)
        print('ResponseCode: ' + str(response.keep_alive_response.response_code));
        print('ResponseMessage: ' + response.keep_alive_response.response_message);
    except Exception as e:
        print("Error:")
        print(e)

    return


start()
