#!/usr/bin/env bash
# Ping IndexNow for snakewise.org. Usage: ./indexnow.sh URL [URL...]  (no args = all sitemap URLs)
KEY=a822d72a62a4cf99a3f79086eeace725
HOST=snakewise.org
if [ $# -eq 0 ]; then set -- $(curl -s https://$HOST/sitemap.xml | grep -o '<loc>[^<]*' | sed 's/<loc>//'); fi
LIST=$(printf '%s\n' "$@" | python3 -c 'import sys,json;print(json.dumps([l.strip() for l in sys.stdin if l.strip()]))')
curl -s -o /dev/null -w "IndexNow HTTP %{http_code} ($# URLs)\n" -X POST https://api.indexnow.org/indexnow \
  -H 'Content-Type: application/json; charset=utf-8' \
  -d "{\"host\":\"$HOST\",\"key\":\"$KEY\",\"keyLocation\":\"https://$HOST/$KEY.txt\",\"urlList\":$LIST}"
