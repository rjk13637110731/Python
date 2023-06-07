import time


def sayLocal(func):
    def wrapper():
        curTime = func()
        return f"当地时间是：{curTime}"
    return wrapper


def getxxxTime():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


getxxxTime = sayLocal(getxxxTime)
print(getxxxTime())
