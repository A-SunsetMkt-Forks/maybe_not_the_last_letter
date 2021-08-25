label zcredits2:
    $ persistent.autoload = "zcredits2"
    # Disables Main Menu, Quick Menu, Everything
    $ config.keymap['game_menu'] = []
    $ config.keymap['hide_windows'] = []
    $ renpy.display.behavior.clear_keymap_cache()
    $ quick_menu = False
    $ config.skipping = False
    $ config.allow_skipping = False
    image zcreditend:
        truecenter
        "gui/end.png"
    scene black
    $ consolehistory = []
    $ import random
    $ zsongname = _("错误：请联系开发者。")
    if random.randint(0,4) != 0:
        if random.randint(0,1) == 0:
            play music "audio/eggend0.ogg" noloop
            $ zsongname = _("【钢琴】《勾指起誓》 洛天依-ilem 高甜预警 纯钢琴版  Bilibili用户@绯绯Feifei")
        else:
            play music "audio/eggend1.ogg" noloop
            $ zsongname = _("勾指起誓 钢琴演奏版  昼夜")
        # 一首甜一些的歌
    else:
        play music "audio/eggend.ogg" noloop
        $ zsongname = _("电影《你的名字》主题曲《前前前世》  Bilibili用户@Ayasa绚沙")
        # 概率低一点 太吵了
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
    show credits_text _("音乐\nEasy Breeze (StarSight Remix)  Player_275x / Thomas Greenberg\n穏やかに過ぎゆく時  小林俊太郎\n【Animenz】secret base 〜你给我的所有〜 - 未闻花名 ED 钢琴版  Bilibili用户@Animenzzz\nLeaves in the Wind  Isaac Shepard\nMidday Prospects 午日的眺望 陈致逸 / HOYO-MiX[persistent.expsongname]\n[zsongname]\n【神里绫华】过场动画“夜场跳舞” 纯音乐  米哈游") as credits_text_1 at credits_text_scroll_middle

    $ pause(53.35 - (datetime.datetime.now() - starttime).total_seconds())
    
    show credits_header _("策划") as credits_header_2 at credits_text_scroll_middle
    show credits_text _("余晖") as credits_text_2 at credits_text_scroll_middle
    
    $ pause(62.45 - (datetime.datetime.now() - starttime).total_seconds())
    
    show credits_header _("") as credits_header_1 at credits_text_scroll_middle
    show credits_text _("早期测试人员\n840a8dbdddece6a56fb9b1f925eac7a75cb274b85e7eddafdfb97573170e5a8b\nEXPLORER\n83235ec96fa3b9c0631863c5e3f998aef8e89c28698a8fc2843509627cb0d295") as credits_text_1 at credits_text_scroll_middle
    
    $ pause(71.55 - (datetime.datetime.now() - starttime).total_seconds())
    
    show credits_header _("") as credits_header_2 at credits_text_scroll_middle
    show credits_text _("特别感谢\nRen'Py\nTeam Salvato\nHasbro, Inc\nSCP Foundation\nUniverse of My Own\n米哈游\n创造音乐和立绘的艺术家们") as credits_text_2 at credits_text_scroll_middle
    
    # $ pause(80.60 - (datetime.datetime.now() - starttime).total_seconds())

    $ pause(80.60 - (datetime.datetime.now() - starttime).total_seconds())
    
    show credits_header _("") as credits_header_1 at credits_text_scroll_middle
    show credits_text _("此项目的部分代码来自DDLCModTemplate2.0，原则上禁止用于除《心跳文学部》第三方模组的其他用途\n除此之外的其他代码使用 GNU General Public License v3.0 发布\n此项目的部分故事和文案使用 Creative Commons Attribution Share Alike 4.0 International 协议授权\n更多信息请查看项目存储库") as credits_text_1 at credits_text_scroll_middle

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
    show credits_header _("") as credits_header_2 at credits_text_scroll_middle
    show credits_text _("特别感谢\nPrincess Celestia\nMonika\n[player]\n[gtext]（[gstr]：5[gchar]45[gchar]18[gchar]2[gchar]98[gchar]8[gchar]2[gchar]）[gchar]") as credits_text_2 at credits_text_scroll_middle
    
    $ pause(95.10 - (datetime.datetime.now() - starttime).total_seconds())

    hide monika
    call updateconsole (_("os.remove(\"game/screens.rpy\")"), _("Permission Denied.")) from _call_updateconsole_6
    call updateconsole (_("os.remove(\"game/gui.rpy\")"), _("Permission Denied.")) from _call_updateconsole_7
    call updateconsole (_("os.remove(\"game/menu.rpy\")"), _("Permission Denied.")) from _call_updateconsole_8
    call updateconsole (_("os.remove(\"game/script.rpy\")"), _("Permission Denied.")) from _call_updateconsole_9
    $ pause(104.72 - (datetime.datetime.now() - starttime).total_seconds())

    
    # Hides console and shows the Team Salvato Logo/Thank You
    call hideconsole from _call_hideconsole_2
    hide noise
    hide vignette
    show credits_ts
    show credits_text _("带着爱创作"):
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

        pause 30
        stop music fadeout 3.0
        pause 3
        play music "audio/tale.ogg" noloop
        pause 2

        # 作者信息：星际联盟第一宇宙物理研究所宇宙基础理论物理部门首席物理学家EXPLORER
        # 授权方式：CC BY-NC-SA 4.0
        # 余晖表示这个童话不太好理解，但是加上去总没错
        # 主要程序员表示这是在浪费程序员的生命
        # 策划表示如果程序员拒绝工作将被解雇
        # 程序员表示其正在工作
        show endscreen _("很久很久以前，珀普乐王国的公主望向漫天星辰。\n公主的面容似被精心雕刻过，比任何雕塑都精致完美。简单柔和的线条勾勒出王国里最美丽的身影。她拥有来自远近千千万万的追随者。\n她微微低下头，好像在思索什么的样子，轻语呼唤着自己的首相，“星星有什么用呢？”")
        with Dissolve(2.0)
        pause 8
        hide endscreen
        with Dissolve(2.0)
        pause 1

        show endscreen _("这个年代里会猎星星的几乎没有。猎星星的男孩在朦胧的夜里盗走星星的光芒，用天上的微光点亮派森国的夜。孤独着，他捕捉着光，一切都好似仅仅是乐趣，直到一天，他注意到了珀普乐王国的佳人。")
        with Dissolve(2.0)
        pause 6
        hide endscreen
        with Dissolve(2.0)
        pause 1

        show endscreen _("猎星者在公主身上看到了自己向往的样子。\n他尝试着与其交流。\n每一个夜幕降下后，星星点点的闪光如钻石般镶嵌在暗色里，等待着，呼唤着。长夜不再寂寞，猎星者为公主献上自己捕捉到的最优雅动人的星光。他把它们封在可爱的细口瓶里，与自己最真挚的心意一起。")
        with Dissolve(2.0)
        pause 8
        hide endscreen
        with Dissolve(2.0)
        pause 1

        show endscreen _("久而久之，公主厌烦了。\n她召来大臣皖，让他把那些来自数亿光年外的礼物一并处理。\n“说真的，星星到底有什么用呢？”")
        with Dissolve(2.0)
        pause 5
        hide endscreen
        with Dissolve(2.0)
        pause 1
        
        show endscreen _("据说，那一晚，珀普乐王国外的森林很亮。")
        with Dissolve(2.0)
        pause 3
        hide endscreen
        with Dissolve(2.0)
        pause 1

        show endscreen _("猎星者再一次送上青蓝的微光，这来自遥远的天狼星。纯洁的蓝光映衬出一切安宁美好，与深邃的天穹一同共振。\n她会喜欢的，她一定会。")
        with Dissolve(2.0)
        pause 6
        hide endscreen
        with Dissolve(2.0)
        pause 1

        show endscreen _("公主接过后打碎了瓶子。\n蓝色悬浮在空中，就像猎星者的心情。")
        with Dissolve(2.0)
        pause 3
        hide endscreen
        with Dissolve(2.0)
        pause 1

        show endscreen _("猎星者一次又一次地寄信，他渴望得到公主的原谅。\n公主的大臣仝为她拦下了这些信件，并抛进光之池中。\n猎星者对接触的尝试每一次都落了空。\n猎星星的男孩永远不能用天上的星星换来一个人的心。")
        with Dissolve(2.0)
        pause 6
        hide endscreen
        with Dissolve(2.0)
        pause 1

        show endscreen _("他口袋里藏着最后一颗星。\n他希望，但愿……")
        with Dissolve(2.0)
        pause 3
        hide endscreen
        with Dissolve(2.0)
        pause 1
        jump zegg_final

    label zegg_final:
        $ persistent.autoload = "zegg_final"
        $ config.keymap['game_menu'] = []
        $ config.keymap['hide_windows'] = []
        $ renpy.display.behavior.clear_keymap_cache()
        $ quick_menu = False
        $ config.skipping = False
        $ config.allow_skipping = False
        scene black
        $ endscreentext = _("游戏结束。\n「请...好好地看着我。」")
        # 原神 https://genshin.honeyhunterworld.com/db/q/q_485/?lang=CHS
        show endscreen "[endscreentext]"
        with dissolve
        $ pause()
        call screen dialog(message=_("游戏结束，请重启游戏并删除存档，否则可能发生意料之外的错误。"), ok_action=Quit(confirm=False))
        return