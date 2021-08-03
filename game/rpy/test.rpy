label test0:
    scene bg basic
    s "你好？"
    show sunset explain0
    s "Hello,world!"
    hide sunset
    scene bg sunset stare
    with dissolve
    s "233"
    $ consolehistory = []
    call updateconsole ("os.remove(\"characters/yuri.chr\")", "yuri.chr deleted successfully.") from _call_updateconsole
    $ pause(1.0)
    call updateconsole ("os.remove(\"characters/natsuki.chr\")", "natsuki.chr deleted successfully.") from _call_updateconsole_1
    $ pause(1.0)
    call hideconsole() from _call_hideconsole
    scene bg basic
    $ zeggcount = 6
    show sunset explain
    s "123"
    jump ending
    return