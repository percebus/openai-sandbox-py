# SRC: https://gist.github.com/mihow/9c7f559807069a03e302605691f85572

# export $( grep -vE "^(#.*|\s*)$" .env )

set -a;
source .env;
set +a
