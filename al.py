
loginurl = "https://sso.douyin.com/get_qrcode/?next=https:%2F%2Fcreator.douyin.com%2Fcontent%2Fmanage&aid=2906&service=https:%2F%2Fcreator.douyin.com&is_vcd=1&fp=kj5j6uhv_tvKYUFA0_qzgZ_4l9c_9Amt_DCywEfwbVFCJ"

import random 
agent = [
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36"
#……可以多添几个认证头
]
def user_agents():
    return random.choice(agent)#随机获取一个认证头

import requests
headers = {'User-Agent': user_agents(),'Referer': "https://creator.douyin.com/"}
loginurl = "https://sso.douyin.com/get_qrcode/?next=https:%2F%2Fcreator.douyin.com%2Fcontent%2Fmanage&aid=2906&service=https:%2F%2Fcreator.douyin.com&is_vcd=1&fp=kj5j6uhv_tvKYUFA0_qzgZ_4l9c_9Amt_DCywEfwbVFCJ"
urldata = requests.get(loginurl, headers=headers).json()
print(urldata)

#注意：headers必须加上 'Referer': "https://creator.douyin.com/"

import base64
with open('test.png', 'wb') as f:
    f.write(base64.b64decode(urldata['data']['qrcode']))  
from threading import Thread
from io import BytesIO
from PIL import Image

class showpng(Thread):
    def __init__(self, data):
        Thread.__init__(self)
        self.data = data
    def run(self):
        img = Image.open(BytesIO(self.data))  
        img.show()

testpng = base64.b64decode(urldata['data']['qrcode'])
t = showpng(testpng)
t.start()

import base64
#base64字符串转换成图片
with open('test.png', 'wb') as f:
    f.write(base64.b64decode('iVBORw0KGgoAAAA……'))
#图片转换成base64字符串
f = base64.b64encode(open(r'test.png','rb').read()).decode('utf-8')
#.decode('utf-8') 去掉b''
#输出'iVBORw0KGgoAAAA……'

from pyzbar.pyzbar import decode
import qrcode
from PIL import Image
#二维码转文字
png = decode(Image.open('test.png')) #获取二维码文字信息
for b in png:
    ewurl = b.data.decode("utf-8")  # 二维码文字信息
#输出png = [Decoded(data=b'https:……', type='QRCODE', rect=Rect(left=31, top=31, width=450, height=450), polygon=[Point(x=31, y=31), Point(x=33, y=481), Point(x=480, y=480), Point(x=481, y=33)])]
#输出ewurl = https:……

#文字转二维码并保存二维码
txt = '你好！'
#打印在操作台
qr = qrcode.QRCode()
qr.add_data(txt)
qr.print_ascii(invert=True)#打印
img = qr.make_image()
img.save('test.png')  #保存二维码图片 方法1

#以图片形式打开
qrcode.make(txt).show()
#保存二维码图片 方法2
qrcode.make(loginurl).save('test.png')
import time
session = requests.session()
tokenurl = 'https://sso.douyin.com/check_qrconnect/?next=https:%2F%2Fcreator.douyin.com%2Fcontent%2Fmanage&token={}&service=https:%2F%2Fcreator.douyin.com%2F%3Flogintype%3Duser%26loginapp%3Ddouyin%26jump%3Dhttps:%2F%2Fcreator.douyin.com%2Fcontent%2Fmanage&correct_service=https:%2F%2Fcreator.douyin.com%2F%3Flogintype%3Duser%26loginapp%3Ddouyin%26jump%3Dhttps:%2F%2Fcreator.douyin.com%2Fcontent%2Fmanage&aid=2906&is_vcd=1&fp=kj5j6uhv_tvKYUFA0_qzgZ_4l9c_9Amt_DCywEfwbVFCJ'.format(token)
token = urldata['data']['token']
tokenurl = 'https://sso.douyin.com/check_qrconnect/?next=https:%2F%2Fcreator.douyin.com%2Fcontent%2Fmanage&token={}&service=https:%2F%2Fcreator.douyin.com%2F%3Flogintype%3Duser%26loginapp%3Ddouyin%26jump%3Dhttps:%2F%2Fcreator.douyin.com%2Fcontent%2Fmanage&correct_service=https:%2F%2Fcreator.douyin.com%2F%3Flogintype%3Duser%26loginapp%3Ddouyin%26jump%3Dhttps:%2F%2Fcreator.douyin.com%2Fcontent%2Fmanage&aid=2906&is_vcd=1&fp=kj5j6uhv_tvKYUFA0_qzgZ_4l9c_9Amt_DCywEfwbVFCJ'.format(token)
while 1:
    tokendata = session.get(tokenurl, headers=headers).json()
    print(tokendata)
    #输出tokendata  = {'data': {'status': '1'}, 'description': '', 'error_code': 0, 'message': 'success'}
    if tokendata['data']['status'] == "3": 
    #扫码确认后'status'值变为3，成功登录停止运行！
        session.get(tokendata['data']['redirect_url'], headers=headers)
        #成功登录以后生成redirect_url链接，进行读取获取真正的登录后的cookies值        
        break
    time.sleep(5)



