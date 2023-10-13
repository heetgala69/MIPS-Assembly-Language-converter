import fileinput
import decode

def b2h(v):
    abc=int(v,2)
    hnum=str(hex(abc).replace('0x',''))
    if len(hnum)==8:
        h='0x'
        hnum=h+hnum
    elif len(hnum)==7:
        a='0x0'
        hnum=a+hnum
    elif len(hnum)==6:
        b='0x00'
        hnum=b+hnum
    elif len(hnum)==5:
        c='0x000'
        hnum=c+hnum
    elif len(hnum)==4:
        d='0x0000'
        hnum=d+hnum
    elif len(hnum)==3:
        e='0x00000'
        hnum=e+hnum
    elif len(hnum)==2:
        f='0x000000'
        hnum=f+hnum
    elif len(hnum)==1:
        g='0x0000000'
        hnum=g+hnum
    else:
        return 'INVALID'
    return hnum

def move(answer):              #function to remove comments and labels
    c1=answer[0].split()    
    a1=' '.join([str(element) for element in c1])
    n1=len(a1)
    if a1[n1-1]==':':             #removes text before colon (label)
        str1 = ' '.join([str(element) for element in answer])
        answer=[n1.strip() for n1 in str1.split(':')[1].split(',')]
        LTS = ' '.join([str(element) for element in answer])
    else:
        LTS = ' '.join([str(element) for element in answer])

    f1=[n1.strip() for n1 in LTS.split('#')[0].split(',')]     #removes text after hashtag (comments)
    str1 = ' '.join([str(element) for element in f1])
    answer=str1.split()
    return answer                  #returns instruction without labels and comments


def ath(i,line):                    #defining funtion to convert assembly code to hexadecimal
    i=move(i)
    print(i)
    if len(i)==4:
        i[3]=i[3].replace('(','') #removes ( from the instruction
        i[3]=i[3].replace(')','') #removes ) from the instruction
        i[1]=i[1].replace(',','')     #removes commas from the instruction
        i[2]=i[2].replace(',','')
    elif len(i)==3:
        i[1]=i[1].replace(',','')     #removes commas from the instruction
        i[2]=i[2].replace(',','')
        i.append('0')
    else:   
        a='INVALID INSTRUCTION'                                   #returns 'INVALID INSTRUCTION' if the instruction isn't valid
        return a

    answer=decode.in_na(i[0],i[1],i[2],i[3])
    if answer!='INVALID':
        answer=str(b2h(answer))                          #returns 'INVALID INSTRUCTION' if the instruction isn't valid
        return answer

    else:                                       #returns answer in hex if the instruction is valid
        b='INVALID INSTRUCTION'
        return b                               
i=0
text=input()
fn=text+'.asm'
with open(fn, 'r') as fo:               #input asm file for reading instruction
    with open("output2.txt", 'w') as fc:         #output text file for writing answer
        for line in fo:
            i+=1
            d = line.split()                 #splits asm file text and iterates each line
            a= ath(d,i)            #hex value of the givem instrction is calculated by calling the function assemblyhex and stored in ans
            fc.write(a)                       #writes the hex value in text file 
            fc.write('\n')