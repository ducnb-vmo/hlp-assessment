import requests


url = 'https://stg-console.9pay.mobi'

resp = requests.post(
    url,
    json={
        'request_id': 'request_id_dump_001',
        'partner_id': 'hlp',
        'bank_no': 4,
        'account_no': '1023020330000',
        'account_type': 1,
        'account_name': 'NGUYEN VAN A',
        'amount': 100000,
        'content': 'blabla'
    })

print(url)
print(resp.content)