# -*- coding: utf-8 -*-
import base64
import agent
from threading import Thread
import time
import requests
from io import BytesIO
import http.cookiejar as cookielib
from PIL import Image
import os

requests.packages.urllib3.disable_warnings()

headers = {'User-Agent': agent.get_user_agents(), 'Referer': "https://creator.douyin.com/"}

#为确保打开二维码还能继续运行
class showpng(Thread):
    def __init__(self, data):
        Thread.__init__(self)
        self.data = data

    def run(self):
        img = Image.open(BytesIO(self.data)) 
        img.show()

#判断cookies值是否失效
def islogin(session):
    loginurl = "https://creator.douyin.com/web/api/media/user/info/"
    try:
        session.cookies.load(ignore_discard=True)
    except Exception:
        pass
    response = session.get(loginurl, verify=False, headers=headers)
    if response.json()['status_code'] == 0:
        print('Cookies值有效，无需扫码登录！')
        return session, True
    else:
        print('Cookies值已经失效，请重新扫码登录！')
        return session, False

#获取cookies值
def dylogin():
    #将获取的cookies值进行文本保存
    if not os.path.exists('cookies.txt'):
        with open("cookies.txt", 'w') as f:
            f.write("")
    session = requests.session()
    session.cookies = cookielib.LWPCookieJar(filename='cookies.txt')
    session, status = islogin(session)
    if not status:
        loginurl = "https://sso.douyin.com/get_qrcode/?next=https:%2F%2Fcreator.douyin.com%2Fcontent%2Fmanage&aid=2906&service=https:%2F%2Fcreator.douyin.com&is_vcd=1&fp=kj5j6uhv_tvKYUFA0_qzgZ_4l9c_9Amt_DCywEfwbVFCJ"
        urldata = session.get(loginurl, headers=headers).json()
        testpng = base64.b64decode(urldata['data']['qrcode'])
        t = showpng(testpng)
        t.start()
        token = urldata['data']['token']
        tokenurl = 'https://sso.douyin.com/check_qrconnect/?next=https:%2F%2Fcreator.douyin.com%2Fcontent%2Fmanage&token={}&service=https:%2F%2Fcreator.douyin.com%2F%3Flogintype%3Duser%26loginapp%3Ddouyin%26jump%3Dhttps:%2F%2Fcreator.douyin.com%2Fcontent%2Fmanage&correct_service=https:%2F%2Fcreator.douyin.com%2F%3Flogintype%3Duser%26loginapp%3Ddouyin%26jump%3Dhttps:%2F%2Fcreator.douyin.com%2Fcontent%2Fmanage&aid=2906&is_vcd=1&fp=kj5j6uhv_tvKYUFA0_qzgZ_4l9c_9Amt_DCywEfwbVFCJ'.format(
            token)
        while 1:
            qrcodedata = session.get(tokenurl, headers=headers).json()
            if qrcodedata['data']['status'] == "1":
                print('二维码未失效，请扫码！')
            elif qrcodedata['data']['status'] == "2":
                print('已扫码，请确认！')
            elif qrcodedata['data']['status'] == "5":
                print('二维码已失效，请重新运行！')
            if qrcodedata['data']['status'] == "3":
                print('已确认，登录成功！')
                session.get(qrcodedata['data']['redirect_url'], headers=headers)
                break
            time.sleep(5)
        session.cookies.save()
    return session


if __name__ == '__main__':
    dylogin()



