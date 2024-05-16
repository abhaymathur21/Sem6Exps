# Dockerfile
FROM python:alpine3.8

# Create a directory to store your HTML files
WORKDIR /app
COPY index.html /app/

# Expose port 8000 to access the server
EXPOSE 8000

# Start a simple HTTP server to serve the HTML file
CMD ["python", "-m", "http.server", "8000"]



