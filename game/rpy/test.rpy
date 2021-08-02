label test0:
    scene bg basic
    s "你好？"
    show sunset explain
    s "Hello,world!"
    hide sunset
    scene bg sunset stare
    with dissolve
    s "233"
    $ consolehistory = []
    call updateconsole ("os.remove(\"characters/yuri.chr\")", "yuri.chr deleted successfully.")
    $ pause(1.0)
    call updateconsole ("os.remove(\"characters/natsuki.chr\")", "natsuki.chr deleted successfully.")
    $ pause(1.0)
    call hideconsole()
    scene bg basic
    show sunset explain
    s "123"
    return