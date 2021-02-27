# -*- coding: utf-8 -*-
import pyautogui
import time
"""Nasıl x ve y yi alıcam?
x ve y mouse'un like buttonuna tam geldiği nokta bunu öğrenmek için 
cmd ekranından
1-pip install pyautogui
2-python
3-import pyautogui
4-Burda mouse likenin tam üstünde olsun sonra pyautogui.position() çalıştır bu x ve y yi vericek
"""

"""Nasıl çalıştırıcam ?
tinder.py'yi masaüstününe koyun sonra cmd ekranını yeniden açıp
1-cd Desktop 
2-python tinder.py yapın hata alırsanız hata yorum satırını okuyunuz(kodda en altta)
"""

x=-864
y=1040

sayac=5

while True:
    for i in range(0,sayac):
        pyautogui.click(x,y)
        time.sleep(0.5)
        
    cevap=pyautogui.confirm(text="Devem Etmek Istiyor Musun?",title="Tinder Like",buttons=["Evet","Hayır"])
    
    if cevap=="Hayır":
        break
    else:
        while True:
            try:
                sayac=int(pyautogui.prompt("Kaç Adet Daha Like Atılmasını Istiyorsunuz?",title="Like Sayisi"))
                break
            except :
                pyautogui.alert(text="Lüten Tam Bir Sayi Giriniz",title="Uyarı",button="Tamam")

"""Hata 
Eğer pip komutunda hatalırsanız https://www.youtube.com/watch?v=zYdHr-LxsJ0 bu linki izleyin
Pyautogui ile hata alırsanız pip install python yapın sonra pip install pyautogui yapın
"""


                