# denon_player
## This is the simplest HEOS player tested with Denon hardware

denon_player is a simple program using HEOS 'Play URL' functionality. Full information about HEOS cli interface can be seen in the special pdf document according to [Denon information](https://support.denon.com/app/answers/detail/a_id/6953).


## Features

- Import a m3u file
- Play any Internet stream by HEOS 'Play URL' command 


## Tech

denon_player uses M3U parser [M3U parser](https://github.com/dvndrsn/M3uParser) to import radio stream information.
## Input data
`radio.ini` file must be created with the following info:
```
ipx : <device_ip_address>
portx : <device_port> (1255 for Denon CEOL N10)
window title : <text>
mygeometry_w : 360
mygeometry_h : 600
pid : <your_pid> (use heos_get_players.py to extract your device pid)
```

`radio.m3u` file must contain the following info:
```
#EXTM3U
...
#EXTINF:-1, Popular classic
https://icecast-radioclassica.cdnvideo.ru/sberzvuk
...
```
The program can be used with non-default `m3u` file:
```
python radio.py yourfile.m3u
```
kivy version consists of module 'main.py'. Handwritten list of radio stations should be created in 'radios' structure (list of dicts).

## How to build

denon_player was tested with Denon CEOL N10 device under Linux with Python 3.8.x
To use it with Windows one can compile it with Windows version of Python or cross compile under wine with Python installed 
by the following command:

```
wine C:/users/<user>/AppData/Local/Programs/Python/Python38/Scripts/pyinstaller.exe --noupx --onefile radio.py
```
To install additional packages:

```
wine C:/users/<user>/AppData/Local/Programs/Python/Python38/Scripts/pip.exe install kivy
```
To build Android version for main.py file with kivi interface:
```
buildozer android clean
buildozer android debug deploy run
```

## License

MIT

**Free Software!**
