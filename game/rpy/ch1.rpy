label ch1:
    menu:
        "你的简介上写着...你是计算机科学初学者？谈谈你的作品吧。":
            jump program0
        "你有想怀念的人吗？":
            jump inmemoryof

label program0:
    show sunset clap0
    s "我就等着你谈这个呢~"
    s "虽然只要打开我们的GitHub资料页就能了解这些..."
    s "我还是想亲自说给你听。"
    show sunset explain7
    s "从文档类项目开始："
    s "doc2019（2019年开源文档）承载了我的第一次水报告经历。"
    s "是给综合素质评价的报告没错了！"
    show sunset explain0
    s "有时我会想：我们的教育目的是...教会孩子们如何伪造报告、图片和经历..."
    s "...并且养成积攒似乎除了名目之外就没什么用的荣誉称号的习惯吗？"
    show sunset explain5
    s "annual-summary-2019（2019年度总结）（私有库）里面有我的一份超级无聊的年度总结。"
    s "比你现在交互的总结要无聊的多。"
    s "所以，还请珍惜你看到的互动小说游戏，它本可以更无聊。"
    show sunset explain2
    s "doc2020（私有库）里面有一份在那时属政治敏感类的文章..."
    s "“对‘形式主义’的批评并不影响我们对遇难者的悼念和正常的情感表达”"
    show sunset explain7
    s "DingTalkUtil 虽然叫Util(s)但只有如何给钉钉直播刷赞的教程。"
    s "简单地说就是利用中间人攻击修改播放页JavaScript达到重复请求刷赞。"
    s "我还想辟个谣，就算有点晚..."
    s "“刷赞”是不可能造成直播卡顿的，无论如何，直播视频推送和点赞数统计两个功能绝对不应该有关联。"
    show sunset explain4
    s "对于刷赞者的污名化我保持理解，但在做出推断前还请亲自证实。我们的世界并不充满了巴浦洛夫式的直观条件反射，很多技术问题是不能通过现象解决的。"
    show sunset explain7
    s "chemistry-pig-story（元素周期表小猪与狼的故事）是一个没人合作的合作项目..."
    s "基于《三只小猪与狼》，讲述了代表某种元素的小猪与狼对抗的故事。"
    s "只有一篇作品——氢小猪..."
    s "如果记得没错，是我在一节拖堂一小时的英语网课上写的。"
    s "about-lwd-temp讲述了一个对于你们来说是个科幻故事、对于我们就是事实的余晖教育和科技集团的基本介绍和职员信息。"
    s "成立于某下层叙事、与SCP Foundation合作，致力于在学园都市内部实行间谍活动并秘密部署大量斯克兰顿现实稳定锚，并以教育和信息技术开发作为前台组织的掩盖工作，余晖教育和科技集团在各个叙事层吸引了大量叙事实体加入，并允许甚至鼓励（相对）上层叙事实体使用此设定。"
    s "顺便提一下，SCP基金会系列也正在被误解..."
    s "文化...是个有趣的现象呢..."
    s "最后一个文档类项目是..."
    $ gtext = glitchtext(3)
    show sunset think0
    show noise zorder 9:
        alpha 0.0
        linear 1.5 alpha 1.0
        time 2.0
        parallel:
            0.05
            choice:
                alpha 0.5
            choice:
                alpha 0.75
            choice:
                alpha 1.0
            repeat
        parallel:
            linear 0.375 alpha 0.7
            linear 0.375 alpha 1.0
        time 2.75
        alpha 0.95
        time 6.45
        alpha 0.3
        time 6.95
        alpha 0.9
        time 8.65
        linear 0.8 alpha 0
        alpha 0.5
        time 22.1
        alpha 0.85
        time 22.35
        alpha 0.5
        time 28.20
        alpha 0.3
        linear 0.45 alpha 0.9
        alpha 0.4
    show vignette zorder 10:
        alpha 0.75
        parallel:
            0.36
            alpha 0.75
            repeat
        parallel:
            0.49
            alpha 0.7
            repeat
    s "in-memory-of-[gtext]..."
    $ gtext = glitchtext(11)
    s "本来是个用于回忆和[gtext]的经历的项目..."
    $ gtext = glitchtext(60)
    show sunset upset3
    s "[gtext]"
    $ zeggcount = zeggcount + 1
    hide noise
    hide vignette
    s "我是不是说得太多了？"
    menu:
        "才没有。":
            jump program1
        "也许...我们可以谈点其他的。":
            jump other0

