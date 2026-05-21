class Dog:
    kind = "Bulldog"  # 클래스 변수 (모든 객체가 공유)
    def __init__(self, name, age):
        self.name = name # 인스턴스 변수 (각 객체마다 다름)
        self.age = age # 인스턴스 변수 (각 객체마다 다름)
        
# 클래스 변수 Lab