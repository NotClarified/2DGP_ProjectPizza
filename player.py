from pico2d import *
import game_world
import game_framework

class Player:
    def __init__(self):
        self.x, self.y = 400, 300
        self.image = None  # 선택된 이미지
        self.topping_class = None  # 현재 토핑 클래스

    def set_topping(self, topping_image, topping_class):
        """선택된 토핑 이미지와 클래스 설정"""
        self.image = load_image(f'E:\\2DGP\\2DGP_ProjectPizza\\asset\\3. topping\\{topping_image}')
        self.topping_class = topping_class

    def update(self):
        pass

    def draw(self):
        if self.image:
            self.image.draw(self.x, self.y)

    def handle_event(self, event):
        if event.type == SDL_MOUSEMOTION:
            self.x, self.y = event.x, 800 - event.y - 1
        elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            if self.topping_class:
                topping = self.topping_class(self.x, self.y)
                game_world.add_object(topping, 1)
