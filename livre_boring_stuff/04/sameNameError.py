def spam():
    """variable locale"""
    print(eggs)  # ERROR!
    eggs = "spam local"


eggs = "global"
spam()
