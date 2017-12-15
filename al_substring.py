class Solution:
    def init_visit(self):
        visit = [0] * 123;
        return visit
    count=0
    cur_count=0
    def parse_long(self,tar,left,right,i):
        if right<len(tar):
            if tar[left] == tar[right]:
                self.cur_count += 1  # 长度加1
                self.parse_long(tar, left + 1, right + 1,i)
            else:
                if self.cur_count>self.count:
                    self.count=self.cur_count
                    self.cur_count=0
                self.parse_long(tar, i, right + 1,i)
        return self.count

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start=-1
        long=0
        tar=list(s)
        for i in range(len(tar)):
            visit = self.init_visit()  # 初始化访问数组
            visit[ord(tar[i])] = 1
            tmp_left = i
            j=i+1
            local_long=1
            succession=i
            # for j in range(len(tar)):
            #     if j>i:
            #         if tar[j]==tar[tmp_left] and j-succession==1 :#当前值与i点处相同and连续，则比较后续
            #             succession+=1
            #             cur_len=1
            #             max_index=-1
            #             flag=True
            #             # while j <len(tar)-1 and flag:
            #             #     if tar[j]==tar[tmp_left]:
            #             #         tmp_left+=1
            #             #     j+=1
            #             #     visit[ord(tar[tmp_left])]=1
            #             #     if tar[j]!=tar[tmp_left]:
            #             #         if cur_len>local_long:
            #             #             local_long=cur_len
            #             #         tmp_left=i  #被匹配字符重置
            #             #         '''可以写一个递归 循环取出当前队列下的最长字串
            #             #         '''
            #             #         # cur_len=0
            #             #         # flag=False
            #             #         # break
            #             #     else:
            #             #         cur_len+=1
            #             #         # max_index = i
            #             tmp_left+=1
            #             j+=1
            #             if tar[tmp_left]==tar[j]:#第一次匹配成功，匹配next
            #                 local_long+=1;
            #             else
            #             if local_long>long:
            #                 long=local_long
            #                 # start=max_index
            #                 start=i
            self.count=0
            self.cur_count=0
            local_long=self.parse_long(tar,i,j,i)
            if local_long>long:
                long=local_long
                start=i
        return start,long

if __name__=='__main__':
    str='abcabcabcabc'
    s=Solution()
    res=s.lengthOfLongestSubstring(str)
    print(res)
    # print(str[0])

