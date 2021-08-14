# Chapter 5

label ch5:
    show sunset explain5
    $ ch5bugflag = False
    $ ch5opensourceflag = False
    $ ch5contactflag = False
    s "别那么着急嘛~"
    s "游戏的最后会有制作人员表的..."
    s "接下来是快速问答时间！"
    jump ch5menu

label ch5menu:
    menu:
        "我找到了一个bug！我该去哪里提交它？":
            jump ch5bug
        "这是个开源游戏吗？":
            jump ch5opensource
        "我该如何与本游戏的开发人员和对话设计者取得联系？":
            jump ch5contact
        "（跳过）":
            jump ch6

label ch5bug:
    if ch5bugflag:
        s "我们已经聊过这个问题了。"
        jump ch5menu
    $ ch5bugflag = True
    s "...有趣。"
    s "在正式发行之后，所有的非恶性bug均视为特性。"
    show sunset explain1
    s "我开玩笑的..."
    s "你可以在此项目的GitHub仓库下发issue。"
    jump ch5menu

label ch5opensource:
    if ch5opensourceflag:
        s "我们已经聊过这个问题了。"
        jump ch5menu
    $ ch5opensourceflag = True
    show sunset smile0
    s "是的。"
    s "此项目的GitHub仓库："
    s "https://github.com/lwd-temp/maybe_not_the_last_letter"
    jump ch5menu

label ch5contact:
    if ch5contactflag:
        s "我们已经聊过这个问题了。"
        jump ch5menu
    $ ch5contactflag = True
    s "此游戏的程序部分由lwd-temp完成..."
    s "对话作者为余晖..."
    s "和另一位还没出现的角色。"
    s "你可以直接在此项目的GitHub仓库下发issue..."
    s "我们会直接与你取得联系。"
    menu:
        "还没出现的角色？":
            jump ch5exp
        "了解了。":
            jump ch5menu

label ch5exp:
    show sunset explain5
    s "虽然听起来有点牵强..."
    s "但在他出现之前..."
    s "这个名字是保密的。"
    menu:
        "无聊...":
            jump ch5menu
        "所以...我还可以见到他？":
            jump ch5expmeet
        "有趣的解释。":
            jump ch5menu
        "确实有点...":
            jump ch5menu

label ch5expmeet:
    s "也许吧..."
    show sunset explain7
    s "也许能看到和他的对话也说不定呢..."
    $ expeggcount = expeggcount + 1
    jump ch5menu