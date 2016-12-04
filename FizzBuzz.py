for x in range(1, 101):
	mod3 = (x % 3 == 0)
	mod5 = (x % 5 == 0)
	print "WizeLine" if mod3 and mod5 else "Wize" if mod3 else "Line" if mod5 else x