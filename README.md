# Tutorial em Português

# Usando Flask e MySQL com docker-compose :triangular_flag_on_post:    


---

## Diagrama
<img src="pydbcompose.png"/>


## Requisitos

- Docker Compose
- Python
- Flask


## Vamos começar! :loudspeaker:

1. Clone este repositório em seu computador
```
git clone https://github.com/
```

2. Vá para a pasta contendo este projeto e o docker-compose.yml para usar os comandos abaixo.

    - Crias as imagens dos containers
    ```
    docker compose build
    ```

    - Iniciar os containers
    ```
    docker compose up
    ```

3. Verfifique se os containers estão rodando.
```
docker compose ps
```

## Dica!

Se o container que está rodando o MySQL iniciar depois do container da aplicação, execute os comandos abaixo.

- 
    ```
    docker compose down
    ```

- 
    ```
    docker compose up
    ```

## Acesse a página web da API

1. Vá para o navegador de sua preferência e acesse http://localhost:5000

    Se você ver está mensagem: 
    
    `
    API Rest - Olá Inoa
    `
    
    Tudo esta correndo bem.
    
2. Acesse o endpoint http://localhost:5000/message da nossa API.
    
    Se você receber este retorno:
    
    `
    {
        "messages": {
            "1": "Ola, Inoa!"
        }
    }
    `
    
    Tudo está correto!

## Simplificando usango o script para executar esses processos de forma automatizada

1. Abra o arquivo pydbcompose.sh e mude o caminho que está na linha 5 pelo caminho onde no seu computador está o docker-compose.yml

2. Execute o comando abaixo, espere e volte para o passo anterior (Acesse a página web da API).
```
bash pydbcompose.sh
```

    
## Finalizamos com sucesso! :rocket:


---
---

# Tutorial in English

# Connecting Flask and MySQL with docker-compose :triangular_flag_on_post: 


---

## Diagram
<img src="pydbcompose.png"/>


## Requeriments

- Docker Compose
- Python
- Flask


## Let's start :loudspeaker:

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

## Using bash script to running these containers

1. Open the pydbcompose.sh and change the path on line 5 by the path of your docker-compose.yaml (something like /opt/app/pydbcompose)

2. Run the following command, wait and follow to the previous step (Acess simple web API).
```
bash pydbcompose.sh
```

    
## Well done! :rocket: