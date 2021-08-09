# Chapter 3

label ch3:
    $ unforgettableflag = False
    $ aboutteachersflag = False
    show sunset clap0
    stop music fadeout 3.0
    s "还有什么问题？请尽管问吧，[player]。"
    play music "<from 13.0>audio/game2.ogg" fadein 20.0
    queue music "<loop 0.0>audio/game2.ogg"
    menu:
        "在学校里经历过什么难忘的事吗？":
            jump unforgettablehub
        "说一说你的老师们吧。":
            jump aboutteachers

label unforgettablehub:
    if unforgettableflag:
        s "[player]，我们不是已经谈过这个话题了么？"
        jump other1
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
    s "最难忘的事..."
    s "是项目AutoRing.py每天都能如预期工作..."
    s "准确地在上课、下课、放学时..."
    s "按需求响铃。"
    s "作为第一个投入生产环境的项目，"
    s "它给了我很大的信心..."
    show sunset explain5
    s "让我相信，即使再乱的逻辑、再差的水平写出来的代码也是能正常工作的。"
    s "从最初用来练手的脚本..."
    s "到重构后的，可用于生产的项目..."
    s "我了解了很多..."
    s "日志、函数化封装、错误处理、基于JSON的数据交流、和第三方可执行文件的配合..."
    s "创造出了一个至少能用的AutoRing.py。"
    show sunset clap1
    s "在最后的两个星期，"
    s "它在我不在场维护的情况下仍在运行..."
    s "正常播放午睡叫醒铃..."
    show sunset explain7
    s "想想还是很滑稽的。"
    jump other1

label unforgettable2:
    show sunset explain6
    s "最难忘的事..."
    s "是“随机姓名选择器”作为参赛作品获奖了..."
    show sunset explain7
    s "说起来是个有趣的故事..."
    s "收到比赛通知后就想到自己手上有好几个垃圾项目可以参赛..."
    show sunset look2
    s "记得当时还想建议几个同学也写点程序交上去..."
    s "当天根据Git提交纪录写了研究报告..."
    s "大概写了开发过程吧..."
    s "更不幸的是，开发时我并没有想到我有一天会回来翻历史记录..."
    show sunset explain7
    s "所以我的每个commit都完全没写有用的备注..."
    s "当时翻历史+写报告用了几个小时吧..."
    s "最后交上去的时候还是没抱希望的。"
    s ""

label unforgettable3:
    show sunset explain6
    s "最难忘的事..."

label unforgettable4:
    show sunset explain6
    s "最难忘的事..."

label unforgettable5:
    show sunset explain6
    s "最难忘的事..."

label aboutteachers:
    if aboutteachersflag:
        s "[player]，我们已经谈过这个话题了。"
        jump other1
    $ aboutteachersflag = True
    show sunset explain6

label other1:
    show sunset smile0
    menu:
        "在学校里经历过什么难忘的事吗？":
            jump unforgettablehub
        "说一说你的老师们吧。":
            jump aboutteachers
        "会跳到ch4的问题，还没写":
            jump ch4