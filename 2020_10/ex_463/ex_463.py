# 给定一个包含 0 和 1 的二维网格地图，其中 1 表示陆地 0 表示水域。
#
# 网格中的格子水平和垂直方向相连（对角线方向不相连）。整个网格被水完全包围，但其中恰好有一个岛屿（或者说，一个或多个表示陆地的格子相连组成的岛屿）。
#
# 岛屿中没有“湖”（“湖” 指水域在岛屿内部且不和岛屿周围的水相连）。格子是边长为 1 的正方形。网格为长方形，且宽度和高度均不超过 100 。计算这个岛屿的周长。


# 递归解，先找到第一块陆地，然后递归判断他的四个方向，若是海域，周长+1
# 需要对原先进行判断过的陆地加标记，不然就会无限递归

class Solution:
    def count(self,i,j,grid):
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]):
            return 1
        elif grid[i][j]==0:
            return 1
        #标记计算过的岛屿
        elif grid[i][j]==2:
            return 0
        else:
            grid[i][j]=2
            return self.count(i-1,j,grid)+self.count(i,j-1,grid)+self.count(i,j+1,grid)+self.count(i+1,j,grid)

    def islandPerimeter(self, grid) -> int:
        res=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    res=self.count(i,j,grid)
                    break
        return res

t=Solution()
print(t.islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))