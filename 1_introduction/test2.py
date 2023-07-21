import pysynth as ps

test = [
    ('a', 8), ('b', 8), ('c5', 8), ('d5', 8),
    ('e5', ), ('e5', 16), ('e5', 8), ('g5', 8), ('e5', 4)

]

ps.make_wav(test, fn = "test.wav")