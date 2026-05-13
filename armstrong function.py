def armstrong(num,power,res=0):
    while num!=0:
        ld=num%10
        res+=ld**power
        num//=10
    return res
num=153
print('armstrong'if armstrong(num,len(str(num)))==num else 'not armstrong')
