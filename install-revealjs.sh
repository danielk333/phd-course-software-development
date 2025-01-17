#!/bin/bash

# or another version,
# or branch name (although not recommended as might break suddenly)
reveal_version=${1:-'5.1.0'}

echo "Installing reveal.js"
wget -q --show-progress https://github.com/hakimel/reveal.js/archive/${reveal_version}.tar.gz
# Path used by gitlab pages is "public"
mkdir revealjs
tar -xf "${reveal_version}.tar.gz" -C revealjs --strip-components 1

# dist and plugin dirs are the only ones used in production
mv -n revealjs/dist revealjs/plugin .

echo "installing plugins"
wget -q --show-progress https://raw.githubusercontent.com/denniskniep/reveal.js-plugin-spotlight/master/spotlight.js
mkdir plugin/spotlight
mv spotlight.js plugin/spotlight/

# support the npm start auto-reload use case
mv -n revealjs/package.json revealjs/package-lock.json revealjs/gulpfile.js .
cat custom-gulp.js >> gulpfile.js

# tidy up source files not referred to from index.html
rm -rf revealjs
rm -f ${reveal_version}.tar.gz
echo "reveal.js Done"

echo "installing custom CSS"
cp -v css/theme/*.css dist/theme/
echo "Done"
