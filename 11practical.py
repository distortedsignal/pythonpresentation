import os, sys

print sys.argv[1:]

for path in sys.argv[1:]:
	scriptList = [i for i in os.listdir(path) if i[-3:] == ".py"]
	print scriptList
	for script in scriptList:
		print 'Running', script
		os.system("python " + script)