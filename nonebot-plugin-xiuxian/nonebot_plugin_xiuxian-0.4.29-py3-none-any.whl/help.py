
from .xiuxian_config import XiuConfig

"""
Help帮助信息

"""

__xiuxian_version__ = "v0.4.26"

__xiuxian_notes__ = f"""
修仙模拟器帮助信息:
指令：
1、我要修仙：进入修仙模式
2、我的修仙信息：获取修仙数据
3、修仙签到：获取灵石及修为
4、重入仙途：重置灵根数据，每次{XiuConfig().remake}灵石
5、金银阁：猜大小/数字，赌灵石 示例:金银阁10大/小/猜3
6、改名xx：修改你的道号
7、突破：修为足够后，可突破境界（一定几率失败）
8、闭关、出关、灵石出关：修炼增加修为，挂机功能
9、送灵石+数量+道号或者艾特对应人
10、排行榜：修仙排行榜，灵石排行榜，战力排行榜，宗门排行榜
11、悬赏令：获取任务单，接取任务示例：悬赏令接取1， 结算命令示例：悬赏令结算
12、偷灵石：偷灵石@xxx;抢灵石：抢灵石@xxx;其他：我的状态
13、宗门系统：发送"宗门帮助"获取
14、钱庄系统：发送"钱庄帮助"获取
15、世界BOSS：发送"世界boss帮助"获取
""".strip()