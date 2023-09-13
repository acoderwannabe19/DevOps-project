#!/bin/bash

set -e

host="$1"
shift
cmd="$@"

until PGPASSWORD=$DJANGO_DB_PASSWORD psql -h "$host" -U "$DJANGO_DB_USER" -d "$DJANGO_DB_NAME" -c '\q'; do
  >&2 echo "PostgreSQL is unavailable - sleeping"
  sleep 1
done

>&2 echo "PostgreSQL is up - executing command"
exec $cmd
