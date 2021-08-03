label zcredits2:
    scene black
    $ consolehistory = []
    play music "audio/eggend.ogg" noloop
    queue music "audio/egg.ogg" noloop
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
    show credits_text "音乐\nEasy Breeze (StarSight Remix) Player_275x / Thomas Greenberg\n穏やかに過ぎゆく時 小林俊太郎\n电影《你的名字》主题曲《前前前世》 Bilibili用户@Ayasa绚沙（UID:321056219）\n更多信息请查看项目存储库" as credits_text_1 at credits_text_scroll_middle

    $ pause(53.35 - (datetime.datetime.now() - starttime).total_seconds())
    
    show credits_header "策划" as credits_header_2 at credits_text_scroll_middle
    show credits_text "余晖" as credits_text_2 at credits_text_scroll_middle
    
    $ pause(62.45 - (datetime.datetime.now() - starttime).total_seconds())
    
    show credits_header "特别感谢" as credits_header_1 at credits_text_scroll_middle
    show credits_text "Masha Gutin\nKagefumi" as credits_text_1 at credits_text_scroll_middle
    
    $ pause(71.55 - (datetime.datetime.now() - starttime).total_seconds())
    
    show credits_header "特别感谢" as credits_header_2 at credits_text_scroll_middle
    show credits_text "David Evelyn\nCorey Shin" as credits_text_2 at credits_text_scroll_middle
    
    # $ pause(80.60 - (datetime.datetime.now() - starttime).total_seconds())

    $ pause(80.60 - (datetime.datetime.now() - starttime).total_seconds())
    
    show credits_header "特别感谢" as credits_header_1 at credits_text_scroll_middle
    show credits_text "Alecia Bardachino\nMatt Naples" as credits_text_1 at credits_text_scroll_middle
    
    $ pause(88.00 - (datetime.datetime.now() - starttime).total_seconds())
    
    show credits_header "特别感谢" as credits_header_2 at credits_text_scroll_middle
    show credits_text "Monika\n[player]" as credits_text_2 at credits_text_scroll_middle
    
    $ pause(95.10 - (datetime.datetime.now() - starttime).total_seconds())

    call updateconsole ("os.remove(\"game/screens.rpy\")", "screens.rpy deleted successfully.") from _call_updateconsole_6
    call updateconsole ("os.remove(\"game/gui.rpy\")", "gui.rpy deleted successfully.") from _call_updateconsole_7
    call updateconsole ("os.remove(\"game/menu.rpy\")", "menu.rpy deleted successfully.") from _call_updateconsole_8
    call updateconsole ("os.remove(\"game/script.rpy\")", "script.rpy deleted successfully.") from _call_updateconsole_9
    $ pause(104.72 - (datetime.datetime.now() - starttime).total_seconds())
    
    # Hides console and shows the Team Salvato Logo/Thank You
    call hideconsole from _call_hideconsole_2
    show credits_ts
    show credits_text "made with love by":
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
        $ pause()
        
        # Fakes Error Corruption. Makes the player quit the game.
        call screen dialog(message="Error: Script file is missing or corrupt.\nPlease reinstall the game.", ok_action=Quit(confirm=False))
        return
