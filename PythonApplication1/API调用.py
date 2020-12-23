import requests
url='https://api.github.com/search/repositories?q=language:python&sort=stars'
URL=requests.get(url)
print('Status code',URL.status_code)
    #状态代码为200表示调用成功
response_dict=URL.json()
print(response_dict.keys())
#'items', 'total_count', 'incomplete_results'
print(response_dict['total_count'])
response_dicts=response_dict['items']
response_dict=response_dicts[0]
for key in response_dict.keys():
    print(key)