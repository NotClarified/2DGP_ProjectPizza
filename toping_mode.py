from pico2d import *

import game_framework
import game_world
import select_mode
from dough import Dough1
from pimento import Pimento1, Pimento2, Pimento3
from onion import Onion1, Onion2, Onion3
from mushroom import Mushroom1, Mushroom2, Mushroom3
from sapm import  Spam1, Spam2, Spam3
from meat import Meat1, Meat2, Meat3
from player import Player

def handle_events():
    global player
    events = get_events()
    for event in events:
        player.handle_event(event)
        if event.type == SDL_KEYDOWN and event.key == SDLK_i:
            select_mode.set_player(player)
            game_framework.push_mode(select_mode)

def init():
    global running
    global player

    player = Player()
    running = True
    pimento1 = Pimento1()
    pimento2 = Pimento2()
    pimento3 = Pimento3()
    onion1 = Onion1()
    onion2 = Onion2()
    onion3 = Onion3()
    mushroom1 = Mushroom1()
    mushroom2 = Mushroom2()
    mushroom3 = Mushroom3()
    spam1 = Spam1()
    sapm2 = Spam2()
    spam3 = Spam3()
    meat1 = Meat1()
    meat2 = Meat2()
    meat3 = Meat3()
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
