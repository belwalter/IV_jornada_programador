# coding: UTF-8

"""
MercadoPago SDK
Create Preference and Show Checkout Example
"""

import mercadopago

def generate_link(items, shipment):
    preference = {
      "items": items,
      'back_urls': {
         'pending': 'http://localhost:5000/pending',
         'success': 'http://localhost:5000/success',
         'failure': 'http://localhost:5000/failure'},
      'auto_return': 'approved',
      "shipments": shipment
    }

    sdk = mercadopago.SDK("TEST-1145830853388434-091121-831b76ae7c6cc5fa1ce8ecfb698b9512-118943122")
    #sdk = mercadopago.SDK("CLIENT_ID", "CLIENT_SECRET")

    preferenceResult = sdk.preference().create(preference)
    # for key, value in preferenceResult['response'].items():
    #   print('#####', key, value)
    url = preferenceResult["response"]["sandbox_init_point"]

    return url
