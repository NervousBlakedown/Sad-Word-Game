print "Hello.  Welcome to the depressing adventure word game.  Life is meaningless.""
name = raw_input("What is your name?");
if len(name) > 0 and name.isalpha():
    print "I am glad you are choosing to proceed, {name}.  Enjoy yourself.  It will be difficult."
else:
    print "My apologies, {name}.  It appears your name sucks and does not qualify as a real name.  Please change your name to proceed."

print "Oh, look, a pig latin translator. Do be careful.  It is a cold, cruel world out there."
#Pig Latin translator
pyg = 'ay'
original = raw_input('Enter a word:')
if len(original) > 0 and original.isalpha():
	word = original.lower()
	first = word[0]
	new_word = word+first+pyg
	new_word = new_word[1:len(new_word)]
  	print new_word
else:
  	print 'empty'
