import mods
# createSite
# If there isn't already a folder in the same directory titled site then generate a folder that includes an index file, an entries folder, and a single entry

# newEntry
# If the site folder exists then add an entry to the entries folder and update the index file to include the latest entry
# I will probably have this command recreate the entire index file in alphabetical or date order rather than appending to the end

userOption = ''
while userOption != 'e':
    userOption = input("[c]reateSite, [n]ewPost, [p]ublish, [r]eindex, [h]elp or [e]xit: ")

    if userOption == 'c':
        mods.createSite()
    elif userOption == 'n':
        mods.newPost()
    elif userOption == 'p':
        mods.publish()
    elif userOption == 'r':
        mods.reindex()
    elif userOption == 'h':
        mods.helpDocs()    
    else:
        break

print("Session Ended")    
