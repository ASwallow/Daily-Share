$ws = New-Object -ComObject WScript.Shell
$shortcut = $ws.CreateShortcut("C:\Users\DELL\Desktop\Daily Manager.lnk")
$shortcut.TargetPath = "pythonw.exe"
$shortcut.Arguments = "D:\DailyShare\gui.py"
$shortcut.WorkingDirectory = "D:\DailyShare"
$shortcut.Description = "Daily Share Manager"
$shortcut.WindowStyle = 7
$shortcut.Save()
Write-Host "Done"
