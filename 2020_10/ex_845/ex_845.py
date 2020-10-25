class Solution:
    def longestMountain(self, A) -> int:
        temp=[]
        res_length=[]
        if len(A)==0:
            return 0
        else:
            temp.append(A[0])
            mark=-1
            for i in range(len(A)-1):
                #开始时，下一元素更大
                if mark==-1 and A[i+1]>temp[-1]:
                    mark=0
                    temp.append(A[i+1])
                #开始时，下一元素相等或更小
                elif mark==-1 and A[i+1]<=temp[-1]:
                    temp=[A[i+1]]
                #上坡时，下一元素更大
                elif mark==0 and A[i+1]>temp[-1]:
                    temp.append(A[i+1])
                #上坡时，下一元素更小
                elif mark==0 and A[i+1]<temp[-1]:
                    mark=1
                    temp.append(A[i+1])
                #上坡时，下一元素相同
                elif mark==0 and A[i+1]==temp[-1]:
                    temp=[A[i+1]]
                    mark=-1
                #下坡时，下一元素更大
                elif mark==1 and A[i+1]>temp[-1]:
                    if len(temp)>=3:
                        res_length.append(len(temp))
                    temp=[temp[-1],A[i+1]]
                    mark=0
                #下坡时，下一元素更小
                elif mark==1 and A[i+1]<temp[-1]:
                    temp.append(A[i+1])
                #下坡时，下一元素相同
                elif mark==1 and A[i+1]==temp[-1]:
                    if len(temp)>=3:
                        res_length.append(len(temp))
                    temp=[A[i+1]]
                    mark=-1
            #算上识别出的最后一个山脉
            if len(temp)>=3 and mark==1:
                res_length.append(len(temp))

            if len(res_length)==0:
                return 0
            else:
                return max(res_length)

t=Solution()
print(t.longestMountain([875,884,239,731,723,685]))