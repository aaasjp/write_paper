"""
图表绘制脚本：资本管理与补充机制的探索实践
数据来源：markdowns/3.资本管理与补充机制的探索实践.md
"""

import matplotlib.pyplot as plt
import numpy as np

from chart_style import set_paper_style

# 统一设置论文风格与中文字体
set_paper_style()

# ========== 图表：资本管理相关指标变化 ==========
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 10))

# 数据
years = ['2020', '2024']
undistributed_profit = [53.08, 103.0]  # 未分配利润（亿元）
owner_equity = [334.5, 483.4]  # 所有者权益（亿元）
share_capital = [41.23, 48.35]  # 股本（亿元）
bonds_payable = [None, 875.2]  # 应付债券（亿元，仅2024年有数据）
bonds_ratio = [None, 13.7]  # 应付债券占总负债比例（%，仅2024年有数据）

# ========== 子图1：未分配利润变化 ==========
bars1 = ax1.bar(years, undistributed_profit, width=0.5, color='#06A77D', 
                alpha=0.8, edgecolor='black', linewidth=1.2)
for bar, value in zip(bars1, undistributed_profit):
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2., height,
            f'{value:.2f}',
            ha='center', va='bottom', fontsize=10, fontweight='bold')
ax1.set_ylabel('金额（亿元）', fontsize=12, fontweight='bold')
ax1.set_title('未分配利润变化', fontsize=13, fontweight='bold', pad=15)
ax1.grid(True, axis='y', linestyle='--', alpha=0.3)
# 计算增长率
growth_rate = ((undistributed_profit[1] - undistributed_profit[0]) / undistributed_profit[0]) * 100
ax1.text(0.5, 0.95, f'增长率：{growth_rate:.1f}%', transform=ax1.transAxes,
         ha='center', va='top', fontsize=10, bbox=dict(boxstyle='round', 
         facecolor='wheat', alpha=0.5))

# ========== 子图2：所有者权益变化 ==========
bars2 = ax2.bar(years, owner_equity, width=0.5, color='#2E86AB', 
                alpha=0.8, edgecolor='black', linewidth=1.2)
for bar, value in zip(bars2, owner_equity):
    height = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2., height,
            f'{value:.1f}',
            ha='center', va='bottom', fontsize=10, fontweight='bold')
ax2.set_ylabel('金额（亿元）', fontsize=12, fontweight='bold')
ax2.set_title('所有者权益变化', fontsize=13, fontweight='bold', pad=15)
ax2.grid(True, axis='y', linestyle='--', alpha=0.3)
# 计算增长率
growth_rate = ((owner_equity[1] - owner_equity[0]) / owner_equity[0]) * 100
ax2.text(0.5, 0.95, f'增长率：{growth_rate:.1f}%', transform=ax2.transAxes,
         ha='center', va='top', fontsize=10, bbox=dict(boxstyle='round', 
         facecolor='wheat', alpha=0.5))

# ========== 子图3：股本变化 ==========
bars3 = ax3.bar(years, share_capital, width=0.5, color='#F18F01', 
                alpha=0.8, edgecolor='black', linewidth=1.2)
for bar, value in zip(bars3, share_capital):
    height = bar.get_height()
    ax3.text(bar.get_x() + bar.get_width()/2., height,
            f'{value:.2f}',
            ha='center', va='bottom', fontsize=10, fontweight='bold')
ax3.set_ylabel('金额（亿元）', fontsize=12, fontweight='bold')
ax3.set_xlabel('年份', fontsize=12, fontweight='bold')
ax3.set_title('股本变化', fontsize=13, fontweight='bold', pad=15)
ax3.grid(True, axis='y', linestyle='--', alpha=0.3)
# 计算增长率
growth_rate = ((share_capital[1] - share_capital[0]) / share_capital[0]) * 100
ax3.text(0.5, 0.95, f'增长率：{growth_rate:.1f}%', transform=ax3.transAxes,
         ha='center', va='top', fontsize=10, bbox=dict(boxstyle='round', 
         facecolor='wheat', alpha=0.5))

# ========== 子图4：应付债券（2024年） ==========
# 只显示2024年的数据
ax4.bar(['2024'], [bonds_payable[1]], width=0.5, color='#A23B72', 
        alpha=0.8, edgecolor='black', linewidth=1.2)
ax4.text(0, bonds_payable[1], f'{bonds_payable[1]:.1f}',
         ha='center', va='bottom', fontsize=10, fontweight='bold')
ax4.set_ylabel('金额（亿元）', fontsize=12, fontweight='bold')
ax4.set_xlabel('年份', fontsize=12, fontweight='bold')
ax4.set_title('应付债券余额（2024年）', fontsize=13, fontweight='bold', pad=15)
ax4.grid(True, axis='y', linestyle='--', alpha=0.3)
# 添加占比信息
ax4.text(0.5, 0.95, f'占总负债比例：{bonds_ratio[1]:.1f}%', transform=ax4.transAxes,
         ha='center', va='top', fontsize=10, bbox=dict(boxstyle='round', 
         facecolor='wheat', alpha=0.5))

# 添加整体标题
fig.suptitle('资本管理与补充机制相关指标变化', fontsize=16, fontweight='bold', y=0.98)

# 添加数据分析说明
analysis_text = '数据分析：银行注重留存收益对资本的补充作用，未分配利润从2020年的53.08亿元增长至2024年的103.0亿元，\n所有者权益从2020年的334.5亿元增长至2024年的483.4亿元。股本从2020年的41.23亿元增长至2024年的48.35亿元。\n银行还探索发行二级资本债优化资本结构，截至2024年末，应付债券余额为875.2亿元，占总负债的13.7%。'
fig.text(0.5, 0.01, analysis_text, ha='center', fontsize=10, 
         style='italic', wrap=True, bbox=dict(boxstyle='round,pad=0.5', 
         facecolor='wheat', alpha=0.3))

plt.tight_layout()
plt.subplots_adjust(top=0.93, bottom=0.12)
plt.savefig('../charts/3_资本管理与补充机制的探索实践.png', dpi=300, bbox_inches='tight')
print("图表已保存：3_资本管理与补充机制的探索实践.png")
plt.close()

print("\n图表绘制完成！")

