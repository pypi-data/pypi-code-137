'''
Created by auto_sdk on 2018.07.26
'''
from third_sdk.top.api.base import RestApi
class WangwangClientidBindRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.app_name = None
		self.client_id = None

	def getapiname(self):
		return 'taobao.wangwang.clientid.bind'
