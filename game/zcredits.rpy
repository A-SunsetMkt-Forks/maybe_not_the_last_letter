label zcredits2:
    image zcreditend:
        truecenter
        "gui/end.png"
    scene black
    $ consolehistory = []
    play music "audio/eggend.ogg" noloop
    $ starttime = datetime.datetime.now()
    pause 0.88
    
    # Actual names for Credits, where you plug in stuff
    show credits_header "也许不是最后一封信" as credits_header_1 at credits_text_scroll_middle
    show credits_text "ProjectZ Studio出品" as credits_text_1 at credits_text_scroll_middle
    
    $ pause(16.95 - (datetime.datetime.now() - starttime).total_seconds())
    
    show credits_header "理念和游戏设计" as credits_header_2 at credits_text_scroll_middle
    show credits_text "余晖" as credits_text_2 at credits_text_scroll_middle

    $ pause(26.05 - (datetime.datetime.now() - starttime).total_seconds())
    
    show credits_header "故事" as credits_header_1 at credits_text_scroll_middle
    show credits_text "余晖" as credits_text_1 at credits_text_scroll_middle
    
    $ pause(35.15 - (datetime.datetime.now() - starttime).total_seconds())
    
    show credits_header "主要程序员" as credits_header_2 at credits_text_scroll_middle
    show credits_text "lwd-temp" as credits_text_2 at credits_text_scroll_middle
    
    $ pause(44.25 - (datetime.datetime.now() - starttime).total_seconds())
    
    show credits_header "" as credits_header_1 at credits_text_scroll_middle
    show credits_text "音乐\nEasy Breeze (StarSight Remix)  Player_275x / Thomas Greenberg\n穏やかに過ぎゆく時  小林俊太郎\n电影《你的名字》主题曲《前前前世》  Bilibili用户@Ayasa绚沙\n更多信息请查看项目存储库" as credits_text_1 at credits_text_scroll_middle

    $ pause(53.35 - (datetime.datetime.now() - starttime).total_seconds())
    
    show credits_header "策划" as credits_header_2 at credits_text_scroll_middle
    show credits_text "余晖" as credits_text_2 at credits_text_scroll_middle
    
    $ pause(62.45 - (datetime.datetime.now() - starttime).total_seconds())
    
    show credits_header "特别感谢" as credits_header_1 at credits_text_scroll_middle
    show credits_text "Starlight Glimmer\nTwilight Sparkle" as credits_text_1 at credits_text_scroll_middle
    
    $ pause(71.55 - (datetime.datetime.now() - starttime).total_seconds())
    
    show credits_header "特别感谢" as credits_header_2 at credits_text_scroll_middle
    show credits_text "Princess Celestian\nPrincess Luna" as credits_text_2 at credits_text_scroll_middle
    
    # $ pause(80.60 - (datetime.datetime.now() - starttime).total_seconds())

    $ pause(80.60 - (datetime.datetime.now() - starttime).total_seconds())
    
    show credits_header "特别感谢" as credits_header_1 at credits_text_scroll_middle
    show credits_text "Applejack\nPinkie Pie" as credits_text_1 at credits_text_scroll_middle

    $ pause(88.00 - (datetime.datetime.now() - starttime).total_seconds())
    play sound "audio/egg.ogg"
    show noise zorder 9:
        alpha 0.0
        linear 1.5 alpha 1.0
        time 2.0
        parallel:
            0.05
            choice:
                alpha 0.5
            choice:
                alpha 0.75
            choice:
                alpha 1.0
            repeat
        parallel:
            linear 0.375 alpha 0.7
            linear 0.375 alpha 1.0
        time 2.75
        alpha 0.95
        time 6.45
        alpha 0.3
        time 6.95
        alpha 0.9
        time 8.65
        linear 0.8 alpha 0
        alpha 0.5
        time 22.1
        alpha 0.85
        time 22.35
        alpha 0.5
        time 28.20
        alpha 0.3
        linear 0.45 alpha 0.9
        alpha 0.4
    show vignette zorder 10:
        alpha 0.75
        parallel:
            0.36
            alpha 0.75
            repeat
        parallel:
            0.49
            alpha 0.7
            repeat
    show black as bar zorder 9:
        alpha 0.3
        size (1280,500)
        block:
            ypos 720
            linear 15 ypos -500
            repeat
    $ gtext = glitchtext(6)
    $ gstr = glitchtext(15)
    $ gchar = glitchtext(4)
    show credits_header "" as credits_header_2 at credits_text_scroll_middle
    show credits_text "特别感谢\nMonika\n[player]\n[gtext]（[gstr]：5[gchar]45[gchar]18[gchar]2[gchar]98[gchar]8[gchar]2[gchar]）[gchar]" as credits_text_2 at credits_text_scroll_middle
    
    $ pause(95.10 - (datetime.datetime.now() - starttime).total_seconds())

    call updateconsole ("os.remove(\"game/screens.rpy\")", "screens.rpy deleted successfully.") from _call_updateconsole_6
    call updateconsole ("os.remove(\"game/gui.rpy\")", "gui.rpy deleted successfully.") from _call_updateconsole_7
    call updateconsole ("os.remove(\"game/menu.rpy\")", "menu.rpy deleted successfully.") from _call_updateconsole_8
    call updateconsole ("os.remove(\"game/script.rpy\")", "script.rpy deleted successfully.") from _call_updateconsole_9
    $ pause(104.72 - (datetime.datetime.now() - starttime).total_seconds())
    
    # Hides console and shows the Team Salvato Logo/Thank You
    call hideconsole from _call_hideconsole_2
    show credits_ts
    show credits_text "带着爱创作":
        zoom 0.75 xalign 0.5 yalign 0.25 alpha 0 subpixel True
        linear 2.0 alpha 1
        4.5
        linear 2.0 alpha 0
    pause 9.3

    # Fade to black and make the player quit
    label zpostcredits_loop:
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
        show zcreditend
        $ pause()
        
        # Fakes Error Corruption. Makes the player quit the game.
        call screen dialog(message="Error: Script file is missing or corrupt.\nPlease reinstall the game.", ok_action=Quit(confirm=False))
        return
