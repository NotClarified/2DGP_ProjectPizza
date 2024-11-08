from pico2d import *

import game_framework
import game_world
from dough import Dough1
from pimento import Pimento1, Pimento2, Pimento3


def handle_events():

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()

def init():
    global running

    running = True
    pimento1 = Pimento1()
    pimento2 = Pimento2()
    pimento3 = Pimento3()
    dough1 = Dough1()
    game_world.add_object(pimento1,2)
    game_world.add_object(pimento2,2)
    game_world.add_object(pimento3,2)
    game_world.add_object(dough1,1)
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
