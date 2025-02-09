import streamlit as st
import vertexai
from vertexai.generative_models import GenerativeModel, ChatSession
from google.cloud import storage
import PyPDF2
import io
from functools import lru_cache
from typing import Optional
import logging

# Constants
BUCKET_NAME = "streamlit-portfolio"
RESUME_BLOB_NAME = "Dhruv_Shah_Master_Resume.docx.pdf"
PROJECT_ID = "ba882-dhruv"
LOCATION = "us-central1"
MAX_RETRIES = 3

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@lru_cache(maxsize=1)
def init_vertex_ai(project_id: str = PROJECT_ID, location: str = LOCATION) -> None:
    """Initialize Vertex AI with caching to prevent repeated initializations"""
    try:
        vertexai.init(project=project_id, location=location)
        logger.info("Vertex AI initialized successfully")
    except Exception as e:
        logger.error(f"Failed to initialize Vertex AI: {str(e)}")
        raise

@lru_cache(maxsize=1)
def load_resume_from_gcs(bucket_name: str = BUCKET_NAME, blob_name: str = RESUME_BLOB_NAME) -> str:
    """Load and extract text from PDF resume in GCS with caching"""
    try:
        storage_client = storage.Client()
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(blob_name)
        
        # Download PDF content with retry logic
        for attempt in range(MAX_RETRIES):
            try:
                pdf_content = blob.download_as_bytes()
                break
            except Exception as e:
                if attempt == MAX_RETRIES - 1:
                    raise
                logger.warning(f"Attempt {attempt + 1} failed, retrying...")
                continue
        
        pdf_file = io.BytesIO(pdf_content)
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        
        # Optimize text extraction
        resume_text = " ".join(
            page.extract_text().strip() 
            for page in pdf_reader.pages
        )
        
        logger.info("Resume loaded successfully")
        return resume_text
    except Exception as e:
        logger.error(f"Failed to load resume: {str(e)}")
        return ""

def get_chat_response(
    chat: ChatSession, 
    prompt: str, 
    resume_context: str = "",
    max_retries: int = MAX_RETRIES
) -> str:
    """Get response from chat model with resume context and retry logic"""
    try:
        if resume_context:
            contextualized_prompt = f"""Context from resume: {resume_context}
            User question: {prompt}
            Please answer based on the resume context if relevant, otherwise provide a general response."""
        else:
            contextualized_prompt = prompt

        # Implement retry logic for API calls
        for attempt in range(max_retries):
            try:
                text_response = []
                responses = chat.send_message(contextualized_prompt, stream=True)
                for chunk in responses:
                    text_response.append(chunk.text)
                return "".join(text_response)
            except Exception as e:
                if attempt == max_retries - 1:
                    raise
                logger.warning(f"Attempt {attempt + 1} failed, retrying...")
                continue
                
    except Exception as e:
        logger.error(f"Failed to get chat response: {str(e)}")
        return "I apologize, but I encountered an error. Please try again."

def create_chat_header():
    """Create the chat header component that only shows the latest message"""
    try:
        # Initialize session states
        if "current_message" not in st.session_state:
            st.session_state.current_message = None
        if "current_response" not in st.session_state:
            st.session_state.current_response = None
        
        # Initialize Vertex AI and model
        if "chat_session" not in st.session_state:
            init_vertex_ai()
            model = GenerativeModel("gemini-1.5-flash-002")
            st.session_state.chat_session = model.start_chat(response_validation=False)
        
        # Load resume
        if "resume_text" not in st.session_state:
            st.session_state.resume_text = load_resume_from_gcs()

        # Chat interface with reset button
        with st.container():
            col1, col2 = st.columns([9, 1])
            
            with col1:
                if prompt := st.chat_input("Feel free to ask this chatbot anything about me! This chatbot is powered by Gemini 1.5 and is trained on information about me."):
                    st.session_state.current_message = prompt
                    
                    if st.session_state.chat_session:
                        response = get_chat_response(
                            st.session_state.chat_session,
                            prompt,
                            st.session_state.resume_text
                        )
                        st.session_state.current_response = response
                        st.rerun()

            with col2:
                if st.button("Reset Chat", type="secondary", use_container_width=True):
                    st.session_state.current_message = None
                    st.session_state.current_response = None
                    if "chat_session" in st.session_state:
                        del st.session_state.chat_session
                    st.rerun()

            # Display only the current message and response
            if st.session_state.current_message:
                with st.chat_message("user"):
                    st.markdown(st.session_state.current_message)
                
                if st.session_state.current_response:
                    with st.chat_message("assistant"):
                        st.markdown(st.session_state.current_response)

    except Exception as e:
        logger.error(f"An error occurred in the chat interface: {str(e)}")
        st.error(f"An error occurred in the chat interface: {str(e)}")

# Export the chat header function
__all__ = ['create_chat_header']
