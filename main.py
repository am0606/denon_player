import kivy
kivy.require('2.0.0')
# Конфиги нужно прописывать до всех остальных импортов
kivy.Config.set('graphics', 'resizable', '0')

from os import environ
from sys import platform as _sys_platform

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.clock import Clock

from myconfig import *
import telnetlib
import random

def telnet_send(myconf, xurl):
    tn = telnetlib.Telnet(myconf.ipx, myconf.portx)
    tn.write(str.encode(myconf.heos_prefix + xurl + '\n'))
    output = tn.read_until(b"FIN\n", timeout = 1).decode('ascii')
    print(output)

radios = [{'name': ' Орфей', 'url': 'http://orfeyfm.hostingradio.ru:8034/orfeyfm192.mp3'}, 
          {'name': ' Орфей: Классика без границ', 'url': 'https://orfeyfm.hostingradio.ru:8034/orpheuscwb192.mp3'}, 
          {'name': ' Орфей: Классика крупных форм', 'url': 'https://channels.fonotron.ru:8000/Chan_8_192.mp3'}, 
          {'name': ' Орфей: Классика киномузыки', 'url': 'https://channels.fonotron.ru:8000/Chan_9_192.mp3'}, 
          {'name': ' Орфей: Популярная классика', 'url': 'https://channels.fonotron.ru:8000/Chan_72_256.mp3'}, 
          {'name': ' Орфей: Русская классика', 'url': 'https://channels.fonotron.ru:8000/Chan_73_128.mp3'}, 
          {'name': ' Орфей: Симфоническая музыка', 'url': 'https://channels.fonotron.ru:8000/Chan_74_256.mp3'}, 
          {'name': ' Орфей: Музыка мьюзиклов', 'url': 'https://channels.fonotron.ru:8000/Chan_66_256.mp3'}, 
          {'name': ' Классик', 'url': 'http://cfm.jazzandclassic.ru:14534/rcstream.mp3'}, 
          {'name': ' Gold (Радио Классик)', 'url': 'https://jfm1.hostingradio.ru:14536/gcstream.mp3'}, 
          {'name': ' Популярная классика', 'url': 'https://icecast-radioclassica.cdnvideo.ru/sberzvuk'}, 
          {'name': ' Симфония FM', 'url': 'https://radiorecord.hostingradio.ru/symph96.aacp'}, 
          {'name': ' Classic (Зайцев.FM)', 'url': 'https://zaycevfm.cdnvideo.ru/ZaycevFM_classic_256.mp3'}, 
          {'name': ' Klassik Radio - Pure Mozart', 'url': 'http://stream.klassikradio.de/mozart/mp3-192/tasmanic/'}, 
          {'name': ' Klassik Radio - Barock', 'url': 'http://stream.klassikradio.de/barock/mp3-192/tasmanic/'}, 
          {'name': ' Klassik Radio - Pure Bach', 'url': 'http://stream.klassikradio.de/purebach/mp3-192/tasmanic/'}, 
          {'name': ' Klassik Radio - Pure Verdi', 'url': 'http://stream.klassikradio.de/verdi/mp3-192/tasmanic/'}, 
          {'name': ' Klassik Radio - Pure Beethoven', 'url': 'http://stream.klassikradio.de/beethoven/mp3-193/tasmanic/'}, 
          {'name': ' Klassik Radio - Opera', 'url': 'http://stream.klassikradio.de/opera/mp3-192/tasmanic/'}, 
          {'name': ' Klassik Radio - Dreams', 'url': 'http://stream.klassikradio.de/dreams/mp3-192/tasmanic/'}, 
          {'name': ' Klassik Radio - Piano', 'url': 'http://stream.klassikradio.de/piano/mp3-192/tasmanic/'}, 
          {'name': ' Klassik Radio - New Classics', 'url': 'http://stream.klassikradio.de/newclassics/mp3-192/tasmanic/'}, 
          {'name': ' Klassik Radio - Nature', 'url': 'http://stream.klassikradio.de/nature/mp3-192/tasmanic/'}, 
          {'name': ' Klassik Radio - Movie', 'url': 'http://stream.klassikradio.de/movie/mp3-192/tasmanic/'}, 
          {'name': ' РНО', 'url': 'https://rnor.ru/data/radioRNO/radio256.mp3'}, 
          {'name': ' Кассиопея', 'url': 'https://stream.cassiopeia-station.ru:5125/stream'}, 
          {'name': ' Книга', 'url': 'http://bookradio.hostingradio.ru:8069/fm'}, 
          {'name': ' Книга вслух', 'url': 'https://radio-soyuz.ru:1045/stream'}, 
          {'name': ' Story FM', 'url': 'https://storyfm.hostingradio.ru:8031/storyfm128.mp3'}, 
          {'name': ' Умное Радио', 'url': 'https://umnoe.amgradio.ru/Umnoe'}, 
          {'name': ' Искатель', 'url': 'https://iskatel.hostingradio.ru:8015/iskatel-128.mp3'}, 
          {'name': ' Комсомольская правда', 'url': 'http://kpradio.hostingradio.ru:8000/russia.radiokp128.mp3'}, 
          {'name': ' Говорит Москва', 'url': 'http://media.govoritmoskva.ru:8880/ru64.mp3'}, 
          {'name': ' Звезда-FM', 'url': 'http://icecast-zvezda.mediacdn.ru/radio/zvezda/zvezda_128'}, 
          {'name': ' Бизнес ФМ', 'url': 'http://bfmstream.bfm.ru:8004/fm64'}, 
          {'name': ' Вести ФМ', 'url': 'http://icecast.vgtrk.cdnvideo.ru/vestifm_aac_32kbps'}, 
          {'name': ' 101.ru Анекдоты', 'url': 'https://pub0102.101.ru:8443/stream/trust/mp3/128/20'}, 
          {'name': ' Радонеж (Благовещение)', 'url': 'https://icecast-radonezh.cdnvideo.ru/rad128'}, 
          {'name': ' Вера', 'url': 'http://radiovera.hostingradio.ru:8007/radiovera_128'}, 
          {'name': ' Ретро ФМ', 'url': 'http://retroserver.streamr.ru:8043/retro256.mp3'}, 
          {'name': ' Романтика', 'url': 'http://ic6.101.ru:8000/stream/air/aac/64/101'}, 
          {'name': ' Best FM', 'url': 'http://nashe1.hostingradio.ru/best-128.mp3'}, 
          {'name': ' Радио 7', 'url': 'http://retroserver.streamr.ru:8040/radio7128.mp3'}, 
          {'name': ' Монте Карло', 'url': 'https://montecarlo.hostingradio.ru/montecarlo96.aacp'}
    ]

