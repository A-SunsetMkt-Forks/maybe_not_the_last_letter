# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。

define n = Character("旁白") # Narrator
define s = Character("余晖")
define e = Character("EXPLORER")
define m = Character("Monika")

# 游戏在此开始。

label start:
    $ quick_menu = True

    stop music fadeout 1.0

    play music "<loop 0.0>audio/game0.ogg" fadein 5.0

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
    jump end
    
    return
