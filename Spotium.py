try:
    from tkinter import *
    import time
    import os
    import tempfile
    import sys
    import urllib.request
    import requests
    import ctypes
    import subprocess
    from sys import exit
except ModuleNotFoundError:
    import ctypes
    from sys import exit
    ctypes.windll.user32.MessageBoxW(0, "Spotium could not start because it could not find the required modules.", "Spotium", 0x40000)
    exit()
try:
    USER_NAME = os.getlogin()
    logpath = "C:/Users/" + USER_NAME + "/AppData/Roaming/Spotium/spotiumlog.txt"
    localpath = "C:/Users/" + USER_NAME + "/AppData/Local/Spotium"
    VERSION = '2.3.8'
    dstpath = "C:/Users/" + USER_NAME + "/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup"
    global loading, spotifytype, loadinginfo, exitallowed, denystepping, setuprun
    loading = True
    spotifytype = 0
    loadinginfo = False
    exitallowed = False
    denystepping = False
    setuprun = False
    def resource_path(relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, "menu", relative_path)
    if os.path.exists(tempfile.gettempdir() + '/Spotifysetup.exe'):
        os.remove(tempfile.gettempdir() + '/Spotifysetup.exe')
    if not os.path.exists(localpath):
        os.mkdir(localpath)
    if not os.path.exists("C:/Users/" + USER_NAME + "/AppData/Roaming/Spotium"):
        os.mkdir("C:/Users/" + USER_NAME + "/AppData/Roaming/Spotium")
    if not os.path.exists(localpath + '/data.spotium'):
        with open(localpath + '/data.spotium', 'w') as f:
            f.write('@nxkclvd89rt4uy38r952789rj23')
            f.close()
    def on_drag(event):
        if not window.winfo_containing(event.x_root, event.y_root).winfo_class() == "Button":
            x = window.winfo_pointerx() - window._offsetx
            y = window.winfo_pointery() - window._offsety
            window.geometry(f"+{x}+{y}")
    def on_click(event):
        window._offsetx = event.x
        window._offsety = event.y
    def btn_exit():
        global loading
        global loadinginfo
        global exitallowed
        if not loading or exitallowed:
            with open (logpath, "a") as f:
                logprefix = "[" + time.strftime("%H:%M:%S") + "] "
                f.write("\n" + logprefix + 'Goodbye!')
            def fade_out():
                opacity = window.attributes("-alpha")
                if opacity > 0.0:
                    opacity -= 0.2
                    window.attributes("-alpha", opacity)
                    window.after(50, fade_out)
                else:
                    exit()
            fade_out()
        else:
            if loadinginfo == True:
                window.wm_attributes("-topmost", 0)
                ctypes.windll.user32.MessageBoxW(0, "Please finish removing Microsoft Spotify from your computer.", "Spotium", 0x40000 | 0x1000)
                window.wm_attributes("-topmost", 1)
            else:
                pass
    def btn_blckads():
        global loading
        if loading == False:
            loading = True
            mainbutton.config(file = resource_path("loading.png"))
            window.update()
            if os.path.exists("C:/Users/" + USER_NAME + "/AppData/Roaming/Spotify/dpapi.dll"):
                si = subprocess.STARTUPINFO()
                si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
                with open (logpath, "a") as f:
                    logprefix = "[" + time.strftime("%H:%M:%S") + "] "
                    f.write("\n" + logprefix + 'Killing Spotify.exe')
                subprocess.call('wmic process where name=' + '"Spotify.exe"' +  ' call terminate', startupinfo=si)
                with open (logpath, "a") as f:
                    logprefix = "[" + time.strftime("%H:%M:%S") + "] "
                    f.write("\n" + logprefix + 'Killed Spotify.exe')
                with open (logpath, "a") as f:
                    logprefix = "[" + time.strftime("%H:%M:%S") + "] "
                    f.write("\n" + logprefix + 'Unpatching Spotify')
                try:
                    os.remove("C:/Users/" + USER_NAME + "/AppData/Roaming/Spotify/dpapi.dll")
                    os.remove("C:/Users/" + USER_NAME + "/AppData/Roaming/Spotify/config.ini")
                    with open (logpath, "a") as f:
                        logprefix = "[" + time.strftime("%H:%M:%S") + "] "
                        f.write("\n" + logprefix + 'Unpatched Spotify')
                    mainbutton.config(file = resource_path("btn-block.png"))
                    window.update()
                    loading = False
                except (OSError, WindowsError):
                    if os.path.exists("C:/Users/" + USER_NAME + "/AppData/Roaming/Spotify/dpapi.dll"):
                        ctypes.windll.user32.MessageBoxW(0, "Spotium patcher could not delete dpapi.dll.\n\nManually delete it by going to C:/Users/" + USER_NAME + "/AppData/Roaming/Spotify/dpapi.dll", "Spotium", 0x40000)
                    exit()
            else:
                si = subprocess.STARTUPINFO()
                si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
                with open (logpath, "a") as f:
                    logprefix = "[" + time.strftime("%H:%M:%S") + "] "
                    f.write("\n" + logprefix + 'Killing Spotify.exe')
                subprocess.call('wmic process where name=' + '"Spotify.exe"' +  ' call terminate', startupinfo=si)
                with open (logpath, "a") as f:
                    logprefix = "[" + time.strftime("%H:%M:%S") + "] "
                    f.write("\n" + logprefix + 'Killed Spotify.exe')
                with open (logpath, "a") as f:
                    logprefix = "[" + time.strftime("%H:%M:%S") + "] "
                    f.write("\n" + logprefix + 'Patching Spotify')
                subprocess.run(['powershell', '-ExecutionPolicy', 'Unrestricted', patch])
                if os.path.exists("C:/Users/" + USER_NAME + "/AppData/Roaming/Spotify/dpapi.dll") and os.path.exists("C:/Users/" + USER_NAME + "/AppData/Roaming/Spotify/config.ini"):
                    with open (logpath, "a") as f:
                        logprefix = "[" + time.strftime("%H:%M:%S") + "] "
                        f.write("\n" + logprefix + 'Patched Spotify')
                    mainbutton.config(file = resource_path("btn-unblock.png"))
                    window.update()
                    loading = False
                else:
                    notificationimage = PhotoImage(file=resource_path("notify-patchfailed.png"))
                    notifylabel = Label(window, image=notificationimage)
                    notifylabel.place(x=517, y=320.1, width=292, height=117)
                    window.update()
                    window.after(2000, notifylabel.destroy())
                    window.update()
                    loading = False
        else:
            pass
                       
    if os.path.exists(logpath):
        os.remove(logpath)
    else:
        with open(logpath, 'w') as f:
            f.close()
    if os.path.exists(tempfile.gettempdir() + '/Spotifysetup.exe'):
        os.remove(tempfile.gettempdir() + '/Spotifysetup.exe')
    with open (logpath, "a") as f:
        logprefix = "[" + time.strftime("%H:%M:%S") + "] "
        f.write(logprefix + 'Spotium ' + VERSION + ' running')
    def fade_in():
        global setuprun
        opacity = window.attributes("-alpha")
        if opacity < 1.0:
            opacity += 0.2
            window.attributes("-alpha", opacity)
            window.after(50, fade_in)
        if opacity >= 1:
            with open(localpath + '/data.spotium', 'r') as f:
                data = f.read()
                f.close()
            if '@nxkclvd89rt4uy38r952789rj23' in data:
                data = data.replace('@nxkclvd89rt4uy38r952789rj23', '@fngeoiru3og398rh98rwji')
                with open(localpath + '/data.spotium', 'w') as f:
                    f.write(data)
                    f.close()
                btn_blckads()
    window = Tk()
    window.geometry("824x443")
    window.configure(bg = "#212121")
    with open (logpath, "a") as f:
        logprefix = "[" + time.strftime("%H:%M:%S") + "] "
        f.write("\n" + logprefix + 'Building menu')
    canvas = Canvas(window,bg = "#212121",height = 443,width = 824,bd = 0,highlightthickness = 0,relief = "ridge")
    canvas.place(x = 0, y = 0)
    window.attributes("-alpha", 0.0)
    loading = False    
    background_img = PhotoImage(file = resource_path("background.png"))
    background = canvas.create_image(
        412.0, 223.5,
        image=background_img)
    def center_window(width=824, height=443):
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        window.geometry('%dx%d+%d+%d' % (width, height, x, y))
    center_window()
    exitcircle = PhotoImage(file = resource_path("exit.png"))
    exitbutton = Button(image = exitcircle,borderwidth = 0,highlightthickness = 0,command = btn_exit,relief = "flat")
    exitbutton.place(x = 798, y = 6,width = 20,height = 20)  
    with open (logpath, "a") as f:
        logprefix = "[" + time.strftime("%H:%M:%S") + "] "
        f.write("\n" + logprefix + 'Menu built')
    with open (logpath, "a") as f:
        logprefix = "[" + time.strftime("%H:%M:%S") + "] "
        f.write("\n" + logprefix + 'Initializing scripts')
        patch = r'''
                $dpapiUrl = "https://app.spotium.dev/dpapi.dll"
                $configUrl = "https://app.spotium.dev/config.ini"
                $destinationFolder = "$env:APPDATA\Spotify"
                if (-not (Test-Path -Path $destinationFolder -PathType Container)) {
                    New-Item -Path $destinationFolder -ItemType Directory -Force
                }
                try {
                    Invoke-WebRequest -Uri $dpapiUrl -OutFile "$destinationFolder\dpapi.dll" -ErrorAction Stop -UseBasicParsing
                } catch {
                    Write-Host "Failed to download dpapi.dll. Error: $_"
                }
                try {
                    Invoke-WebRequest -Uri $configUrl -OutFile "$destinationFolder\config.ini" -ErrorAction Stop -UseBasicParsing
                } catch {
                    Write-Host "Failed to download config.ini. Error: $_"
                }
        '''
    with open (logpath, "a") as f:
        logprefix = "[" + time.strftime("%H:%M:%S") + "] "
        f.write("\n" + logprefix + '1 of 2 scripts initialized')
    checkspotifyver = r'''
            $username = $env:USERNAME
            $spotiumPath = "C:\\Users\\$username\AppData\\Local\Spotium"

            if (Get-AppxPackage -Name SpotifyAB.SpotifyMusic) {
                $filePath = Join-Path $spotiumPath "microsoft.spotium"
                New-Item -ItemType File -Path $filePath -Force
            } else {
                $filePath = Join-Path $spotiumPath "none.spotium"
                New-Item -ItemType File -Path $filePath -Force
            }
    '''
    with open (logpath, "a") as f:
        logprefix = "[" + time.strftime("%H:%M:%S") + "] "
        f.write("\n" + logprefix + '2 of 2 scripts initialized')

    with open (logpath, "a") as f:
        logprefix = "[" + time.strftime("%H:%M:%S") + "] "
        f.write("\n" + logprefix + 'Checking Spotify details')
    if os.path.exists("C:/Users/" + USER_NAME + "/AppData/Local/Spotify"):
        spotifytype = '1'
        with open (logpath, "a") as f:
            logprefix = "[" + time.strftime("%H:%M:%S") + "] "
            f.write("\n" + logprefix + 'Spotify OK')
        if os.path.exists("C:/Users/" + USER_NAME + "/AppData/Roaming/Spotify/dpapi.dll"):
            mainbutton = PhotoImage(file = resource_path("btn-unblock.png"))
        else:
            mainbutton = PhotoImage(file = resource_path("btn-block.png"))
        blockadsbutton = Button(image = mainbutton,borderwidth = 0,highlightthickness = 0,command = btn_blckads,relief = "flat")
        blockadsbutton.place(x = 200, y = 205,width = 422,height = 105)
    else:
        with open (logpath, "a") as f:
            logprefix = "[" + time.strftime("%H:%M:%S") + "] "
            f.write("\n" + logprefix + 'Windows Spotify is not installed')
        with open (logpath, "a") as f:
            logprefix = "[" + time.strftime("%H:%M:%S") + "] "
            f.write("\n" + logprefix + 'Looking for Spotify installations')
        subprocess.run(['powershell', '-ExecutionPolicy', 'Unrestricted', checkspotifyver])
        time.sleep(1)
        if os.path.exists(localpath + '/microsoft.spotium'):
            global stepping
            global stepscomplete
            spotifytype = '2'
            stepping = False
            stepscomplete = 0
            os.remove(localpath + '/microsoft.spotium')
            with open (logpath, "a") as f:
                logprefix = "[" + time.strftime("%H:%M:%S") + "] "
                f.write("\n" + logprefix + 'Microsoft Spotify found')
            def runspotifyinstaller():
                local_file = tempfile.gettempdir() + '/Spotifysetup.exe'
                window.destroy()
                with open (logpath, "a") as f:
                    logprefix = "[" + time.strftime("%H:%M:%S") + "] "
                    f.write("\n" + logprefix + 'Running SpotifySetup.exe')
                subprocess.call(local_file, shell=True)
                with open (logpath, "a") as f:
                    logprefix = "[" + time.strftime("%H:%M:%S") + "] "
                    f.write("\n" + logprefix + 'Goodbye!')
                exit()
            def nextstep():
                global stepping
                global stepscomplete
                global loading
                global loadinginfo
                if not stepping and not denystepping:
                    stepping = True
                    loadinginfo = True
                    loading = True
                    if stepscomplete == 0:
                        stepscomplete = stepscomplete + 1
                        stepsbuttonimage.config(file =resource_path("loading.png"))
                        window.update()
                        with open (logpath, "a") as f:
                            logprefix = "[" + time.strftime("%H:%M:%S") + "] "
                            f.write("\n" + logprefix + 'Uninstalling Spotify')
                        command = 'Get-AppxPackage -Name SpotifyAB.SpotifyMusic | Remove-AppxPackage'
                        subprocess.run(["powershell", "-Command", command], text=True, shell=False)
                        stepsbuttonimage.config(file =resource_path("btn-installwindowspotify.png"))
                        background_img.config(file=resource_path("step2.png"))
                        with open (logpath, "a") as f:
                            logprefix = "[" + time.strftime("%H:%M:%S") + "] "
                            f.write("\n" + logprefix + 'Uninstalled Spotify with Windows Powershell')
                        stepping = False
                        window.update()
                    elif stepscomplete == 1:
                        stepscomplete = stepscomplete + 1
                        stepsbuttonimage.config(file =resource_path("loading.png"))
                        window.update()
                        time.sleep(2)
                        with open (logpath, "a") as f:
                            logprefix = "[" + time.strftime("%H:%M:%S") + "] "
                            f.write("\n" + logprefix + 'Downloading SpotifySetup.exe from https://download.scdn.co/SpotifySetup.exe')
                        remoteurlfile = 'https://download.scdn.co/SpotifySetup.exe'
                        local_file = tempfile.gettempdir() + '/Spotifysetup.exe'
                        urllib.request.urlretrieve(remoteurlfile, local_file)
                        stepsbuttonimage.config(file =resource_path("btn-launchinstaller.png"))
                        background_img.config(file=resource_path("step3.png"))
                        stepping = False
                        window.update()
                    elif stepscomplete == 2:
                        stepsbuttonimage.config(file =resource_path("loading.png"))     
                        window.update()
                        time.sleep(1)
                        runspotifyinstaller()
            background_img.config(file=resource_path("step1.png"))
            stepsbuttonimage = PhotoImage(file = resource_path("btn-uninstallspotify.png"))
            stepbutton = Button(image = stepsbuttonimage,borderwidth = 0,highlightthickness = 0,command = nextstep,relief = "flat")
            stepbutton.place(x = 196, y = 156,width = 424,height = 104) 
        if os.path.exists(localpath + '/none.spotium'):
            with open (logpath, "a") as f:
                logprefix = "[" + time.strftime("%H:%M:%S") + "] "
                f.write("\n" + logprefix + 'No Spotify installation found')
            spotifytype = '3'    
            os.remove(localpath + '/none.spotium')
            response = ctypes.windll.user32.MessageBoxW(0, 'Spotium could not find any installation of Spotify. Download it from the official Spotify website?', 'Spotium', 0x04)
            if response == 6:
                with open(logpath, "a") as f:
                    logprefix = "[" + time.strftime("%H:%M:%S") + "] "
                    f.write("\n" + logprefix + 'Downloading SpotifySetup.exe from https://download.scdn.co/SpotifySetup.exe')
                remoteurlfile = 'https://download.scdn.co/SpotifySetup.exe'
                local_file = os.path.join(tempfile.gettempdir(), 'Spotifysetup.exe')
                print(f"Downloading file to: {local_file}")
                response = requests.get(remoteurlfile, stream=True)
                if response.status_code == 200:
                    with open(local_file, 'wb') as file:
                        for chunk in response.iter_content(chunk_size=1024):
                            file.write(chunk)
                    subprocess.Popen([local_file])
                else:
                    ctypes.windll.user32.MessageBoxW(0, 'Failed to download SpotifySetup.exe', 'Spotium', 0x40000)
                exit()
            else:
                ctypes.windll.user32.MessageBoxW(0, 'Please download Windows Spotify from the official website, then run Spotium again.', 'Spotium', 0x40000)    
                exit()
    window.bind("<B1-Motion>", on_drag)
    window.bind("<Button-1>", on_click)
    window.resizable(False, False)
    window.wm_attributes("-topmost", 1)
    window.overrideredirect(True)
    window.update()
    window.after(500, fade_in)
    window.mainloop()
except (Exception, OSError, PermissionError) as error:
    if os.path.exists(logpath):
        with open (logpath, 'a') as f:
            logprefix = "[" + time.strftime("%H:%M:%S") + "] "
            f.write("\n" + logprefix + "Something went wrong while Spotium was running ->" + format(error))
    else:
        with open (logpath, 'w') as f:
            logprefix = "[" + time.strftime("%H:%M:%S") + "] "
            f.write("\n" + logprefix + "Something went wrong while Spotium was running ->" + format(error))
    exit()