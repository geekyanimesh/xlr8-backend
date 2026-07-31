import os
import resend
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Lead
from .serializers import LeadSerializer # We will create this next

# Initialize the Resend SDK with your API key
resend.api_key = os.environ.get("RESEND_API_KEY")

@api_view(['POST'])
def submit_lead(request):
    serializer = LeadSerializer(data=request.data)
    
    if serializer.is_valid():
        # Save the lead to the database (Django Admin)
        lead = serializer.save()
        
        # Prepare the email using Resend
        try:
            params = {
                "from": "Acme <onboarding@resend.dev>", # Replace with your verified domain later
                "to": ["your_email@example.com"], # Replace with your actual admin email
                "subject": f"New Project Lead: {lead.name}",
                "html": f"""
                    <h2>New Lead from xlr8 devs</h2>
                    <p><strong>Name:</strong> {lead.name}</p>
                    <p><strong>Email:</strong> {lead.email}</p>
                    <p><strong>Scope:</strong> {lead.scope}</p>
                    <p><strong>Budget:</strong> {lead.budget_range}</p>
                    <p><strong>Timeline:</strong> {lead.timeline}</p>
                """,
            }
            
            # Send the email
            email_response = resend.Emails.send(params)
            
            return Response({"message": "Lead submitted successfully", "id": lead.id}, status=status.HTTP_201_CREATED)
            
        except Exception as e:
             return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
             
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)