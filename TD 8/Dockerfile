# use an official nginx image
FROM nginx:1.24

# copy the HTML file at /usr/share/nginx/html
COPY index.html /usr/share/nginx/html

# expose port 80
EXPOSE 80

# healthcheck instruction
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD curl -f http://localhost/ || exit 1

# specify an user
USER nginx