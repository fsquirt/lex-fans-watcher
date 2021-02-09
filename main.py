import time
import re
from urllib import request

print("欢迎使用 雷哩雷哩 雷皇帝粉丝实时监控器！")

begin_follower = int(input("输入起始粉丝数量"))
oldnow_follower = 0

while True:
    localtime = time.asctime( time.localtime(time.time()) )

    url = 'https://api.bilibili.com/x/relation/stat?vmid=777536&jsonp=jsonp'
    req = request.Request(url)
    page = request.urlopen(req).read()
    page = page.decode('utf-8')
    string = page

    time.sleep(2)

    now_follower = int(re.findall('"follower":([0-9]*)',string,flags=0)[0])
    rundis_follower = oldnow_follower  - now_follower
    dis_follower = begin_follower - now_follower

    print(localtime  + "    雷蝗帝粉丝现在为:" + str(now_follower) + "。  总共取关了" + str(dis_follower) + "人。   实时取关了" + str(rundis_follower) + "人。")
    with open("lex.txt","a") as f:
        f.writelines("\n" + localtime  + "    雷蝗帝粉丝现在为:" + str(now_follower) + "。  总共取关了" + str(dis_follower) + "人。   实时取关了" + str(rundis_follower) + "人。")
        f.close()
    
    oldnow_follower = now_follower
