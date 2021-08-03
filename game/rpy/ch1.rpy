label ch1:
    menu:
        "你的简介上写着...你是计算机科学初学者？谈谈你的作品吧。":
            jump program
        "你有想怀念的人吗？":
            jump memory

label program:
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
    s "in-memory-of-[gtext]..."
    $ gtext = glitchtext(11)
    s "本来是个用于回忆和[gtext]的经历的项目..."
    $ gtext = glitchtext(60)
    show sunset upset3
    s "我...我们...[gtext]"
    $ zeggcount = zeggcount + 1
    jump ending