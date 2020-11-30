'''
Just like it’s hard to find a simple stopwatch application, it can be hard to
find a simple countdown application. Let’s write a countdown program that
plays an alarm at the end of the countdown.
'''

import time, subprocess

timeLeft = 60
while timeLeft > 0:
	print(timeLeft, end=' ')
	time.sleep(1)
	timeLeft -= 1

# At the end of the countdown, play a sound file.
subprocess.Popen(['start', 'alarm.wav'], shell=True)

'''
Instead of playing a sound file, you could save a text file somewhere
with a message like Break time is over! and use Popen() to open it at the end of
the countdown. This will effectively create a pop-up window with a message.
Or you could use the webbrowser.open() function to open a specific website at
the end of the countdown. Unlike some free countdown application you’d
find online, your own countdown program’s alarm can be anything you want!
'''