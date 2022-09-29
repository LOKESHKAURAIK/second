def increment(num):
    try:
        return int(num)+1
    except:
        raise ValueError("this is not good")
# a=increment('lk')
a=increment(99)
print(a)