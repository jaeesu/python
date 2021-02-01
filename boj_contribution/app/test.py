from request import get_message
<<<<<<< HEAD
from service.SettingResponse import send_request, Response_repos, Response_commit_activity

if __name__=='__main__':
    h_req = get_message()
    h_req.repos("jaeesu")
    print(Response_commit_activity(h_req))
=======
from service.SettingResponse import send_request, Response_repos

if __name__=='__main__':
    h_req = get_message()
    h_req.repos('jaeesu')
    print(Response_repos(send_request(h_req)))

>>>>>>> 11bad59436e9438bb04e962bca0248aec7450538
