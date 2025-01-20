# Themes

This is the main difference between the two sites created, apart from having separate config yml files.
If a file exists in a theme layout, it overrides any one defined in `/layouts`.

## Base template, `baseof.html`

As the name implies, it forms the base of all templates. It [defines blocks](https://gohugo.io/templates/base/)
that the other, more specialised templates fill in. Block names with usage

* title: overrides the content of the <title> tag
* main: rendering the main content of the page with additional metadata from frontmatter
* scripts: any javascript needed, set at the end of the base template to not block page loading

Every template defining a main block should have an element with `id="main"`, to allow the skip-link defined in the 
base template to link to where actual content begins. This is to allow users of accessibility tools to skip over 
repeating content such as the main menu.