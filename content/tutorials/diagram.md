---
title: Drawing diagrams
---

## C4

### Using `graphviz`

[Graphviz](https://graphviz.org/) is a powerful open source graph visualization tool written in (mostly) C that allows you
to define graphs using the `dot` language.

I did not find any good pre-defined templates for making C4 diagrams using Graphviz so I have written my own. As I have also made a bunch of other diagrams in this course using the `dot` language I wanted to keep the graphing language consistent. You can have a look at one example here:

{{< details summary="Example c4 container diagram made in the dot language" >}}
{{< include-code "dot" "code/c4_container_example.gv" "">}}
{{< /details >}}

The above code generates this figure:

![C4 container example diagram](c4_container_example.png#expandable.light "Example C4 Container
diagram for a solar-system simulation tool")

### Using `plantUML`

[PlantUML](https://plantuml.com/) is a Java tool for drawing a wide range of diagrams, notably
[Unified Modeling Language (UML)](https://en.wikipedia.org/wiki/Unified_Modeling_Language) and
similar diagrams. 

There is a predefined set for drawing specifically C4-architecture diagrams called [C4-PlantUML](https://github.com/plantuml-stdlib/C4-PlantUML) that you can include into your PlantUML files by

```plantuml
!include <C4/C4_Container>
```

To read more on how to use C4-PlantUML, see the [github README.md](https://github.com/plantuml-stdlib/C4-PlantUML?tab=readme-ov-file#getting-started).

### Other tooling

There is an extensive list of other tooling for C4 listen on [c4model.com's tooling page](https://c4model.com/tooling).

## State diagrams

A state diagram is fairly simple to draw. If we follow the [UML definition](https://en.wikipedia.org/wiki/UML_state_machine) we can draw them:

- [Using `plantUML`](https://plantuml.com/state-diagram)

### Using `graphviz`

```dot
digraph finite_state_machine {
    label="Pressure valve";
    rankdir="LR";
    dpi=300;
    node [shape=point, label=""];
    ENTRY;
    EXIT;
    node [shape=rect, style=rounded];

    A[label="Low flow"];
    B[label="High flow"];
    C[label="No flow"];

    ENTRY->A [label="Start"];
    A->C [label="Shutdown"];
    B->A [label="Pressure drops"];
    A->B [label="Request recived"];
    C->EXIT [label="End"];
}
```
