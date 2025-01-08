## Docker Monitoring API

This is a simple API that allows you to monitor your Docker containers. It is built using Python and FastAPI.

### Running with Docker

1. Clone the repository
2. Open directory
3. Change IP address in `docker-compose.yml` to your local IP address
4. Start with docker compose
```bash
docker-compose up -d
```

### How To Use

1. List Containers
```bash
curl http://localhost:8000/containers
```

2. Get Container Info
```bash
curl http://localhost:8000/containers/{container_name}
```

3. Get Container Status
```bash
curl http://localhost:8000/containers/status/{container_nam}
```
