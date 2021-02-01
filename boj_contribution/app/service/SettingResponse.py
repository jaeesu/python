from requests import get
<<<<<<< HEAD
from request import get_message, PAGE_URL, HEADER

from .Date import convert_datetime


def send_request(message: get_message):
    message.url = PAGE_URL + message.endpoint
    message.response = get(message.url, headers=HEADER).json()
    return(message.response)

def Response_repos(message : get_message):
    #@param message(username)
    response = send_request(message)
    repos_list=[]
    for i in response:
        repos_list.append(i['name'])
    return(repos_list)


def Response_commit_activity(message : get_message):
    #response = enumerate(responsdde)
    #@param message(username, repos)
    repos_list = Response_repos(message)
    commit_list=[[0]*7]*52
    for i in repos_list:
        response = send_request(message.commit_activity(i))
        print("\n<<<  "+i+"  >>>\n")
        j=0
        for j in range(len(response)):
            print("week: ", convert_datetime(response[j]['week']), response[j]['days'])
            commit_list[j]+=response[j]['days']
            j+=1
            
    print("\n\n<<<   commit_list   >>>\n")

    for i in commit_list:
        print(i,"\n")
        
            #commit_list.append(response['days'])

=======

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
>>>>>>> 11bad59436e9438bb04e962bca0248aec7450538
