class Song(object):

    def __init__(self,lyrics):     #下划线有两个
        self.lyrics=lyrics
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday=Song(["happy birthday to you",
                 "I don't want to get sued",
                 "So I'll stop right there"])

bulls_on_parada=Song(["They rally around the family",
                  "With pockets full of shells"])



happy_bday.sing_me_a_song()
bulls_on_parada.sing_me_a_song()
