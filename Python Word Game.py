# Begin/Name and Age Validation.
print "Hello.  Welcome to the depressing adventure word game.  Life is meaningless."
name = raw_input("What is your name?");
if len(name) > 0 and name.isalpha():
    print "I am glad you are choosing to proceed, {name}.  Welcome.  I will forget your name, but do not take it personally, even though it is very personal."
else:
    print "My apologies, {name}.  It appears your name sucks and does not qualify as a real name.  Please change your name to proceed."
        if len(name) > 0 and name.isalpha():
            print "Ah, finally, {name}, thank you for not being a smart-ass anymore.  Welcome."


print "Now that we know your name, we must confirm your age is eighteen years or older.  This game is not inappropriate, we just feel safer knowing you are old enough to be held responsible for all of your stupid decisions."
age = raw_input("What is your age?");
if len(age) < 18:
    print "I am sorry, but you cannot proceed.  You are far too young.  I can still smell breast milk on your breath.  Please go outside and play with a sports ball or something."
else:
    print "Really?  {age}?  Prove it."

# Age validation with Nsync.
def age_validation(age):
	if age <= Nsync_debut:
	print "*Sigh*, okay, I believe you.  Let's proceed."
	else:
		print "That's what I thought.  Get lost, kid."


print "Okay, {name}, age {age}, let's begin the story."
print "It is a boring day like all the others.  You wake up at 5:30 A.M.  An ungodly hour."
place = raw_input("Where do you go first?")
#find way to list options (dropdown or lettered multiple choice), options: "work", "school", "brothel"
if place = "Work"
print "Ah."


# Pig Latin translator.
print "Oh, look, a pig latin translator.  You must use it to proceed.  Do be careful.  It is a cold, cruel world out there."
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


print "Now, we've come for the bill."
