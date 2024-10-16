
# k8s Operator with my name

The **Ali Lotfi Operator** is a Kubernetes operator that manages the deployment of pods based on a custom resource definition (CRD) named `helloworlds`. This README overviews the project, installation instructions, and usage examples.

## Overview

This Operator automates the deployment of multiple pods running a "Hello World" application in a Kubernetes cluster. It uses Kopf, a Python framework for Kubernetes operators, to watch for changes in custom resources of type `helloworlds` and create corresponding pods based on the specifications provided.

## Installation

To deploy the Operator in your Kubernetes cluster, follow these steps:

1. **Clone the Repository:**

   ```bash
   git https://github.com/alilotfi23/simple-k8s-operator.git
   cd simple-k8s-operator
   ```

2. **Install Dependencies:**

   Ensure you have Python 3.6+ installed along with `pip`. Then, install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

3. **Deploy the Operator:**

   Deploy the operator into your Kubernetes cluster. This typically involves creating Custom Resource Definitions (CRDs) and deploying the operator as a Kubernetes deployment or pod.

   ```bash
   kubectl apply -f deploy/
   ```

   This command will apply the necessary Kubernetes manifests located in the `deploy/` directory, including the CRD definition and the operator deployment.

## Usage

Once the Operator is deployed, you can create instances of the `helloworlds` custom resource to automatically create pods in your Kubernetes cluster.

### Example Custom Resource

Create a YAML file (e.g., `hello-world.yaml`) with the following content to define a `helloworlds` resource:

```yaml
apiVersion: sample.com/v1
kind: HelloWorld
metadata:
  name: example-helloworld
spec:
  replicas: 3
  image: nginx:latest
```

### Apply the Custom Resource

Apply the custom resource definition to your Kubernetes cluster:

```bash
kubectl apply -f hello-world.yaml
```

### Verify Pods Creation

Check that the pods have been created:

```bash
kubectl get pods
```

You should see pods named `hello-world-1`, `hello-world-2`, etc., running the specified `nginx` image.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## Acknowledgments

- **Kopf**: Kubernetes Operator Framework for Python
- **Kubernetes Python Client**: Python client library for Kubernetes API

