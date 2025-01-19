# Use Nginx as the base image
FROM nginx:alpine

# Remove the default Nginx configuration
RUN rm -rf /usr/share/nginx/html/*

# Copy HTML, CSS, and JS files to Nginx's serving directory
COPY . /usr/share/nginx/html

# Expose port 80 for the service
EXPOSE 80

# Start Nginx when the container runs
CMD ["nginx", "-g", "daemon off;"]
