from pico2d import *

# 페퍼로니 기본 클래스 생성
class Meat1:
    image = None

    def __init__(self, x = 400, y = 400, size = 0.1):
        if Meat1.image == None:
            Meat1.image = load_image('asset/3. topping/meat1.png')
        # 위치 크기 조절을 위한 변수
        self.x, self.y = x, y
        self.size = size
        self.growing = True # 크기 증가 여부 조절
        self.angle = 0  # 회전 각도 초기화
        self.rotation_speed = 360 / 200000  # 20초 동안 360도 회전 생각해서 360 / 각도로 진행

    # 페퍼로니 - meat123: 42 * 42

    # clip_composite_draw(self, left, bottom, width, height, rad, flip, x, y, w = None, h = None):

    def draw(self):
        self.image.clip_composite_draw(0, 0,42, 42, self.angle, '', self.x, self.y, self.size * 42, self.size * 42)
        print('meat1 draw') # 확인용 주석
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

        self.angle += self.rotation_speed
        if self.angle >= 360: #360도 각도에 맞춰서 360 넘기면 초기화 진행
            self.angle -= 360
        self.image.clip_composite_draw(0, 0, 42, 42, self.angle, '', self.x, self.y, self.size * 42, self.size * 42)
        print('meat1 update')
    def handle_event(self, event):
        pass

class Meat2:
    image = None

    def __init__(self, x = 200, y = 200, size = 0.1):
        if Meat2.image == None:
            Meat2.image = load_image('asset/3. topping/meat2.png')
        # 위치 크기 조절을 위한 변수
        self.x, self.y = x, y
        self.size = size
        self.growing = True # 크기 증가 여부 조절
        self.angle = 0  # 회전 각도 초기화
        self.rotation_speed = 360 / 200000  # 20초 동안 360도 회전 생각해서 360 / 각도로 진행

    # 페퍼로니 - meat123: 42 * 42
    # clip_composite_draw(self, left, bottom, width, height, rad, flip, x, y, w = None, h = None):

    def draw(self):
        self.image.clip_composite_draw(0, 0, 42, 42, self.angle, '', self.x, self.y, self.size * 42, self.size * 42)
        print('meat2 draw') # 확인용 주석
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

        self.angle += self.rotation_speed
        if self.angle >= 360: #360도 각도에 맞춰서 360 넘기면 초기화 진행
            self.angle -= 360
        self.image.clip_composite_draw(0, 0, 42, 42, self.angle, '', self.x, self.y, self.size * 42, self.size * 42)
        print('meat2 update')
    def handle_event(self, event):
        pass

class Meat3:
    image = None

    def __init__(self, x = 300, y = 300, size = 0.1):
        if Meat3.image == None:
            Meat3.image = load_image('asset/3. topping/meat3.png')
        # 위치 크기 조절을 위한 변수
        self.x, self.y = x, y
        self.size = size
        self.growing = True # 크기 증가 여부 조절
        self.angle = 0  # 회전 각도 초기화
        self.rotation_speed = 360 / 200000  # 20초 동안 360도 회전 생각해서 360 / 각도로 진행

    # 페퍼로니 - meat123: 42 * 42
    # clip_composite_draw(self, left, bottom, width, height, rad, flip, x, y, w = None, h = None):

    def draw(self):
        self.image.clip_composite_draw(0, 0, 42, 42, self.angle, '', self.x, self.y, self.size * 42, self.size * 42)
        print('meat3 draw') # 확인용 주석
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

        self.angle += self.rotation_speed
        if self.angle >= 360: #360도 각도에 맞춰서 360 넘기면 초기화 진행
            self.angle -= 360
        self.image.clip_composite_draw(0, 0, 42, 42, self.angle, '', self.x, self.y, self.size * 42, self.size * 42)
        print('meat3 update')
    def handle_event(self, event):
        pass
