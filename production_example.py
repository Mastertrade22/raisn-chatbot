"""
Production Integration Examples
Demonstrates how to integrate chatbot_core into production applications
"""

# ============================================================================
# EXAMPLE 1: FastAPI REST API
# ============================================================================

"""
Install: pip install fastapi uvicorn

Run: uvicorn production_example:app --reload
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from chatbot_core import create_chatbot
from config import AVAILABLE_MODELS

# Initialize FastAPI app
app = FastAPI(
    title="Real Estate Chatbot API",
    description="Production-ready chatbot API for real estate queries",
    version="1.0.0"
)

# Initialize chatbot (do this once at startup)
chatbot_instances = {}

@app.on_event("startup")
async def startup_event():
    """Initialize chatbots on startup"""
    try:
        for model_key, model_info in AVAILABLE_MODELS.items():
            chatbot_instances[model_key] = create_chatbot(model_id=model_info['id'])
        print("✅ Chatbots initialized successfully")
    except Exception as e:
        print(f"❌ Failed to initialize chatbots: {e}")


# Request/Response models
class ChatRequest(BaseModel):
    question: str
    model: Optional[str] = "qwen"  # Default model
    preserve_history: Optional[bool] = True


class ChatResponse(BaseModel):
    answer: str
    query_type: str
    sql_query: Optional[str] = None
    error: Optional[str] = None


@app.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    """
    Chat endpoint - ask questions to the chatbot

    Args:
        request: ChatRequest with question and optional model selection

    Returns:
        ChatResponse with answer and metadata
    """
    try:
        # Validate model
        if request.model not in chatbot_instances:
            raise HTTPException(
                status_code=400,
                detail=f"Invalid model. Available: {list(chatbot_instances.keys())}"
            )

        # Get chatbot instance
        chatbot = chatbot_instances[request.model]

        # Get response
        response = chatbot.ask(
            question=request.question,
            preserve_history=request.preserve_history
        )

        # Return formatted response
        return ChatResponse(
            answer=response['final_answer'],
            query_type=response['query_type'],
            sql_query=response.get('sql_query', ''),
            error=response.get('error', '')
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/chat/reset")
async def reset_chat(model: str = "qwen"):
    """Reset chat history for a specific model"""
    try:
        if model not in chatbot_instances:
            raise HTTPException(
                status_code=400,
                detail=f"Invalid model. Available: {list(chatbot_instances.keys())}"
            )

        chatbot_instances[model].reset_history()
        return {"status": "success", "message": f"Chat history reset for {model}"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/models")
async def list_models():
    """List available models"""
    return {
        "models": list(chatbot_instances.keys()),
        "default": "qwen"
    }


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "chatbots_loaded": len(chatbot_instances)
    }


# ============================================================================
# EXAMPLE 2: Flask REST API
# ============================================================================

"""
Install: pip install flask flask-cors

Run: python production_example.py (uncomment Flask section)
"""

# from flask import Flask, request, jsonify
# from flask_cors import CORS
# from chatbot_core import create_chatbot
#
# flask_app = Flask(__name__)
# CORS(flask_app)
#
# # Initialize chatbot
# chatbot = create_chatbot()
#
# @flask_app.route('/chat', methods=['POST'])
# def flask_chat():
#     """Chat endpoint"""
#     data = request.get_json()
#     question = data.get('question')
#
#     if not question:
#         return jsonify({"error": "No question provided"}), 400
#
#     try:
#         response = chatbot.ask(question)
#         return jsonify(response), 200
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500
#
# @flask_app.route('/health', methods=['GET'])
# def flask_health():
#     """Health check"""
#     return jsonify({"status": "healthy"}), 200
#
# if __name__ == '__main__':
#     flask_app.run(host='0.0.0.0', port=5000, debug=True)


# ============================================================================
# EXAMPLE 3: AWS Lambda Handler
# ============================================================================

"""
Deployment:
1. Package code: zip -r lambda.zip chatbot_core.py config.py database.py llm_client.py real_estate_db.py
2. Upload to AWS Lambda
3. Set environment variables (OPENROUTER_API_KEY)
4. Configure API Gateway trigger
"""

# import json
# from chatbot_core import create_chatbot
#
# # Initialize chatbot outside handler for reuse across invocations
# chatbot = None
#
# def lambda_handler(event, context):
#     """
#     AWS Lambda handler
#
#     Event format:
#     {
#         "question": "How many projects are under construction?"
#     }
#     """
#     global chatbot
#
#     # Lazy initialization
#     if chatbot is None:
#         chatbot = create_chatbot()
#
#     try:
#         # Parse request
#         body = json.loads(event.get('body', '{}'))
#         question = body.get('question')
#
#         if not question:
#             return {
#                 'statusCode': 400,
#                 'body': json.dumps({'error': 'No question provided'})
#             }
#
#         # Get response
#         response = chatbot.ask(question, preserve_history=False)
#
#         return {
#             'statusCode': 200,
#             'headers': {
#                 'Content-Type': 'application/json',
#                 'Access-Control-Allow-Origin': '*'
#             },
#             'body': json.dumps(response)
#         }
#
#     except Exception as e:
#         return {
#             'statusCode': 500,
#             'body': json.dumps({'error': str(e)})
#         }


