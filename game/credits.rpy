# Credits.rpy

# This controls the ending of DDLC and your mod!

# Use this as a starting point if want to override this with your own.

# Import the datetime python library to calculate time.
init python:
    import datetime

# Team Salvato Logo
image credits_ts:
    "images/splash-white.png"
    xalign 0.5 yalign 0.6
    zoom 0.65 alpha 0 subpixel True
    linear 2.0 alpha 1
    4.5
    linear 2.0 alpha 0

# Style fonts for the credits
style credits_header:
    # font "gui/font/RifficFree-Bold.ttf"
    color "#ffaae6"
    size 36
    text_align 0.5
    outlines []

style credits_text:
    # font "gui/font/Halogen.ttf"
    color "#fff"
    size 36
    text_align 0.5
    outlines []


image credits_header = ParameterizedText(style="credits_header", ypos=-40)
image credits_text = ParameterizedText(style="credits_text", ypos=40)

# Credit animations to make the credits and images move.
transform credits_scroll:
    subpixel True
    yoffset 740
    linear 15 yoffset -380

transform credits_text_scroll:
    anchor (0.5, 0.5) subpixel True
    yoffset 920
    linear 15 yoffset -200

transform credits_sticker_scroll:
    subpixel True
    yoffset 940
    7.8
    linear 15 yoffset -180

transform credits_scroll_right:
    xalign 0.9
    credits_scroll

transform credits_scroll_left:
    xalign 0.1
    credits_scroll

transform credits_text_scroll_right:
    xpos 960
    credits_text_scroll

transform credits_text_scroll_left:
    xpos 320
    credits_text_scroll

transform credits_text_scroll_middle:
    xpos 640
    credits_text_scroll

define credits_ypos = 250

# Start of the actual credits scene
label credits:
    # Reloads DDLC to credits
    $ persistent.autoload = "credits" 
    $ renpy.save_persistent()
    $ config.keymap['game_menu'] = []
    $ config.keymap['hide_windows'] = []
    $ renpy.display.behavior.clear_keymap_cache()
    $ quick_menu = False
    $ config.skipping = False
    $ config.allow_skipping = False
    scene black

    jump credits2

# This is where the credit scroll starts
label credits2:
    scene black
    $ consolehistory = []
    # play music "<from 50.0>audio/credits.ogg" noloop
    $ starttime = datetime.datetime.now()
    pause 0.88
    
    # Actual names for Credits, where you plug in stuff
    show credits_header "Concept & Game Design" as credits_header_1 at credits_text_scroll_middle
    show credits_text "Dan Salvato" as credits_text_1 at credits_text_scroll_middle
    
    $ pause(16.95 - (datetime.datetime.now() - starttime).total_seconds())
    
    show credits_header "Character Art" as credits_header_2 at credits_text_scroll_middle
    show credits_text "Satchely" as credits_text_2 at credits_text_scroll_middle

    $ pause(26.05 - (datetime.datetime.now() - starttime).total_seconds())
    
    show credits_header "Background Art" as credits_header_1 at credits_text_scroll_middle
    show credits_text "Velinquent" as credits_text_1 at credits_text_scroll_middle
    
    $ pause(35.15 - (datetime.datetime.now() - starttime).total_seconds())
    
    show credits_header "Writing" as credits_header_2 at credits_text_scroll_middle
    show credits_text "Dan Salvato" as credits_text_2 at credits_text_scroll_middle
    
    $ pause(44.25 - (datetime.datetime.now() - starttime).total_seconds())
    
    show credits_header "Music" as credits_header_1 at credits_text_scroll_middle
    show credits_text "Dan Salvato" as credits_text_1 at credits_text_scroll_middle

    $ pause(53.35 - (datetime.datetime.now() - starttime).total_seconds())
    
    show credits_header "Vocals" as credits_header_2 at credits_text_scroll_middle
    show credits_text "Jillian Ashcraft" as credits_text_2 at credits_text_scroll_middle
    
    $ pause(62.45 - (datetime.datetime.now() - starttime).total_seconds())
    
    show credits_header "Special Thanks" as credits_header_1 at credits_text_scroll_middle
    show credits_text "Masha Gutin\nKagefumi" as credits_text_1 at credits_text_scroll_middle
    
    $ pause(71.55 - (datetime.datetime.now() - starttime).total_seconds())
    
    show credits_header "Special Thanks" as credits_header_2 at credits_text_scroll_middle
    show credits_text "David Evelyn\nCorey Shin" as credits_text_2 at credits_text_scroll_middle
    
    # $ pause(80.60 - (datetime.datetime.now() - starttime).total_seconds())

    $ pause(88.00 - (datetime.datetime.now() - starttime).total_seconds())
    
    show credits_header "Special Thanks" as credits_header_1 at credits_text_scroll_middle
    show credits_text "Alecia Bardachino\nMatt Naples" as credits_text_1 at credits_text_scroll_middle
    
    $ pause(95.00 - (datetime.datetime.now() - starttime).total_seconds())
    
    show credits_header "Special Thanks" as credits_header_2 at credits_text_scroll_middle
    show credits_text "Monika\n[player]" as credits_text_2 at credits_text_scroll_middle
    
    $ pause(104.10 - (datetime.datetime.now() - starttime).total_seconds())

    call updateconsole ("os.remove(\"game/screens.rpy\")", "screens.rpy deleted successfully.")
    call updateconsole ("os.remove(\"game/gui.rpy\")", "gui.rpy deleted successfully.")
    call updateconsole ("os.remove(\"game/menu.rpy\")", "menu.rpy deleted successfully.")
    call updateconsole ("os.remove(\"game/script.rpy\")", "script.rpy deleted successfully.")
    $ pause(115.72 - (datetime.datetime.now() - starttime).total_seconds())
    
    # Hides console and shows the Team Salvato Logo/Thank You
    call hideconsole
    show credits_ts
    show credits_text "made with love by":
        zoom 0.75 xalign 0.5 yalign 0.25 alpha 0 subpixel True
        linear 2.0 alpha 1
        4.5
        linear 2.0 alpha 0
    pause 9.3

    # Fade to black and make the player quit
    label postcredits_loop:
        # Game reloads to the postcredits_loop
        $ persistent.autoload = "postcredits_loop"

        # Disables Main Menu, Quick Menu, Everything
        $ config.keymap['game_menu'] = []
        $ config.keymap['hide_windows'] = []
        $ renpy.display.behavior.clear_keymap_cache()
        $ quick_menu = False
        $ config.skipping = False
        $ config.allow_skipping = False

        # Fade to black
        scene black

        # Shows either Monika's or Dan's Goodbye Message
        $ pause()
        
        # Fakes Error Corruption. Makes the player quit the game.
        call screen dialog(message="Error: Script file is missing or corrupt.\nPlease reinstall the game.", ok_action=Quit(confirm=False))
        return
