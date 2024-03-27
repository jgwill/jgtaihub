FROM lightsing/openai-hub



COPY config.toml acl.toml /opt/openai-hub/config/
CMD ["/opt/openai-hub/openai-hubd", "-c", "config/config.toml", "-a", "config/acl.toml"]
