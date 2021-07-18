import time
import MusicPlayer


weekday_alarm_time = (6, 15)
states = ["Initial", "Mid", "Energy"]
curr_state = 0

vol_change_delay = 20 # Time in seconds between volume change
state_switch_time = 5*60 # Time in seconds before switching states

mp = MusicPlayer.MusicPlayer()

# Routine to call when alarm is triggered. Will start with soft music from initial state
# then build in volume and switch to more energy states
def alarm_routine():
    alarm_started_time = time.time()
    alarm_finished = False
    while not (alarm_finished):
        mp.set_volume(0.1)
        # Start playing song from first wakeup state
        mp.play_random(states[0])
        # Crescendo volume
        vols = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
        for vol in vols:
            time.sleep(vol_change_delay)
            mp.set_volume(vol)

        while time.time() - alarm_started_time < state_switch_time:
            if not (mp.is_currently_playing_song()):
                mp.play_random(states[0])

        last_state_switch_time = time.time()
        mp.play_random(states[1])

        while time.time() - last_state_switch_time < state_switch_time:
            if not(mp.is_currently_playing_song()):
                mp.play_random(states[1])

        last_state_switch_time = time.time()
        mp.play_random(states[2])

        while time.time() - last_state_switch_time < state_switch_time:
            if not(mp.is_currently_playing_song()):
                mp.play_random(states[2])

while True:
    curr_time = time.localtime(time.time())
    # If the current time is equal to the alarm time, go into alarm loop
    if True:
    #if curr_time.tm_hour == weekday_alarm_time[0] and curr_time.tm_min == weekday_alarm_time[1]:
        alarm_routine()