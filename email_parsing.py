emails=["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com",
        "testemail+david@lee.tcode.com","a..@leetcode.com","a...+.dfsdf.@leetcode.com","a@leetcode.com",
        "b@leetcode.com","c@leetcode.com"]
arr=[]
for i in emails:
    a=list(i)
    j=0
    b=""
    y = i.split('@')
    while a[j]!= "@":
        if a[j]== "+":
            break
        elif a[j]!= ".":
            b=b+str(a[j])
        j=j+1
    b=b+"@"+y[1]
    if b not in arr:
        arr.append(b)
for i in arr:
    print(i)