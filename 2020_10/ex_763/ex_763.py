# 字符串 S 由小写字母组成。我们要把这个字符串划分为尽可能多的片段，同一个字母只会出现在其中的一个片段。返回一个表示每个字符串片段的长度的列表。

class Solution:
    def partitionLabels(self, S: str):
        if S=="":
            return [0]
        else:
            alpha_bet_dict=dict()
            for i in range(len(S)):
                temp=alpha_bet_dict.get(S[i],0)
                if temp==0:
                    alpha_bet_dict[S[i]]=[]
                    alpha_bet_dict[S[i]].append(i)
                else:
                    alpha_bet_dict[S[i]].append(i)
            res=[]
            first=S[0]
            index_begin=alpha_bet_dict[first][0]
            index_end=alpha_bet_dict[first][-1]
            res.append([index_begin,index_end])


            for j in alpha_bet_dict.keys():
                flag = True
                index_begin_temp=alpha_bet_dict[j][0]
                index_end_temp=alpha_bet_dict[j][-1]
                for i in res:
                    if flag==False:
                        break
                    if index_begin_temp<=i[0] and index_end_temp>=i[-1]:
                        i[0]=index_begin_temp
                        i[-1]=index_end
                        flag=False
                    elif index_begin_temp>=i[0] and index_end_temp<=i[-1]:
                        flag=False
                    elif index_begin_temp<=i[0] and index_end_temp<=i[-1] and index_end_temp>=i[0]:
                        i[0]=index_begin_temp
                        flag=False
                    elif index_begin_temp>=i[0] and index_begin_temp<=i[-1] and index_end_temp>=i[-1]:
                        i[-1]=index_end_temp
                        flag=False
                if flag:
                    res.append([index_begin_temp,index_end_temp])

            for k in range(len(res)):
                res[k] = res[k][-1] - res[k][0] + 1
            return res

temp=Solution()
print(temp.partitionLabels("ababcbacadefegdehijhklij"))