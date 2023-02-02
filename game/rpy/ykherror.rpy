label youknowwhoerror:
    # 其实完全没必要单独放在一个文件里，但是我就是想这么做
    stop music
    $ persistent.autoload = "youknowwhoerror"
    $ config.keymap['game_menu'] = []
    $ config.keymap['hide_windows'] = []
    $ renpy.display.behavior.clear_keymap_cache()
    $ quick_menu = False
    $ config.skipping = False
    $ config.allow_skipping = False
    "（未知）" "你是..."
    "（未知）" "..."
    "（未知）" "我以为你不会..."
    "（未知）" "...无论你真的是..."
    "（未知）" "还是冒用别人名字的家伙..."
    "（未知）" "这里都不适合你..."
    "（未知）" "这个设备上的存档已经被标记了，"
    # "（未知）" "使用Ren'Py SDK的 删除持久化数据 选项可以删除标记"
    "（未知）" "请直接关闭游戏。"
    "（未知）" "这是个循环对话..."
    "（未知）" "你无法离开。"
    jump youknowwhoerror