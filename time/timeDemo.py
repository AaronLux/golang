import time

# 返回时间戳
time_stamp = time.time()
print(time_stamp)

# 将时间戳以本地实践返回,注意这里返回的是time struct
local_time = time.localtime(time.time())
print(local_time)

# 格式化日期
local_time = time.asctime(local_time)
print(local_time)

# 这里需要传入元组
t = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
print(t)

# 星期几 日期 时间 年份格式
t = time.strftime("%a %b %d %H:%M:%S %Y",time.localtime())
print(t)

# 反向操作，转换成时间戳   将格式化的日期和其格式化的格式传入
a = "Tue Jul 23 10:41:57 2019"
time_stamp = time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y"))
print(time_stamp)