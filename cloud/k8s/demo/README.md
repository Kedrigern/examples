# K8S demo

```bash
cd demo/simple-app
eval $(minikube docker-env)     # hack for local container registry
docker build -t simple-app:latest .
cd ..
kubectl apply -f manifests/simple-app-deployment.yaml
kubectl apply -f manifests/simple-app-service.yaml

# Info
kubectl get deployments
kubectl get services
kubectl get pods -l app=simple-app

# Temp access from localhost
kubectl port-forward service/simple-app-service 8000:80

# Setup ingress
minikube addons list
minikube addons enable ingress

# Qemu is complicated
kubectl get pods -n ingress-nginx | grep controller
kubectl port-forward -n ingress-nginx ingress-nginx-controller-67c5cb88f-ff256 8080:80
curl -H "Host: simple.local" http://localhost:8080/
```
