# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。

define n = Character(_("旁白")) # Narrator
define s = Character(_("余晖"))
define e = Character(_("EXPLORER"))
define m = Character(_("Monika"))

# 游戏在此开始。

label start:
    $ quick_menu = True

    stop music fadeout 1.0

    jump care


label realstart:
    
    play music "<loop 0.0>audio/game0.ogg" fadein 5.0

    # 玩家名不可以是某人的名字或变体（检测不可靠）
    $ playerhash = str(get_hash256(player).lower().replace(" ","").replace("\n",""))
    if playerhash in ["e04e141499000d4d40bdf3d58379319d1615d392f40582e62e90d4dd69032eee","5701d526c31aec856315d00424ed2bb8f54511efd000df924ddaf9aef92d6cd8","a179952a22a8c600b384719a28342d869e17aaa51806dc122378d20c90d219ef","569a765f52d764ddc9d16437fd72534f015a4c886ebef72dcaedc5709a321b95","aa8dd20c818ac4dc53826a44703dd89ac6cc4486889c373fa5756b12a8112c51"]:
        jump youknowwhoerror
    
    # 当我写下游戏逻辑的时候，只有我和Celestia知道我写的是什么；
    # 一周之后就只有Celestia知道了；
    # 一个月之后Celestia也不知道了。

    # 显示一个背景。

    # scene bg black

    # 显示角色立绘。

    # show spirit blank

    # 此处显示各行对话。

    # n "您已创建一个新的 Ren'Py 游戏。"

    # n "当您完善了故事、图片和音乐之后，您就可以向全世界发布了！"

    n "这是一个未完成的作品。"

    menu:
        "运行测试脚本。":
            jump test0
        "进入游戏流程。":
            jump ch0

    jump ch0

    # 此处为游戏结尾。

    n "你永远都不应该看到这句话。"
    n "请将此错误报告给开发者或自行修复。"
    jump start
    
    return
