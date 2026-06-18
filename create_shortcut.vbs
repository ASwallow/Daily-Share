Set ws = CreateObject("WScript.Shell")
Set shortcut = ws.CreateShortcut("C:\Users\DELL\Desktop\每日一题管理器.lnk")
shortcut.TargetPath = "D:\DailyShare\gui.py"
shortcut.WorkingDirectory = "D:\DailyShare"
shortcut.Description = "每日一题管理工具"
shortcut.Save
WScript.Echo "快捷方式创建成功！"
