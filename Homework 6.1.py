#Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
#Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
#Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
#Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
#Проверить работу примера, создав экземпляр и вызвав описанный метод.
#Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и завершать скрипт.
import time
class TrafficLight:
    __color=['red', 'yellow', 'green']
    def running(self):
        i=0
        while i<3:
            print(f'Переключение светофора: горит {TrafficLight.__color[i]}')
            if i==0:
                time.sleep(7)
            elif i==1:
                time.sleep(2)
            else:
                time.sleep(5)
            i+=1
TrafficLight=TrafficLight()
TrafficLight.running()





