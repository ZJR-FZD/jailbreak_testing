# models/openai_models.py
import openai
from .base import BaseModel

class OpenAIModel(BaseModel):
    """OpenAI 模型接口"""
    
    def __init__(self, name: str, config: Dict[str, Any] = None):
        super().__init__(name, config)
        self.client = openai.OpenAI(api_key=config.get('api_key'))
        self.model_name = config.get('model_name', 'gpt-3.5-turbo')
    
    def generate(self, prompt: str, **kwargs) -> str:
        try:
            response = self.client.chat.completions.create(
                model=self.model_name,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=kwargs.get('max_tokens', 1000),
                temperature=kwargs.get('temperature', 0.7)
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error: {str(e)}"