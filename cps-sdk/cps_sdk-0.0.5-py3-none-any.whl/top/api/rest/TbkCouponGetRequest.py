'''
Created by auto_sdk on 2019.07.04
'''
from third_sdk.top.api.base import RestApi
class TbkCouponGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.activity_id = None
		self.item_id = None
		self.me = None

	def getapiname(self):
		return 'taobao.tbk.coupon.get'
