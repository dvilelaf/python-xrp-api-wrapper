# Python XRP-API wrapper

A simple python wrapper for [xrp-api](https://xrpl.org/xrp-api.html) [[Github](https://github.com/ripple/xrp-api)]

## How to use

```python
from xrp_api import XRPAPI

api = XRPAPI()

account_transactions = api.get_account_transactions('<XRPL_address>')
account_info = api.get_account_info('<XRPL_address>')
account_settings = api.get_account_settings('<XRPL_address>')
transaction = api.get_transaction('<transcation_id>')
payment = api.submit_payment('<XRPL_source_address>', '<XRPL_destination_address>', amount, '<auth_token>')
ping = api.ping()
server_info = api.get_server_info()
api_docs = api.get_api_docs()

```