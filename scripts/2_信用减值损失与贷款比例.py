"""
图表绘制脚本：信用减值损失与贷款比例
数据来源：markdowns/2.信用减值损失与贷款比例.md
"""

import matplotlib.pyplot as plt
import numpy as np

from chart_style import set_paper_style

# 统一设置论文风格与中文字体
set_paper_style()

# ========== 图表：信用减值损失、贷款余额与比例（单图展示） ==========
fig, ax_bar = plt.subplots(figsize=(12, 6))
ax_line = ax_bar.twinx()

# 数据
years = ['2020', '2024']
impairment_losses = [27.26, 36.27]  # 亿元
loan_balances = [1675, 3255]  # 亿元
ratios = [1.63, 1.11]  # 百分比

x = np.arange(len(years))
width = 0.35

# --- 柱状图：信用减值损失、贷款余额（左轴：金额） ---
bars1 = ax_bar.bar(
    x - width / 2,
    impairment_losses,
    width,
    label='信用减值损失',
    color='#C73E1D',
    alpha=0.85,
    edgecolor='black',
    linewidth=1.2,
)
bars2 = ax_bar.bar(
    x + width / 2,
    loan_balances,
    width,
    label='贷款余额',
    color='#2E86AB',
    alpha=0.85,
    edgecolor='black',
    linewidth=1.2,
)

# 柱状图数值标签
for bars in (bars1, bars2):
    for bar in bars:
        height = bar.get_height()
        if height > 1000:
            label = f'{height:.0f}'
        else:
            label = f'{height:.2f}'
        ax_bar.text(
            bar.get_x() + bar.get_width() / 2.0,
            height,
            label,
            ha='center',
            va='bottom',
            fontsize=10,
            fontweight='bold',
        )

# --- 折线图：减值损失/贷款比例（右轴：百分比） ---
line = ax_line.plot(
    x,
    ratios,
    marker='o',
    markersize=9,
    linewidth=2.5,
    color='#A23B72',
    markerfacecolor='white',
    markeredgewidth=2.2,
    markeredgecolor='#A23B72',
    label='减值损失/贷款比例',
)

for i, (xi, ratio) in enumerate(zip(x, ratios)):
    ax_line.text(
        xi,
        ratio,
        f'{ratio:.2f}%',
        ha='center',
        va='bottom',
        fontsize=10,
        fontweight='bold',
        bbox=dict(
            boxstyle='round,pad=0.4',
            facecolor='white',
            edgecolor='#A23B72',
            linewidth=1.5,
        ),
    )

# 轴、标题与网格设置
ax_bar.set_xlabel('年份', fontsize=12, fontweight='bold')
ax_bar.set_ylabel('金额（亿元）', fontsize=12, fontweight='bold', color='#2E86AB')
ax_line.set_ylabel('减值损失/贷款比例（%）', fontsize=12, fontweight='bold', color='#A23B72')

ax_bar.set_title('信用减值损失、贷款余额与减值损失/贷款比例', fontsize=14, fontweight='bold', pad=18)

ax_bar.set_xticks(x)
ax_bar.set_xticklabels(years)

ax_bar.grid(True, axis='y', linestyle='--', alpha=0.3)
ax_line.grid(False)

ax_bar.tick_params(axis='y', labelcolor='#2E86AB')
ax_line.tick_params(axis='y', labelcolor='#A23B72')
ax_line.set_ylim(0.8, 1.8)

# 图例（合并柱状和折线）
handles_bar, labels_bar = ax_bar.get_legend_handles_labels()
handles_line, labels_line = ax_line.get_legend_handles_labels()
ax_bar.legend(
    handles_bar + handles_line,
    labels_bar + labels_line,
    loc='upper left',
    frameon=True,
    fancybox=True,
    shadow=True,
)

# 数据分析说明
analysis_text = (
    '数据分析：2024年信用减值损失为36.27亿元，占营业支出的49.4%。\n'
    '减值损失与贷款的比例从2020年的1.63%下降至2024年的1.11%，\n'
    '在贷款余额大幅增长的同时，风险计量和减值计提更加审慎、规范。'
)
fig.text(
    0.5,
    0.02,
    analysis_text,
    ha='center',
    fontsize=10,
    style='italic',
    wrap=True,
    bbox=dict(boxstyle='round,pad=0.5', facecolor='wheat', alpha=0.3),
)

plt.tight_layout()
plt.subplots_adjust(bottom=0.18)
plt.savefig('../charts/2_信用减值损失与贷款比例.png', dpi=300, bbox_inches='tight')
print("图表已保存：2_信用减值损失与贷款比例.png")
plt.close()

print("\n图表绘制完成！")

