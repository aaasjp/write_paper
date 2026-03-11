"""
论文第四章用图：贷款行业集中度与关注类/不良率变化
数据来源：邯郸银行2020—2024年年度报告（md资料）
对应论文章节：四、邯郸银行信用风险管理存在的问题
"""

import matplotlib.pyplot as plt
import numpy as np

from chart_style import set_paper_style

set_paper_style()

years = ['2020', '2021', '2022', '2023', '2024']
# 前三大行业占比（%）
manufacturing = [28.33, 28.50, 24.77, 25.24, 25.31]
wholesale_retail = [20.13, 17.02, 14.86, 15.39, 12.45]
construction = [4.67, 6.15, 7.44, 9.17, 9.73]
# 关注类与不良率
attention_pct = [3.54, 4.60, 8.04, 10.07, 8.90]
npl_ratio = [1.90, 1.96, 1.90, 2.24, 1.38]
provision_ratio = [175.63, 182.26, 154.73, 136.84, 204.35]

fig, axes = plt.subplots(1, 2, figsize=(14, 6))
fig.suptitle('邯郸银行信用风险管理存在的问题（2020—2024年）', fontsize=14, fontweight='bold', y=1.02)

# （a）贷款行业集中度 柱状图（前三大行业）
ax1 = axes[0]
x = np.arange(len(years))
w = 0.25
ax1.bar(x - w, manufacturing, w, label='制造业', color='#2E86AB', alpha=0.85)
ax1.bar(x, wholesale_retail, w, label='批发和零售业', color='#06A77D', alpha=0.85)
ax1.bar(x + w, construction, w, label='建筑业', color='#F18F01', alpha=0.85)
ax1.set_xticks(x)
ax1.set_xticklabels(years)
ax1.set_ylabel('占贷款总额比例（%）')
ax1.set_xlabel('年份')
ax1.set_title('(a) 前三大行业贷款占比', fontsize=12, fontweight='bold')
ax1.legend(loc='upper right', fontsize=10)
ax1.grid(True, axis='y', linestyle='--', alpha=0.3)

# （b）关注类占比与不良率、拨备覆盖率 折线图
ax2 = axes[1]
ax2.plot(years, attention_pct, 'o-', color='#F18F01', linewidth=2, markersize=8, label='关注类贷款占比（%）')
ax2.plot(years, npl_ratio, 's-', color='#C73E1D', linewidth=2, markersize=8, label='不良贷款率（%）')
ax2_twin = ax2.twinx()
ax2_twin.plot(years, provision_ratio, '^-', color='#2E86AB', linewidth=2, markersize=8, label='拨备覆盖率（%）')
ax2_twin.axhline(y=150, color='gray', linestyle=':', alpha=0.7)
ax2.set_ylabel('关注类/不良率（%）')
ax2_twin.set_ylabel('拨备覆盖率（%）', color='#2E86AB')
ax2_twin.tick_params(axis='y', labelcolor='#2E86AB')
ax2.set_title('(b) 关注类占比、不良率与拨备覆盖率', fontsize=12, fontweight='bold')
ax2.legend(loc='upper left')
ax2_twin.legend(loc='upper right')
ax2.grid(True, linestyle='--', alpha=0.3)
ax2.set_ylim(0, 12)

plt.tight_layout(rect=[0, 0, 1, 0.98])
plt.savefig('../charts/8_第四章_行业集中与关注类不良.png', dpi=300, bbox_inches='tight')
print("已保存：charts/8_第四章_行业集中与关注类不良.png")
plt.close()
