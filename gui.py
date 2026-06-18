# -*- coding: utf-8 -*-
"""
每日一题 - 图形界面
双击运行后可选择：上传新题目 或 更新发布
"""

import os
import sys
import shutil
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from datetime import datetime
from pathlib import Path


# 项目根目录
PROJECT_ROOT = Path(__file__).parent
DAILY_DIR = PROJECT_ROOT / "docs" / "daily"


class DailyShareApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("每日一题管理工具")
        self.root.geometry("400x300")
        self.root.resizable(False, False)

        # 设置图标（如果有的话）
        try:
            self.root.iconbitmap(default="")
        except:
            pass

        self.create_widgets()

    def create_widgets(self):
        # 标题
        title_label = tk.Label(
            self.root,
            text="📝 每日一题",
            font=("Microsoft YaHei", 20, "bold")
        )
        title_label.pack(pady=20)

        # 按钮框架
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=20)

        # 上传文件按钮
        upload_btn = tk.Button(
            button_frame,
            text="📤 上传文件",
            command=self.upload_file,
            width=15,
            height=2,
            font=("Microsoft YaHei", 12),
            bg="#4CAF50",
            fg="white",
            relief=tk.RAISED
        )
        upload_btn.grid(row=0, column=0, padx=20)

        # 更新按钮
        update_btn = tk.Button(
            button_frame,
            text="🔄 更新发布",
            command=self.update_publish,
            width=15,
            height=2,
            font=("Microsoft YaHei", 12),
            bg="#2196F3",
            fg="white",
            relief=tk.RAISED
        )
        update_btn.grid(row=0, column=1, padx=20)

        # 状态栏
        self.status_var = tk.StringVar()
        self.status_var.set("就绪")
        status_label = tk.Label(
            self.root,
            textvariable=self.status_var,
            font=("Microsoft YaHei", 9),
            fg="gray"
        )
        status_label.pack(side=tk.BOTTOM, pady=10)

    def upload_file(self):
        """上传 Markdown 文件到 daily 目录"""
        # 选择文件
        file_path = filedialog.askopenfilename(
            title="选择 Markdown 文件",
            filetypes=[
                ("Markdown 文件", "*.md"),
                ("所有文件", "*.*")
            ]
        )

        if not file_path:
            return

        try:
            file_path = Path(file_path)

            # 检查文件类型
            if file_path.suffix.lower() != '.md':
                messagebox.showerror("错误", "请选择 .md 文件！")
                return

            # 如果文件名是日期格式，直接使用；否则用当前日期
            stem = file_path.stem
            if len(stem) == 10 and stem[4] == '-' and stem[7] == '-':
                # 看起来是日期格式 (YYYY-MM-DD)
                new_name = f"{stem}.md"
            else:
                # 使用当前日期
                today = datetime.now().strftime("%Y-%m-%d")
                new_name = f"{today}.md"

            # 目标路径
            target_path = DAILY_DIR / new_name

            # 检查是否已存在
            if target_path.exists():
                if not messagebox.askyesno("确认", f"文件 {new_name} 已存在，是否覆盖？"):
                    return

            # 复制文件
            shutil.copy2(file_path, target_path)

            self.status_var.set(f"已上传: {new_name}")
            messagebox.showinfo("成功", f"文件已上传到:\n{target_path}")

        except Exception as e:
            messagebox.showerror("错误", f"上传失败:\n{str(e)}")

    def update_publish(self):
        """Git add, commit, push"""
        try:
            self.status_var.set("正在更新...")
            self.root.update()

            # 检查是否是 git 仓库
            git_dir = PROJECT_ROOT / ".git"
            if not git_dir.exists():
                messagebox.showerror(
                    "错误",
                    "项目还未初始化 Git 仓库！\n\n请先运行：\n"
                    "cd D:\\DailyShare\n"
                    "git init\n"
                    "git add .\n"
                    "git commit -m '初始化'\n"
                    "git remote add origin <你的仓库地址>\n"
                    "git push -u origin main"
                )
                self.status_var.set("Git 未初始化")
                return

            # 检查是否有变更
            result = subprocess.run(
                ["git", "status", "--porcelain"],
                cwd=PROJECT_ROOT,
                capture_output=True,
                text=True
            )

            if not result.stdout.strip():
                messagebox.showinfo("提示", "没有需要提交的变更")
                self.status_var.set("没有变更")
                return

            # Git add
            subprocess.run(
                ["git", "add", "."],
                cwd=PROJECT_ROOT,
                check=True
            )

            # Git commit
            today = datetime.now().strftime("%Y-%m-%d %H:%M")
            subprocess.run(
                ["git", "commit", "-m", f"更新题目 {today}"],
                cwd=PROJECT_ROOT,
                check=True
            )

            # Git push
            subprocess.run(
                ["git", "push"],
                cwd=PROJECT_ROOT,
                check=True
            )

            self.status_var.set("更新成功！")
            messagebox.showinfo("成功", "已成功推送到 GitHub！\n\n网站将在 1-2 分钟后自动更新。")

        except subprocess.CalledProcessError as e:
            error_msg = f"操作失败:\n{e.stderr if e.stderr else str(e)}"
            messagebox.showerror("错误", error_msg)
            self.status_var.set("更新失败")
        except Exception as e:
            messagebox.showerror("错误", f"发生错误:\n{str(e)}")
            self.status_var.set("更新失败")

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = DailyShareApp()
    app.run()
