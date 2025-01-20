# Layouts

Hugo has a [lookup order](https://gohugo.io/templates/lookup-order/) on which template to use for a type of content
it needs to render. Layouts defined here work as fallback templates when something is not defined in 
`/themes/theme-name/layouts`.

* _default: Fallback templates for Kind and Output formats, e.g. ics, rss, json 
* aktuellt, event, personal: Templates for the corresponding Section in `/content`
  (not front page items, those are in each theme's index.html)
* partials: Small reusable snippets of sub-templates used in other layouts, such as menus and calendar items
* shortcodes: much like their WordPress equivalent, templates that can be called from inside
  `/content` files to output video, figures, sidebars etc in a consistent manner

## Templates

[Official template documentation](https://pkg.go.dev/html/template)

In its simplest form, variables are evaluated using `{{ . }}`, where `.` is the *context* in Hugo, which in most
cases would be an object, which you can access attributes from using dot notation like `{{ .Title }}`. In that case,
we are still referring to the *context* (maybe a Page object) with the heading `.`.

## Coding style

Prefer using the pipe syntax `|` where allowed, as it is easier to untangle than nested polish notation with lots of
parenthesis, and should feel familiar from Bash scripting. 
E.g. use `{{ i18n .Month | first 3 }}` instead of `{{ first 3 (i18n .Month) }}`.

To untangle further and improve readability, consider creating a variable instead of nesting function calls:

```
{{ $authors := where .data.creators "creatorType" "author"}}
{{ range $authors }}
  {{/* I am in a loop */}}
{{ end }}
```

instead of (there are a lot worse examples than this):

```
{{ range where .data.creators "creatorType" "author" }}
  {{/* I am in a loop */}}
{{ end }}
```
