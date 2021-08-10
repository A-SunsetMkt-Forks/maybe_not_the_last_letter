# Chapter 3

label ch3:
    $ unforgettableflag = False
    $ aboutteachersflag = False
    show sunset clap0
    stop music fadeout 3.0
    s "还有什么问题？请尽管问吧，[player]。"
    # 这个奇怪的播放方式可以让音乐第一次播放时从较平静的位置开始，第二次播放起开始循环
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
    $ unforgettablerandnum = random.randint(1,6)
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
    s "不幸的是，开发时我并没有想到我有一天会回来翻历史记录..."
    show sunset explain7
    s "所以我的每个commit都完全没写有用的备注..."
    s "当时翻历史+写报告用了几个小时吧..."
    s "最后交上去的时候还是没抱希望的。"
    if aboutarflag:
        s "当然，后面的事情你已经知道了。"
        jump other1
    else:
        s "直到疫情期间被通知通过市级竞赛，要提交省级竞赛..."
        s "也是在那时，我才注意到全校似乎只有两个参赛项目..."
        s "然后就出人意料地拿了个奖..."
        s "很有可能只是个鼓励性的奖项。"
        jump other1

label unforgettable3:
    show sunset explain6
    s "最难忘的事..."
    $ gtext = glitchtext(6)
    show sunset think0
    s "是和[gtext]经历的每一件事。"
    $ zeggcount = zeggcount + 1
    s "每一次相遇..."
    s "每一次对视..."
    s "和每一次冲突..."
    s "躲避..."
    s "尴尬..."
    s "和分别..."
    s "以及最后也没能原谅的..."
    s "结局。"
    jump other1

label unforgettable4:
    show sunset explain6
    s "最难忘的事..."
    s "是成绩第一次进入校前百名。"
    show sunset look1
    s "在旅途中知道了自己的排名..."
    show sunset explain5
    s "但并没有多激动..."
    s "就很平静地过去了。"
    s "遗憾的是..."
    show sunset upset2
    s "这也是我三年以来的最高成绩..."
    s "然后就再也没有比这还好的了。"
    s "在最后一场考试中..."
    s "因为很多原因吧..."
    show sunset upset5
    $ gtext = glitchtext(6)
    s "也没能超过[gtext]..."
    $ zeggcount = zeggcount + 1
    show sunset upset0
    s "所以还是有点怨念的。"
    jump other1

label unforgettable5:
    show sunset explain6
    s "最难忘的事..."
    show sunset look4
    s "说出来恐怕会泄露出不应该公开的东西吧..."
    s "例如了解到考试作弊问题..." # 这里需要补充
    show sunset explain5
    s "还是少说为妙。"
    jump other1

label unforgettable6:
    show sunset explain6
    s "最难忘的事..."
    s "是作了个大死..."
    show sunset explain5
    s "关于ProjectZ的相关信息..."
    s "请还是去问EXPLORER吧。"
    $ expeggcount = expeggcount + 1
    jump other1

label aboutteachers:
    if aboutteachersflag:
        s "[player]，我们已经谈过这个话题了。"
        jump other1
    $ aboutteachersflag = True
    show sunset explain6
    s "这里应该有一些很有趣的回忆，"
    show sunset explain5
    s "但...我的记忆力不太好..."
    s "简单地说..."
    s "是一群很可爱的人吧。"
    s "如果说比较重要的是..."
    show sunset clap0
    s "非常幸运有一个管理并不太严格的班主任..."
    s "这事实上减少了很多回影响学生学习的因素..."
    show sunset clap1
    s "这种管理方式..."
    s "也是一种智慧吧。"
    jump other1

label other1:
    # show sunset smile0
    menu:
        "在学校里经历过什么难忘的事吗？":
            jump unforgettablehub
        "说一说你的老师们吧。":
            jump aboutteachers
        "会跳到ch4的问题，还没写":
            jump ch4