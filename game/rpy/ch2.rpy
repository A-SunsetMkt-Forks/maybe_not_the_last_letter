# Chapter 2

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
    show sunset look2
    s "好吧..."
    show sunset smile0
    s "那么...你的问题是？"
    menu:
        "没什么...":
            jump ch3
        "为什么你选择了...？":
            jump ch2reason
            
label maybeyes:
    show sunset smile0
    s "别担心，我不会因为你的质疑就破坏你的设备的~"
    s "当然，我可以理解你的疑问..."
    s "毕竟，我的选择和我的优势领域差得太多了。"
    jump ch2reason
    
label ch2reason:
    s "理由比你想象的简单..."