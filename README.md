# Connecting Flask and MySQL with docker-compose    

**Note: Tested on Windows 11**

---

## Simplified Diagram
<img src="pydbcompose.png"/>


## Requeriments

- Docker Compose
- Python
- Flask


## Let's start

1. Clone this repo on your computer
```
git clone https://github.com/
```
2. Move to the folder containing the project and docker-compose.yml, to run the following commands.

    - Build docker images
    ```
    docker compose build
    ```

    - Running containers
    ```
    docker compose up
    ```

3. Check if the containers are running.
```
docker compose ps
```

## Good to know

If the Mysql container runs after app container, you can following this commands to solve this issue.

- 
    ```
    docker compose down
    ```

- 
    ```
    docker compose up
    ```

## Acess simple web API

1. Go to the browser of your preference and acess http://localhost:5000

    If you see this message: 
    
    `
    API Rest - Olá Inoa
    `
    
    Everything is working fine.
    
2. Acess the endpoint http://localhost:5000/message of the API.
    If you see this return:
    
    `
    {
        "messages": {
            "1": "Ola, Inoa!"
        }
    }
    `
    
    Everithing is ok!
    
## Well done! :rocket: