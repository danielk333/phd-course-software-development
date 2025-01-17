const originalReplaceState = history.replaceState;

function enable_hash(path) {
    history.replaceState = (_a, _b, url) => {
        url = url.toString();
        if (url[0] == '#') {
            url = path + url;
        } 
        originalReplaceState.bind(history)(_a, _b, url);
    };

    if (window.location.href.includes('file://')) {
        Reveal.configure({hash: false});
    }
    else {
        Reveal.configure({hash: true});
    }
}