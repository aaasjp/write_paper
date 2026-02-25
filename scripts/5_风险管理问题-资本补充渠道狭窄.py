"""
图表绘制脚本：风险管理问题-资本补充渠道狭窄
数据来源：markdowns/5.风险管理问题-资本补充渠道狭窄.md
"""

import matplotlib.pyplot as plt
import numpy as np

from chart_style import set_paper_style

# 统一设置论文风格与中文字体
set_paper_style()

# ========== 图表：资本补充渠道狭窄问题分析 ==========
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 10))

# ========== 子图1：未分配利润与资产总额对比 ==========
years = ['2020', '2024']
undistributed_profit = [53.08, 103.0]  # 未分配利润（亿元）
total_assets = [3602, 6895]  # 资产总额（亿元）

x = np.arange(len(years))
width = 0.35

bars1a = ax1.bar(x - width/2, undistributed_profit, width, label='未分配利润', 
                 color='#06A77D', alpha=0.8, edgecolor='black', linewidth=1.2)
bars1b = ax1.bar(x + width/2, total_assets, width, label='资产总额', 
                 color='#2E86AB', alpha=0.8, edgecolor='black', linewidth=1.2)

for bars in [bars1a, bars1b]:
    for bar in bars:
        height = bar.get_height()
        if height > 1000:
            label = f'{height:.0f}'
        else:
            label = f'{height:.2f}'
        ax1.text(bar.get_x() + bar.get_width()/2., height,
                label,
                ha='center', va='bottom', fontsize=9, fontweight='bold')

ax1.set_xlabel('年份', fontsize=12, fontweight='bold')
ax1.set_ylabel('金额（亿元）', fontsize=12, fontweight='bold')
ax1.set_title('未分配利润与资产总额对比', fontsize=13, fontweight='bold', pad=15)
ax1.set_xticks(x)
ax1.set_xticklabels(years)
ax1.legend(loc='upper left', frameon=True, fancybox=True, shadow=True)
ax1.grid(True, axis='y', linestyle='--', alpha=0.3)

# 计算增长率
profit_growth = ((undistributed_profit[1] - undistributed_profit[0]) / undistributed_profit[0]) * 100
asset_growth = ((total_assets[1] - total_assets[0]) / total_assets[0]) * 100
ax1.text(0.5, 0.95, f'未分配利润增长：{profit_growth:.1f}%\n资产总额增长：{asset_growth:.1f}%', 
         transform=ax1.transAxes, ha='center', va='top', fontsize=9,
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

# ========== 子图2：净利润变化 ==========
years_profit = ['2020', '2021']
net_profit = [25.45, 30.72]

bars2 = ax2.bar(years_profit, net_profit, width=0.5, color='#F18F01', 
                alpha=0.8, edgecolor='black', linewidth=1.2)

for bar, value in zip(bars2, net_profit):
    height = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2., height,
            f'{value:.2f}',
            ha='center', va='bottom', fontsize=10, fontweight='bold')

ax2.set_xlabel('年份', fontsize=12, fontweight='bold')
ax2.set_ylabel('金额（亿元）', fontsize=12, fontweight='bold')
ax2.set_title('净利润变化', fontsize=13, fontweight='bold', pad=15)
ax2.grid(True, axis='y', linestyle='--', alpha=0.3)

# 计算增长率
profit_growth_rate = ((net_profit[1] - net_profit[0]) / net_profit[0]) * 100
ax2.text(0.5, 0.95, f'增长率：{profit_growth_rate:.1f}%', transform=ax2.transAxes,
         ha='center', va='top', fontsize=10, bbox=dict(boxstyle='round', 
         facecolor='wheat', alpha=0.5))

# ========== 子图3：股本变化 ==========
years_capital = ['2020', '2024']
share_capital = [41.23, 48.35]

bars3 = ax3.bar(years_capital, share_capital, width=0.5, color='#A23B72', 
                alpha=0.8, edgecolor='black', linewidth=1.2)

for bar, value in zip(bars3, share_capital):
    height = bar.get_height()
    ax3.text(bar.get_x() + bar.get_width()/2., height,
            f'{value:.2f}',
            ha='center', va='bottom', fontsize=10, fontweight='bold')

ax3.set_xlabel('年份', fontsize=12, fontweight='bold')
ax3.set_ylabel('金额（亿元）', fontsize=12, fontweight='bold')
ax3.set_title('股本变化', fontsize=13, fontweight='bold', pad=15)
ax3.grid(True, axis='y', linestyle='--', alpha=0.3)

# 计算增长率
capital_growth = ((share_capital[1] - share_capital[0]) / share_capital[0]) * 100
ax3.text(0.5, 0.95, f'增长率：{capital_growth:.1f}%', transform=ax3.transAxes,
         ha='center', va='top', fontsize=10, bbox=dict(boxstyle='round', 
         facecolor='wheat', alpha=0.5))

# ========== 子图4：资本积累与资产扩张增速对比 ==========
categories = ['未分配利润\n增长率', '股本\n增长率', '资产总额\n增长率']
growth_rates = [profit_growth, capital_growth, asset_growth]
colors = ['#06A77D', '#A23B72', '#2E86AB']

bars4 = ax4.bar(categories, growth_rates, width=0.5, color=colors, 
                alpha=0.8, edgecolor='black', linewidth=1.2)

for bar, rate in zip(bars4, growth_rates):
    height = bar.get_height()
    ax4.text(bar.get_x() + bar.get_width()/2., height,
            f'{rate:.1f}%',
            ha='center', va='bottom', fontsize=10, fontweight='bold')

ax4.set_ylabel('增长率（%）', fontsize=12, fontweight='bold')
ax4.set_title('资本积累与资产扩张增速对比', fontsize=13, fontweight='bold', pad=15)
ax4.grid(True, axis='y', linestyle='--', alpha=0.3)
ax4.axhline(y=0, color='black', linewidth=0.8)

# 添加整体标题
fig.suptitle('资本补充渠道狭窄问题分析', fontsize=16, fontweight='bold', y=0.98)

# 添加数据分析说明
analysis_text = '数据分析：未分配利润从2020年的53.08亿元增长至2024年的103.0亿元，但资产总额同期增长91.4%，\n资本积累速度相对不足。股本五年间增幅仅为17.3%，难以完全覆盖资产快速扩张带来的资本消耗。\n内源性资本补充能力受盈利能力周期性波动影响大，外源性资本补充渠道较为单一。'
fig.text(0.5, 0.01, analysis_text, ha='center', fontsize=10, 
         style='italic', wrap=True, bbox=dict(boxstyle='round,pad=0.5', 
         facecolor='wheat', alpha=0.3))

plt.tight_layout()
plt.subplots_adjust(top=0.93, bottom=0.12)
plt.savefig('../charts/5_风险管理问题-资本补充渠道狭窄.png', dpi=300, bbox_inches='tight')
print("图表已保存：5_风险管理问题-资本补充渠道狭窄.png")
plt.close()

print("\n图表绘制完成！")

