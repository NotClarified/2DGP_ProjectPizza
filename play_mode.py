from pico2d import *

import game_framework
import game_world
from pimento import Pimento1


def handle_events():

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()

def init():
    global running

    running = True
    pimento = Pimento1()
    game_world.add_object(pimento,1)
def finish():
    game_world.clear()
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
