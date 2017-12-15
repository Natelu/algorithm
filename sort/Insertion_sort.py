class Insertion_sort:
    '''
    descend false 升序
            true 降序
    '''
    def sort(self,lis,descend):
        for i in range(len(lis)):
            if i>0:
                key = lis[i]
                j =i-1
                if descend:#降序
                    while j>=0 and lis[j]<key:
                        lis[j+1]=lis[j]
                        j-=1
                else:
                    while j>=0 and lis[j]>key:
                        lis[j+1]=lis[j]
                        j-=1
                lis[j+1]=key
        return lis

if __name__=='__main__':
    a=[9,8,6,7,5,4,3,2,1,0]
    res=Insertion_sort()
    result=res.sort(a,False)
    print(result)