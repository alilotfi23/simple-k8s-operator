import kopf  # Importing the Kopf framework for building Kubernetes operators
from kubernetes import client, config  # Importing Kubernetes client and config modules


@kopf.on.create('sample.com', 'v1', 'helloworlds')  # Event handler for creating 'helloworlds' resources
def create_fn(body, **kwargs):
    # Load Kubernetes configuration from the default location (usually ~/.kube/config)
    config.load_kube_config()  
    # Create an instance of the CoreV1Api to interact with Kubernetes core resources
    api_instance = client.CoreV1Api()

    # Retrieve the number of replicas from the resource spec, defaulting to 2 if not specified
    replicas = body['spec'].get('replicas', 2)
    # Retrieve the container image from the resource spec, defaulting to 'hello-world' if not specified
    image = body['spec'].get('image', 'hello-world')

    # Loop to create the specified number of pod replicas
    for i in range(replicas):
        # Define the pod manifest with necessary specifications
        pod_manifest = {
            "apiVersion": "v1",  # Specify the API version
            "kind": "Pod",  # Specify the kind of resource
            "metadata": {
                "name": f"hello-world-{i+1}",  # Name the pod uniquely based on the index
                "labels": {"app": "hello-world"}  # Add labels for identification
            },
            "spec": {
                "containers": [{  # Define the container specifications
                    "name": "hello-world",  # Name of the container
                    "image": image,  # Container image to use
                    "ports": [{"containerPort": 80}]  # Expose port 80
                }]
            }
        }

        # Create the pod in the 'default' namespace using the defined manifest
        api_instance.create_namespaced_pod(namespace='default', body=pod_manifest)


if __name__ == '__main__':
    # Run the Kopf operator, allowing it to handle events from the Kubernetes API
    kopf.run(default_registry=None)
