label ch0:
    scene bg basic
    n "你好，[player]！"
    n "这是一个...互动小说游戏。"
    n "与其说是互动小说..."
    n "还不如说是作者的毕业总结。"
    menu:
        "那...作者是谁？":
            jump author
        "毕业总结？":
            jump graduate

label author:
    n "请允许我介绍本项目的作者..."
    show sunset smile0
    n "余晖！"
    show sunset explain7
    s "也许你认为这个形象过于诡异？"
    s "“余晖”这个假名来自《My Little Pony》及其衍生剧集，她的形象也来源于此。"
    s "也就是你现在看到我的样子。"
    show sunset explain5
    s "选择这个形象的另一个原因是..."
    s "作者不想画立绘。"
    show sunset explain1
    s "注意：版权声明！"
    s "“余晖烁烁”及其艺术作品版权属Hasbro, Inc。"
    s "My Little Pony®是Hasbro, Inc的注册商标。此项目与Hasbro, Inc无关。"
    jump reason

label graduate:
    n "是的。"
    n "如果您并不了解，那么此游戏可能并不适合你。"
    n "请退出并删除此游戏。"
    menu:
        "退出。":
            $ renpy.quit()
            return
        "我知道了...":
            pass
    n "那么..."
    jump author

label reason:
    jump credits
    return