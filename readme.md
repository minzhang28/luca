#### Luca version tracker

A simple version tracker tool which uses Python Falcon and Redis to save the version metadata

#### How to use it
- run `docker-compose up -d` 
- issue a `POST` request to `localhost:5000` with the payload
    ```bash
    {
      "project_name": "kafka",
      "project_url": "www.kafka.com",
      "project_env": "stg",
      "version": "0.5",
      "branch": "release",
      "git_hash": "3143214324RDASFEW",
      "user": "minzhang"
    }
    ```
- open browser and go to `localhost:38080`

#### It's flexible
You can post any JSON to `luca-api` server, it will automatically render the table on HTML page. 
In case if you need to sort your columns in the order you want, just add the following section in to the `index.html` file under `/usr/share/nginx/html` in the `minzhang/luca-web` docker, or fork the project form `https://github.com/minzhang28/luca-web`.
 
```bash

                data:json,
                schema: [
                  {"header":"Project Name", "key":"project_name"},
                  {"header":"Environment", "key":"project_env"},
                  {"header":"Build Branch", "key":"branch"},
                  {"header":"Version", "key":"version"},
                  {"header":"Commit Hash", "key":"git_hash"},
                  {"header":"Commit User", "key":"user"}
                ]
```
