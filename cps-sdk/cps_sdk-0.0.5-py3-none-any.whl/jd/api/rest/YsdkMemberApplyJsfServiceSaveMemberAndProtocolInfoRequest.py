from third_sdk.jd.api.base import RestApi

class YsdkMemberApplyJsfServiceSaveMemberAndProtocolInfoRequest(RestApi):
		def __init__(self,domain='gw.api.360buy.com',port=80):
			"""
			"""
			RestApi.__init__(self,domain, port)
			self.memberAndProtocolInfoJson = None

		def getapiname(self):
			return 'jingdong.ysdk.MemberApplyJsfService.saveMemberAndProtocolInfo'

			





