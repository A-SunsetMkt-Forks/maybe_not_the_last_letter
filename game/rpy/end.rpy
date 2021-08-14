label ending:
    $ expsongname = ""
    if expeggcount >= 2:
        stop music fadeout 3.0
        s "在游戏结束之前，EXPLORER也有些话要说..."
        jump chexp
    jump realending

label realending:
    show sunset bye
    stop music fadeout 5.0
    s "到目前为止，您已经完成了大部分的游戏流程。"
    s "游戏到这里就要结束了。"
    s "感谢游玩..."
    s "我们下封信再见。"
    hide sunset
    $ import datetime
    if datetime.datetime.now().month == 5 and datetime.datetime.now().day == 5:
        jump endinghappy
    else:
        jump endingshow


label endingshow:
    show end
    $ pause(1.0)
    show black
    with dissolve
    jump credits

label endinghappy:
    $ gtext = glitchtext(6)
    n "等一下..."
    n "还有一件事..."
    if zeggcount >= 5:
        n "生日快乐，[gtext]。"
        $ zeggcount = zeggcount + 1
    else:
        n "这是个小概率bug..."
        n "在某些特殊情况下，对话会跳转到这里。"
        n "既然都看到这了..."
        n "你还真的是很幸运..."
        n "奖励自己吃顿火锅吧..."
        n "或者做点别的什么也可以啊。"
    jump endingshow