label program1:
    show sunset smile0
    s "好吧。"
    s "除了文档类项目，实用（？）类项目也同样令人印象深刻！"
    s "unscrupulous-jimoky.cn包含一个用于攻击QQ钓鱼盗号网站的Python程序。"
    $ gtext = glitchtext(6)
    $ gtext2 = glitchtext(6)
    $ gtextl = glitchtext(11)
    show sunset explain6
    s "happy-birthday-[gtext]是一个用于嵌入各种Python程序员用于提供[gtextl]生日彩蛋的Python模块。"
    s "happy-birthday-[gtext]-win32是上述模块的独立版。通过调用Win32 API实现部分操作系统交互功能。同样是给[gtextl]的生日彩蛋！"
    s "[gtext]fy.py是用于将二进制文件转换成由[gtext]组成的文本的Python程序。"
    $ zeggcount = zeggcount + 1
    s "lwd-temp.github.io-jekyll是基于Jekyll的个人博客。"
    s "也是我实践HTML、JavaScript和CSS的地方。"
    s "接下来是我最有趣的两个作品："
    show sunset explain1
    s "rns.py——“随机姓名选择器（Random Name Selector）”是一个无聊的练手作品，"
    s "有趣的是，这个项目作为全校唯二的项目参赛..."
    s "...获得了汉东省青少年科技创新大赛三等奖。"
    $ zeggcount = zeggcount + 1
    s "（另一个项目是[gtext]和[gtext2]的合作项目，貌似是用于研磨深孔钻头的...）"
    show sunset explain2
    s "（根据已知信息，这两个参赛项目似乎都没什么用...）"
    show sunset explain5
    s "接下来的作品是在生产环境运行最久的——"
    s "AutoRing.py——自动化上下课放学铃播放和自动关机解决方案！"
    s "本来是疫情复课期间的无聊想法，在框架写好之后刚好派上用场，"
    show sunset clap0
    s "在版本迭代中增加了...许多有趣的功能..."
    s "例如：自助式放学铃自定义..."
    show sunset upset0
    s "虽然造成了很多麻烦、也在其间反映了一些学生的品德问题..."
    show sunset smile0
    s "AutoRing.py仍然是我最引以为傲，同时使用时间最长的作品。"
    s "当然还有你面前的——maybe_not_the_last_letter，基于Renpy的互动小说游戏。"
    s "谢谢你问了这个问题，"
    show sunset explain5
    s "我一直在找机会把它们介绍一遍。"
    jump other0

label inmemoryof:
    show sunset explain2
    s "“怀念”？"
    s "听起来好奇怪..."
    s "不过...我明白你的意思。"
    s "答案是：真的有。"
    s "你真的想听吗？"
    menu:
        "真的！":
            jump reallyinmemoryof
        "如果不想说的话...就算了吧。":
            show sunset think0
            s "额..."
            show sunset smile0
            s "好吧..."
            jump other0

label reallyinmemoryof:
    # 下面提到的名字全部使用SHA-256计算hash
    # https://tool.oschina.net/encrypt
    show sunset think0
    s "既然这样..."
    s "（吸气）"
    s "（呼气）"
    $ gtext = glitchtext(6)
    s "ed0f93dfaac17459514c02cb936ae1f23db6ba5eaad82ad456f3eb7fb445f4ae，你在理科方面给了我很多帮助..."
    s "也给对[gtext]的道歉信提出了一些有价值的建议。"
    s "就算最后因为看起来“价值观不合”而不再联系..."
    s "我仍然相信你最后会理解我的意思。"
    s "840a8dbdddece6a56fb9b1f925eac7a75cb274b85e7eddafdfb97573170e5a8b，你在最后的几个星期给了我支持..."
    s "告诉我学校里的情况、授课进度，和我分享秘密，尝试让我不再焦虑..."
    s "看起来很平凡但对我意义重大..."
    show sunset smile0
    s "还记得那朵封存在透明有机物块中的云状物体吗？"
    s "b5f0b1a060a51d4bfaa5b3375a6ba0a8e632c0946066af94a9c47082811ac14c，你帮助了我实施我疯狂的计划..."
    s "写作交流、情报提供、应急处理，不仅如此..."
    s "你成功地让我适应和其他人用餐和近距离交流，无论这个人是谁。"
    s "别忘了尝试学Python啊。"
    show sunset clap0
    s "d88702965eb2acf84424cd64d9bba294a8c2a00d0b4604496723fd2063bf78cf、83235ec96fa3b9c0631863c5e3f998aef8e89c28698a8fc2843509627cb0d295..."
    s "学校里的Brony不多..."
    s "你们是我认识的两个。"
    s "还有被我吓到的一些人..."
    s "221c63aa425164d25f6d2fc5d79d7e06403f1716e93cacb394f32caf451916f0..."
    s "62818288f696eb3eddc601010b407153f2594ddf86858bbad9492fcfd3e7c072..."
    s "以及其他的一些人..."
    s "也许...我成功地将自己最令人意外的形象刻入你们的记忆..."
    show sunset upset5
    s "我...欠你们一个道歉。"
    menu:
        "冷静！停下吧...":
            show sunset think0
            s "（看向你）"
            show sunset smile0
            s "好吧..."
            jump other0
        "你还好吗？":
            jump reallyinmemoryofz

label reallyinmemoryofz:
    s "还有..."
    s "还有...."
    s "还有....."
    s "e04e141499000d4d40bdf3d58379319d1615d392f40582e62e90d4dd69032eee..."