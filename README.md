# rabbitmq-cluster
Proof of concept rabbitmq cluster using docker container. Auto-discovery and mirror queue via management.load_definitions. Producer and Consumer setup in separate containers.

---

# Prerequisites
- docker
- docker-compose

---

# Usage
Start RabbitMQ Cluster: 
```
docker-compose up
```

Start Producer and Consumer:
```
cd messages
docker-compose up
```

Notes:
- Sometimes cluster container may crash, ctrl-c and start the cluster again.
- Must wait till cluster fully started before starting producer and consumer. Otherwise they will not be able to connect to the broker and container would exit.
- Can log into the web interface via: `localhost:8080` with username/password: `admin/password`. You may want to change the password through web interface after log in.
- If creating a new user for producer/consumer, make sure the user have necessary permission set for the queue. Refer to [Documentation](https://www.rabbitmq.com/access-control.html) for more details.
---

# Environment Variables:
Broker:
`RABBITMQ_ERLANG_COOKIE`: String of Erlang cookie for the brokers. They must be identical for all broker nodes.

Producer/Consumer:
`BROKER_HOST`: DNS Hostname of broker node that producer/consumer connects to.
`RABBIT_USER`: Username for producer/consumer to log into rabbitmq cluster. Default `admin`.
`RABBIT_PASS`: Password for producer/consumer to log into rabbitmq cluster. Default `password`.
