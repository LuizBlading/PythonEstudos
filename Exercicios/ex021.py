# Abrir um arquivo em MP3
# Importe o audio para dentro do projeto
# importe o Mixer e use um INPUT para manter o programa funcionando

from pygame import mixer

mixer.init()
mixer.music.load("hoot.mp3")
mixer.music.play()
input("Gostou da musica?")
# pygame.event.wait()
