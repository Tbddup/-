#coding=utf-8
def anyBaseAdOne(num,base):                        
    num[-1]+=1                                          
    for x in range(len(num)):
        x = -x+len(num)-1                               
        if num[x] >= base:                              
            num[x] = 0
            if x-1 < 0:
                num.insert(0,1)                         
            else:
                num[x-1]+=1
    return num
def genKey(chars,length):                           
    num=[0]
    for x in xrange(len(chars)**length):
        r = ''
        for i in num:
            r = r + chars[i]
        r = chars[0] * (length-len(r)) + r
        yield r
        num = anyBaseAdOne(num,len(chars))
def save():                                         
    f = open('pass.txt','a')
    print "请输入字符串："
    chars = raw_input()
    print "请输入长度："
    length = input()
    for x in genKey(chars,length):
        f.write(x + '\n')
    f.close()
save()

