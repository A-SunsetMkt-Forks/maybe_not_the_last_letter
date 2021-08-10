label ending:
    if expeggcount >= 2:
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
    n "生日快乐，[gtext]。"
    jump endingshow