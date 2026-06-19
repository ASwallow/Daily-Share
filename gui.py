# -*- coding: utf-8 -*-
"""
每日一题 - 图形界面管理工具
功能：上传题目（PDF+Markdown）、按日期组织、打开Obsidian、推送到GitHub
"""

import os
import sys
import shutil
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from datetime import datetime
from pathlib import Path


# 项目配置
PROJECT_ROOT = Path(__file__).parent
GITHUB_REPO = "https://github.com/ASwallow/Daily-Share.git"
DAILY_DIR = PROJECT_ROOT / "daily"


class DailyShareApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("每日一题管理工具")
        self.root.geometry("500x400")
        self.root.resizable(False, False)

        # 设置图标
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
            font=("Microsoft YaHei", 24, "bold")
        )
        title_label.pack(pady=15)

        # 说明
        desc_label = tk.Label(
            self.root,
            text="分享遇到的题目，督促自己保持练习",
            font=("Microsoft YaHei", 10),
            fg="gray"
        )
        desc_label.pack(pady=5)

        # 按钮框架
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=20)

        # 上传题目按钮
        upload_btn = tk.Button(
            button_frame,
            text="📤 上传题目",
            command=self.upload_question,
            width=18,
            height=2,
            font=("Microsoft YaHei", 12),
            bg="#4CAF50",
            fg="white",
            relief=tk.RAISED,
            cursor="hand2"
        )
        upload_btn.grid(row=0, column=0, padx=15, pady=10)

        # 打开Obsidian按钮
        obsidian_btn = tk.Button(
            button_frame,
            text="📖 打开 Obsidian",
            command=self.open_obsidian,
            width=18,
            height=2,
            font=("Microsoft YaHei", 12),
            bg="#9C27B0",
            fg="white",
            relief=tk.RAISED,
            cursor="hand2"
        )
        obsidian_btn.grid(row=0, column=1, padx=15, pady=10)

        # 提交到GitHub按钮
        push_btn = tk.Button(
            button_frame,
            text="🚀 提交到 GitHub",
            command=self.push_to_github,
            width=18,
            height=2,
            font=("Microsoft YaHei", 12),
            bg="#2196F3",
            fg="white",
            relief=tk.RAISED,
            cursor="hand2"
        )
        push_btn.grid(row=1, column=0, padx=15, pady=10)

        # 打开文件夹按钮
        folder_btn = tk.Button(
            button_frame,
            text="📁 打开题目文件夹",
            command=self.open_folder,
            width=18,
            height=2,
            font=("Microsoft YaHei", 12),
            bg="#FF9800",
            fg="white",
            relief=tk.RAISED,
            cursor="hand2"
        )
        folder_btn.grid(row=1, column=1, padx=15, pady=10)

        # 状态栏
        self.status_var = tk.StringVar()
        self.status_var.set("就绪 - 欢迎使用每日一题管理工具")
        status_label = tk.Label(
            self.root,
            textvariable=self.status_var,
            font=("Microsoft YaHei", 9),
            fg="gray",
            wraplength=450
        )
        status_label.pack(side=tk.BOTTOM, pady=10)

    def get_today_folder(self):
        """获取今天的日期文件夹路径"""
        today = datetime.now()
        return DAILY_DIR / f"{today.year}.{today.month}.{today.day}"

    def upload_question(self):
        """上传题目 - 支持同时选择PDF和Markdown文件"""
        # 选择文件（支持多选）
        file_paths = filedialog.askopenfilenames(
            title="选择题目文件（可同时选择PDF和Markdown）",
            filetypes=[
                ("题目文件", "*.md *.pdf"),
                ("Markdown", "*.md"),
                ("PDF", "*.pdf"),
                ("所有文件", "*.*")
            ]
        )

        if not file_paths:
            return

        try:
            # 获取今天的日期文件夹
            today_folder = self.get_today_folder()
            today_folder.mkdir(parents=True, exist_ok=True)

            uploaded_files = []

            for file_path in file_paths:
                file_path = Path(file_path)

                # 复制文件到日期文件夹
                target_path = today_folder / file_path.name

                # 检查是否已存在
                if target_path.exists():
                    if not messagebox.askyesno("确认", f"文件 {file_path.name} 已存在，是否覆盖？"):
                        continue

                shutil.copy2(file_path, target_path)
                uploaded_files.append(file_path.name)

            if uploaded_files:
                self.status_var.set(f"已上传 {len(uploaded_files)} 个文件到 {today_folder.name}")
                messagebox.showinfo(
                    "上传成功",
                    f"已上传到: {today_folder}\n\n文件列表:\n" + "\n".join(uploaded_files)
                )

        except Exception as e:
            messagebox.showerror("错误", f"上传失败:\n{str(e)}")
            self.status_var.set("上传失败")

    def open_obsidian(self):
        """打开Obsidian编辑器"""
        try:
            # 尝试多种方式打开Obsidian
            obsidian_opened = False

            # 方式1：通过obsidian://协议打开
            try:
                # Windows上使用start命令打开obsidian协议
                subprocess.Popen(
                    ["cmd", "/c", "start", f"obsidian://open?vault={PROJECT_ROOT.name}"],
                    shell=True
                )
                obsidian_opened = True
            except:
                pass

            # 方式2：直接打开Obsidian应用
            if not obsidian_opened:
                try:
                    # 尝试常见的Obsidian安装路径
                    possible_paths = [
                        Path(os.environ.get("LOCALAPPDATA", "")) / "Obsidian" / "Obsidian.exe",
                        Path(os.environ.get("PROGRAMFILES", "")) / "Obsidian" / "Obsidian.exe",
                        Path(os.environ.get("PROGRAMFILES(X86)", "")) / "Obsidian" / "Obsidian.exe",
                    ]

                    for obsidian_path in possible_paths:
                        if obsidian_path.exists():
                            subprocess.Popen([str(obsidian_path)])
                            obsidian_opened = True
                            break
                except:
                    pass

            # 方式3：使用系统默认方式打开
            if not obsidian_opened:
                try:
                    os.startfile(str(PROJECT_ROOT))
                    obsidian_opened = True
                except:
                    pass

            if obsidian_opened:
                self.status_var.set("正在打开 Obsidian...")
            else:
                messagebox.showwarning(
                    "提示",
                    "无法自动打开Obsidian，请手动打开。\n\n"
                    f"项目路径: {PROJECT_ROOT}"
                )

        except Exception as e:
            messagebox.showerror("错误", f"打开Obsidian失败:\n{str(e)}")

    def push_to_github(self):
        """提交并推送到GitHub"""
        try:
            self.status_var.set("正在提交到GitHub...")
            self.root.update()

            # 检查是否是git仓库
            git_dir = PROJECT_ROOT / ".git"
            if not git_dir.exists():
                # 初始化git仓库
                if messagebox.askyesno("初始化Git", "项目还未初始化Git仓库，是否初始化？"):
                    subprocess.run(["git", "init"], cwd=PROJECT_ROOT, check=True)
                    subprocess.run(
                        ["git", "remote", "add", "origin", GITHUB_REPO],
                        cwd=PROJECT_ROOT,
                        check=True
                    )
                else:
                    self.status_var.set("已取消")
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
            subprocess.run(["git", "add", "."], cwd=PROJECT_ROOT, check=True)

            # Git commit
            today = datetime.now().strftime("%Y-%m-%d %H:%M")
            subprocess.run(
                ["git", "commit", "-m", f"更新题目 {today}"],
                cwd=PROJECT_ROOT,
                check=True
            )

            # Git push
            self.status_var.set("正在推送到GitHub...")
            self.root.update()

            # 尝试push，如果失败则尝试设置上游分支
            result = subprocess.run(
                ["git", "push"],
                cwd=PROJECT_ROOT,
                capture_output=True,
                text=True
            )

            if result.returncode != 0:
                # 尝试设置上游分支
                subprocess.run(
                    ["git", "push", "-u", "origin", "main"],
                    cwd=PROJECT_ROOT,
                    check=True
                )

            self.status_var.set("提交成功！")
            messagebox.showinfo(
                "成功",
                "已成功推送到 GitHub！\n\n"
                f"仓库地址: {GITHUB_REPO}\n"
                "网站将在 1-2 分钟后自动更新。"
            )

        except subprocess.CalledProcessError as e:
            error_msg = f"操作失败:\n{e.stderr if e.stderr else str(e)}"
            messagebox.showerror("错误", error_msg)
            self.status_var.set("提交失败")
        except Exception as e:
            messagebox.showerror("错误", f"发生错误:\n{str(e)}")
            self.status_var.set("提交失败")

    def open_folder(self):
        """打开题目文件夹"""
        try:
            # 如果daily文件夹不存在，创建它
            if not DAILY_DIR.exists():
                DAILY_DIR.mkdir(parents=True, exist_ok=True)

            os.startfile(str(DAILY_DIR))
            self.status_var.set("已打开题目文件夹")
        except Exception as e:
            messagebox.showerror("错误", f"打开文件夹失败:\n{str(e)}")

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = DailyShareApp()
    app.run()
