from read_data import fromJson
def get_post_per_week(data:dict,month:int)->dict:
    a={}
    for i in range(1,5):
        k=0
        for j in data['messages']:
            if int(j['date'][5:7])==month and j['type']=='message':
                if (int(j['date'][8:10])>=(7*i-6) and int(j['date'][8:10])<=7*i):
                    k+=1
        a[i]=k
    return a

f=fromJson('data/result.json')
print(get_post_per_week(f,10))

