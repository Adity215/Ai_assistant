import os
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from elevenlabs.conversational_ai.conversation import Conversation
from elevenlabs.conversational_ai.default_audio_interface import DefaultAudioInterface

# Load environment variables
load_dotenv()

AGENT_ID = os.getenv("AGENT_ID")
API_KEY = os.getenv("API_KEY")

# Initialize ElevenLabs client
client = ElevenLabs(api_key=API_KEY)

# Create conversation with your agent
conversation = Conversation(
    client=client,
    agent_id=AGENT_ID,
    requires_auth=True,
    audio_interface=DefaultAudioInterface(),
)

if __name__ == "__main__":
    print("🎤 Starting your AI voice assistant... (Press Ctrl+C to quit)")
    conversation.start_session()
