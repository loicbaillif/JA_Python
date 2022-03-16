# ****** TAKING INPUT - Exercise : Catchy song ******
#
# Have you ever dreamed of becoming a songwriter? It's time to make a hit. 
# We will leave a verse for later and write the chorus part instead.
# All you need to do is to read the input number n and an input word 
# (they are given on separate lines) and to repeat this word exactly n times. 
# Don't specify any message when reading the input. 
# 
# Finally, print your song for us, please!

nb_reps = int(input())
word = input()

print(word*nb_reps)