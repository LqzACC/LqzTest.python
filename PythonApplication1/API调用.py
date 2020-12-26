import requests
from operator import itemgetter 

"""
url='https://api.github.com/search/repositories?q=language:python&sort=stars'
URL=requests.get(url)
print('Status code',URL.status_code)
    #状态代码为200表示调用成功
response_dict_url=URL.json()
#{'items':[{'1':,'2':,'3':....},{},{}],'total_count':,'i_c':}
print(response_dict_url.keys())
#'items', 'total_count', 'incomplete_results'
print(response_dict_url['total_count'])
response_dicts=response_dict_url['items']
#response_dict=response_dicts[0]
names,star=[],[]
for response_dict in response_dicts:
    names.append(response_dict['name'])
    dict={'value':response_dict['stargazers_count'],
          'label':str(response_dict['description']),
          'xlink':response_dict['html_url'],
          }
    star.append(dict)
"""

"""
url='https://hacker-news.firebaseio.com/v0/topstories.json'
URL=requests.get(url)
print('status_code',URL.status_code)
res_dict=URL.json()
title,sub_dicts=[],[]
for res_dicts in res_dict[:100]:
    url='https://hacker-news.firebaseio.com/v0/item/'+str(res_dicts)+'.json'
    submission=requests.get(url)
    print('status_code',submission.status_code)
    submission_dict=submission.json()
    submission_dicts={'value':submission_dict.get('descendants',0),
                      'xlink':'http://news.ycombinator.com/item?id='+str(res_dicts),
                      'label':submission_dict['title']
                      }
    sub_dicts.append(submission_dicts)

sub_dicts=sorted(sub_dicts,key=itemgetter('value'),reverse=True)
for a in sub_dicts:
    title.append(a['label'])
"""