# ============================================================================
# EXAMPLE 4: Simple Python Script Integration
# ============================================================================

def simple_integration_example():
    """
    Simple example of integrating chatbot into your Python application
    """
    from chatbot_core import create_chatbot

    # Initialize chatbot
    chatbot = create_chatbot()

    # Example: Process user queries from a queue
    user_queries = [
        "How many projects are under construction?",
        "Show me all 3BHK units",
        "What is the average price per sqft?"
    ]

    results = []
    for query in user_queries:
        response = chatbot.ask(query)
        results.append({
            "query": query,
            "answer": response['final_answer'],
            "metadata": {
                "type": response['query_type'],
                "sql": response.get('sql_query', '')
            }
        })

    return results


# ============================================================================
# EXAMPLE 5: Batch Processing
# ============================================================================

def batch_processing_example():
    """
    Example of batch processing multiple queries
    """
    from chatbot_core import create_chatbot
    import json

    # Initialize chatbot
    chatbot = create_chatbot()

    # Load queries from file
    queries = [
        "How many projects are there?",
        "List all 2BHK apartments",
        "What's the price range for villas?"
    ]

    # Process all queries
    results = []
    for idx, query in enumerate(queries):
        print(f"Processing query {idx + 1}/{len(queries)}: {query}")
        response = chatbot.ask(query, preserve_history=False)
        results.append({
            "id": idx + 1,
            "query": query,
            "answer": response['final_answer'],
            "type": response['query_type'],
            "sql": response.get('sql_query', ''),
            "error": response.get('error', '')
        })

    # Save results
    with open('batch_results.json', 'w') as f:
        json.dump(results, f, indent=2)

    print(f"✅ Processed {len(results)} queries. Results saved to batch_results.json")
    return results


# ============================================================================
# EXAMPLE 6: Custom Application Integration
# ============================================================================

class RealEstateAssistant:
    """
    Custom wrapper around chatbot_core for your specific application
    """

    def __init__(self, model_id: str = "qwen/qwen-2.5-72b-instruct"):
        from chatbot_core import create_chatbot
        self.chatbot = create_chatbot(model_id=model_id)
        self.query_log = []

    def ask(self, question: str) -> str:
        """
        Ask a question and get an answer

        Args:
            question: User's question

        Returns:
            str: Plain text answer
        """
        response = self.chatbot.ask(question)

        # Log the query
        self.query_log.append({
            "question": question,
            "answer": response['final_answer'],
            "type": response['query_type']
        })

        return response['final_answer']

    def get_detailed_response(self, question: str) -> dict:
        """
        Get detailed response with metadata

        Args:
            question: User's question

        Returns:
            dict: Complete response with metadata
        """
        return self.chatbot.ask(question)

    def clear_history(self):
        """Clear chat history"""
        self.chatbot.reset_history()
        self.query_log = []

    def get_query_stats(self) -> dict:
        """Get statistics about queries"""
        total = len(self.query_log)
        data_queries = sum(1 for q in self.query_log if q['type'] == 'data')
        general_queries = total - data_queries

        return {
            "total_queries": total,
            "data_queries": data_queries,
            "general_queries": general_queries
        }


# ============================================================================
# Testing
# ============================================================================

if __name__ == "__main__":
    print("🧪 Running production integration examples...\n")

    # Example 4: Simple integration
    print("=" * 70)
    print("Example 4: Simple Integration")
    print("=" * 70)
    results = simple_integration_example()
    for r in results:
        print(f"\nQ: {r['query']}")
        print(f"A: {r['answer'][:100]}...")

    # Example 6: Custom application
    print("\n" + "=" * 70)
    print("Example 6: Custom Application Wrapper")
    print("=" * 70)
    assistant = RealEstateAssistant()
    answer = assistant.ask("How many projects are there?")
    print(f"\nAnswer: {answer}")
    stats = assistant.get_query_stats()
    print(f"Stats: {stats}")

    print("\n✅ All examples completed!\n")
