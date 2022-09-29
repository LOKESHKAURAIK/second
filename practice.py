def deco(func):
    def disp():
        print("display is running")
        return func()
    print("deco is running")
    return disp

# def show():
#     print("show is running")

# a=deco(show)
# a()

@deco
def ravi():
    print("ravindra is running...")

ravi()