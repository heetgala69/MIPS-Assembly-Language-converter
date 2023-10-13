from ast import literal_eval

def tod(r1):                     #converts register to a decimal value
    arr13=['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']
    arr12=['$zero','$at','$v0','$v1','$a0','$a1','$a2','$a3','$t0','$t1','$t2','$t3','$t4','$t5','$t6','$t7','$s0','$s1','$s2','$s3','$s4','$s5','$s6','$s7','$t8','$t9','$k0','$k1','$gp','$sp','$fp','$ra']
    for o in range(len(arr12)):
        if r1==(arr12[o]) or r1==('$'+arr13[o]):
            return arr13[o]
    else:
        a='INVALID'
        return a

def rev(s1):                        #reversing the binary number (1s with 0s and 0s with 1s)    
    if (s1 == '0'):
        a='1'
        return a
    else:
        a='0'
        return a

def twoc(r):                           #calculating twos complement of a binary number
    o1 = len(r)
    t_c = ""
    o_c = ""
    for q in range(o1):
        o_c = o_c + rev(r[q])
        
    o_c = list(o_c.strip(""))
    t_c = list(o_c)
    for q in range(o1 - 1, -1, -1):
     
        if (o_c[q] == '1'):
            t_c[q] = '0'
        else:        
            t_c[q] = '1'
            break
    q=q-1  
    if (q == -1):
        t_c.insert(0, '1')
    t_c=''.join(t_c)
    return t_c

def tb(r):
    r=''.join(r)
    r=int(r)
    a1=str(bin(r).replace('0b',''))
    return a1

def reg(r):
    if len(r)==0:
        return '00000'
    elif len(r)==1:   
        return '0000'
    elif len(r)==2:
        return '000'
    elif len(r)==3:
        return '00'
    elif len(r)==4:
        return'0'
    elif len(r)==5:
        return ''
    else:
        print("INVALID register")
def imm(r):
    if len(r)==0:
        return '0000000000000000'
    elif len(r)==1:
        return  '000000000000000'
    elif len(r)==2:
        return '00000000000000'
    elif len(r)==3:
        return '0000000000000'
    elif len(r)==4:
        return '000000000000'
    elif len(r)==5:
        return '00000000000'
    elif len(r)==6:
        return '0000000000'
    elif len(r)==7:
        return '000000000'
    elif len(r)==8:
        return '00000000'
    elif len(r)==9:
        return '0000000'
    elif len(r)==10:
        return '000000'
    elif len(r)==11:
        return '00000'
    elif len(r)==12:
        return '0000'
    elif len(r)==13:
        return '000'
    elif len(r)==14:
        return'00'
    elif len(r)==15:
        return '0'
    elif len(r)==16:
        return ''


def cimm(r):
    if len(r)==1:
        a='111111111111111'
        return a
    elif len(r)==2:
        b='11111111111111'
        return b
    elif len(r)==3:
        c='1111111111111'
        return c
    elif len(r)==4:
        d='111111111111'
        return d
    elif len(r)==5:
        e='11111111111'
        return e
    elif len(r)==6:
        f='1111111111'
        return f
    elif len(r)==7:
        g='111111111'
        return g
    elif len(r)==8:
        h='11111111'
        return h
    elif len(r)==9:
        i='1111111'
        return i
    elif len(r)==10:
        j='111111'
        return j
    elif len(r)==11:
        k='11111'
        return k
    elif len(r)==12:
        l='1111'
        return l
    elif len(r)==13:
        m='111'
        return m
    elif len(r)==14:
        n='11'
        return n
    elif len(r)==15:
        o='1'
        return o
    elif len(r)==16:
        p=''
        return p

def rtb(r):
    if r[0:2]=='0x':
        a1=str(literal_eval(r))
        abc=tb(a1)
        a5=reg(abc)
    else:
        c=tod(r)
        if c=='INVALID':
            q='INVALID'
            return q
        else:
            abc=tb(c)
            a5=reg(abc)
    return(a5+abc)
def itb(r):                   #function to convert immediate values(decimal, hexadecimal or t1,t2,etc) to binary
    if r[0]=='$':
        r='INVALID'
        return r

    if r[0:2]=='0x':
        reg1=r.replace('0x','').replace(' ','')
        n=0
        for chara in reg1:
            if ((chara>= 'a' and chara<='f') or (chara>= '0' and chara<='9') or (chara>= 'A' and chara<='F')):
                n+=1
        if n==4:
            r=str(literal_eval(r))
        else:
            ca='INVALID'
            return ca
    if r[0]=='-':                                 #handling negative immediate
        r=r.split()
        r[0]=r[0].replace('-','')
        r = ' '.join([str(elem) for elem in r])
        r=int(r)
        if r>65535 or r<-65535:
            v='INVALID'
            return v
        else:
            r=str(r)
            s1=tb(r)
            q1=twoc(s1)
            a=cimm(q1)
    else:
        r = ''.join([str(elem) for elem in r])
        print (r)
        r=int(r)
        if r>65535 or r<-65535:
            f='INVALID'
            return f
        else:
            r=str(r)
            q1=tb(r)
            a=imm(q1)
    r=''.join(r)
    return(a+q1)
