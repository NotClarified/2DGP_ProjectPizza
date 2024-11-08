from pico2d import *

# 피망 기본 클래스 생성
class Pimento1:
    image = None

    def __init__(self, x = 0, y = 0, size = 1):
        if Pimento1.image == None:
            Pimento1.image = load_image('/asset/topping/pimento1.png')
        # 위치 크기 조절을 위한 변수
        self.x, self.y = x, y
        self.size = size
        self.growing = True # 크기 증가 여부 조절
    # 피망 - pimento123 :54*54
    # clip_composite_draw(self, left, bottom, width, height, rad, flip, x, y, w = None, h = None):

    def draw(self):
        self.image.clip_composite_draw(0, 0, 54, 54, 0, '', self.x, self.y, self.size * 54, self.size * 54)
        print('pimento1 draw') # 확인용 주석
    def update(self):
        # 크기 조절 로직
        if self.growing:
            self.size *= 1.0001  # 크기 1.0001배 증가
            if self.size >= 1.05:  # 크기가 너무 커지면 감소 모드로 전환
                self.growing = False
        else:
            self.size *= 0.9999  # 크기 0.9999배 감소
            if self.size <= 0.95:  # 크기가 너무 작아지면 증가 모드로 전환
                self.growing = True
        self.image.clip_composite_draw(0, 0, 54, 54, 0, '', self.x, self.y, self.size * 54, self.size * 54)
        print('pimento update')
    def handle_event(self, event):
        pass
