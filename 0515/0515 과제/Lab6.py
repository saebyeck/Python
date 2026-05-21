class Vector2D:
    def __init__(self, x, y): # 좌표 값 저장
        self.x = x
        self.y = y

    def __add__(self, other): # + 연산자 
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other): # - 연산자
        return Vector2D(self.x - other.x, self.y - other.y)

    def __eq__(self, other): # == 비교 연산자 
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return '(%g, %g)' % (self.x, self.y)


u = Vector2D(0, 1)
v = Vector2D(1, 0)
w = Vector2D(1, 1)
a = u + v
print(a)

# 2차원 공간에서 벡터(vector)는 (a, b)와 같이 2개의 실수로 표현될 수 있다. 벡터 간에는 덧셈이나 뺄셈이 정의된다. 
# (a, b) + (c, d) = (a+c, b+d) , (a, b) - (c, d) = (a-c, b-d)
