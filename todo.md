# TODO

- [x] make a gitlab template with ci, docs, pages, python packaing,
- [x] add basic setup of a package for simulation and pipelines
- [x] add basic project structure recommendations
- [ ] download js sources and include them locally instead of fetching them
- [ ] add info about sidecar files
- [ ] redraw all git graphs in mermaid so that i can remove the figures by progit 


This is how far i got with mermaid and revealjs, i need someone more javascript than me to fix this

        <script type="module">
            import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs';
            Reveal.on('ready', (event) => {
                let config = {startOnLoad: false, theme: "dark"};
                mermaid.initialize(config);
            });

            const drawDiagram = async function () {
                const data = document.querySelectorAll(".pre-mermaid");
                const render = document.querySelectorAll(".render-mermaid");
                if (render.length > 0 && data.length > 0) {
                    let config = {startOnLoad: false, theme: "dark"};
                    mermaid.initialize(config);
                    for (let ind = 0; ind < data.length; ind++) {
                        console.log(render[ind]);
                        data[ind].id = "mermaid-render-now"
                        const { svg } = await mermaid.render('mermaid-render-now', data[ind].innerText);
                        render[ind].innerHTML = svg;
                    }
                }
            };

            Reveal.on('slidechanged', (event) => {
                drawDiagram();
            });
        </script>
