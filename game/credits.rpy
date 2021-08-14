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
    color "#fff"
    size 36
    text_align 0.5
    outlines []

style credits_text:
    # font "gui/font/Halogen.ttf"
    color "#fff"
    size 36
    text_align 0.5
    outlines []

style endscreen_text:
    size 24
    color "#fff"
    text_align 0.5
    outlines []

image endscreen = ParameterizedText(style="endscreen_text", xalign=0.5, yalign=0.5)

image credits_header = ParameterizedText(style="credits_header", ypos=-40)
image credits_text = ParameterizedText(style="credits_text", ypos=40)

image creditend:
    truecenter
    "gui/end.png"

# Credit animations to make the credits and images move.
transform credits_scroll:
    subpixel True
    yoffset 740
    linear 15 yoffset -380

transform credits_text_scroll:
    anchor (0.5, 0.5) subpixel True
    yoffset 920
    linear 15 yoffset -300

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
    
    if zeggcount >= 7:
        $ zegg = True

    if zegg:
        jump zcredits2

    jump credits2

# This is where the credit scroll starts
label credits2:
    scene black
    $ consolehistory = []
    play music "audio/end.ogg" noloop
    $ starttime = datetime.datetime.now()
    pause 0.88
    
    # Actual names for Credits, where you plug in stuff
    show credits_header _("也许不是最后一封信") as credits_header_1 at credits_text_scroll_middle
    show credits_text _("ProjectZ Studio出品") as credits_text_1 at credits_text_scroll_middle
    
    $ pause(16.95 - (datetime.datetime.now() - starttime).total_seconds())
    
    show credits_header _("理念和游戏设计") as credits_header_2 at credits_text_scroll_middle
    show credits_text _("余晖") as credits_text_2 at credits_text_scroll_middle

    $ pause(26.05 - (datetime.datetime.now() - starttime).total_seconds())
    
    show credits_header _("故事") as credits_header_1 at credits_text_scroll_middle
    show credits_text _("余晖\nEXPLORER") as credits_text_1 at credits_text_scroll_middle
    
    $ pause(35.15 - (datetime.datetime.now() - starttime).total_seconds())
    
    show credits_header _("主要程序员") as credits_header_2 at credits_text_scroll_middle
    show credits_text _("lwd-temp") as credits_text_2 at credits_text_scroll_middle
    
    $ pause(44.25 - (datetime.datetime.now() - starttime).total_seconds())
    
    show credits_header _("") as credits_header_1 at credits_text_scroll_middle
    show credits_text _("音乐\nEasy Breeze (StarSight Remix)  Player_275x / Thomas Greenberg\n穏やかに過ぎゆく時  小林俊太郎\n【Animenz】secret base 〜你给我的所有〜 - 未闻花名 ED 钢琴版  Bilibili用户@Animenzzz\nLeaves in the Wind  Isaac Shepard\nMidday Prospects 午日的眺望 陈致逸 / HOYO-MiX[persistent.expsongname]\n所念皆星河  CMJ") as credits_text_1 at credits_text_scroll_middle

    $ pause(53.35 - (datetime.datetime.now() - starttime).total_seconds())
    
    show credits_header _("策划") as credits_header_2 at credits_text_scroll_middle
    show credits_text _("余晖") as credits_text_2 at credits_text_scroll_middle
    
    $ pause(62.45 - (datetime.datetime.now() - starttime).total_seconds())
    
    show credits_header _("") as credits_header_1 at credits_text_scroll_middle
    show credits_text _("早期测试人员\n840a8dbdddece6a56fb9b1f925eac7a75cb274b85e7eddafdfb97573170e5a8b\nEXPLORER\n83235ec96fa3b9c0631863c5e3f998aef8e89c28698a8fc2843509627cb0d295") as credits_text_1 at credits_text_scroll_middle
    
    $ pause(71.55 - (datetime.datetime.now() - starttime).total_seconds())
    
    show credits_header _("") as credits_header_2 at credits_text_scroll_middle
    show credits_text _("特别感谢\nRen'Py\nTeam Salvato\nHasbro, Inc\nSCP Foundation\nUniverse of My Own\n创造音乐和立绘的艺术家们") as credits_text_2 at credits_text_scroll_middle
    
    # $ pause(80.60 - (datetime.datetime.now() - starttime).total_seconds())

    $ pause(80.60 - (datetime.datetime.now() - starttime).total_seconds())
    
    show credits_header _("") as credits_header_1 at credits_text_scroll_middle
    show credits_text _("此项目的部分代码来自DDLCModTemplate2.0，原则上禁止用于除《心跳文学部》第三方模组的其他用途\n除此之外的其他代码使用 GNU General Public License v3.0 发布\n此项目的部分故事和文案使用 Creative Commons Attribution Share Alike 4.0 International 协议授权\n更多信息请查看项目存储库") as credits_text_1 at credits_text_scroll_middle
    
    $ pause(88.00 - (datetime.datetime.now() - starttime).total_seconds())
    
    show credits_header _("") as credits_header_2 at credits_text_scroll_middle
    show credits_text _("特别感谢\nPrincess Celestia\nMonika\n[player]") as credits_text_2 at credits_text_scroll_middle
    
    $ pause(95.10 - (datetime.datetime.now() - starttime).total_seconds())

    call updateconsole (_("os.remove(\"game/screens.rpy\")"), _("screens.rpy deleted successfully.")) from _call_updateconsole_2
    call updateconsole (_("os.remove(\"game/gui.rpy\")"), _("gui.rpy deleted successfully.")) from _call_updateconsole_3
    call updateconsole (_("os.remove(\"game/menu.rpy\")"), _("menu.rpy deleted successfully.")) from _call_updateconsole_4
    call updateconsole (_("os.remove(\"game/script.rpy\")"), _("script.rpy deleted successfully.")) from _call_updateconsole_5
    $ pause(104.72 - (datetime.datetime.now() - starttime).total_seconds())
    
    # Hides console and shows the Team Salvato Logo/Thank You
    call hideconsole from _call_hideconsole_1
    show credits_ts
    show credits_text _("带着爱创作"):
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
        $ endscreentext = _("游戏结束...？\n「在夜空里所有星星熄灭的时候，所有溪流、所有的梦想，都能汇入同一片大海之中。那时我们终会再见的。」")
        # 原神 https://genshin.honeyhunterworld.com/db/q/q_41422/?lang=CHS
        show endscreen "[endscreentext]"
        with dissolve
        $ pause()
        
        # Fakes Error Corruption. Makes the player quit the game.
        call screen dialog(message=_("游戏结束，请重启游戏并删除存档，否则可能发生意料之外的错误。"), ok_action=Quit(confirm=False))
        return
