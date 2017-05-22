import requests
import re
import os

def getHTML(url):
    try:
        r=requests.get(url)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        print("getHTML")


def parsePage(raw):
    a = re.findall('setTimeout', raw)
    if not a == []:
        with open('reserved.txt', 'a') as reserved:
            reserved.write(str(i) + '\n')
        continue

    b = re.findall('alt="(\S+)"', raw)
    if not b == []:
        dt = re.findall(r'<strong>(\d+)</strong>动态', raw)[0]
        yy = re.findall(r'<strong>(\d+)</strong>应用关注', raw)[0]
        fx = re.findall(r'<strong>(\d+)</strong>发现', raw)[0]
        fs = re.findall(r'<strong>(\d+)</strong>好友关注', raw)[0]
        try:
            with open('users.csv', 'a') as users:
                users.write(str(i) + ',' + b[0] + ',' + dt + ',' + yy + ',' + fx + ',' + fs + '\n')
        except UnicodeEncodeError:
            with open('unicode.txt', 'a') as un:
                un.write(str(i) + '\n')
        except:
            with open('others.txt', 'a') as others:
                others.write(str(i) + '\n')
    else:
        with open('others.txt', 'a') as others:
            others.write(str(i) + '\n')

'''def writeUserList(a,b):
    tplt="{:4}\t{:8}\t{:16}\n"
'''
def main():
    for i in range(784579, 790156):
        start_url = ('http://coolapk.com/u/' + str(i)).text
        raw = getHTML(start_url)
        parsePage(raw)
    users.close()
    un.close()
    others.close()

main()
