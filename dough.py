from pico2d import *

class Dough1:
    image = None

    def __init__(self, x = 400, y = 400, size = 1):
        if Dough1.image ==None:
            Dough1.image = load_image(('asset/1. dough/dough0.png'))

        self.x, self.y = x, y
        self.bake = 0 # 오븐에 구은 횟수

    #379*381
    def draw(self):
        self.image.clip_draw(0, 0, 379, 381, self.x, self.y)

    def update(self):
        self.image.clip_draw(0, 0, 379, 381, self.x, self.y)

    def handle_event(self, event):
        pass