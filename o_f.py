def rtype_(name):          #opcode of rtype instruction is returned
    if name=='add':
        a='100000'
        return a
    elif name=='addu':
        b='100001'
        return b
    elif name=='and':
        c='100100'
        return c
    elif name=='nor':
        d='100111'
        return d
    elif name=='or':
        e='100101'
        return e
    elif name=='slt':
        f='101010'
        return f
    elif name=='sltu':
        g='101011'
        return g
    elif name=='sub':
        h='100010'
        return h
    elif name=='subu':
        i='100011'
        return i
    else:
        return shift_(name)
def shift_(name):          #opcode of shift instruction is returned
    if name=='sll':
        j='000000'
        return j
    elif name=='srl':
        k='000010'
        return k
    else:
        return itype_(name)
def itype_(name):         #opcode of itype instruction is returned
    if name=='addi':
        l='001000'
        return l
    elif name=='addiu':
        m='001001'
        return m
    elif name=='ori':
        n='001101'
        return n
    elif name=='slti':
        o='001010'
        return o
    elif name=='sltiu':
        p='001011'
        return p
    else:
        return lwsw_(name)
def lwsw_(name):       #opcode of lwsw instruction is returned
    if name=='lbu':
        q='100100'
        return q
    elif name=='lhu':
        r='100101'
        return r
    elif name=='ll':
        s='110000'
        return s
    elif name=='lw':
        t='100011'
        return t
    elif name=='sb':
        u='101000'
        return u
    elif name=='sc':
        v='111000'
        return v
    elif name=='sh':
        w='101001'
        return w
    elif name=='sw':
        x='101011'
        return x
    else:
        return lui_(name)
def lui_(name):      #opcode of lui instruction is returned
    if name=='lui':
        y='001111'
        return y
    else:
        z='INVALID'
        return z
