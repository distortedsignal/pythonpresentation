# I'm working with this hosts file, and I'm only going to be reading from it
f = open("C:\Windows\System32\drivers\etc\hosts", "r")

# For every line in the file
for line in f:
	# If it isn't a comment
	if line[0] != '#':
		# And it doesn't alias something to 0.0.0.0
		if line[:7] != "0.0.0.0":
			# And it isn't a newline
			if line != '\n':
				# Print the line (without any newline characters/leading spaced/trailing spaces)
				print line.strip()
