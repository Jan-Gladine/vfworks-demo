# RobosapiensIO Backend

This repository contains the backend setup for the RobosapiensIO framework, used to develop and commission trustworthy self-adaptive systems using the RoboSAPIENS Adaptive Platform architecture. It includes the following services bundled in a Docker Compose configuration:

- **EMQX Enterprise MQTT Broker**
- **Redis**

## Prerequisites

Before you begin, ensure you have the following installed on your system:

1. [Docker](https://docs.docker.com/get-docker/)
2. [Docker Compose](https://docs.docker.com/compose/install/)

## Getting Started

Follow these steps to spin up the RobosapiensIO backend:

1. Clone the repository:
   ```bash
   git clone https://github.com/BertVanAcker/rpio-backend-docker.git
   cd rpio-backend-docker
   ```

2. Start the services using Docker Compose:
   ```bash
   docker compose up --detach
   ```

   This command will pull the required images (if not already present) and start the EMQX Enterprise MQTT Broker and Redis services in the background and leaves them running.

3. Verify that the services are running:
   - EMQX MQTT Broker should be accessible on its default port (e.g., `1883` for MQTT and `8081` for the dashboard).
   - Redis will be running on its default port (`6379`).

## Stopping the Services

To stop the running services, use:
```bash
docker compose down
```
This command will stop and remove the containers but will retain the images and volumes.

## Configuration

- Configuration files for EMQX and Redis can be found in the `Resources/` directory (`acl.conf; redis.conf`).
- You can customize the `compose.yaml` file to change ports, volumes, or other settings as needed.

## Troubleshooting

- Ensure Docker and Docker Compose are installed correctly.
- Use `docker compose logs` to view service logs for debugging.
- Check for port conflicts with other services running on your machine.

## References

- [EMQX Enterprise Documentation](https://www.emqx.com/en/docs)
- [Redis Documentation](https://redis.io/docs)
- [Docker Documentation](https://docs.docker.com/)
- [Docker Compose Documentation](https://docs.docker.com/compose/)
