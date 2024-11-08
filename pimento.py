from pico2d import *

# 피망 기본 클래스 생성
class Pimento1:
    image = None

    def __init__(self, x = 0, y = 0, size = 1):
        if Pimento1.image == None:
            Pimento1.image = load_image('/asset/topping/pimento1.png')
        # 위치, 크기 조절을 위한 변수
        self.x, self.y, self.size = size
    # 피망 - pimento123 :54*54
    # clip_composite_draw(self, left, bottom, width, height, rad, flip, x, y, w = None, h = None):

    def draw(self):
        self.image.clip_composite_draw(0, 0, 0, 54, 54, self.size, self.size, 100, 100)

    def update(self):
        self.state_machine.update()

    def handle_event(self, event):
        self.state_machine.add_event(('INPUT', event))


