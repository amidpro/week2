num = 42
txt = 3

# ints concatinate with ints, str with str, can't mix both

if txt < num:
    print('Wow!')
else:
    print('Doh!')
# is txt (3) less than num (42)? True. Prints out 'Wow!', if statement was False, script would print out 'Doh!' (else statement)

# example of if and else statements. Always start off with if:, then elif: then end with else: as last option

# is txt (3) is greater than num (42)? False. Prints out 'Doh!' as original if statement is False, else statement in use instead
if int(txt) > num:
    print('Wow!')
else:
    print('Doh!')