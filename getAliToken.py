# -*- coding: utf8 -*-

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest
import json

def get_ali_token():
	# 创建AcsClient实例
	client = AcsClient(
		"LTAI4GBVV78zXMGhPPspW9Yg",
		"P9vrjQHlKXv1wj6p5CdfIiHR1KYxCW",
		"cn-shanghai"
	);

	# 创建request，并设置参数。
	request = CommonRequest()
	request.set_method('POST')
	request.set_domain('nls-meta.cn-shanghai.aliyuncs.com')
	request.set_version('2019-02-28')
	request.set_action_name('CreateToken')
	response = client.do_action_with_exception(request)

	#print(response)
	
	token = json.loads(response)["Token"]["Id"]
	return(token)
	
#if __name__ == '__main__':
	#get_ali_token()