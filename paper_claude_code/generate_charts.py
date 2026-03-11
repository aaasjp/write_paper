#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
生成邯郸银行信用风险管理分析图表
"""

import matplotlib.pyplot as plt
import matplotlib
import numpy as np

# 设置中文字体
matplotlib.rcParams['font.sans-serif'] = ['SimHei', 'Arial Unicode MS', 'DejaVu Sans']
matplotlib.rcParams['axes.unicode_minus'] = False

# 数据准备
years = ['2020', '2021', '2022', '2023', '2024']

# 资产和贷款数据（亿元）
total_assets = [1809, 2024, 2224, 2309, 2492]
loan_balance = [760, 969, 1185, 1252, 1385]

# 不良贷款率和关注类贷款占比
npl_ratio = [1.90, 1.96, 1.90, 2.24, 1.38]
concern_ratio = [3.54, 4.60, 8.04, 10.07, 8.90]

# 拨备覆盖率和资本充足率
provision_coverage = [175.63, 182.26, 154.73, 136.84, 204.35]
capital_adequacy = [11.22, 13.15, 12.91, 13.07, 13.88]
core_capital_adequacy = [8.64, 9.33, 9.67, 9.92, 10.65]

# 行业分布数据（2024年）
industries = ['制造业', '批发和零售业', '建筑业', '租赁和商务服务业',
              '交通运输仓储邮政', '房地产业', '电力热力及水', '采矿业', '其他']
industry_ratio_2024 = [25.31, 12.45, 9.73, 7.22, 4.56, 3.59, 3.46, 2.41, 31.27]
industry_ratio_2020 = [28.33, 20.13, 4.67, 5.27, 3.85, 7.03, 2.93, 2.90, 24.89]

# 创建输出目录
import os
output_dir = 'charts_paper'
os.makedirs(output_dir, exist_ok=True)

# 图1：总资产和贷款余额增长（柱状图+折线图）
fig, ax1 = plt.subplots(figsize=(10, 6))
x = np.arange(len(years))
width = 0.35

bars1 = ax1.bar(x - width/2, total_assets, width, label='总资产（亿元）', color='#4472C4')
bars2 = ax1.bar(x + width/2, loan_balance, width, label='贷款余额（亿元）', color='#ED7D31')

ax1.set_xlabel('年份', fontsize=12)
ax1.set_ylabel('金额（亿元）', fontsize=12)
ax1.set_xticks(x)
ax1.set_xticklabels(years)
ax1.legend(loc='upper left')
ax1.set_title('邯郸银行2020-2024年资产与贷款规模增长', fontsize=14, fontweight='bold')

# 添加数据标签
for bar in bars1:
    height = bar.get_height()
    ax1.annotate(f'{height}', xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontsize=9)
for bar in bars2:
    height = bar.get_height()
    ax1.annotate(f'{height}', xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontsize=9)

plt.tight_layout()
plt.savefig(f'{output_dir}/chart1_assets_loans.png', dpi=150, bbox_inches='tight')
plt.close()
print("图1已生成: chart1_assets_loans.png")

# 图2：不良贷款率变化趋势（折线图）
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(years, npl_ratio, marker='o', linewidth=2, markersize=10, color='#C00000', label='不良贷款率(%)')
ax.plot(years, concern_ratio, marker='s', linewidth=2, markersize=10, color='#FF6600', label='关注类贷款占比(%)')

ax.set_xlabel('年份', fontsize=12)
ax.set_ylabel('比例（%）', fontsize=12)
ax.set_title('邯郸银行2020-2024年不良贷款率与关注类贷款占比变化', fontsize=14, fontweight='bold')
ax.legend(loc='upper right')
ax.grid(True, linestyle='--', alpha=0.7)
ax.set_ylim(0, 12)

# 添加数据标签
for i, (npl, con) in enumerate(zip(npl_ratio, concern_ratio)):
    ax.annotate(f'{npl}%', xy=(i, npl), xytext=(0, 10), textcoords="offset points",
               ha='center', fontsize=9, color='#C00000')
    ax.annotate(f'{con}%', xy=(i, con), xytext=(0, 10), textcoords="offset points",
               ha='center', fontsize=9, color='#FF6600')

plt.tight_layout()
plt.savefig(f'{output_dir}/chart2_npl_trend.png', dpi=150, bbox_inches='tight')
plt.close()
print("图2已生成: chart2_npl_trend.png")

# 图3：拨备覆盖率与资本充足率（双轴折线图）
fig, ax1 = plt.subplots(figsize=(10, 6))

color1 = '#4472C4'
ax1.set_xlabel('年份', fontsize=12)
ax1.set_ylabel('拨备覆盖率（%）', color=color1, fontsize=12)
line1 = ax1.plot(years, provision_coverage, marker='o', linewidth=2, markersize=10,
                 color=color1, label='拨备覆盖率(%)')
ax1.tick_params(axis='y', labelcolor=color1)
ax1.set_ylim(100, 250)

ax2 = ax1.twinx()
color2 = '#70AD47'
ax2.set_ylabel('资本充足率（%）', color=color2, fontsize=12)
line2 = ax2.plot(years, capital_adequacy, marker='s', linewidth=2, markersize=10,
                 color=color2, label='资本充足率(%)')
line3 = ax2.plot(years, core_capital_adequacy, marker='^', linewidth=2, markersize=10,
                 color='#FFC000', label='核心一级资本充足率(%)')
ax2.tick_params(axis='y', labelcolor=color2)
ax2.set_ylim(7, 16)

ax1.set_title('邯郸银行2020-2024年拨备覆盖率与资本充足率变化', fontsize=14, fontweight='bold')

# 合并图例
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left')

ax1.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig(f'{output_dir}/chart3_provision_capital.png', dpi=150, bbox_inches='tight')
plt.close()
print("图3已生成: chart3_provision_capital.png")

# 图4：行业贷款分布饼图（2024年）
fig, ax = plt.subplots(figsize=(10, 8))
colors = ['#4472C4', '#ED7D31', '#A5A5A5', '#FFC000', '#5B9BD5',
          '#70AD47', '#264478', '#9E480E', '#636363']

# 合并其他行业
explode = (0.05, 0.02, 0.02, 0, 0, 0.02, 0, 0, 0)
wedges, texts, autotexts = ax.pie(industry_ratio_2024, explode=explode, labels=industries,
                                   colors=colors, autopct='%1.1f%%', startangle=90,
                                   pctdistance=0.75)

ax.set_title('邯郸银行2024年贷款行业分布', fontsize=14, fontweight='bold')

# 调整字体
for text in texts:
    text.set_fontsize(10)
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontsize(9)
    autotext.set_weight('bold')

plt.tight_layout()
plt.savefig(f'{output_dir}/chart4_industry_2024.png', dpi=150, bbox_inches='tight')
plt.close()
print("图4已生成: chart4_industry_2024.png")

# 图5：行业集中度变化（堆积柱状图）
fig, ax = plt.subplots(figsize=(10, 6))

x = np.arange(len(years))
width = 0.15

# 2020-2024年各行业数据
manufacturing = [28.33, 28.50, 24.77, 25.24, 25.31]
wholesale = [20.13, 17.02, 14.86, 15.39, 12.45]
construction = [4.67, 6.15, 7.44, 9.17, 9.73]
real_estate = [7.03, 5.57, 5.17, 4.13, 3.59]

ax.bar(x - 1.5*width, manufacturing, width, label='制造业', color='#4472C4')
ax.bar(x - 0.5*width, wholesale, width, label='批发和零售业', color='#ED7D31')
ax.bar(x + 0.5*width, construction, width, label='建筑业', color='#A5A5A5')
ax.bar(x + 1.5*width, real_estate, width, label='房地产业', color='#70AD47')

ax.set_xlabel('年份', fontsize=12)
ax.set_ylabel('占比（%）', fontsize=12)
ax.set_xticks(x)
ax.set_xticklabels(years)
ax.set_title('邯郸银行2020-2024年主要行业贷款占比变化', fontsize=14, fontweight='bold')
ax.legend(loc='upper right')
ax.grid(True, linestyle='--', alpha=0.7, axis='y')

plt.tight_layout()
plt.savefig(f'{output_dir}/chart5_industry_change.png', dpi=150, bbox_inches='tight')
plt.close()
print("图5已生成: chart5_industry_change.png")

# 图6：贷款五级分类变化（堆积面积图）
fig, ax = plt.subplots(figsize=(10, 6))

# 数据
normal = [94.56, 93.44, 90.05, 87.69, 89.72]
concern = [3.54, 4.60, 8.04, 10.07, 8.90]
substandard = [0.06, 0.06, 0.57, 0.58, 0.68]
doubtful = [1.72, 1.85, 1.29, 1.64, 0.69]
loss = [0.12, 0.05, 0.05, 0.02, 0.02]

ax.stackplot(years, normal, concern, substandard, doubtful, loss,
             labels=['正常类', '关注类', '次级类', '可疑类', '损失类'],
             colors=['#70AD47', '#FFC000', '#FF6600', '#C00000', '#7030A0'],
             alpha=0.8)

ax.set_xlabel('年份', fontsize=12)
ax.set_ylabel('占比（%）', fontsize=12)
ax.set_title('邯郸银行2020-2024年贷款五级分类结构变化', fontsize=14, fontweight='bold')
ax.legend(loc='upper right')
ax.set_ylim(0, 110)
ax.grid(True, linestyle='--', alpha=0.7, axis='y')

plt.tight_layout()
plt.savefig(f'{output_dir}/chart6_loan_classification.png', dpi=150, bbox_inches='tight')
plt.close()
print("图6已生成: chart6_loan_classification.png")

# 图7：AI技术在银行风险管理中的应用架构图
fig, ax = plt.subplots(figsize=(12, 8))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')

# 标题
ax.text(5, 9.5, '大模型时代AI技术在银行风险管理中的应用框架', ha='center', fontsize=16, fontweight='bold')

# 边框
rect = plt.Rectangle((0.5, 0.5), 9, 8.5, fill=False, edgecolor='#4472C4', linewidth=2)
ax.add_patch(rect)

# 数据层
ax.add_patch(plt.Rectangle((1, 7), 2.5, 1.2, facecolor='#D9E1F2', edgecolor='#4472C4', linewidth=1.5))
ax.text(2.25, 7.6, '数据层', ha='center', fontsize=11, fontweight='bold')
ax.text(2.25, 7.25, '征信/税务/工商\n法院/舆情', ha='center', fontsize=9)

# 技术层
ax.add_patch(plt.Rectangle((3.75, 7), 2.5, 1.2, facecolor='#E2EFDA', edgecolor='#70AD47', linewidth=1.5))
ax.text(5, 7.6, '技术层', ha='center', fontsize=11, fontweight='bold')
ax.text(5, 7.25, '机器学习/知识图谱\nNLP/深度学习', ha='center', fontsize=9)

# 应用层
ax.add_patch(plt.Rectangle((6.5, 7), 2.5, 1.2, facecolor='#FCE4D6', edgecolor='#ED7D31', linewidth=1.5))
ax.text(7.75, 7.6, '应用层', ha='center', fontsize=11, fontweight='bold')
ax.text(7.75, 7.25, '智能风控/预警\n授信评估/催收', ha='center', fontsize=9)

# 智能风控模块
ax.add_patch(plt.Rectangle((1, 4.8), 4, 1.8, facecolor='#FFF2CC', edgecolor='#FFC000', linewidth=1.5))
ax.text(3, 6.3, '智能风控系统', ha='center', fontsize=12, fontweight='bold')
ax.text(3, 5.8, '• 智能评级模型    • 大数据画像', fontsize=9)
ax.text(3, 5.35, '• 实时风险预警    • 反欺诈检测', fontsize=9)

# 风险管理流程
ax.add_patch(plt.Rectangle((5.25, 4.8), 4, 1.8, facecolor='#F8CBAD', edgecolor='#C00000', linewidth=1.5))
ax.text(7.25, 6.3, '风险管理流程', ha='center', fontsize=12, fontweight='bold')
ax.text(7.25, 5.8, '• 贷前智能筛查    • 贷中动态管控', fontsize=9)
ax.text(7.25, 5.35, '• 贷后敏捷响应    • 全流程留痕', fontsize=9)

# 效果提升
ax.add_patch(plt.Rectangle((1, 2.5), 4, 1.8, facecolor='#C6E0B4', edgecolor='#548235', linewidth=1.5))
ax.text(3, 4, '效果提升', ha='center', fontsize=12, fontweight='bold')
ax.text(3, 3.5, '• 风险识别效率提升50%+', fontsize=9)
ax.text(3, 3.1, '• 预警响应时间缩短80%', fontsize=9)
ax.text(3, 2.7, '• 人工成本降低30%', fontsize=9)

# 保障体系
ax.add_patch(plt.Rectangle((5.25, 2.5), 4, 1.8, facecolor='#B4C7E7', edgecolor='#2F5597', linewidth=1.5))
ax.text(7.25, 4, '保障体系', ha='center', fontsize=12, fontweight='bold')
ax.text(7.25, 3.5, '• 数据安全合规    • 模型可解释性', fontsize=9)
ax.text(7.25, 3.1, '• 持续模型迭代    • 人才队伍建设', fontsize=9)
ax.text(7.25, 2.7, '• 监管沙盒测试', fontsize=9)

# 箭头连接
ax.annotate('', xy=(5, 6.2), xytext=(3, 6.2), arrowprops=dict(arrowstyle='->', color='#4472C4', lw=1.5))

plt.tight_layout()
plt.savefig(f'{output_dir}/chart7_ai_framework.png', dpi=150, bbox_inches='tight')
plt.close()
print("图7已生成: chart7_ai_framework.png")

# 图8：AI技术应用效果对比
fig, ax = plt.subplots(figsize=(10, 6))

categories = ['风险识别\n准确率', '预警响应\n时效', '人工审核\n效率', '客户画像\n维度', '违约预测\n精度']
traditional = [65, 40, 50, 30, 60]
ai_enhanced = [92, 95, 88, 85, 88]

x = np.arange(len(categories))
width = 0.35

bars1 = ax.bar(x - width/2, traditional, width, label='传统风控', color='#A5A5A5')
bars2 = ax.bar(x + width/2, ai_enhanced, width, label='AI智能风控', color='#4472C4')

ax.set_ylabel('评分/效率（%）', fontsize=12)
ax.set_title('传统风控 vs AI智能风控效果对比', fontsize=14, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(categories)
ax.legend()
ax.set_ylim(0, 110)
ax.grid(True, linestyle='--', alpha=0.7, axis='y')

# 添加数据标签
for bar in bars1:
    height = bar.get_height()
    ax.annotate(f'{height}%', xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontsize=10)
for bar in bars2:
    height = bar.get_height()
    ax.annotate(f'{height}%', xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontsize=10)

plt.tight_layout()
plt.savefig(f'{output_dir}/chart8_ai_comparison.png', dpi=150, bbox_inches='tight')
plt.close()
print("图8已生成: chart8_ai_comparison.png")

print("\n所有图表已生成完成！")
print(f"图表保存在: {output_dir}/ 目录")