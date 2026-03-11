"""
论文第三章用图：邯郸银行2024年贷款五级分类结构（饼图）
数据来源：邯郸银行2024年度报告
对应论文章节：三、邯郸银行信用风险管理的现状（四）成效
"""

import matplotlib.pyplot as plt
import numpy as np

from chart_style import set_paper_style

set_paper_style()

# 2024年末五级分类占比（%）
labels = ['正常类', '关注类', '次级类', '可疑类', '损失类']
sizes = [89.72, 8.90, 0.68, 0.69, 0.02]
colors = ['#2E86AB', '#F18F01', '#E09F3A', '#C73E1D', '#A23B72']
explode = (0, 0.03, 0.05, 0.05, 0.05)

fig, ax = plt.subplots(figsize=(10, 8))
wedges, texts, autotexts = ax.pie(
    sizes, labels=labels, colors=colors, autopct='%1.2f%%',
    explode=explode, startangle=90,
    textprops={'fontsize': 11}, wedgeprops=dict(edgecolor='white', linewidth=1.5)
)
for t in autotexts:
    t.set_fontsize(10)
    t.set_fontweight('bold')
ax.set_title('邯郸银行2024年末贷款五级分类结构', fontsize=14, fontweight='bold', pad=15)
plt.tight_layout()
plt.savefig('../charts/7_第三章_贷款五级分类饼图.png', dpi=300, bbox_inches='tight')
print("已保存：charts/7_第三章_贷款五级分类饼图.png")
plt.close()
