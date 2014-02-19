from mathHelp import fibGen

print sum(filter(lambda i: i % 2 == 0, fibGen(4000000)))
