# 你将会获得一系列视频片段，这些片段来自于一项持续时长为 T 秒的体育赛事。这些片段可能有所重叠，也可能长度不一。
#
# 视频片段 clips[i] 都用区间进行表示：开始于 clips[i][0] 并于 clips[i][1] 结束。我们甚至可以对这些片段自由地再剪辑，例如片段 [0, 7] 可以剪切成 [0, 1] + [1, 3] + [3, 7] 三部分。
#
# 我们需要将这些片段进行再剪辑，并将剪辑后的内容拼接成覆盖整个运动过程的片段（[0, T]）。返回所需片段的最小数目，如果无法完成该任务，则返回 -1 。
#

class Solution:
    def judge_contain(self,lst1,lst2):
        """
        :param lst1: 区间1
        :param lst2: 区间2
        :return: 若区间2包含区间1，返回1，若区间1包含区间2，返回-1，互不包含返回0
        """
        if lst1[0]<=lst2[0] and lst1[1]>=lst2[1]:
            return -1
        elif lst1[0]>=lst2[0] and lst1[1]<=lst2[1]:
            return 1
        else:
            return 0

    def judge_filled(self,lst1,size):
        """
        :param lst1:
        :param size:
        :return: lst1区间之和包含[0,size],则返回True，反之False
        """

        mark_list=[0]*(size+1)
        for i in range(len(lst1)):
            left=lst1[i][0]
            right=lst1[i][1]
            if left>size:
                continue
            if right>size:
                right=size
            for j in range(right-left+1):
                mark_list[j+left]=1
            if sum(mark_list)==(size+1):
                return True
        return False

    def videoStitching(self, clips, T: int) -> int:
        res=[]
        for i in clips:
            contain_flag=False
            for j in range(len(res)):
                if self.judge_contain(res[j],i)==1:
                    if not contain_flag:
                        contain_flag=True
                        res.remove(res[j])
                        res.insert(j,i)
                    else:
                        res.remove(res[j])
                elif self.judge_contain(res[j],i)==-1:
                    contain_flag=True
                    break
                elif self.judge_contain(res[j],i)==0:
                    continue
            if not contain_flag:
                res.append(i)
        print(res)
        if self.judge_filled(res,T):
            return len(res)
        else:
            return -1

t=Solution()
print(t.videoStitching([[0,1],[6,8],[0,2],[5,6],[0,4],[0,3],[6,7],[1,3],[4,7],[1,4],[2,5],[2,6],[3,4],[4,5],[5,7],[6,9]],9))