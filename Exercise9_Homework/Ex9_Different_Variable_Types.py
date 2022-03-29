# 1. Created a new PyCharm project: Exercise9.
# 2. Add a new Python file to the project called types.py


# 3. Create two variables: one containing your firstname and another containing your lastname.
firstname = "Pri"
lastname = "Adom"

# 4. Usetheprintfunctiontooutputyourfullnamewithaspacebetweenyourfirst and lastname.
print(firstname, lastname)
# comma separates variables - (str)

# 5. Nowtransferthesevariablevaluesintoalistanddisplaythelist.
myfullname = ["Pri","P.","Adom"]
# lists variable []

# 6. Take the variables and now store the values in a dictionary, using the keys 'first' and 'last'. Display the dictionary values.
print(myfullname[0],myfullname[2])
# lists start with [0] = first (n-1)

# only use git init to initialise new repository - struggled with this command most, kept doing git init to pull and push, do not need, only when initiallizing
# managed to upload work on git hub which is a success
# find folder you're git is connected to using terminal: cd (check directory), ls (check list), cd .. to go back cd ., cd ../., cd../..
# next git clone with link to github repository
# git add ., git commit -m "name or description"
# git status
# git push


mydict = {"first":"Pri", "last":"Adom"}
# first and last alternative for dictionaries

print(mydict["first"], mydict["last"])
# print statement = mydict - first value + mydict - last value


# Output - Pri Adom x3, new lines - per each print statment (3)

