from pypresence import Presence  
import time  

CLIENT_ID = "1351507907597828096"  #ID приложения  
rpc = Presence(CLIENT_ID)  
rpc.connect()  

while True:  
    rpc.update(state="В просмотре...", details="Смотрит видео")  
    print("Статус обновлен!")
    time.sleep(840000) # Обновление активности каждые