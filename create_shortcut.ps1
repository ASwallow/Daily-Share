$ws = New-Object -ComObject WScript.Shell
$shortcut = $ws.CreateShortcut("C:\Users\DELL\Desktop\DailyShare.lnk")
$shortcut.TargetPath = "D:\DailyShare\gui.py"
$shortcut.WorkingDirectory = "D:\DailyShare"
$shortcut.Description = "Daily Share Manager"
$shortcut.Save()
Write-Host "Shortcut created"
