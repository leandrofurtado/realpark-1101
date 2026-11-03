#!/usr/bin/env bash
# Gera o 3d.html a partir de _fonte/3d-fonte.js. Rodar na raiz do repositório.
set -e
cd "$(dirname "$0")"
[ -d node_modules/three ] || npm i --no-save three@0.160.0 esbuild@0.20.2
npx esbuild 3d-fonte.js --bundle --format=iife --target=safari13 --minify-syntax --minify-whitespace \
  --alias:three/addons=./node_modules/three/examples/jsm --outfile=/tmp/bundle3d.js
python3 - <<'P'
b=open('/tmp/bundle3d.js').read(); assert '</script' not in b.lower()
c=open('3d-casca.html').read(); open('../3d.html','w').write(c.replace('/*BUNDLE*/',b,1)); print('3d.html gerado')
P
