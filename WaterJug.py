"""
Universal Solution To WaterJug Problem.
"""

class WaterJug:

    def __init__(self,file):
        self.num=3;
        self.aim=''
        self.vol=[];
        self.states=[]
        self.mem={self.joinStates(self.states,self.connecter):[]}
        self.connecter=' '
        self.bestPath=[]
        
    def findSuccessfullPaths(self,path):
        #print path
        if path[-1]==self.aim and (len(path)<=len(self.bestPath) or len(self.bestPath)==0):
            print path;
            self.bestPath=path[:]
        else:
            for each in self.mem[path[-1]]:
                if each not in path and (len(path)<=len(self.bestPath) or len(self.bestPath)==0) :
                    path.append(each)
                    self.findSuccessfullPaths(path)
                    path.pop()

    def performOperation(self,condition,do):
        if condition:
            stat=

    def compleetSearch(self):
        cur_stat=self.joinStates(self.states,self.connecter)
        for i in range(0,self.num):
            if self.states[i]==0:
                stat=self.states[:]
                stat[i]=self.vol[i]
                #print stat
                self.mem[cur_stat].append(self.joinStates(stat,self.connecter))
                statstr=self.joinStates(stat,self.connecter)
                if statstr not in self.mem[cur_stat]:
                    self.mem[cur_stat].append(statstr)
                if statstr not in self.mem:
                    self.mem[statstr]=[]
    
            elif self.states[i]==self.vol[i]:
               stat=self.states[:]
               stat[i]=0
               #print stat
               self.mem[cur_stat].append(self.joinStates(stat,self.connecter))
               statstr=self.joinStates(stat,self.connecter)
               if statstr not in self.mem[cur_stat]:
                   self.mem[cur_stat].append(statstr)
               if statstr not in self.mem:
                    self.mem[statstr]=[]

            for j in range(0,self.num):
                if self.states[i]!=0 and i!=j and self.states[j]<self.vol[j]:
                    stat=self.states[:]
                    volChg=self.vol[j]-stat[j]
                    if volChg<=stat[i]:
                        stat[j]+=volChg
                        stat[i]-=volChg
                    else:
                        stat[j]+=stat[i]
                        stat[i]=0
                        
                    #print stat
                    statstr=self.joinStates(stat,self.connecter)
                    if statstr not in self.mem[cur_stat]:
                        self.mem[cur_stat].append(statstr)
                    if statstr not in self.mem:
                        self.mem[statstr]=[]

        #print self.mem

        for elment in self.mem[cur_stat]:
            if self.mem[elment]==[]:
                self.states=self.splitStates(elment,self.connecter)
                self.compleetSearch()

    def splitStates(self,elment,elm):
        tmplst=[]
        for i in elment.split(self.connecter):
            tmplst.append(int(i))

        return tmplst

    def joinStates(self,stat,elm):
        st=[]
        for each in stat:
            st.append(str(each))

        return self.connecter.join(st)


if __name__=="__main__":
   
    store=WaterJug()
    store.compleetSearch()
    print "Sorted Breadth first:",store.mem
    print "all Successfull Paths:"
    store.findSuccessfullPaths(['0 0 0'])
