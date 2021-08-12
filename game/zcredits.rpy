label zcredits2:
    $ persistent.autoload = "zcredits2"
    image zcreditend:
        truecenter
        "gui/end.png"
    scene black
    $ consolehistory = []
    $ import random
    $ zsongname = "错误：请联系开发者。"
    if random.randint(0,1) == 0:
        play music "audio/eggend0.ogg" noloop
        $ zsongname = "【钢琴】《勾指起誓》 洛天依-ilem 高甜预警 纯钢琴版  Bilibili用户@绯绯Feifei"
        # 一首甜一些的歌
    else:
        play music "audio/eggend.ogg" noloop
        $ zsongname = "电影《你的名字》主题曲《前前前世》  Bilibili用户@Ayasa绚沙"
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
    show credits_text "余晖\nEXPLORER" as credits_text_1 at credits_text_scroll_middle
    
    $ pause(35.15 - (datetime.datetime.now() - starttime).total_seconds())
    
    show credits_header "主要程序员" as credits_header_2 at credits_text_scroll_middle
    show credits_text "lwd-temp" as credits_text_2 at credits_text_scroll_middle
    
    $ pause(44.25 - (datetime.datetime.now() - starttime).total_seconds())
    
    show credits_header "" as credits_header_1 at credits_text_scroll_middle
    show credits_text "音乐\nEasy Breeze (StarSight Remix)  Player_275x / Thomas Greenberg\n穏やかに過ぎゆく時  小林俊太郎\n【Animenz】secret base 〜你给我的所有〜 - 未闻花名 ED 钢琴版  Bilibili用户@Animenzzz\nLeaves in the Wind  Isaac Shepard[expsongname]\n[zsongname]" as credits_text_1 at credits_text_scroll_middle

    $ pause(53.35 - (datetime.datetime.now() - starttime).total_seconds())
    
    show credits_header "策划" as credits_header_2 at credits_text_scroll_middle
    show credits_text "余晖" as credits_text_2 at credits_text_scroll_middle
    
    $ pause(62.45 - (datetime.datetime.now() - starttime).total_seconds())
    
    show credits_header "" as credits_header_1 at credits_text_scroll_middle
    show credits_text "早期测试人员\n840a8dbdddece6a56fb9b1f925eac7a75cb274b85e7eddafdfb97573170e5a8b\nEXPLORER\n83235ec96fa3b9c0631863c5e3f998aef8e89c28698a8fc2843509627cb0d295" as credits_text_1 at credits_text_scroll_middle
    
    $ pause(71.55 - (datetime.datetime.now() - starttime).total_seconds())
    
    show credits_header "" as credits_header_2 at credits_text_scroll_middle
    show credits_text "特别感谢\nRen'Py\nTeam Salvato\nHasbro, Inc\n创造音乐和立绘的艺术家们\nEXPLORER" as credits_text_2 at credits_text_scroll_middle
    
    # $ pause(80.60 - (datetime.datetime.now() - starttime).total_seconds())

    $ pause(80.60 - (datetime.datetime.now() - starttime).total_seconds())
    
    show credits_header "" as credits_header_1 at credits_text_scroll_middle
    show credits_text "此项目的部分代码来自DDLCModTemplate2.0，原则上禁止用于除《心跳文学部》第三方模组的其他用途\n除此之外的其他代码使用 GNU General Public License v3.0 发布\n此项目的部分故事和文案使用 Creative Commons Attribution Share Alike 4.0 International 协议授权\n更多信息请查看项目存储库" as credits_text_1 at credits_text_scroll_middle

    $ pause(88.00 - (datetime.datetime.now() - starttime).total_seconds())
    if zeggcount >= 100:
        play sound "audio/egg.ogg"
        # 除非作弊否则不可能触发
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
    $ gtext = glitchtext(6)
    $ gstr = glitchtext(15)
    $ gchar = glitchtext(4)
    show monika basic
    show credits_header "" as credits_header_2 at credits_text_scroll_middle
    show credits_text "特别感谢\nPrincess Celestia\nMonika\n[player]\n[gtext]（[gstr]：5[gchar]45[gchar]18[gchar]2[gchar]98[gchar]8[gchar]2[gchar]）[gchar]" as credits_text_2 at credits_text_scroll_middle
    
    $ pause(95.10 - (datetime.datetime.now() - starttime).total_seconds())

    hide monika
    call updateconsole ("os.remove(\"game/screens.rpy\")", "screens.rpy deleted successfully.") from _call_updateconsole_6
    call updateconsole ("os.remove(\"game/gui.rpy\")", "gui.rpy deleted successfully.") from _call_updateconsole_7
    call updateconsole ("os.remove(\"game/menu.rpy\")", "menu.rpy deleted successfully.") from _call_updateconsole_8
    call updateconsole ("os.remove(\"game/script.rpy\")", "script.rpy deleted successfully.") from _call_updateconsole_9
    $ pause(104.72 - (datetime.datetime.now() - starttime).total_seconds())

    
    # Hides console and shows the Team Salvato Logo/Thank You
    call hideconsole from _call_hideconsole_2
    hide noise
    hide vignette
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
        $ persistent.autoload = "zpostcredits_loop"

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
        show endscreen ""
        with dissolve
        $ pause()
        
        # Fakes Error Corruption. Makes the player quit the game.
        call screen dialog(message="游戏结束，请重启游戏并删除存档，否则可能发生意料之外的错误。", ok_action=Quit(confirm=False))
        return
