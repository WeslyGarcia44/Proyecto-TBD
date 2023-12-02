# Import the Tenant class from the tenants.models module
from tenants.models import Tenant

# Define the TenantMiddleware class
class TenantMiddleware:
    # Initializer method for TenantMiddleware
    def __init__(self, get_response):
        # Assign the get_response argument to self.get_response
        self.get_response = get_response

    # Special method to allow instances to be called like a function
    def __call__(self, request):
        # Extract the hostname from the incoming HTTP request
        hostname = request.get_host().split(':')[0]
        # Assuming the first part of the hostname is the subdomain
        subdomain = hostname.split('.')[0]

        # Try to get the Tenant object that matches the subdomain
        try:
            request.tenant = Tenant.objects.get(subdomain=subdomain)
        except Tenant.DoesNotExist:
            # If no tenant is found, set request.tenant to None
            request.tenant = None

        # Call the next middleware in the chain with the request
        response = self.get_response(request)

        # Return the response obtained from the next middleware
        return response
