label ending:
    show sunset bye
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
    stop music fadeout 1.0
    show end
    $ pause(1.0)
    show black
    with dissolve
    jump credits

label endinghappy:
    $ gtext = glitchtext(6)
    n "生日快乐，[gtext]。"
    jump endingshow