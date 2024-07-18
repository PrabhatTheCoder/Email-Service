from rest_framework import serializers
from emailapi.utils import Util

class EmailSerializer(serializers.Serializer):
    email = serializers.EmailField()
    subject = serializers.CharField(max_length=255)
    body_text = serializers.CharField()
    cc_email = serializers.ListField(
        child=serializers.EmailField(), 
        required=False
    )
    attachments = serializers.ListField(
        child=serializers.FileField(), 
        required=False
    )

    class Meta:
        fields = ['email', 'subject', 'body_text', 'cc_email', 'attachments']

    def validate(self, attrs):
        to_email = attrs.get('email')
        subject = attrs.get('subject')
        body_text = attrs.get('body_text')
        cc_email = attrs.get('cc_email', [])
        attachments = attrs.get('attachments', [])

        print(f"Attachments: {attachments}")  # Add logging here

        data = {
            'to_email': to_email,
            'subject': subject,
            'body': body_text,
            'cc_email': cc_email,
            'attachments': attachments
        }

        try:
            Util.send_email(data)
        except Exception as e:
            raise serializers.ValidationError("Error sending email: " + str(e))
        return attrs
