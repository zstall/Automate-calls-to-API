import requests
def iterate_all_hosts():
  s = requests.session()
  s.params = {
    'api_key': '',
    'application_key': '',
    'include_muted_hosts_data': False,
    'include_hosts_metadata': False,
    'start': 0
  }
  infra_link = 'https://app.datadoghq.com/api/v1/hosts?count=1000'
  while True:
    response = s.request(method='GET', url=infra_link, params=s.params).json()
    for host in response['host_list']:
        yield host
    if response['total_returned'] == 0:
        return
    s.params['start'] += response['total_returned']

for host in iterate_all_hosts():
    print(host['host_name'])
