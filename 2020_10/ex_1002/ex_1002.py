# 给定仅有小写字母组成的字符串数组 A，返回列表中的每个字符串中都显示的全部字符（包括重复字符）组成的列表。
# 例如，如果一个字符在每个字符串中出现 3 次，但不是 4 次，则需要在最终答案中包含该字符 3 次。
#
# 你可以按任意顺序返回答案。

class Solution:
    def StrToDict(self,ss):
        res=dict()
        for i in [s for s in ss]:
            res[i]=res.get(i,0)+1
        return res

    def DictToList(self,dict):
        res=[]
        for i in dict.keys():
            for j in range(dict[i]):
                res.append(i)
        return res

    def commonChars(self, A: List[str]) -> List[str]:
        dict_list=[self.StrToDict(s) for s in A]
        res_dict=dict_list[0]
        for temp in dict_list[1:]:
            temp_res=dict()
            for i in temp.keys():
                if(res_dict.get(i,0)!=0):
                    temp_res[i]=min(res_dict[i],temp[i])
            res_dict=temp_res
        return self.DictToList(res_dict)