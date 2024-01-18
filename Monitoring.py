import time
import platform
import GPUtil
import psutil
from datetime import datetime


def Haupt():
     
     GPU = GPUtil.showUtilization(all)
     CPU = psutil.cpu_percent()
     memory = psutil.virtual_memory()
     Festplatte, Festplatte2 = psutil.disk_usage("C:"), psutil.disk_usage("D:")
     
     time.sleep(5)

     print (GPU)
     print("///////////////////////////////////////////////")
     print(CPU, "Prozent CPU Auslastung")
     print("///////////////////////////////////////////////")
     time.sleep(5)
     
     try:
         memory / 1024
         print(memory)
     except:
         pass
     print("///////////////////////////////////////////////")

     time.sleep(5)

     print(Festplatte, 
           Festplatte2)
     print("//////////////////////////////////////////7/////")
     exit()
     








def SystemOS():
     system = platform.system()
     lokale_zeit = datetime.now()
     print(system, lokale_zeit.strftime("%d-%m-%y %H:%M:%S"))


    
def Error():
    if Haupt() == False:
        print("Ein Fehler ist auf getretten")
        exit()
    else:
     pass

              
      
time.localtime()
SystemOS()
print("///////////////////////////////////////////////")

time.sleep(5)
Haupt()

Error()

exit()
