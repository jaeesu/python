from request import get_message
from service.SettingResponse import send_request, Response_repos, Response_commit_activity

if __name__=='__main__':
    h_req = get_message()
    h_req.repos("jaeesu")
    Response_commit_activity(h_req)
