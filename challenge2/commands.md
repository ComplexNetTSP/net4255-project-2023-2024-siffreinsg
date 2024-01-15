```
use movies
```

```
db.createCollection("movies")
```

```
db.movies.insertMany([
    {
        "name": "The Lord of the Rings: The Fellowship of the Ring",
        "year": 2001,
        "director": "Peter Jackson"
    },
    {
        "name": "The Lord of the Rings: The Two Towers",
        "year": 2002,
        "director": "Peter Jackson"
    },
    {
        "name": "The Lord of the Rings: The Return of the King",
        "year": 2003,
        "director": "Peter Jackson"
    }
])
```

```
db.movies.find().pretty()
```
