"""
LLM Client Module
Handles all interactions with the OpenRouter API
"""

import requests
from typing import Optional
from config import (
    OPENROUTER_API_URL,
    OPENROUTER_API_KEY,
    API_TIMEOUT,
    ERROR_MESSAGES
)


class OpenRouterLLM:
    """OpenRouter API client with error handling"""

    def __init__(self, model_id: str, api_key: Optional[str] = None, temperature: float = 0.3):
        """
        Initialize LLM client

        Args:
            model_id: The model identifier (e.g., "qwen/qwen-2.5-72b-instruct")
            api_key: Optional API key (defaults to config)
            temperature: Temperature for generation (0.0-1.0)
        """
        self.model_id = model_id
        self.api_key = api_key or OPENROUTER_API_KEY
        self.temperature = temperature
        self.base_url = OPENROUTER_API_URL

        if not self.api_key:
            raise ValueError("API key is required. Set OPENROUTER_API_KEY in environment.")

    def invoke(self, prompt: str, system_prompt: Optional[str] = None) -> str:
        """
        Call the OpenRouter API with error handling

        Args:
            prompt: User prompt/question
            system_prompt: Optional system instructions

        Returns:
            str: The model's response

        Raises:
            Exception: For API errors with user-friendly messages
        """
        try:
            messages = []

            if system_prompt:
                messages.append({"role": "system", "content": system_prompt})

            messages.append({"role": "user", "content": prompt})

            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }

            payload = {
                "model": self.model_id,
                "messages": messages,
                "temperature": self.temperature
            }

            response = requests.post(
                self.base_url,
                headers=headers,
                json=payload,
                timeout=API_TIMEOUT
            )
            response.raise_for_status()

            result = response.json()
            return result["choices"][0]["message"]["content"]

        except requests.exceptions.Timeout:
            raise Exception(ERROR_MESSAGES["api_timeout"])
        except requests.exceptions.ConnectionError:
            raise Exception(ERROR_MESSAGES["api_connection"])
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 401:
                raise Exception(ERROR_MESSAGES["invalid_api_key"])
            elif e.response.status_code == 429:
                raise Exception(ERROR_MESSAGES["rate_limit"])
            else:
                raise Exception(f"API error: {str(e)}")
        except KeyError:
            raise Exception("Unexpected API response format.")
        except Exception as e:
            raise Exception(ERROR_MESSAGES["unexpected"].format(error=str(e)))


def create_llm_client(model_id: str, temperature: float = 0.3) -> OpenRouterLLM:
    """
    Factory function to create LLM client

    Args:
        model_id: Model identifier
        temperature: Generation temperature

    Returns:
        OpenRouterLLM: Configured LLM client
    """
    return OpenRouterLLM(model_id=model_id, temperature=temperature)
