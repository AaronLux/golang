import urllib3

http = urllib3.PoolManager()
r = http.request('GET', 'http://httpbin.org/robots.txt')
print(r.status)
print(r.data)

for i in range(1,100):
    try:
        r = http.request('GET', 'http://httpbin.org/robots.txt')
        print(len(r.data))
    except Exception as e:
        print(e)