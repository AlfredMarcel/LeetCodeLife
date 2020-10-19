# 给定 S 和 T 两个字符串，当它们分别被输入到空白的文本编辑器后，判断二者是否相等，并返回结果。 # 代表退格字符。
#
# 注意：如果对空文本输入退格字符，文本继续为空。

class Solution:
    def str_handle(self,s):
        res=[]
        for i in s:
            if i =="#":
                if res==[]:
                    continue
                else:
                    res=res[:-1]
            else:
                res.append(i)
        return "".join(res)

    def backspaceCompare(self, S: str, T: str) -> bool:
        if(self.str_handle(S)==self.str_handle(T)):
            return True
        else:
            return False