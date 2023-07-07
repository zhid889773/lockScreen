import os,time,sys,tkinter
from tkinter.messagebox import *
if __name__=="__main__":
    if len(sys.argv)<2:
        print("command miniutesNum")
        sys.exit(0)
    minCount=int(sys.argv[1])
    while 1:
        time.sleep(minCount*60)
        top=tkinter.Tk()
        top.geometry('0x0+999999+0')
        lockCmd="cmd /c %windir%\\system32\\rundll32.exe user32.dll,LockWorkStation"
        os.system(lockCmd)
        result=askyesno("提示","继续护眼锁屏？")
        top.destroy()
        if not result:
            sys.exit(0)
