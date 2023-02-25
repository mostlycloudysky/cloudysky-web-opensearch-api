# cloudysky-web-opensearch-api


```
curl -XGET "http://localhost:9200/_search" -H 'Content-Type: application/json' -d'
{
  "query": {
    "match_phrase_prefix": {
      "title": {
        "query": "how to use aws secret manager",
        "slop": 3,
        "max_expansions": 5
      }
    }
  }
}'
```
 
