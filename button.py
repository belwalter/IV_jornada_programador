# coding: UTF-8

"""
MercadoPago SDK
Create Preference and Show Checkout Example
"""

import os, sys
import mercadopago
import json

def index(req, **kwargs):
    preference = {
      "items": [
        {
          "title": "sdk-python",
          "quantity": 1,
          # "currency_id": "ARS",
          "unit_price": 10.5
        },
        {
          "title": "otro",
          "quantity": 3,
          # "currency_id": "ARS",
          "unit_price": 30.5
        },
        {
          "title": "nuevo",
          "quantity": 4,
          # "currency_id": "ARS",
          "unit_price": 500
        }
      ],
    'back_urls': {'pending': 'www.gmail.com', 'success': 'http://localhost:5000/', 'failure': 'http://www.google.com'},
    'auto_return': 'approved'
    }

    sdk = mercadopago.SDK("ACCESS_TOKEN")
    #mp = mercadopago.SDK("CLIENT_ID", "CLIENT_SECRET")

    preferenceResult = sdk.preference().create(preference)
    print(preferenceResult)
    url = preferenceResult["response"]["sandbox_init_point"]

    output = """
    <!doctype html>
    <html>
        <head>
            <title>MercadoPago SDK - Create Preference and Show Checkout Example</title>
        </head>
      <body>
        <a href="{url}" name="MP-Checkout" class="blue-l-arall-rn">Pagar</a>
        <script type="text/javascript" src="//resources.mlstatic.com/mptools/render.js"></script>
      </body>
    </html>
    """.format (url=url)

    return url
