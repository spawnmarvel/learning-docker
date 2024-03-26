# version: '3.8'
services:
  grafana:
    # https://grafana.com/docs/grafana/latest/setup-grafana/configure-docker/
    image: grafana/grafana-oss
    container_name: grafana
    restart: unless-stopped
    environment:
      # increases the log level from info to debug
      - GF_LOG_LEVEL=debug
      - GF_SECURITY_ADMIN_USER=linuxuser
      - GF_SECURITY_ADMIN_PASSWORD=Minime789gotooslo
    ports:
      - '3000:3000'
    volumes:
      - vol_grafana:/var/lib/grafana
volumes:
  vol_grafana: