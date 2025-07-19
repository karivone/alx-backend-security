from django.core.management.base import BaseCommand
from ip_tracking.models import BlockedIP

class Command(BaseCommand):
    """
    Command to block an IP address by adding it to the BlockedIP model.
    Usage: python manage.py block_ip <ip_address>
    """

    help = 'Block an IP address by adding it to the BlockedIP model.'

    def add_arguments(self, parser):
        parser.add_argument('ip_address', type=str, help='The IP address to block.')

    def handle(self, *args, **kwargs):
        ip_address = kwargs['ip_address']
        block_ip(ip_address)

def block_ip(ip_address):
    """
    Block an IP address by adding it to the BlockedIP model.
    """

    if not BlockedIP.objects.filter(ip_address=ip_address).exists():
        blocked_ip = BlockedIP(ip_address=ip_address)
        blocked_ip.save()
        print(f"Blocked IP: {ip_address}")
    else:
        print(f"IP {ip_address} is already blocked.")
