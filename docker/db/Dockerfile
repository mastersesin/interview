FROM mysql:8.0.32

WORKDIR /sql
# Set the root password
ENV MYSQL_ROOT_PASSWORD=123

# Copy the SQL script to initialize the database
COPY docker/db/init.sql /sql