print 'Hello.  Welcome to the depressing adventure word game.  Life is meaningless.'
name = raw_input("What is your name?");
if len(name) > 0 and name.isalpha():
    print "I am glad you are choosing to proceed, {name}.  Enjoy yourself.  It will be difficult."
else:
    print "My apologies, {name}.  It appears your name sucks.  Please change your name to proceed."
