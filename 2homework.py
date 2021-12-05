put = input("put Y for start ")
while put=="Y":
    put = input("put Y for start ")
    put2 = input('put word:').lower()
    lene = len(put2)
    print(lene)
    vowels = set(" a e i o u")
    cons = set("b c d f g h j k l m n p q r s t v w x y z ")
    text = put2

    countV = 0
    for V in text:
        if V in vowels:
            countV += 1
    countC = 0
    for C in text:
        if C in cons:
            countC += 1
    print("гласные", countC, 'гласные', countV)
    num1= countV/lene*100
    num2= countC/lene*100
    num11=round(num1,2)
    num22=round(num2,2)
    print('гласные',num11  ,'согласные',num22 )


