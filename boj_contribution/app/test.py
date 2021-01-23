from request import get_message
from service.SettingResponse import send_request, Response_repos

if __name__=='__main__':
    h_req = get_message()
    h_req.repos('jaeesu')
    print(Response_repos(send_request(h_req)))

