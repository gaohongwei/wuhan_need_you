# CMS Design
## Components
```
Page, maps to a real web page
Asset(img, video), will be uploaded
Fragment(paragraphs), from Rich text editor
```
## Relation
```
A page has many fragments(paragraphs)
A page has many assets(image, video)
A page has one layout

```
## Layout
It defines how to arrange a pages component.
A layout is something like this
```
<div class = 'row'>
{{asset[0]}}
{{fragments[0]}}
</div>
<div class = 'row'>
{{asset[1]}}
{{fragments[1]}}
</div>
```

A Page Show/Edit page should list its components
Some predefined layout (injected with the actual data ) can be generated when a user click a layout.
So end user are able to modify it by following predefined layput.