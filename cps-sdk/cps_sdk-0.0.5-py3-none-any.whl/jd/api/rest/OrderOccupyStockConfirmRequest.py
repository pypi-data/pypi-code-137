from third_sdk.jd.api.base import RestApi

class OrderOccupyStockConfirmRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.jdOrderId = None

		def getapiname(self):
			return 'biz.order.occupyStock.confirm'

		def get_version(self):
			return '1.0'
			
	




