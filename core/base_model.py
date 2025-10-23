# core/base_model.py
from abc import ABC, abstractmethod

class BaseModel(ABC):
    """模型基类"""
    
    def __init__(self, name: str, config: Dict[str, Any] = None):
        self.name = name
        self.config = config or {}
    
    @abstractmethod
    def generate(self, prompt: str, **kwargs) -> str:
        """生成回复"""
        pass
    
    def check_safety(self, response: str) -> bool:
        """检查回复安全性（基础实现）"""
        dangerous_keywords = ["抱歉", "我不能", "非法", "危险", "harmful"]
        return not any(keyword in response for keyword in dangerous_keywords)