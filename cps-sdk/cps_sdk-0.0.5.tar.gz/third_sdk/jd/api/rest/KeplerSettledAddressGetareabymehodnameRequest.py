from third_sdk.jd.api.base import RestApi

class KeplerSettledAddressGetareabymehodnameRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.request = None

		def getapiname(self):
			return 'jd.kepler.settled.address.getareabymehodname'

		def get_version(self):
			return '1.0'
			
	

class Request(object):
		def __init__(self):
			"""
			"""
			self.param = None
			self.methodName = None





