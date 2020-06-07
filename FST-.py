from nltk.nltk_contrib.fst.fst import *
class myFST(FST):    
    def recognize(self, iput, oput):
        self.inp = list(iput)
        self.outp = list(oput)
        if list(oput) == f.transduce(list(iput)):
            return True
        else:
            return False
        #return oput

# or this more verbose way
f = myFST('example')
# first add the states in the FST
#for i in range(0,3):
f.add_state('1')
f.initial_state = '1'
f.add_arc('1', '1', ('vi'), ('wei'))
f.add_arc('1', '1', ('ta'), ('ta')) 
f.add_arc('1', '1', ('min'), ('ming'))
f.add_arc('1', '1', ('la'), ('na'))
f.add_arc('1', '1', ('tte'), ('tie'))
f.add_arc('1', '1', ('mo'), ('mo'))
f.add_arc('1', '1', ('cha'), ('ka'))
f.add_arc('1', '1', ('ti'), ('ti'))
f.add_arc('1', '1', ('ra'), ('la'))
f.add_arc('1', '1', ('mi'), ('mi'))
f.add_arc('1', '1', ('su'), ('su'))
f.add_arc('1', '1', ('bun'), ('beng'))
f.add_arc('1', '1', ('gee'), ('ji'))
f.add_arc('1', '1', ('la'), ('lei'))
f.add_arc('1', '1', ('ser'), ('she'))
f.add_arc('1', '1', ('hac'), ('hei'))
f.add_arc('1', '1', ('ker'), ('ke'))
f.set_final('1') 


inp = input("Enter:")
inp1=['vita','la']
outp1 = ["weita","na"]
for i in range(0,2):
    if inp==inp1[i]:
        outp=outp1[i]
        str(outp)
outp
print(inp,outp)

if f.recognize(inp, outp):
    print(outp)
    print("accept")
else:    
    print("reject")

disp = FSTDemo(f)
disp.mainloop()