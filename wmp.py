from subprocess import call,Popen
from sys import argv 
script,pll=argv
playerpath="C:/Program Files (x86)/Windows Media Player/wmplayer.exe"
filepath="C:/Users/arawat/Music/music/Final Fantasy X-2 - Eternity (Memory of Lightwaves (Piano).mp3"
playlist="C:/Users/arawat/Music/Playlists/"+pll+".wpl"
Popen([playerpath,playlist])

