'''
Created by auto_sdk on 2019.07.04
'''
from third_sdk.top.api.base import RestApi
class TbkUatmFavoritesGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.fields = None
		self.page_no = None
		self.page_size = None
		self.type = None

	def getapiname(self):
		return 'taobao.tbk.uatm.favorites.get'
