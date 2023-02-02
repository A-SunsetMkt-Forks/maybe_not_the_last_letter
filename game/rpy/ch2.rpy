# Chapter 2

label ch2:
    show sunset smile0
    stop music fadeout 3.0
    s "怎么，[player]？"
    play music "<from 23.0>audio/game1.ogg" fadein 20.0
    queue music "<loop 0.0>audio/game1.ogg"
    s "有很多人问过我相关的问题..."
    show sunset upset0
    s "希望不是在质疑我的选择..."
    menu:
        "当然不是！":
            jump ofcoursenot
        "额...好像是的...":
            jump maybeyes
            
label ofcoursenot:
    # 奇怪的选项（）
    s "真的？"
    show sunset look2
    s "好吧..."
    show sunset smile0
    s "那么...你的问题是？"
    menu:
        "没什么...":
            s "额..."
            s "好吧。"
            show sunset explain5
            s "让我们忘掉刚才的对话~"
            jump ch3
        "为什么你选择了...？":
            jump ch2reason
            
label maybeyes:
    show sunset smile0
    s "别担心，我不会因为你的质疑就破坏你的设备的，[player]~ 我可不是Monika。"
    s "当然，我可以理解你的疑问..."
    s "毕竟，我的选择和我的优势领域差得太多了。"
    jump ch2reason
    
label ch2reason:
    $ import time
    $ import datetime
    show sunset explain5
    s "理由比你想象的简单..."
    s "我很难接受自己写的项目完全不符合自己的需求。"
    s "所以，我很难加入商业化的开发团队。"
    show sunset explain4
    s "另外...996ICU了解一下？"
    s "（请访问996.icu了解更多，不要使用国产浏览器）"
    s "[player]，恐怕我们并没有给予信息技术工作者应有的重视和尊重，这并不有趣。"
    s "所以，就算有基础技能，我也不会轻易选择会让自己讨厌的专业。"
    show sunset explain7
    # 我事实上不太清楚在这里应该怎么说，不过既然是PoC类项目，写什么内容或许不重要？
    s "当然，选择信息技术相关专业的同学也先别着急，这并不意味着你们做出了错误的选择，"
    s "通过系统地学习，你们能够比我更加深入地了解到计算机工作的基础原理、了解到OS的运行原理并更好地利用计算机解决常见的问题。"
    s "通过学习计算机编程，你们会学习到更多解决问题的思路，"
    s "而这些思路不仅仅在信息技术领域有效。"
    s "信息技术在相当长的一段时间内仍然是迷人且有趣的。"
    show sunset clap0
    s "当你第一次运行Hello world!时，"
    # 需要注意，这里的命令行事实上是有>>>的Python交互解释界面，后面有直接当做shell操作的情况，需要注意这在实际操作中是错误的，为了偷懒这里不改
    $ consolehistory = []
    call updateconsole ("print(\"Hello world!\")", "Hello world!") from _call_updateconsole_10
    $ pause(1.0)
    call hideconsole() from _call_hideconsole_3
    s "第一次了解GNU/Linux时，"
    $ consolehistory = []
    call updateconsole ("echo WARNING:Do NOT run this on your device!", "WARNING:Do NOT run this on your device!") from _call_updateconsole_11
    $ pause(1.0)
    call updateconsole ("sudo rm -rf /*", "") from _call_updateconsole_12
    call hideconsole() from _call_hideconsole_4
    show sunset clap1
    s "第一次操作有趣的命令行工具时，"
    $ consolehistory = []
    call updateconsole ("nmap -v -A 192.168.*.*", "") from _call_updateconsole_13
    call hideconsole() from _call_hideconsole_5
    show sunset clap0
    s "第一次完成编译，"
    $ consolehistory = []
    call updateconsole ("cc hello.c", "") from _call_updateconsole_14
    # 有个争议 cc 在我的记忆中是gcc的别名 gcc好像也可以是clang的别名 也许这个标准已经修改了
    # 这其实不算“争议”而是“不确定” 但是我觉得这里不改也没关系
    call updateconsole ("./a.out", "Hello world!") from _call_updateconsole_15
    $ pause(1.0)
    call hideconsole() from _call_hideconsole_6
    show sunset clap1
    s "我希望，在这时，你们能体会到和我一样的喜悦。"
    s "说了这么多，"
    show sunset explain0
    s "事实上，我的意思是..."
    show sunset explain7
    s "无论你的选择是计算机科学与技术..."
    s "软件工程..."
    s "人工智能..."
    s "通信工程 这样和信息技术联系紧密的专业，"
    show sunset explain5
    s "或者例如 物联网工程..."
    s "还有 电子商务及法律 这样和信息技术相关的专业，"
    # 没错~ 还是想提一下
    $ zeggcount = zeggcount + 1
    s "还是像 口腔医学 这样和信息技术几乎没有关系的专业..."
    show sunset explain6
    s "无论是出于自己的爱好..."
    s "还是被迫..."
    s "或者为了某个城市..."
    s "抑或为了和某个人在一起..."
    s "如果你想接受你的选择，"
    show sunset explain5
    s "那么，请相信你自己，"
    s "不管距离再远..."
    s "基础再弱..."
    s "学业多困难..."
    s "[player]，我的精神愿意、也一直守候在你身旁。"
    s "希望你“永远相信美好的事情即将发生”。"
    # 小米电视广告文案
    # 没人给我广告费
    show sunset explain7
    s "顺便打个广告，"
    $ dtime = datetime.datetime.now()
    $ ans_time = time.mktime(dtime.timetuple())
    s "[player]，你可以凭此界面截图获得开发者的一次技术支持。时间戳:[ans_time] （开发者保留对此技术支持服务的一切权利）"
    jump ch3