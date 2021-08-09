# Chapter 3

label ch3:
    $ unforgettableflag = False
    $ aboutteachersflag = False
    show sunset clap0
    s "还有什么问题？请尽管问吧。"
    menu:
        "在学校里经历过什么难忘的事吗？":
            jump unforgettablehub
        "说一说你的老师们吧。":
            jump aboutteachers

label unforgettablehub:
    $ unforgettableflag = True
    $ import random
    show sunset look1
    s "让我回忆一下..."
    $ pause(1.0 + random.randint(0,2))
    # 随机一个已经准备好的对话编号，注意randint是闭区间
    $ unforgettablerandnum = random.randint(1,5)
    $ unforgettablelabel = "unforgettable" + str(unforgettablerandnum)
    $ renpy.jump(unforgettablelabel)

label unforgettable1:
    show sunset explain6

label unforgettable2:
    show sunset explain6

label unforgettable3:
    show sunset explain6

label unforgettable4:
    show sunset explain6

label unforgettable5:
    show sunset explain6

label aboutteachers:
    $ aboutteachersflag = True
    show sunset explain6