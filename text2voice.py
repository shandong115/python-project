# -*- coding: UTF-8 -*-
# Python 2.x 引入httplib模块
# import httplib
# Python 3.x 引入http.client模块
import http.client
# Python 2.x 引入urllib模块
# import urllib
# Python 3.x 引入urllib.parse模块
import urllib.parse
import json
import time
import sys
def processGETRequest(appKey, token, text, audioSaveFile, format, sampleRate) :
    host = 'nls-gateway.cn-shanghai.aliyuncs.com'
    url = 'https://' + host + '/stream/v1/tts'
    # 设置URL请求参数
    url = url + '?appkey=' + appKey
    url = url + '&token=' + token
    url = url + '&text=' + text
    url = url + '&format=' + format
    url = url + '&sample_rate=' + str(sampleRate)
    # voice 发音人，可选，默认是xiaoyun
    # url = url + '&voice=' + 'xiaoyun'
    # volume 音量，范围是0~100，可选，默认50
    # url = url + '&volume=' + str(50)
    # speech_rate 语速，范围是-500~500，可选，默认是0
    # url = url + '&speech_rate=' + str(0)
    # pitch_rate 语调，范围是-500~500，可选，默认是0
    # url = url + '&pitch_rate=' + str(0)
    #print(url)
    # Python 2.x 请使用httplib
    # conn = httplib.HTTPSConnection(host)
    # Python 3.x 请使用http.client
    conn = http.client.HTTPSConnection(host)
    conn.request(method='GET', url=url)
    # 处理服务端返回的响应
    response = conn.getresponse()
    print('Response status and response reason:')
    print(response.status ,response.reason)
    contentType = response.getheader('Content-Type')
    print(contentType)
    body = response.read()
    conn.close()
    if 'audio/mpeg' == contentType :
        with open(audioSaveFile, mode='wb') as f:
            f.write(body)
        print('The GET request succeed!')
        return 0
    else :
        print('The GET request failed: ' + str(body))
        return -1

def processPOSTRequest(appKey, token, text, audioSaveFile, format, sampleRate) :
    host = 'nls-gateway.cn-shanghai.aliyuncs.com'
    url = 'https://' + host + '/stream/v1/tts'
    # 设置HTTPS Headers
    httpHeaders = {
        'Content-Type': 'application/json'
        }
    # 设置HTTPS Body
    body = {'appkey': appKey, 'token': token, 'text': text, 'format': format, 'sample_rate': sampleRate}
    body = json.dumps(body)
    print('The POST request body content: ' + body)
    # Python 2.x 请使用httplib
    # conn = httplib.HTTPSConnection(host)
    # Python 3.x 请使用http.client
    conn = http.client.HTTPSConnection(host)
    conn.request(method='POST', url=url, body=body, headers=httpHeaders)
    # 处理服务端返回的响应
    response = conn.getresponse()
    print('Response status and response reason:')
    print(response.status ,response.reason)
    contentType = response.getheader('Content-Type')
    print(contentType)
    body = response.read()
    if 'audio/mpeg' == contentType :
        with open(audioSaveFile, mode='wb') as f:
            f.write(body)
        print('The POST request succeed!')
    else :
        print('The POST request failed: ' + str(body))
    conn.close()

if __name__ == '__main__':
    appKey = 'O8LBi6qHgMfCIapF'
    token = 'cacd926b7fdb40e6bb7fe9a54408a59a'
    #format = 'wav'
    format = 'mp3'
    sampleRate = 16000
    #path = "F:\\zhanlang\\200818\\中东局势凶险异常！美国开始绞杀伊朗\\"
    path = sys.argv[1]
    slice_len = 300
    textFile = path + "doc"
    punctuation = ['，', '。', '？', '：', '、', '！', '；']
    print('textFile: ' + textFile)
    with open(textFile, mode='r',encoding='utf-8') as f:
        content = f.read()
        #print('text: ' + content)
        content_len = len(content)
        print('content_len: '+ str(content_len))
        start = 0
        end = start + slice_len
        ii = 1
        while(start<=content_len):
            sTmp = content[start:end]
            index = 0
            for pp in punctuation:
                i = sTmp.rfind(pp)
                if i>0 and i>index:
                    index = i
            #print('last index='+str(index))
            if index==0:
                break
            
            end = start + index + 1
            slice = content[start:end]
            print('slice: ' + slice)
            
            textUrlencode = slice
            textUrlencode = urllib.parse.quote_plus(textUrlencode)
            textUrlencode = textUrlencode.replace("+", "%20")
            textUrlencode = textUrlencode.replace("*", "%2A")
            textUrlencode = textUrlencode.replace("%7E", "~")
            #audioSaveFile = path + "voice\\" + str(ii) + "." + format
            audioSaveFile = path + str(ii) + "." + format
            for k in range(3):
                if(0==processGETRequest(appKey, token, textUrlencode, audioSaveFile, format, sampleRate)):
                    break
                else:
                    time.sleep(2)
            start = end
            end = start + slice_len
            ii = ii + 1
            time.sleep(1)
            #break
            
        
#text = '今天是周一，天气挺好的，我现在北京。'
## 采用RFC 3986规范进行urlencode编码
#textUrlencode = text
## Python 2.x请使用 urllib.quote
## textUrlencode = urllib.quote(textUrlencode, '')
## Python 3.x请使用urllib.parse.quote_plus
#textUrlencode = urllib.parse.quote_plus(textUrlencode)
#textUrlencode = textUrlencode.replace("+", "%20")
#textUrlencode = textUrlencode.replace("*", "%2A")
#textUrlencode = textUrlencode.replace("%7E", "~")
#print('text: ' + textUrlencode)
#audioSaveFile = 'test01.wav'

# GET 请求方式
#processGETRequest(appKey, token, textUrlencode, audioSaveFile, format, sampleRate)
# POST 请求方式
# processPOSTRequest(appKey, token, text, audioSaveFile, format, sampleRate)