#전화 번호부 프로그램
#전화번호를 가나다 순으로 저장, 검색은 빠르나, 첫 부분에 전화번호를 추가한다면 오래 걸린다.

#해싱의 핵심 : 넓은 공간을 이용해, 데이터의 저장과 검색 시 시간을 줄이는 것

#저장 : 이름을 놓으면 해시가 나오는 해시 함수를 이용해 리턴을 받음. 그 해시값을 주소로 하는 저장공간에 전화번호를 저장

#검색 : 해시 함수에 kim을 넣고 해시 값을 리턴 받은 후, 해시값을 주소로 하는 저장공간을 찾아 읽으면 된다.
#빠른 검색 가능

#이름이라는 문자열 -> 저장공간의 주소(숫자) : 각 글자의 아스키 코드를 합하여 리턴하는 해시 함수
#현재 만드는 해시함수에서 ABC, ACB는 충돌

#해시값 -> 주소 : direct-address table


class Hashtable:
    def __init__(self):
        self.table = [None for _ in range(139)]
       
    def simple_hash(self, name):
        ord_sum=0
        for letter in name:
            ord_sum += ord(letter)
        return ord_sum % len(self.table)
        # return sum(map(ord, name)) % len(len.table)

    def put(self, name, num):
        self.table[self.simple_hash(name)] = num

    def show(self):
        for idx, value in enumerate(self.table):
            if value:  # is not None
                print(idx, value)

    def find(self, name):
        return self.table[self.simple_hash(name)]

