from rest_framework.views import exception_handler
from rest_framework.response import Response

def custom_exception_handler(exc, context):
    """
    Custom exception handler for consistent API error responses.
    """
    response = exception_handler(exc, context)
    
    if response is not None:
        response.data = {
            'status': 'error',
            'code': response.status_code,
            'message': response.data,
        }
    
    return response
