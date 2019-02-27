import pandas as pd
s = """
<table bgcolor="#bfbfbf" border="0" cellspacing="1" style="text-align:left;" width="600"><tr><td colspan="4"><b>公告信息：</b></td></tr><tr><td class="title" width="128">采购项目名称</td><td colspan="3" width="430">新乡学院2019年公务印刷（其他印刷品）项目结果公告</td></tr><tr><td class="title">品目</td><td colspan="3"><p></p></td></tr><tr><td class="title">采购单位</td><td colspan="3">新乡学院</td></tr><tr><td class="title">行政区域</td><td width="168">新乡市</td><td class="title" width="128">公告时间</td><td width="168">2019年02月27日  10:29</td></tr><tr><td class="title">本项目招标公告日期</td><td width="168">2019年01月18日</td><td class="title" width="128">中标日期</td><td width="168">2019年02月27日</td></tr><tr><td class="title">评审专家名单</td><td colspan="3">李斌 、薛梅荣、范伟、刘晓、秦昆</td></tr><tr><td class="title">总中标金额</td><td colspan="3">￥54.745000 万元（人民币）</td></tr><tr><td colspan="4"><b>联系人及联系方式：</b></td></tr><tr><td class="title">项目联系人</td><td colspan="3"> 申先生</td></tr><tr><td class="title">项目联系电话</td><td colspan="3">0373-3035300</td></tr><tr><td class="title" width="128">采购单位</td><td colspan="3" width="430">新乡学院</td></tr><tr><td class="title">采购单位地址</td><td colspan="3">新乡市人民东路与新二街交叉口东北角市民中心大楼五楼（533）</td></tr><tr><td class="title">采购单位联系方式</td><td colspan="3">0373-3683105</td></tr><tr><td class="title">代理机构名称</td><td colspan="3">新乡市公共资源交易管理中心</td></tr><tr><td class="title">代理机构地址</td><td colspan="3">新乡市人民东路与新二街交叉口东北角市民中心大楼五楼（533）</td></tr><tr><td class="title">代理机构联系方式</td><td colspan="3">0373-3035300</td></tr></table>
"""

df = pd.read_html(s)

print(df)
