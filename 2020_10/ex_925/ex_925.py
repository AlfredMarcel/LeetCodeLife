# 你的朋友正在使用键盘输入他的名字 name。偶尔，在键入字符 c 时，按键可能会被长按，而字符可能被输入 1 次或多次。
#
# 你将会检查键盘输入的字符 typed。如果它对应的可能是你的朋友的名字（其中一些字符可能被长按），那么就返回 True。

class Solution:
    def handleStr(self,ss):
        res=[]
        temp=""
        for i in ss:
            if temp=="" or i==temp[0] :
                temp+=i
            else:
                res.append(temp)
                temp=i
        res.append(temp)
        return res

    def isLongPressedName(self, name: str, typed: str) -> bool:
        name_lst=self.handleStr(name)
        typed_lst=self.handleStr(typed)
        res=False
        if len(name_lst)==len(typed_lst):
            for i in range(len(name_lst)):
                if len(typed_lst[i])<len(name_lst[i]):
                    return res
                if typed_lst[i][0]!=name_lst[i][0]:
                    return res
            res=True
        return res

te=Solution()
print(te.handleStr("laidez"))
print(te.handleStr("laideccc"))
print(te.isLongPressedName("laidez","laideccc"))
