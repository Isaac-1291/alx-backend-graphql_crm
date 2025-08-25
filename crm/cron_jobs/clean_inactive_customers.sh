#!/bin/bash

# Go to project root (where manage.py is located)
cd "$(dirname "$0")/../.." || exit 1

# Run Django command to delete inactive customers and capture count
deleted_count=$(python manage.py shell -c '
import datetime
from django.utils import timezone
from crm.models import Customer

one_year_ago = timezone.now() - datetime.timedelta(days=365)
qs = Customer.objects.filter(orders__isnull=True, created_at__lt=one_year_ago)
count = qs.count()
qs.delete()
print(count)
' | tr -d '\n')

# Log result with timestamp
echo "$(date '+%Y-%m-%d %H:%M:%S') - Deleted $deleted_count inactive customers" >> /tmp/customer_cleanup_log.txt