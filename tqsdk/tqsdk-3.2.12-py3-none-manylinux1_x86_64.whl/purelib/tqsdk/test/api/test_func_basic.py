#!/usr/bin/env python
#  -*- coding: utf-8 -*-

import os
import random

from tqsdk import TqApi, utils

from tqsdk.test.base_testcase import TQBaseTestcase
from tqsdk.test.test_chan_helper import set_test_script

class TestFuncBasic(TQBaseTestcase):
    """
    TqApi中功能函数的基本功能测试.

    注：
    1. 在本地运行测试用例前需设置运行环境变量(Environment variables), 保证api中dict及set等类型的数据序列在每次运行时元素顺序一致: PYTHONHASHSEED=32
    2. 若测试用例中调用了会使用uuid的功能函数时（如insert_order()会使用uuid生成order_id）,
        则：在生成script文件时及测试用例中都需设置 TqApi.RD = random.Random(x), 以保证两次生成的uuid一致, x取值范围为0-2^32
    3. 对盘中的测试用例（即非回测）：因为TqSim模拟交易 Order 的 insert_date_time 和 Trade 的 trade_date_time 不是固定值，所以改为判断范围。
        盘中时：self.assertAlmostEqual(1575292560005832000 / 1e9, order1.insert_date_time / 1e9, places=1)
        回测时：self.assertEqual(1575291600000000000, order1.insert_date_time)
    """

    def setUp(self):
        super(TestFuncBasic, self).setUp()

    def tearDown(self):
        super(TestFuncBasic, self).tearDown()

    def test_is_changing(self):
        """
            is_changing() 测试
            注：本函数不是回测，重新生成测试用例script文件时更改为当前可交易的合约代码,在盘中生成,且_ins_url可能需修改。
        """
        # 预设服务器端响应
        dir_path = os.path.dirname(os.path.realpath(__file__))
        md_url = "wss://api.shinnytech.com/t/nfmd/front/mobile"
        set_test_script(os.path.join(dir_path, "log_file", "test_func_basic_is_changing.script.lzma"))

        # 测试: 模拟账户下单
        utils.RD = random.Random(4)
        # (TQBaseTestcase):
        api = TqApi(auth="tianqin,tianqin", _md_url=md_url)

        quote = api.get_quote("SHFE.rb2201")
        position = api.get_position("SHFE.rb2201")
        order1 = api.insert_order("DCE.m2201", "BUY", "OPEN", 1)
        api.wait_update()
        order2 = api.insert_order("SHFE.rb2201", "SELL", "OPEN", 2, quote.bid_price1)
        api.wait_update()
        self.assertTrue(api.is_changing(order2, "status"))
        self.assertTrue(api.is_changing(position, "volume_short"))
        self.assertFalse(api.is_changing(position, "volume_long"))
        order3 = api.insert_order("SHFE.rb2201", "BUY", "CLOSETODAY", 1, quote.ask_price1)
        while order3.status == "ALIVE":
            api.wait_update()
        self.assertTrue(api.is_changing(order3, "status"))
        self.assertTrue(api.is_changing(position, "volume_short"))
        self.assertFalse(api.is_changing(quote, "last_price"))
        api.close()
