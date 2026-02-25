"""
图表绘制脚本：风险管理问题-区域经济依赖性强
数据来源：markdowns/4.风险管理问题-区域经济依赖性强.md
"""

import matplotlib.pyplot as plt
import numpy as np

from chart_style import set_paper_style

# 统一设置论文风格与中文字体
set_paper_style()

# ========== 图表：区域经济依赖性问题分析 ==========
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 10))

# ========== 子图1：贷款增速变化趋势 ==========
years_growth = ['2021', '2022', '2023', '2024']
growth_rates = [25.50, 18.40, 16.40, 12.30]

line1 = ax1.plot(years_growth, growth_rates, marker='o', markersize=9, 
                 linewidth=2.5, color='#C73E1D', markerfacecolor='white', 
                 markeredgewidth=2.5, markeredgecolor='#C73E1D', 
                 label='贷款同比增长率')

for i, (year, rate) in enumerate(zip(years_growth, growth_rates)):
    ax1.text(i, rate, f'{rate:.2f}%',
            ha='center', va='bottom', fontsize=10, fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white', 
                     edgecolor='#C73E1D', linewidth=1.5))

ax1.set_xlabel('年份', fontsize=12, fontweight='bold')
ax1.set_ylabel('同比增长率（%）', fontsize=12, fontweight='bold')
ax1.set_title('贷款增速变化趋势', fontsize=13, fontweight='bold', pad=15)
ax1.set_xticks(range(len(years_growth)))
ax1.set_xticklabels(years_growth)
ax1.legend(loc='upper right', frameon=True, fancybox=True, shadow=True)
ax1.grid(True, linestyle='--', alpha=0.3)
ax1.set_ylim([10, 28])

# ========== 子图2：信用减值损失变化 ==========
years_loss = ['2022', '2023', '2024']
impairment_losses = [41.51, 41.45, 36.27]

bars2 = ax2.bar(years_loss, impairment_losses, width=0.5, color='#A23B72', 
                alpha=0.8, edgecolor='black', linewidth=1.2)

for bar, value in zip(bars2, impairment_losses):
    height = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2., height,
            f'{value:.2f}',
            ha='center', va='bottom', fontsize=10, fontweight='bold')

ax2.set_xlabel('年份', fontsize=12, fontweight='bold')
ax2.set_ylabel('金额（亿元）', fontsize=12, fontweight='bold')
ax2.set_title('信用减值损失变化', fontsize=13, fontweight='bold', pad=15)
ax2.grid(True, axis='y', linestyle='--', alpha=0.3)

# ========== 子图3：贷款规模与利息净收入对比 ==========
years_comparison = ['2020', '2024']
loan_balances = [1675, 3255]
interest_income = [20.14, 90.31]

x = np.arange(len(years_comparison))
width = 0.35

bars3a = ax3.bar(x - width/2, loan_balances, width, label='贷款余额', 
                 color='#2E86AB', alpha=0.8, edgecolor='black', linewidth=1.2)
bars3b = ax3.bar(x + width/2, interest_income, width, label='利息净收入', 
                 color='#F18F01', alpha=0.8, edgecolor='black', linewidth=1.2)

for bars in [bars3a, bars3b]:
    for bar in bars:
        height = bar.get_height()
        if height > 1000:
            label = f'{height:.0f}'
        else:
            label = f'{height:.2f}'
        ax3.text(bar.get_x() + bar.get_width()/2., height,
                label,
                ha='center', va='bottom', fontsize=9, fontweight='bold')

ax3.set_xlabel('年份', fontsize=12, fontweight='bold')
ax3.set_ylabel('金额（亿元）', fontsize=12, fontweight='bold')
ax3.set_title('贷款规模与利息净收入对比', fontsize=13, fontweight='bold', pad=15)
ax3.set_xticks(x)
ax3.set_xticklabels(years_comparison)
ax3.legend(loc='upper left', frameon=True, fancybox=True, shadow=True)
ax3.grid(True, axis='y', linestyle='--', alpha=0.3)

# ========== 子图4：贷款余额变化趋势 ==========
years_loan = ['2020', '2021', '2022', '2023', '2024']
loan_trend = [1675, 2102, 2489, 2898, 3255]

bars4 = ax4.bar(years_loan, loan_trend, width=0.6, color='#06A77D', 
                alpha=0.8, edgecolor='black', linewidth=1.2)

for bar, value in zip(bars4, loan_trend):
    height = bar.get_height()
    ax4.text(bar.get_x() + bar.get_width()/2., height,
            f'{value}',
            ha='center', va='bottom', fontsize=9, fontweight='bold')

ax4.set_xlabel('年份', fontsize=12, fontweight='bold')
ax4.set_ylabel('贷款余额（亿元）', fontsize=12, fontweight='bold')
ax4.set_title('贷款余额变化趋势', fontsize=13, fontweight='bold', pad=15)
ax4.grid(True, axis='y', linestyle='--', alpha=0.3)

# 添加整体标题
fig.suptitle('区域经济依赖性问题分析', fontsize=16, fontweight='bold', y=0.98)

# 添加数据分析说明
analysis_text = '数据分析：贷款增速从2021年的25.5%逐年放缓至2024年的12.3%，反映出本地优质信贷资源趋于饱和。\n2022-2024年间，信用减值损失始终处于高位（41.51亿元、41.45亿元、36.27亿元），虽有所下降，\n但仍反映出经济转型过程中资产质量承压的现实。贷款规模从2020年的1675亿元增至2024年的3255亿元，\n但利息净收入仅从20.14亿元增至90.31亿元，增速明显滞后于资产扩张，反映出优质资产获取难度加大。'
fig.text(0.5, 0.01, analysis_text, ha='center', fontsize=10, 
         style='italic', wrap=True, bbox=dict(boxstyle='round,pad=0.5', 
         facecolor='wheat', alpha=0.3))

plt.tight_layout()
plt.subplots_adjust(top=0.93, bottom=0.12)
plt.savefig('../charts/4_风险管理问题-区域经济依赖性强.png', dpi=300, bbox_inches='tight')
print("图表已保存：4_风险管理问题-区域经济依赖性强.png")
plt.close()

print("\n图表绘制完成！")

