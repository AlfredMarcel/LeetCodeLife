# 你的朋友正在使用键盘输入他的名字 name。偶尔，在键入字符 c 时，按键可能会被长按，而字符可能被输入 1 次或多次。
#
# 你将会检查键盘输入的字符 typed。如果它对应的可能是你的朋友的名字（其中一些字符可能被长按），那么就返回 True。

class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        class Solution:
            def isLongPressedName(self, name: str, typed: str) -> bool:
                name_index = 0
                typed_index = 0
                while typed_index < len(typed):
                    if name_index < len(name) and name[name_index] == typed[typed_index]:
                        name_index += 1
                        typed_index += 1
                    elif typed_index > 0 and typed[typed_index] == name[name_index - 1]:
                        typed_index += 1
                    else:
                        return False
                return name_index == len(name)