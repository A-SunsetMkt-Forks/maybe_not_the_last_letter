# Definitions.rpy

# This section defines stuff for DDLC and your mod!
# Use this as a starting point if you would like to override with your own.

define persistent.demo = False
define persistent.steam = ("steamapps" in config.basedir.lower())
# Change this to True to enable Developer Mode
define config.developer = "auto"

python early:
    import singleton
    me = singleton.SingleInstance()
    # 计算hash的函数
    import hashlib
    def get_hash256(data): # 对data使用sha256计算hash
        hash256 = hashlib.sha256()
        hash256.update(data.encode('utf-8'))
        return hash256.hexdigest()

init python:
    config.keymap['game_menu'].remove('mouseup_3')
    config.keymap['hide_windows'].append('mouseup_3')
    config.keymap['self_voicing'] = []
    config.keymap['clipboard_voicing'] = []
    config.keymap['toggle_skip'] = []
    renpy.music.register_channel("music_poem", mixer="music", tight=True)
    
    # Get's position of Music
    def get_pos(channel='music'):
        pos = renpy.music.get_pos(channel=channel)
        if pos: return pos
        return 0

    # Delete's All Saves
    def delete_all_saves():
        for savegame in renpy.list_saved_games(fast=True):
            renpy.unlink_save(savegame)

    # Controls time.
    def pause(time=None):
        #global _windows_hidden
        if not time:
            #_windows_hidden = True
            renpy.ui.saybehavior(afm=" ")
            renpy.ui.interact(mouse='pause', type='pause', roll_forward=None)
            #_windows_hidden = False
            return
        if time <= 0: return
        #_windows_hidden = True
        renpy.pause(time)
        #_windows_hidden = False

# Music

# This section is where you can reference DDLC audio and add your own!
# audio. - tells Ren'Py this is sound
# t1 - tells Ren'Py the label of the music/sound file
# <loop 22.073> - tells Ren'Py to loop the song at that time interval
# "audio/1.ogg" - location of your music
define audio.menu = "<loop 0.0>audio/menu.ogg"

# Backgrounds
# To define a new color background do like so
# image blue = "#XXXXXX" where X is your hex digits (#158353)
# To define a new background, do so like this
# image bg bathroom = "mod_assets/bathroom.png" (make sure you use the right file type [.png, .jpg])
image black = "#000000"
image dark = "#000000e4"
image darkred = "#110000c8"
image white = "#ffffff"
image splash = "images/splash.png"
image end:
    truecenter
    "gui/end.png"

image bg glitch = LiveTile("images/glitch.jpg")

image glitch_color:
    ytile 3
    zoom 2.5
    parallel:
        "images/glitch-red.png"
        0.1
        "images/glitch-green.png"
        0.1
        "images/glitch-blue.png"
        0.1
        repeat
    parallel:
        yoffset 720
        linear 0.5 yoffset 0
        repeat
    parallel:
        choice:
            xoffset 0
        choice:
            xoffset 10
        choice:
            xoffset 20
        choice:
            xoffset 35
        choice:
            xoffset -10
        choice:
            xoffset -20
        choice:
            xoffset -30
        0.01
        repeat
    parallel:
        alpha 0.6
        linear 0.15 alpha 0.1
        0.2
        alpha 0.6
        linear 0.15 alpha 0.1
        0.2
        alpha 0.7
        linear 0.45 alpha 0



image glitch_color2:
    ytile 3
    zoom 2.5
    parallel:
        "images/glitch-red.png"
        0.1
        "images/glitch-green.png"
        0.1
        "images/glitch-blue.png"
        0.1
        repeat
    parallel:
        yoffset 720
        linear 0.5 yoffset 0
        repeat
    parallel:
        choice:
            xoffset 0
        choice:
            xoffset 10
        choice:
            xoffset 20
        choice:
            xoffset 35
        choice:
            xoffset -10
        choice:
            xoffset -20
        choice:
            xoffset -30
        0.01
        repeat
    parallel:
        alpha 0.7
        linear 0.45 alpha 0


define _dismiss_pause = config.developer

# Persistent Variables

# These variables are load at game startup and exist on all saves.
## To make a new persistent variable, do so like this
# default persistent.monika = X 
# X is either true/false, a number, array (see persistent.clear for arrays) or string based off your choosing
default persistent.playername = ""
default player = persistent.playername
default persistent.playthrough = 0
default persistent.anticheat = 0
default persistent.clear = [False, False, False, False, False, False, False, False, False, False]
default persistent.clearall = None
default persistent.first_load = None

# Other Persistent Variables
default anticheat = 0
define config.mouse = None
default allow_skipping = True
default basedir = config.basedir
default chapter = 0
default currentpos = 0
default faint_effect = None

# 这里是给神秘人的彩蛋变量
default zegg = False
default persistent.splashegg = False
default zeggcount = 0

default expeggcount = 0