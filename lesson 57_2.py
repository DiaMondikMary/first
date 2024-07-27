ip_=['12.546.34.21','45.21.66.255','45.23.1','fjdg.guergn.sdfw','1.1.1.1','13.67.34.56']
def ip_check(ip:str):
    count=0
    ip_list=ip.split('.')
    if len(ip_list)==4:
        try:
            for i in ip_list:
                if 0<=int(i)<=255:
                    count+=1
                else:
                    continue
        except ValueError:
            return False
    if count==4:
        return True
    else:
        return False
for i in ip_:
    print('-------------------------------')
    print(i)
    print(ip_check(i))
    print('-------------------------------')