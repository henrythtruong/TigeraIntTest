
class Log:
    def __init__(self,logfn):
        self.logtypes = {}
        with open(logfn,'r') as fn:
            for ll in fn:
                colvals = ll.split(" ")
                self.logtypes.setdefault(colvals[2],0)
                self.logtypes[colvals[2]] += 1

    def getCountByType(self,ltype):
        if ltype in self.logtypes:
            return self.logtypes[ltype]
        else:
            return 0
