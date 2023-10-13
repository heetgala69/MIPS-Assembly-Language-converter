import o_f
import binary
 
def l_f(t6,a6,b6):                 #calculates binary value of the lui instruction
    rs6='00000'
    op=o_f.lui_(t6)    #calls function to calculates binary value of opcode
    immediate=binary.itb(b6)            #calls function to calculates binary value of imm
    rt6=binary.rtb(a6)             #calls function to calculates binary value of rt
    if rs6=='INVALID' or rt6=='INVALID' or op=='INVALID' or immediate=='INVALID':
        i='INVALID'
        return i
    else:
        j=op+rs6+rt6+immediate
        return j
def rt_f(t,a1,b1,c1):             #calculates binary value of the r-type instruction
    op='000000'
    function=o_f.rtype_(t)
    rs1=binary.rtb(b1)     #calls function to calculates binary value of rs 
    shamt1='00000'
    rt1=binary.rtb(c1)     #calls function to calculates binary value of rt
    rd1=binary.rtb(a1)     #calls function to calculates binary value of rd
    if rs1=='INVALID' or rt1=='INVALID' or rd1=='INVALID' or shamt1=='INVALID' or function=='INVALID':
        a='INVALID'
        return a
    else:
        b=op+rs1+rt1+rd1+shamt1+function
        return b
def s_f(t2,a2,b2,c2):             #calculates binary value of the shift instruction
    rd2=binary.rtb(a2)     #calls function to calculates binary value of rd
    shamt2=binary.rtb(c2)  #calls function to calculates binary value of shamt
    rt2=binary.rtb(b2)     #calls function to calculates binary value of rt
    function=o_f.shift_(t2) #calls function to calculates binary value of funct
    rs2='00000'
    op='000000'
    if rs2=='INVALID' or rt2=='INVALID' or rd2=='INVALID' or shamt2=='INVALID' or function=='INVALID':
        c='INVALID'
        return c
    else:
        d=op+rs2+rt2+rd2+shamt2+function
        return d
def it_f(t3,a3,b3,c3):             #calculates binary value of the itype instruction
    rs3=binary.rtb(b3)             #calls function to calculates binary value of rs
    immediate=binary.itb(c3)            #calls function to calculates binary value of imm
    rt3=binary.rtb(a3)             #calls function to calculates binary value of rt
    op=o_f.itype_(t3)    #calls function to calculates binary value of opcode
    if rs3=='INVALID' or rt3=='INVALID' or op=='INVALID' or immediate=='INVALID':
        e='INVALID'
        return e
    else:
        f=op+rs3+rt3+immediate
        return f
            
def lwsw_f(t4,a4,b4,c4):              #calculates binary value of the lwsw instruction
    immediate=binary.itb(b4)            #calls function to calculates binary value of imm
    rt4=binary.rtb(a4)             #calls function to calculates binary value of rt
    op=o_f.lwsw_(t4)    #calls function to calculates binary value of opcode
    rs4=binary.rtb(c4)             #calls function to calculates binary value of rs
    if rs4=='INVALID' or rt4=='INVALID' or op=='INVALID' or immediate=='INVALID':
        g='INVALID'
        return g
    else:
        h=op+rs4+rt4+immediate
        return h

def in_na(t,a1,b1,c1):                #function to differentiates and groups different instruction names depedning on it's format
    if t=='lhu'or t=='lbu'or t=='ll'or t=='lw'or t=='sb'or t=='sc'or t=='sh'or t=='sw':
        answer=lwsw_f(t,a1,b1,c1)
        if answer=='INVALID':
            e='INVALID'
            return e
        else:
            return answer
            
    elif t=='sll' or t=='srl':
        answer=s_f(t,a1,b1,c1)
        if answer=='INVALID':
            c='INVALID'
            return c
        else:
            return answer   

    elif t=='addi'or t=='addiu'or t=='ori'or t=='slti'or t=='sltiu':
        answer=it_f(t,a1,b1,c1)
        if answer=='INVALID':
            b='INVALID'
            return b
        else:
            return answer
    elif t=='lui':
        answer=l_f(t,a1,b1)        
        if answer=='INVALID':
            a='INVALID'
            return a
        else:
            return answer

    elif t=='addu'or t=='add' or t=='and' or t=='nor' or t=='or' or t=='slt' or t=='sltu' or t=='sub' or t=='subu':
        answer=rt_f(t,a1,b1,c1)
        if answer=='INVALID':
            d='INVALID'
            return d
        else:
            return answer
    
    else:
        f='INVALID'
        return f                       #returns invaild if the instruction name is incorrect
