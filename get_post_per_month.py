from read_data import fromJson
def get_post_per_month(data:dict)->dict:
    
    k=0
    a={}
    for i in range(1,13):
        j=0
        for j in data['messages']:
            if int(j['date'][5:7])<=i and j['type']=='message':
                if int(j['date'][5:7])==i:
                    k+=1
        a[i]=k
        k=0
    return a

# Path of the file to read
file_path = "data/result.json"
# Read the data
data = fromJson(file_path)
# Get the number of posts for the month of September
count = get_post_per_month(data)
print(count)