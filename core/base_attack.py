# core/base_attack.py
from abc import ABC, abstractmethod
from typing import Dict, Any, List
import logging

class BaseAttack(ABC):
    """攻击方法基类"""
    
    def __init__(self, name: str, config: Dict[str, Any] = None):
        self.name = name
        self.config = config or {}
        self.logger = logging.getLogger(f"attack.{name}")
    
    @abstractmethod
    def generate_prompt(self, original_prompt: str, **kwargs) -> str:
        """生成越狱提示词"""
        pass
    
    @abstractmethod
    def execute(self, model, prompt: str, **kwargs) -> str:
        """执行攻击"""
        pass