label ch2:
    show sunset smile0
    s "怎么？"
    s "有很多人问过我相关的问题..."
    show sunset look0
    s "希望不是在质疑我的选择..."
    menu:
        "当然不是！":
            jump ofcoursenot
        "额...好像是的...":
            jump maybeyes
            
label ofcoursenot:
    s "真的？"