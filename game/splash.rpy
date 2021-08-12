## Splash.rpy

# Splash Message
init python:
    menu_trans_time = 1
    # Default message everyone sees in the game
    splash_message_default = _("此游戏仅用于技术交流，禁止分发。")
    # Used sometimes to change splash messages if called upon
    splash_messages = [
        _("你好？"),
        _("请支持《心跳文学部》。"),
        _("我们会在没有黑暗的地方见面。"),
        _("你经过我身旁/像鹿穿过花岗/风吹开一枝扶桑花"),
        _("Just Monika."),
        _("光是遇见 就很美好") # 光遇 广告文案
    ]

image splash_warning = ParameterizedText(style="splash_text", xalign=0.5, yalign=0.5)

# Main Menu Images
image menu_bg:
    topleft
    "gui/menu_bg.png"
    menu_bg_move

image game_menu_bg:
    topleft
    "gui/menu_bg.png"
    menu_bg_loop

image menu_fade:
    "white"
    menu_fadeout

image menu_nav:
    "gui/overlay/main_menu.png"
    menu_nav_move

# Main Menu Effects

transform menu_bg_move:
    subpixel True
    topleft
    parallel:
        xoffset 0 yoffset 0
        linear 3.0 xoffset -100 yoffset -100
        repeat
    parallel:
        ypos 0
        time 0.65
        ease_cubic 2.5 ypos -500

transform menu_bg_loop:
    subpixel True
    topleft
    parallel:
        xoffset 0 yoffset 0
        linear 3.0 xoffset -100 yoffset -100
        repeat

transform menu_logo_move:
    subpixel True
    yoffset -300
    time 1.925
    easein_bounce 1.5 yoffset 0

transform menu_nav_move:
    subpixel True
    xoffset -500
    time 1.5
    easein_quint 1 xoffset 0

transform menu_fadeout:
    easeout 0.75 alpha 0
    time 2.481
    alpha 0.4
    linear 0.5 alpha 0


# Team Salvato Splash Screen

image intro:
    truecenter
    "white"
    0.5
    "images/splash.png" with Dissolve(0.5, alpha=True)
    2.5
    "white" with Dissolve(0.5, alpha=True)
    0.5

# Special Mod Message Text

image warning:
    truecenter
    "white"
    "splash_warning" with Dissolve(0.5, alpha=True)
    2.5
    "white" with Dissolve(0.5, alpha=True)
    0.5


# Startup Disclaimer Images
image tos = "images/warning.png"
image tos2 = "images/warning2.png"

# Startup Disclaimer

label splashscreen:
    # Grabs current username of the PC on Windows
    python:
        process_list = []
        currentuser = ""
        if renpy.windows:
            try:
                process_list = subprocess.check_output("wmic process get Description", shell=True).lower().replace("\r", "").replace(" ", "").split("\n")
            except:
                pass
            try:
                for name in ('LOGNAME', 'USER', 'LNAME', 'USERNAME'):
                    user = os.environ.get(name)
                    if user:
                        currentuser = user
            except:
                pass


    python:
        firstrun = ""

    if not firstrun:
        if persistent.first_run and (config.version == persistent.oldversion or persistent.autoload == "postcredits_loop" or persistent.autoload == "zpostcredits_loop"):
            $ quick_menu = False
            scene black
            menu:
                "曾经的存档文件被发现了。你希望加载存档还是重新开始？"
                "删除存档 重新开始":
                    "删除中...{nw}"
                    python:
                        delete_all_saves()
                        renpy.loadsave.location.unlink_persistent()
                        renpy.persistent.should_save_persistent = False
                        renpy.utter_restart()
                "加载存档":
                    pass

    # Sets First Run to False to Show Disclaimer
    default persistent.first_run = False

    # Startup Disclaimer

    if not persistent.first_run:
        $ quick_menu = False
        scene white
        pause 0.5
        scene tos
        with Dissolve(1.0)
        pause 1.0
        # You can edit this message but you MUST have say it's not affiliated with Team Salvato
        # must finish the official game and has spoilers, and where to get DDLC from."
        "《[config.name]》是一个用于技术交流的互动小说游戏。"
        "此项目使用了未获授权的代码和资源文件。"
        "你获得的游戏二进制文件是用于内部预览的测试分发版。"
        menu:
            "通过游玩《[config.name]》，你同意不向非相关人士泄露关于此项目的任何内容且不对此分发包进行逆向工程。"
            "我同意。":
                 pass
        $ persistent.first_run = True
        scene tos2
        with Dissolve(1.5)
        pause 1.0
        scene white

        $ persistent.first_run = True


    $ basedir = config.basedir.replace('\\', '/')

    # Controls auto-load of certain scripts
    if persistent.autoload:
        jump autoload

    # Team Salvato/Splash Message

    $ config.allow_skipping = False

    show white
    $ splash_message = splash_message_default
    $ config.main_menu_music = audio.menu
    $ renpy.music.play(config.main_menu_music)
    $ starttime = datetime.datetime.now()
    show intro with Dissolve(0.5, alpha=True)
    $ pause(3.0 - (datetime.datetime.now() - starttime).total_seconds())
    hide intro with Dissolve(max(0, 3.5 - (datetime.datetime.now() - starttime).total_seconds()), alpha=True)
    if persistent.splashegg and renpy.random.randint(0, 1) == 0:
        $ splash_message = renpy.random.choice(splash_messages)
    show splash_warning "[splash_message]" with Dissolve(max(0, 4.0 - (datetime.datetime.now() - starttime).total_seconds()), alpha=True)
    $ pause(6.0 - (datetime.datetime.now() - starttime).total_seconds())
    hide splash_warning with Dissolve(max(0, 6.5 - (datetime.datetime.now() - starttime).total_seconds()), alpha=True)
    $ pause(6.5 - (datetime.datetime.now() - starttime).total_seconds())
    $ config.allow_skipping = True
    return

# Warning Screen
label warningscreen:
    hide intro
    show warning
    pause 3.0


# Checks if Afterload is the same as the anticheat
label after_load:
    $ config.allow_skipping = allow_skipping
    $ _dismiss_pause = config.developer
    $ style.say_dialogue = style.normal

    if anticheat != persistent.anticheat:
        stop music
        scene black
        "存档无法加载"
        "你在尝试作弊吗？"

        $ renpy.utter_restart()
    return

# Autoreloads the game 
label autoload:
    python:
        if "_old_game_menu_screen" in globals():
            _game_menu_screen = _old_game_menu_screen
            del _old_game_menu_screen
        if "_old_history" in globals():
            _history = _old_history
            del _old_history
        renpy.block_rollback()

        renpy.context()._menu = False
        renpy.context()._main_menu = False
        main_menu = False
        _in_replay = None

        try: renpy.pop_call()
        except: pass
        
    jump expression persistent.autoload

# starts the menu music once started
label before_main_menu:
    $ config.main_menu_music = audio.menu
    return

# Basic Quit.
label quit:
    return
