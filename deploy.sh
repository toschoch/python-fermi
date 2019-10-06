gittool tag v$1
docker build . -t shocki/fermiapp:$1
docker push shocki/fermiapp:$1