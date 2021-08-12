label test0:
    scene bg basic
    $ testdemodev = True
    s "你好，[player]？"
    show sunset explain7
    s "Hello,world!"
    hide sunset
    jump testmenu
label testmenu:
    menu:
        "回到start":
            jump start
        "zeggcount自加1":
            $ zeggcount = zeggcount + 1
            jump testmenu
        "expeggcount自加1":
            $ expeggcount = expeggcount + 1
            jump testmenu
        "raise Exception":
            $ raise Exception
            jump testmenu
        "交互演示":
            jump testdemo
    jump start
label testdemo:
    #scene bg sunset stare
    #with dissolve
    show sunset look0
    s "你怎么会在这？"
    if config.developer and testdemodev:
        show sunset explain5
        s "哦，是开发者啊。"
        show sunset look3
        s "抱歉看错人了。"
        s "下面就是结局了。"
    else:
        show sunset upset0
        s "这不是你该来的地方！"
        show sunset explain2
        s "如果你在发行版中看到了这个，那一定是开发者忘了删掉某些东西了。"
        show sunset smile0
        s "为了避免剧透，请退出此存档。"
        show sunset upset3 at left
        show monika basic at right
        m "没错，快听她的~"
        s "你这已经剧透了好吧......"
        m "哦...抱歉啦。"
        s "（为什么她比我高那么多...）"
        m "（还不是因为开发者懒得修改图像大小又不会用Ren'Py的动画效果功能缩放图片...）"
        show sunset upset2 at left
        s "剧透倒计时：----------"
        s "=---------"
        s "==--------"
        s "===-------"
        s "====------"
        s "=====-----"
        s "======----"
        s "=======---"
        s "========--"
        s "=========-"
        s "=========="
        s "好吧..."
        hide sunset
        hide monika
    #$ consolehistory = []
    #call updateconsole ("os.remove(\"characters/yuri.chr\")", "yuri.chr deleted successfully.") from _call_updateconsole
    #$ pause(1.0)
    #call updateconsole ("os.remove(\"characters/natsuki.chr\")", "natsuki.chr deleted successfully.") from _call_updateconsole_1
    #$ pause(1.0)
    #call hideconsole() from _call_hideconsole
    #scene bg basic
    jump ending
    return