"""
论文第四章用图：贷款行业分布饼图（2024年末）
数据来源：邯郸银行2024年度报告 贷款主要行业分布（前十）
对应论文章节：四、邯郸银行信用风险管理存在的问题（一）信用风险管理体系与业务特点不匹配
"""

import matplotlib.pyplot as plt
import numpy as np

from chart_style import set_paper_style

set_paper_style()

# 2024年前十行业占比（%），其余合并为“其他”
labels = ['制造业', '批发和零售业', '建筑业', '租赁和商务服务业', '交通运输仓储邮政', '房地产业',
          '电力热力燃气及水', '采矿业', '水利环境公共设施', '住宿和餐饮', '其他']
sizes = [25.31, 12.45, 9.73, 7.22, 4.56, 3.59, 3.46, 2.41, 1.87, 1.42, 27.99]
colors = ['#2E86AB', '#06A77D', '#F18F01', '#A23B72', '#C73E1D', '#E09F3A', '#6A994E', '#BC4B51', '#5C4D7D', '#3D5A80', '#95A3B8']

fig, ax = plt.subplots(figsize=(11, 8))
wedges, texts, autotexts = ax.pie(
    sizes, labels=labels, colors=colors, autopct='%1.1f%%',
    startangle=90, textprops={'fontsize': 10},
    wedgeprops=dict(edgecolor='white', linewidth=1.2)
)
for t in autotexts:
    t.set_fontsize(9)
ax.set_title('邯郸银行2024年末贷款行业分布（前十大行业+其他）', fontsize=13, fontweight='bold', pad=15)
plt.tight_layout()
plt.savefig('../charts/8_第四章_贷款行业分布饼图.png', dpi=300, bbox_inches='tight')
print("已保存：charts/8_第四章_贷款行业分布饼图.png")
plt.close()
