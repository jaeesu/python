from requests import get

from request import get_message, PAGE_URL, HEADER

def send_request(message : get_message):
    message.url = PAGE_URL+message.endpoint
    message.response = get(message.url, headers=HEADER)
    return(message.response)

def Response_repos(response):
    repos_list=[]
    data = response.json()
    for i in data:
        repos_list.append(i)
    return(repos_list)


def Response_commit_activity(repos_list):
    return 0



######
