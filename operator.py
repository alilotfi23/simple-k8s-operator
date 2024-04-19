import kopf
from kubernetes import client, config


@kopf.on.create('sample.com', 'v1', 'helloworlds')
def create_fn(body, **kwargs):
    config.load_kube_config()  # Load kube config from default location
    api_instance = client.CoreV1Api()

    replicas = body['spec'].get('replicas', 2)
    image = body['spec'].get('image', 'hello-world')

    for i in range(replicas):
        pod_manifest = {
            "apiVersion": "v1",
            "kind": "Pod",
            "metadata": {
                "name": f"hello-world-{i+1}",
                "labels": {"app": "hello-world"}
            },
            "spec": {
                "containers": [{
                    "name": "hello-world",
                    "image": image,
                    "ports": [{"containerPort": 80}]
                }]
            }
        }

        api_instance.create_namespaced_pod(namespace='default', body=pod_manifest)


if __name__ == '__main__':
    kopf.run(default_registry=None)
