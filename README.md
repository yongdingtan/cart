# cart

This is a python Application which listen on port 5000 
Features : Add product to the cart 
Dependency - Python and flask 

### dockerise the app 
git clone your repo
cd cart 
docker buildx build -t dockerhub-id/cart:v1
docker run -itd --name c1 -p 80:5000 dockerhub-id/cart:v1 /bin/bash

