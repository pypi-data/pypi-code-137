from third_sdk.jd.api.base import RestApi

class KeplerXuanpinGenclickurlBatchRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.skuIds = None

		def getapiname(self):
			return 'jd.kepler.xuanpin.genclickurl.batch'

		def get_version(self):
			return '1.0'
			
	




