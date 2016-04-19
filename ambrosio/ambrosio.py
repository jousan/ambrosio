#!/usr/bin/env python
# -*- coding: utf-8 -*-

from commandlist import CommandList
import channels as ch #ch is alias of channels
import actions as ac
import time
import yaml

class Ambrosio(object):
    """class for Ambrosio Personal Digital Butler will run our house"""
    def __init__(self):
            super(Ambrosio, self).__init__()
            self.cl = CommandList()

            self._get_config() #els metodes per us intern tenen _davant
            self.channels = []
            self.channels.append(ch.TextChannel())
            self.channels.append(ch.TelegramChannel())

            self.actions = []
            self.actions.append(ac.MusicPlayer())

    def _get_config(self):
        with open ("ambrosio/ambrosio.yaml") as f:
            self.cfg = yaml.load(f)

            print "Configuracio: "
            print json.dumps(self.cfg), indent=4)


    def next_command(self):
        try:
            return self.cl.next()
        except:
            return None,None

    def update_channels(self):
        for chan in self.channels:
            while chan.msg_avail():
                self.cl.append((chan, chan.get_msg()))
                 #canal i missage es una tuple

    def execute_command(self, command):
        print "Will execute", command
        # for each action in actions
        # if is_for_you()
        # action.do
        words = command.split()
        first_words = words[0]
        rest_words = words[1:] #from position 1 until the end
        response = None
        for a in self.actions:
            if a.is_for_you(first_words):
                response = a.do(rest_words)
                break
        else:  #if there is no word after finishing the bucle, is the else form for
            print "No t'entenc"
        return response

    def mainloop(self):
        # While True:
        # command = get_command
        # do_command(command)
        # update
        while True:
            chan, command = self.next_command()
            if command:
                #print command
                response = self.execute_command(command)
                chan.respond(response)

            time.sleep(1)
            self.update_channels()




if __name__ == "__main__":
    print "Here be dragons!"
    amb=Ambrosio()
    amb.mainloop()
