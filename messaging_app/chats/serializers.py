from rest_framework import serializers
from .models import User, Message, Conversation


class UserSerializer(serializers.ModelSerializer):
	email = serializers.CharField(
        max_length=100,
        help_text="The email has a (max 100 characters)."
    )
	class Meta:
		model = User
		fields = ['user_id', 'username', 'email']

class MessageSerializer(serializers.ModelSerializer):

	last_activity = serializers.SerializerMethodField()
	class Meta:
		model = Message
		fields = ['message_id', 'sender_id', 'message_body', 'sent_at', 'last_activity']
	
	def get_last_activity(self, obj):
		"""Returns the timestamp of the last message, or creation time if no messages."""
		last_message = obj.messages.last()
		if last_message:
			return last_message.timestamp
		return obj.created_at
	
	def validate_message(self, msg):
		msg = Message.message_body
		if msg == None:
			raise serializers.ValidationError("Please write a message.")


class ConversationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Conversation
		fields = ['conversation_id', 'message_id', 'created_at']
