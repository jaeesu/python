from requests import get, post

#curl   -H "Accept: application/vnd.github.v3+json"   https://api.github.com/users/jaeesu/repos | grep '"name"'
#curl   -H "Accept: application/vnd.github.v3+json"   https://api.github.com/repos/jaeesu/BOJ/stats/commit_activity

PAGE_URL = "https://api.github.com/"
HEADER = {'Accept': 'application/vnd.github.v3+json'}

class get_message:

    def __init__(self):
        self.url=""
        self.username=""
        self.endpoint=""
        self.response = None

    def repos(self, username) :
        self.username = username
        self.endpoint = "users/"+self.username+"/repos"
        #self.endpoint = "repos/"+username+"/"+repos+"/stats/commit_activity"
        return self

    def commit_activity(self, repos) :
        self.endpoint = "repos/" + self.username +"/"+repos+"/stats/commit_activity"
        return self




