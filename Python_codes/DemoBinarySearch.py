import pdb
data=[2,4,7,9,10,20,30,100]

print(data)

print("Enter the key you want to search")
key=int(input())

print(key)


low=0;
high=len(data)-1
#pdb.set_trace()
while low<=high:
    mid=int((low+high)/2)
    if key==data[mid]:
        print("Key Found @"+str(mid+1)+"th Position")
        break
    else:
        if key < data[mid]:
            high=mid-1
        else:
            low=mid+1

if(low>high):
    print("Key Not Present:")
