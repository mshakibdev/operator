num = str(input("Enter Your Mobile Number : "))
l = []
l.extend(num)
def operator(x):
    d ={'1':'Citycell','5':'Teletalk','6':'AirTell','7':'Gp','8':'Robi','9':'Banglalink'}
    y =len(l)
    if l[0] == '0' and l[1]== '1' and y == 11:
        x = d.get(l[2])
        print(x)
        return x
    else:
        print('Invalid Number')
   
operator(l)

