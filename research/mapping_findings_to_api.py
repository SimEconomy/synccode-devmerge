from dev_merge.models import APIEndpoints

# Define API endpoints based on findings
api_endpoints = [
    {'name': 'integration_complexity', 'description': 'Endpoints for handling integration complexity.'},
    {'name': 'fast_feedback_loops', 'description': 'Endpoints for reducing feedback loops.'},
    {'name': 'developer_productivity', 'description': 'Endpoints for improving developer productivity.'},
    {'name': 'security', 'description': 'Endpoints for enhancing security.'},
    {'name': 'scalability', 'description': 'Endpoints for addressing scalability and maintenance issues.'}
]

# Create APIEndpoints objects
for endpoint in api_endpoints:
    APIEndpoints.objects.create(**endpoint)