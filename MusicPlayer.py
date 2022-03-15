
import pygame as pg
import random
import os

class MusicPlayer:

    def __init__(self, path=''):
        self.music_folder_start = path + 'V2_Music_Files/'

        self.freq = 44100
        self.bitsize = -16
        self.channels = 2
        self.buffer = 2048
        pg.mixer.init(self.freq, self.bitsize, self.channels, self.buffer)

    def play_random(self, folder):
        folder = folder + '/'

        clock = pg.time.Clock()

        basedir = os.path.dirname(os.path.abspath(__file__)) + '/'
        music_filepath = basedir + self.music_folder_start + folder
        print(music_filepath)

        music_list = os.listdir(music_filepath)
        #music_list.pop(0)
        ind = random.randint(0, len(music_list)-1)
        music_file = music_filepath + music_list[ind]

        try:
            pg.mixer.music.load(music_file)
            print("Music file {} loaded!".format(music_file))
        except pg.error:
            print("File {} not found! {}".format(music_file, pg.get_error()))
            return
        pg.mixer.music.play()

        #while pg.mixer.music.get_busy():
            #clock.tick(30)

    # Set volume. Accepts float between 0 and 1
    def set_volume(self, val):
        pg.mixer.music.set_volume(val)

    def is_currently_playing_song(self):
        return pg.mixer.music.get_busy()
