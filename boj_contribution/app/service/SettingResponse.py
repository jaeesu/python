from requests import get
from request import get_message, PAGE_URL, HEADER
from .Date import convert_datetime

import numpy as np
import json


commit_list = []

def send_request(message: get_message) -> json:
    message.url = PAGE_URL + message.endpoint
    message.response = get(message.url, headers=HEADER).json()
    return(message.response)

def Response_repos(message : get_message) -> list:
    #@param message(username)
    response = send_request(message)
    repos_list=[]
    for i in response:
        repos_list.append(i['name'])

    return(repos_list)


def Response_commit_activity(message : get_message) -> list:
    #@param message(username, repos)
    repos_list = Response_repos(message)
    global commit_list
    commit_list=[[0]*7]*52
    commit_list = np.array(commit_list)
    for i in repos_list:
        response = send_request(message.commit_activity(i))
        make_repos_act(response)

    return commit_list


def make_repos_act(response) -> None:
    global commit_list
    lst =[]
    for i in range(0, len(response)):
        lst.append(response[i]['days'])
    
    lst = np.array(lst)
    commit_list += lst
