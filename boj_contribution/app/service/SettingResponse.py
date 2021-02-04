from requests import get
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
    global commit_list
    commit_list=[[0]*8]*52
    for i in repos_list:
        response = send_request(message.commit_activity(i))
        print("\n<<<  "+i+"  >>>\n")
        make_repos_act(response)
    print("\n<<<<< coommit list >>>>>\n")
    print(commit_list)

def make_repos_act(response) :
    i=0
    for i in range(len(response)):
        j=0
        for j in range(8):
            commit_list[i][j] += response[i]['days'][j]
            j+=1
        commit_list[i][7] = "\n"
        i+=1

            

