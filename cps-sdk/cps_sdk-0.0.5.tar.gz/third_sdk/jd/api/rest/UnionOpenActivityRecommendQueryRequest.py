from third_sdk.jd.api.base import RestApi

class UnionOpenActivityRecommendQueryRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.req = None

		def getapiname(self):
			return 'jd.union.open.activity.recommend.query'

		def get_version(self):
			return '1.0'
			
	

class Req(object):
		def __init__(self):
			"""
			"""
			self.userId = None
			self.userIdType = None
			self.orderId = None
			self.pid = None
			self.subUnionId = None
			self.siteId = None
			self.positionId = None
			self.needClickUrl = None
			self.imageWidth = None
			self.imageHeight = None





