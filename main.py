from urllib.parse import urlencode

PAYPAL_URL = "https://www.sandbox.paypal.com/cgi-bin/webscr"
PAYPAL_ACCOUNT = "merchange@mydomain.tld" # as set in the paypal developer console
my_order_id = 3
my_price = 20.00
my_ngrok_url = "http://8acfc9049ed2.ngrok.io"

def paypal_url():
    params = {
        'business': PAYPAL_ACCOUNT,
        'cmd': '_xclick',
        'invoice': my_order_id,
        'amount': my_price,
        'item_name': 'my_order_string_reference',
        'item_number': 'order_user_id',
        'quantity': 1,
        'currency_code': 'EUR',
        'notify_url': my_ngrok_url + "/payment/real_ipn",
        'on0': '0'
    }
    return PAYPAL_URL + '?' + urlencode(params)

if __name__ == '__main__':
    print(paypal_url())
