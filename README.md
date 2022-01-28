# Pytgen

A simple static site generator built with Python. This script will generate starter files in a new directory for a very simple blog. The script can be ran from multiple directories to create multiple sites. After creating a site, the script will allow the user to generate new posts, publish all posts, and reindex posts on the homepage.

## Instructions

1. Download to a directory and run main.py.
2. Use create site to generate starter files.
3. Use new post to create a txt template.
4. Edit the template using the included pseudo-markdown syntax.
5. Use publish to convert your post.txt files into html.
6. Be sure to reindex after publishing. This will rebuild your index page to include an updated list of post links.

### Styling and Dynamic Content

Pytgen currently uses [pico.css](https://github.com/picocss/pico) and [list.js](https://github.com/javve/list.js) for styling, searching, and sorting. However, they aren't generated automatically upon site creation. Simple copy the contents of the included template folder into the root directory of your newly generated site if you would like to enable those features. After overwriting the default styles and scripts files, be sure to run main.py and publish then reindex.

## Requirements

- Python 3.9
- Access to a Terminal

## Coming Soon

- Automatic images feature
- Better Navigation
- Built in help documentation
