from pico2d import *

import game_framework
import game_world
from player import Player
import toping_mode
from pannel import Pannel
from player import Player
from pimento import Pimento1
from onion import Onion1
from mushroom import Mushroom1
from sapm import Spam1
from meat import Meat1

def set_player(p):
    global player
    player = p

def init():
    global pannel
    pannel = Pannel()
    game_world.add_object(pannel, 3)

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_1:
                player.set_topping('asset/3. topping/pimento1.png', Pimento1)
            elif event.key == SDLK_2:
                player.set_topping('asset/3. topping/onion1.png', Onion1)
            elif event.key == SDLK_3:
                player.set_topping('asset/3. topping/mushroom1.png', Mushroom1)
            elif event.key == SDLK_4:
                player.set_topping('asset/3. topping/spam1.png', Spam1)
            elif event.key == SDLK_5:
                player.set_topping('asset/3. topping/meat1.png', Meat1)
            elif event.key == SDLK_i:
                game_framework.change_mode(toping_mode)


def finish():
    game_world.remove_object(pannel)
    pass

def update():
    game_world.update()

def draw():
    clear_canvas()
    game_world.render()
    update_canvas()

def pause():
    pass
def resume():
    pass

