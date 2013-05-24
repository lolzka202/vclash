#variables demonstrated
print("Code Example 3 - Variables")
print "This program is a demo of variables"
v = 1
print "The value of v is now", v
v = v + 1
print "v now equals itself plus one, making it worth", v
v = 51
print "v can store any numerical value, to be used elsewhere."
print "for example, in a sentence. v is now worth", v
print "v times 5 equals", v * 5
print "but v still only remains", v
print "to make v five times bigger, you would have to type v = v * 5"
v = v * 5
print "there you go, now v equals", v, "and not", v / 5
print("\n")

print("Basic syntax and spacing demonstration")
s1 = "Good"
s2 = "day"
s3 = "to me"
print s1, s2
s4 = s1 + " " + s2 + " " + s3
print(s4);
print("\n")

print("Code Example 1 - The while loop")
a = 0
while a < 10:
    a = a + 1
    print a
print("\n")

print('Code Example 5 - if statement and example')
print "We will show the even numbers up to 20"
n = 1
while n <= 20:
    if n % 2 == 0:
        print n
    n = n + 1
print "there, done."
print("\n")

print('Code Example 6 - the else statement')
f = 6
if f > 5:
    print "This shouldn't happen."
else:
    print "This should happen."
print("\n")

print("Code Example 7 - The elif statement")
z = 4
if z > 70:
    print "Something is very wrong"
elif z < 7:
    print "This is normal"
print("\n")

#The use of Indention (Lesson 4)

print("The use of Indention - Lesson 4")
a = 10
while a > 0:
    print a
    if a > 5:
        print "Big number!"
    elif a % 2 != 0:
        print "This is an odd number"
        print "It isn't greater than five, either"
    else:
        print "this number isn't greater than 5"
        print "nor is it odd"
        print "feeling special?"
    a = a - 1
    print "we just made 'a' one less than what it was!"
    print "and unless a is not greater than 0, we'll do the loop again."
print "well, it seems as if 'a' is now no bigger than 0!"
print "the loop is now over, and without furthur adue, so is this program!"
print("\n")


