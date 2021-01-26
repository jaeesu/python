from hashing import Hashtable

boo = Hashtable()
boo.put('Kim', 7458)
boo.put('John', 8569)
boo.put('Smith', 1452)
boo.put('Michael', 2563)
boo.put('Raymond', 1598)
boo.put('Clayton', 7532)

#Raymond의 번호가 사라짐. 해시값이 겹치기 때문이다.
#이를 해결하려면 해시값이 겹치지 않도록 해시 함수가 더 넓은 범위의 숫자를 생성할 수 있도록 수정해야 함.
#-> 다항식을 표현하는 방법 : 호너의 룰 : 반복적으로 숫자를 곱한 뒤 더한다.

boo.show()
