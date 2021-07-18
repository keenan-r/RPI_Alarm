from context import MusicPlayer


mp = MusicPlayer.MusicPlayer()
mp.play_random('Energy')

while mp.is_currently_playing_song():
    pass