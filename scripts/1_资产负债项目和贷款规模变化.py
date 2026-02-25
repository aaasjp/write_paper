"""
图表绘制脚本：资产负债项目和贷款规模变化
数据来源：markdowns/1.资产负债项目和贷款规模变化.md
"""

import matplotlib.pyplot as plt
import numpy as np

from chart_style import set_paper_style

# 统一设置论文风格与中文字体
set_paper_style()

# ========== 图表1：2024年主要资产负债项目（合并图表） ==========
fig1 = plt.figure(figsize=(16, 10))
gs = fig1.add_gridspec(2, 2, hspace=0.3, wspace=0.3)

# 数据
items = ['发放贷款及垫款', '债权投资', '其他债权投资', '吸收存款', '应付债券']
amounts = [3255, 1254, 1299, 4490, 875.2]
percentages = [47.20, 18.20, 18.80, 70.00, 13.70]

# 资产端数据
asset_items = ['发放贷款及垫款', '债权投资', '其他债权投资']
asset_amounts = [3255, 1254, 1299]
asset_percentages = [47.20, 18.20, 18.80]
asset_colors = ['#2E86AB', '#06A77D', '#F18F01']

# 负债端数据
liability_items = ['吸收存款', '应付债券']
liability_amounts = [4490, 875.2]
liability_percentages = [70.00, 13.70]
liability_colors = ['#A23B72', '#C73E1D']

# ========== 子图1：主要资产负债项目柱状图+折线图 ==========
ax1 = fig1.add_subplot(gs[0, :])
ax1_bar = ax1
ax1_line = ax1.twinx()

# 绘制柱状图（金额）
bars = ax1_bar.bar(range(len(items)), amounts, width=0.6, color='#2E86AB', 
                   alpha=0.8, edgecolor='black', linewidth=1.2)

# 在柱状图上添加数值标签
for i, (bar, amount) in enumerate(zip(bars, amounts)):
    height = bar.get_height()
    ax1_bar.text(bar.get_x() + bar.get_width()/2., height,
                f'{amount:.1f}',
                ha='center', va='bottom', fontsize=10, fontweight='bold')

# 绘制折线图（占比）
line = ax1_line.plot(range(len(items)), percentages, marker='o', 
                     markersize=8, linewidth=2.5, color='#A23B72', 
                     markerfacecolor='white', markeredgewidth=2, 
                     markeredgecolor='#A23B72', label='占比')

# 在折线上添加数值标签
for i, (x, pct) in enumerate(zip(range(len(items)), percentages)):
    ax1_line.text(x, pct, f'{pct:.2f}%',
                  ha='center', va='bottom', fontsize=10, fontweight='bold',
                  bbox=dict(boxstyle='round,pad=0.3', facecolor='white', 
                           edgecolor='#A23B72', linewidth=1.5))

# 设置标签和标题
ax1_bar.set_xlabel('项目', fontsize=12, fontweight='bold')
ax1_bar.set_ylabel('金额（亿元）', fontsize=12, fontweight='bold', color='#2E86AB')
ax1_line.set_ylabel('占比（%）', fontsize=12, fontweight='bold', color='#A23B72')
ax1_bar.set_title('2024年主要资产负债项目', fontsize=14, fontweight='bold', pad=20)

# 设置x轴刻度
ax1_bar.set_xticks(range(len(items)))
ax1_bar.set_xticklabels(items, rotation=0, ha='center')

# 添加网格
ax1_bar.grid(True, axis='y', linestyle='--', alpha=0.3)
ax1_line.grid(False)

# 设置y轴颜色
ax1_bar.tick_params(axis='y', labelcolor='#2E86AB')
ax1_line.tick_params(axis='y', labelcolor='#A23B72')

# 添加图例
ax1_bar.legend(['金额'], loc='upper left', frameon=True, 
              fancybox=True, shadow=True)
ax1_line.legend(['占比'], loc='upper right', frameon=True, 
               fancybox=True, shadow=True)

# ========== 子图2：资产端饼图 ==========
ax2 = fig1.add_subplot(gs[1, 0])
wedges, texts, autotexts = ax2.pie(asset_percentages, labels=asset_items, 
                                   colors=asset_colors, autopct='%1.2f%%',
                                   startangle=90, textprops={'fontsize': 11, 'fontweight': 'bold'},
                                   wedgeprops=dict(edgecolor='black', linewidth=1.2))

# 添加金额标签
for i, (wedge, amount) in enumerate(zip(wedges, asset_amounts)):
    angle = (wedge.theta2 + wedge.theta1) / 2
    x = 1.2 * np.cos(np.deg2rad(angle))
    y = 1.2 * np.sin(np.deg2rad(angle))
    ax2.text(x, y, f'{amount:.0f}亿元', ha='center', va='center', 
            fontsize=10, fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white', 
                     edgecolor='black', linewidth=1, alpha=0.8))

ax2.set_title('资产端结构', fontsize=13, fontweight='bold', pad=15)

# ========== 子图3：负债端饼图 ==========
ax3 = fig1.add_subplot(gs[1, 1])
wedges, texts, autotexts = ax3.pie(liability_percentages, labels=liability_items, 
                                   colors=liability_colors, autopct='%1.2f%%',
                                   startangle=90, textprops={'fontsize': 11, 'fontweight': 'bold'},
                                   wedgeprops=dict(edgecolor='black', linewidth=1.2))

