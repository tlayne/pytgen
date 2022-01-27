from genericpath import isfile
import os
import shutil

# ToDo
# - use root + path  throughout program instead of within global file paths
# - create a copy template feature 

# Global Filepaths
root = 'site'
posts = root + '/posts'
published = root + '/published'
publishLinks = 'published/'
styles = root + '/styles.css'
scripts = root + '/scripts.js'
index = root + '/index.html'

# Global Header
header = """<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="styles.css">
    <title>Pytgen</title>
  </head>
  <body>
    <header>
        <hgroup>
            <h1>Blog Title</h1>
            <h2>A simple python generated blog.</h2>
        </hgroup>
    </header>
    <main>
"""

# Global Footer
footer = """</main>
    <footer>
        <small>Built with Python</small>
    </footer>
    <script src="scripts.js"></script> 
    <script>
    var options = {
        valueNames: [ 'name' ]
    };

    var userList = new List('postlist', options);
    </script>
  </body>
</html>
"""

# Create a new site
def createSite():
    path = root 
    isDir = os.path.isdir(path) 

    if isDir == True:
        print("A site already exists")
    
    else:
        cwd = os.getcwd()

        os.makedirs(posts)
        os.makedirs(published)
        os.chdir(path) 

        f = open('index.html', 'w')
        s = open('scripts.js', 'w')
        t = open('styles.css', 'w')

        htmlTemplate = header + footer
        jsTemplate = ""
        cssTemplate = ""

        f.write(htmlTemplate)
        s.write(jsTemplate)
        t.write(cssTemplate)
        f.close()
        s.close()
        t.close()

        os.chdir(cwd)

# Add a templatized markdown file to entries folder
def newPost():
    path = root 
    isDir = os.path.isdir(path) 

    if isDir != True:
        print("A site doesn't exist yet.")
    
    else:    
        cwd = os.getcwd()
        path = posts
        os.chdir(path)
        postName = input("Enter a name for your post.\n")
        postFix = postName + '.txt'

        isFile = os.path.isfile(postFix) 

        if isFile == True:
            print("A post with this title already exists.")

        else:
            f = open(postFix, 'w')

            mdTemplate = """
## Post Title
### Likes
*-
- list item
- list item
-*
### Dislikes
*-
- list item
- list item
-*
## Summary 
<-
Paragraph starting here
->
        """
        
            f.write(mdTemplate)
            f.close()
            print(f"Post {postFix} has been saved.")
            os.chdir(cwd)

# Search post directory and write list of published files to index
# Todo
# - Add more classes to sort by using list.js
def reindex():
    path = root 
    isDir = os.path.isdir(path) 

    if isDir != True:
        print("A site doesn't exist yet.")
    
    else:  
        cwd = os.getcwd()
        postList = os.listdir(published)
        postList.sort()


        os.chdir(root)

        indexFile = open('index.html', 'w')
        indexFile.write(header)
        indexFile.write("""<div id="postlist">
    <nav>
    <input class="search" placeholder="Search" style="margin-right: 15px;" /> <button class="sort" data-sort="name" style="max-width: 200px;">
    Sort
    </button>
    </nav>
  <ul class="list" style="list-style-type: none;">
        """)
    
        for i in postList:
            if i.endswith('.html'):
                iFix = i.replace('.html','')
                indexFile.write(f"<li style=\"list-style: none;\"><a href=\"{publishLinks}{i}\" class=\'name\'>" + iFix + "</a></li>" + "\n")

        indexFile.write("</ul></div>")
        indexFile.write(footer)
        indexFile.close()

        os.chdir(cwd)

# Opens each txt file and saves its contents to an html file of the same name.
def publish():
    path = root 
    isDir = os.path.isdir(path) 

    if isDir != True:
        print("A site doesn't exist yet.")
    
    else:  
        cwd = os.getcwd()

        textPosts = [f for f in os.listdir(posts) if f.endswith('.txt')]

        os.chdir(posts)    

        for post in textPosts:
                with open(post, 'r') as file:
                    text = file.readlines()
                    text = [i.replace("\n", '') if i.endswith("\n") else i for i in text]
                    text = [i.replace('- ', '<li>') + '</li>\n' if i.startswith('- ') else i for i in text]
                    text = [i.replace('# ', '<h1>') + '</h1>\n' if i.startswith('# ') else i for i in text]
                    text = [i.replace('## ', '<h2>') + '</h2>\n' if i.startswith('## ') else i for i in text]
                    text = [i.replace('### ', '<h3>') + '</h3>\n' if i.startswith('### ') else i for i in text]                    
                    text = [i.replace('*-', '<ul>') if i.startswith('*-') else i for i in text]
                    text = [i.replace('-*', '</ul>\n') if i.startswith('-*') else i for i in text]                 
                    text = [i.replace('<-', '<p>') if i.startswith('<-') else i for i in text]
                    text = [i.replace('->', '</p>\n') if i.startswith('->') else i for i in text]
                    newPost = post.replace(".txt", ".html") 
                os.chdir(cwd)
                os.chdir(published)   
                with open(newPost, 'w') as file:
                    postTitle = header.replace("Pytgen", post.replace(".txt", ""))
                    postHeader = postTitle.replace("styles.css", f"../../{styles}")
                    file.write(postHeader)
                    for lines in text:    
                            file.write(lines)
                    postFooter = footer.replace("scripts.js", f"../../{scripts}")
                    file.write(postFooter)        
                os.chdir(cwd)
                os.chdir(posts)

        os.chdir(cwd)

# Scrapes image folder and prepares images to be added to published posts
def scrapeImg():
    print("Coming Soon")

# Lists help text for all the options in main.py
def helpDocs():
    print("Coming Soon")