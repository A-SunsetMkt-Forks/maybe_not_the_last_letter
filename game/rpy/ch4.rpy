# Chapter 4

label ch4:
    show sunset think0
    s "我对高考的印象？"
    s "..."
    s "是一场噩梦。"
    s "从6月7日起的两周内，我在认知上一直处于一场没有醒来的噩梦中..."
    show sunset upset2
    s "那种感觉...很痛苦..."
    s "即使在考试结束后...也没有消失..."
    menu:
        "为什么？":
            jump ch4why
        "我...也一样。":
            jump ch4metoo

label ch4why:
    s "我也说不清楚..."
    s "在我的认知中，考试在成绩公布前是不会离开我的意识的。"
    s "也是直到这时，我才意识到...这好像不太对劲..."
    # 大概是焦虑症的表现吧，可能还有抑郁？不专业的解释
    # 中国的青少年抑郁率还是挺高的
    show sunset upset1
    s "我看着、听着其他同学放下一切去做自己想做的事情..."
    s "我看着他们不再因高考带来的压力而痛苦..."
    s "我却...做不到..."
    show sunset upset4
    s "这些和考试有关的东西...给我的印象太深..."
    s "我想...我们更应该思考的是..."
    s "为什么一场考试的结束可以让我们的高中学生全都放松下来？"
    s "为什么直到这个时候才可以尽情地做自己想做的事情？"
    s "这个局面是怎么造成的？"
    show sunset think0
    s "我们...能给出令人满意的答案吗？"
    show sunset upset5
    s "「我来自一个受过伤痛的国家，我们的国家飞速发展，只是有些人被牺牲了而已。没有人听到他们的声音，没有人看到他们。"
    s "所以我想，我能看到他们，在正确的浪潮中，逆流而上看到那些被牺牲的无辜者，帮助他们。"
    s "可是现在我还是站在大多数人那边，站在世界那边，站在‘正确’那边。"
    s "那么，至少让我听到她吧。」Site-CN-34 三级研究员，站点代主管 M Hannah" # http://scp-wiki-cn.wikidot.com/montauk-hesitation
    # 有其他关于Hannah的注释，见care.rpy
    s "我甚至都无法确定我..."
    s "为了高考所做的事情..."
    s "是否是正确的..."
    s "很“有趣”...对吧？"
    jump ch41end

label ch4metoo:
    s "真的？"
    s "也许...你可以理解我的想法..."
    s "这种奇怪的感觉的产生原因..."
    jump ch4why

label ch41end:
    stop music fadeout 5.0
    if zeggcount != 0:
        jump ch4glitch
    else:
        jump ch4noglitch

label ch4glitch:
    menu:
        "之前的对话中...为什么会有乱码？":
            play music "<loop 0.0>audio/game3.ogg" fadein 3.0
            jump whyglitch
        "关于制作团队的名字...":
            play music "<loop 0.0>audio/game3.ogg" fadein 3.0
            jump projectzstudio

label ch4noglitch:
    menu:
        "关于制作团队的名字...":
            play music "<loop 0.0>audio/game3.ogg" fadein 3.0
            jump projectzstudio
        "关于制作人员...":
            play music "<loop 0.0>audio/game3.ogg" fadein 3.0
            jump ch5

label whyglitch:
    show sunset explain5
    s "没想到你居然注意到了..."
    s "当我们相信某个名字不应该在这里被提到的时候..."
    s "乱码就会出现..."
    s "也许你会找到答案？"
    s "谁知道呢~"
    $ zeggcount = zeggcount + 1
    jump whygdone

label whygdone:
    menu:
        "关于制作团队的名字...":
            jump projectzstudio
        "关于制作人员...":
            jump ch5

label toch5:
    menu:
        "关于制作人员...":
            jump ch5

label projectzstudio:
    show sunset explain2
    s "我...并不是特别想解释这个..."
    s "也许在此之前...你已经听到过这个名字了。"
    s "恐怕由我来解释...会破坏中立性。"
    s "也许...你可以在其他地方找到有用的信息。"
    jump toch5