# 添加金额标签
for i, (wedge, amount) in enumerate(zip(wedges, liability_amounts)):
    angle = (wedge.theta2 + wedge.theta1) / 2
    x = 1.2 * np.cos(np.deg2rad(angle))
    y = 1.2 * np.sin(np.deg2rad(angle))
    ax3.text(x, y, f'{amount:.1f}亿元', ha='center', va='center', 
            fontsize=10, fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white', 
                     edgecolor='black', linewidth=1, alpha=0.8))

ax3.set_title('负债端结构', fontsize=13, fontweight='bold', pad=15)

# 添加数据分析说明
analysis_text = '数据分析：截至2024年末，邯郸银行贷款余额达到3255亿元，较2020年增长94.3%，贷款年均复合增长率约为18.1%。\n贷款占总资产的比例从2020年的46.5%提升至2024年的47.2%，表明信贷业务继续发挥核心资产作用。\n资产端以发放贷款及垫款为主（47.20%），债权投资和其他债权投资合计占比37.00%，资产结构相对集中。\n负债端以吸收存款为主（70.00%），应付债券占比13.70%，负债结构较为稳定，存款是主要资金来源。'
fig1.text(0.5, 0.02, analysis_text, ha='center', fontsize=10, 
         style='italic', wrap=True, bbox=dict(boxstyle='round,pad=0.5', 
         facecolor='wheat', alpha=0.3))

plt.tight_layout()
plt.subplots_adjust(bottom=0.15)
plt.savefig('../charts/1_资产负债项目.png', dpi=300, bbox_inches='tight')
print("图表1已保存：1_资产负债项目.png")
plt.close()

# ========== 图表2：2020-2024年贷款规模变化 ==========
fig2, ax2 = plt.subplots(figsize=(12, 6))

# 数据
years = ['2020', '2021', '2022', '2023', '2024']
loan_balances = [1675, 2102, 2489, 2898, 3255]
growth_rates = [None, 25.50, 18.40, 16.40, 12.30]  # 2020年无同比增长数据

# 创建双轴
ax2_bar = ax2
ax2_line = ax2.twinx()

# 绘制柱状图（贷款余额）
bars = ax2_bar.bar(range(len(years)), loan_balances, width=0.6, 
                   color='#06A77D', alpha=0.8, edgecolor='black', linewidth=1.2)

# 在柱状图上添加数值标签
for i, (bar, balance) in enumerate(zip(bars, loan_balances)):
    height = bar.get_height()
    ax2_bar.text(bar.get_x() + bar.get_width()/2., height,
                f'{balance}',
                ha='center', va='bottom', fontsize=10, fontweight='bold')

# 绘制折线图（同比增长率）
growth_data = [g for g in growth_rates if g is not None]
growth_indices = [i for i, g in enumerate(growth_rates) if g is not None]
line = ax2_line.plot(growth_indices, growth_data, marker='o', 
                     markersize=8, linewidth=2.5, color='#F18F01', 
                     markerfacecolor='white', markeredgewidth=2, 
                     markeredgecolor='#F18F01', label='同比增长率')

# 在折线上添加数值标签
for i, (idx, rate) in enumerate(zip(growth_indices, growth_data)):
    ax2_line.text(idx, rate, f'{rate:.2f}%',
                  ha='center', va='bottom', fontsize=10, fontweight='bold',
                  bbox=dict(boxstyle='round,pad=0.3', facecolor='white', 
                           edgecolor='#F18F01', linewidth=1.5))

# 设置标签和标题
ax2_bar.set_xlabel('年份', fontsize=12, fontweight='bold')
ax2_bar.set_ylabel('贷款余额（亿元）', fontsize=12, fontweight='bold', color='#06A77D')
ax2_line.set_ylabel('同比增长率（%）', fontsize=12, fontweight='bold', color='#F18F01')
ax2_bar.set_title('2020-2024年贷款规模变化', fontsize=14, fontweight='bold', pad=20)

# 设置x轴刻度
ax2_bar.set_xticks(range(len(years)))
ax2_bar.set_xticklabels(years)

# 添加网格
ax2_bar.grid(True, axis='y', linestyle='--', alpha=0.3)
ax2_line.grid(False)

# 设置y轴颜色
ax2_bar.tick_params(axis='y', labelcolor='#06A77D')
ax2_line.tick_params(axis='y', labelcolor='#F18F01')

# 添加图例
ax2_bar.legend(['贷款余额'], loc='upper left', frameon=True, 
              fancybox=True, shadow=True)
ax2_line.legend(['同比增长率'], loc='upper right', frameon=True, 
               fancybox=True, shadow=True)

# 添加数据分析说明
analysis_text = '数据分析：贷款余额逐年持续增长，从2020年的1675亿元增长至2024年的3255亿元，\n年均复合增长率约为18.1%。同比增长率在2021年达到高点25.5%后呈现下降趋势，\n2024年降至12.3%，反映出本地优质信贷资源趋于饱和。'
fig2.text(0.5, 0.01, analysis_text, ha='center', fontsize=10, 
         style='italic', wrap=True, bbox=dict(boxstyle='round,pad=0.5', 
         facecolor='wheat', alpha=0.3))

plt.tight_layout()
plt.subplots_adjust(bottom=0.25)
plt.savefig('../charts/1_贷款规模变化.png', dpi=300, bbox_inches='tight')
print("图表2已保存：1_贷款规模变化.png")
plt.close()

print("\n所有图表绘制完成！")

