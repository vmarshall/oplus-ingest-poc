  sudo rabbitmqctl add_user partner partner
  sudo rabbitmqctl add_vhost partner_vhost
  sudo rabbitmqctl set_user_tags partner partner_tag
  sudo rabbitmqctl set_permissions -p partner_vhost partner ".*" ".*" ".*"