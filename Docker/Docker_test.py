import docker
import logging
import time



client = docker.from_env()

# Create and run a container
container = client.containers.run(
    image='hello-world',  # Using a simple test image
    detach=True,  # Run in detached mode (background)
    name='my_test_container'
)


# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Log container information
logger.info(f"Container created with ID: {container.id}")
logger.info(f"Container status: {container.status}")

# Wait for 2 seconds

time.sleep(2)


# Stop and remove the container
try:
    container.stop()
    container.remove()
    logger.info("Container stopped and removed successfully")
except docker.errors.APIError as e:
    logger.error(f"Error stopping/removing container: {e}")
