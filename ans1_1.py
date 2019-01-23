# Part1_1
urls = ["http://www.google.com/a.txt",
        "http://www.google.com/a.txt",
        "http://www.google.com/c.jpg",
        "http://www.google.com/a.txt",
        "http://www.google.com/b.txt",
        "http://www.google.com/b.txt",
        "http://www.google.com/c.jpg",
        "http://www.google.com/haha.png"
       ]

def common_three(urls):
    temp = []
    ans = {}
    
    for i in range(0,len(urls)):
        temp.append(urls[i].split('/')[-1])
    
    for i in temp:
        if temp.count(i)>=1:
            ans[i] = temp.count(i)
    
    from collections import Counter
    word_counts = Counter(temp)
    top_three = word_counts.most_common(3)
    
    return(top_three)

print(common_three(urls))