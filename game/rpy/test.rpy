label test0:
    scene bg basic
    s "你好？"
    show sunset explain0
    s "Hello,world!"
    hide sunset
    jump testmenu
label testmenu:
    menu:
        "回到start":
            jump start
        "config.developer设为True":
            $ config.developer = True
            n "尝试设置完成"
            n "使用分发版的用户并不能通过此选项尝试开启开发者模式"
            n "使用Shift+D开启开发者菜单时会报错"
            jump testmenu
        "zeggcount自加1":
            $ zeggcount = zeggcount + 1
            jump testmenu
        "raise Exception":
            $ raise Exception
            jump testmenu
        "交互演示":
            jump testdemo
    jump start
label testdemo:
    scene bg sunset stare
    with dissolve
    s "233"
    $ consolehistory = []
    call updateconsole ("os.remove(\"characters/yuri.chr\")", "yuri.chr deleted successfully.") from _call_updateconsole
    $ pause(1.0)
    call updateconsole ("os.remove(\"characters/natsuki.chr\")", "natsuki.chr deleted successfully.") from _call_updateconsole_1
    $ pause(1.0)
    call hideconsole() from _call_hideconsole
    scene bg basic
    show sunset explain
    s "123"
    jump ending
    return