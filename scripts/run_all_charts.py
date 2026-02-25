"""
统一执行所有图表绘制脚本。
运行本脚本前，请确保已安装 matplotlib、numpy 等依赖。

功能：
1. 先清空上一次生成的 charts 目录内容；
2. 依次执行当前目录下的各个绘图脚本，重新生成所有图表。
"""

import os
import shutil
import runpy
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
CHARTS_DIR = BASE_DIR.parent / "charts"

# 需要统一执行的绘图脚本（按论文结构顺序）
PLOT_SCRIPTS = [
    "1_资产负债项目和贷款规模变化.py",
    "2_信用减值损失与贷款比例.py",
    "3_资本管理与补充机制的探索实践.py",
    "4_风险管理问题-区域经济依赖性强.py",
    "5_风险管理问题-资本补充渠道狭窄.py",
]


def clear_charts_dir() -> None:
    """清空 charts 目录下原有的图表文件。"""
    CHARTS_DIR.mkdir(parents=True, exist_ok=True)

    for item in CHARTS_DIR.iterdir():
        if item.is_file() or item.is_symlink():
            item.unlink()
        elif item.is_dir():
            shutil.rmtree(item)

    print(f"已清空目录：{CHARTS_DIR}")


def run_all_scripts() -> None:
    """依次执行所有绘图脚本。"""
    for script_name in PLOT_SCRIPTS:
        script_path = BASE_DIR / script_name
        if not script_path.exists():
            print(f"跳过：未找到脚本 {script_path}")
            continue

        print(f"\n====== 开始执行脚本：{script_name} ======")
        # 使用 runpy 在当前进程中执行脚本，等价于直接运行该 .py 文件
        runpy.run_path(str(script_path), run_name="__main__")
        print(f"====== 完成脚本：{script_name} ======")


if __name__ == "__main__":
    clear_charts_dir()
    run_all_scripts()
    print("\n所有图表已重新生成，保存在 charts 目录中。")


