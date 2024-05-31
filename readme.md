### Subir o container
```shell
docker compose up -d
```

### Verificando a versão
```shell
docker exec ollama-server ollama --version
```

### Executando LLM no ollama
```shell
docker exec -it ollama-server ollama run llama2
```

### Listando modelos
```shell
docker exec ollama-server ollama list
```

### Removendo modelos
```shell
docker exec ollama-server ollama rm llama2
```

### Interface gráfica do ollama
```shell
docker run -d -p 3000:8080 --add-host=host.docker.internal:host-gateway -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:main
```

### Repositório do Open WebUI
```shell
git clone https://github.com/open-webui/open-webui.git
```