class ScrollViewApp(App):
    def build(self):        
        self.title = 'Radio app'
        self.myconf = myconfig()

        # Создаем GridLayout для размещения кнопок
        self.layout = GridLayout(cols=1, spacing=5, size_hint_y=None)
        # Устанавливаем размер GridLayout, чтобы он был больше экрана
        self.layout.bind(minimum_height=self.layout.setter('height'))

        # Создаем кнопки и добавляем их в GridLayout
        for r in radios:
            btn = Button(text=f'{r["name"]}', size_hint_y=None, height=100, on_press = self.on_btn_press)
            self.layout.add_widget(btn)

        # Создаем ScrollView и добавляем в него GridLayout
        root = ScrollView(size_hint=(1, None), size=(Window.width, Window.height),
                           pos_hint={'top': 1})
        root.add_widget(self.layout)   

        return root
    
    def on_btn_press(self, instance):
        for r in radios:
            if r["name"]==instance.text:
                self.xurl = r["url"]
                print(f'{r["name"]}')
                break
        
        telnet_send(self.myconf,self.xurl)
        random_color = [random.random() for _ in range(3)] + [1]  # RGBA
        instance.background_color = random_color

        Clock.schedule_once(lambda _: self.change_color(instance), 3) # Запланировать вызов через 3 секунду, lambda _ (вызов функции c аргументом отличным от dt)

    def change_color(self,instance):
        instance.background_color = [1,1,1,1]

if __name__ == '__main__':
    ScrollViewApp().run()