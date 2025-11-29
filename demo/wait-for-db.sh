#!/bin/sh
set -e

host="$DB_HOST"
shift
cmd="$@"

echo "Waiting for database at $host..."

until pg_isready -h "$host" -p 5432 -U "$DB_USER"; do
  echo "Database not ready yet..."
  sleep 2
done

echo "Database is ready — starting app."
exec $cmd

