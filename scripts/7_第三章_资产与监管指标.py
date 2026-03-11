"""
论文第三章用图：邯郸银行2020—2024年资产规模、贷款余额与主要监管指标
数据来源：邯郸银行2020—2024年年度报告（md资料）
对应论文章节：三、邯郸银行信用风险管理的现状（四）邯郸银行信用风险管理成效
"""

import matplotlib.pyplot as plt
import numpy as np

from chart_style import set_paper_style

set_paper_style()

# 年报数据（单位：亿元；监管指标为%）
years = ['2020', '2021', '2022', '2023', '2024']
total_assets = [1809, 2024, 2224, 2309, 2492]
loan_balance = [760, 969, 1185, 1252, 1385]
npl_ratio = [1.90, 1.96, 1.90, 2.24, 1.38]
provision_ratio = [175.63, 182.26, 154.73, 136.84, 204.35]
capital_ratio = [11.22, 13.15, 12.91, 13.07, 13.88]
liquidity_ratio = [66.11, 76.40, 83.25, 101.84, 112.07]

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('邯郸银行信用风险管理现状（2020—2024年）', fontsize=14, fontweight='bold', y=1.02)

# （a）总资产与贷款余额 柱状图
ax1 = axes[0, 0]
x = np.arange(len(years))
w = 0.35
b1 = ax1.bar(x - w/2, total_assets, w, label='总资产（亿元）', color='#2E86AB', alpha=0.85, edgecolor='black', linewidth=1)
b2 = ax1.bar(x + w/2, loan_balance, w, label='贷款余额（亿元）', color='#06A77D', alpha=0.85, edgecolor='black', linewidth=1)
for bar in b1:
    ax1.text(bar.get_x() + bar.get_width()/2., bar.get_height(), f'{int(bar.get_height())}', ha='center', va='bottom', fontsize=9)
for bar in b2:
    ax1.text(bar.get_x() + bar.get_width()/2., bar.get_height(), f'{int(bar.get_height())}', ha='center', va='bottom', fontsize=9)
ax1.set_xticks(x)
ax1.set_xticklabels(years)
ax1.set_ylabel('金额（亿元）', fontsize=11)
ax1.set_title('(a) 总资产与贷款余额', fontsize=12, fontweight='bold')
ax1.legend(loc='upper left')
ax1.grid(True, axis='y', linestyle='--', alpha=0.3)

# （b）不良贷款率与拨备覆盖率 折线图（双Y）
ax2 = axes[0, 1]
ax2.plot(years, npl_ratio, 'o-', color='#C73E1D', linewidth=2, markersize=8, label='不良贷款率（%）')
ax2_twin = ax2.twinx()
ax2_twin.plot(years, provision_ratio, 's-', color='#F18F01', linewidth=2, markersize=8, label='拨备覆盖率（%）')
ax2.set_ylabel('不良贷款率（%）', color='#C73E1D')
ax2_twin.set_ylabel('拨备覆盖率（%）', color='#F18F01')
ax2.tick_params(axis='y', labelcolor='#C73E1D')
ax2_twin.tick_params(axis='y', labelcolor='#F18F01')
ax2.set_title('(b) 不良贷款率与拨备覆盖率', fontsize=12, fontweight='bold')
ax2.legend(loc='upper left')
ax2_twin.legend(loc='upper right')
ax2.grid(True, linestyle='--', alpha=0.3)
ax2.set_ylim(0, 4)
ax2.axhline(y=2.5, color='gray', linestyle=':', alpha=0.7)

# （c）资本充足率与流动性比例 折线图
ax3 = axes[1, 0]
ax3.plot(years, capital_ratio, 'o-', color='#2E86AB', linewidth=2, markersize=8, label='资本充足率（%）')
ax3.plot(years, liquidity_ratio, 's-', color='#A23B72', linewidth=2, markersize=8, label='流动性比例（%）')
ax3.axhline(y=10.5, color='gray', linestyle=':', alpha=0.7, label='资本充足率监管线10.5%')
ax3.axhline(y=25, color='gray', linestyle='--', alpha=0.5, label='流动性监管线25%')
ax3.set_xlabel('年份')
ax3.set_ylabel('比例（%）')
ax3.set_title('(c) 资本充足率与流动性比例', fontsize=12, fontweight='bold')
ax3.legend(loc='upper left', fontsize=9)
ax3.grid(True, linestyle='--', alpha=0.3)

# （d）净利润 柱状图（单位：亿元，数据来自年报净利润千元÷10万）
ax4 = axes[1, 1]
net_profit = [8.47, 10.10, 14.97, 6.21, 8.01]  # 对应2020—2024年净利润（亿元）
colors = ['#06A77D'] * 5
colors[3] = '#C73E1D'  # 2023年利润下滑突出显示
bars = ax4.bar(years, net_profit, color=colors, alpha=0.85, edgecolor='black', linewidth=1)
for bar in bars:
    ax4.text(bar.get_x() + bar.get_width()/2., bar.get_height(), f'{bar.get_height():.2f}', ha='center', va='bottom', fontsize=10)
ax4.set_xlabel('年份')
ax4.set_ylabel('净利润（亿元）')
ax4.set_title('(d) 净利润', fontsize=12, fontweight='bold')
ax4.grid(True, axis='y', linestyle='--', alpha=0.3)

plt.tight_layout(rect=[0, 0, 1, 0.98])
plt.savefig('../charts/7_第三章_信用风险管理现状.png', dpi=300, bbox_inches='tight')
print("已保存：charts/7_第三章_信用风险管理现状.png")
plt.close()
