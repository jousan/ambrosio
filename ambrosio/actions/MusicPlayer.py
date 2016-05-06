from Action import Action
from mpd import (MPDClient, CommandError)


class MusicPlayer(Action):
    """MusicPlayer for Ambrosio"""
    def __init__(self, cfg):
        super(MusicPlayer, self).__init__(cfg)
        self.triggers = ["music", "audio"]
        self.mpd = MPDClient()
        self.mpd.connect("localhost","6600")

    def do_update(self, command):
        self.mpd.update()

    def do_play(self, command):
        self.mpd.play()

    def do_add(self, command):
        canco = " ".join(command[1:])
        return self.mpd.addid(canco)

    def do_queue(self,command):
        return "list: %s" %(self.mpd.playlist())

    def do_songs(self, command):
        llista = self.mpd.list('file')
        print llista
        if len(llista) > 0:
            return '\n'.join(llista)
        else:
            return 'llista buida'

    def do(self, command):
        print "Will play music ", " ".join(command)
        if command[0] == "update":
            self.do_update(command)
        elif command[0] == "songs":
            self.do_songs(command)
        elif command[0] == "add":
            self.do_add(command)
        elif command[0] == "play":
            self.do_play(command)
        return "OK"

    def is_for_you(self, word):
        if word in self.triggers:
            return True
        return False
