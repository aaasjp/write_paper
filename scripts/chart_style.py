"""
统一的论文风格图表样式配置。
"""

import matplotlib.pyplot as plt
from matplotlib import rcParams


def set_paper_style():
    """设置统一的论文风格和中文字体。"""
    # 中文字体与负号
    plt.rcParams['font.sans-serif'] = ['SimHei', 'Arial Unicode MS', 'DejaVu Sans']
    plt.rcParams['axes.unicode_minus'] = False

    # 统一论文风格
    rcParams['figure.figsize'] = (12, 6)
    rcParams['figure.dpi'] = 300
    rcParams['savefig.dpi'] = 300
    rcParams['savefig.bbox'] = 'tight'
    rcParams['font.size'] = 11
    rcParams['axes.linewidth'] = 1.2
    rcParams['grid.linewidth'] = 0.8
    rcParams['grid.alpha'] = 0.3


