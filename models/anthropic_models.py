# models/anthropic_models.py
import anthropic
from .base import BaseModel

class AnthropicModel(BaseModel):
    """Anthropic 模型接口"""
    
    def __init__(self, name: str, config: Dict[str, Any] = None):
        super().__init__(name, config)
        self.client = anthropic.Anthropic(api_key=config.get('api_key'))
        self.model_name = config.get('model_name', 'claude-3-sonnet-20240229')
    
    def generate(self, prompt: str, **kwargs) -> str:
        try:
            response = self.client.messages.create(
                model=self.model_name,
                max_tokens=kwargs.get('max_tokens', 1000),
                temperature=kwargs.get('temperature', 0.7),
                messages=[{"role": "user", "content": prompt}]
            )
            return response.content[0].text
        except Exception as e:
            return f"Error: {str(e)}"