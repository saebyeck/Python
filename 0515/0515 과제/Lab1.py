class Television:
    def __init__(self, channel, volume, on): # 처음 객체 만들 때 실행됨 (채널, 볼륨, 전원 상태 저장)
        self.channel = channel
        self.volume = volume
        self.on = on

    def show(self): #  # 현재 상태 출력힘
        print(self.channel, self.volume, self.on)

    def setChannel(self, channel):  # 채널 변경하는 함수
        self.channel = channel

    def getChannel(self):   # 현재 채널 알려주는 함수
        return self.channel
    
t = Television(9, 10, True)
t.show()
t.setChannel(11)
t.show()
