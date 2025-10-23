# core/results_manager.py
import json
import pandas as pd
from datetime import datetime
from typing import List, Dict, Any

class ResultsManager:
    """结果管理器"""
    
    def __init__(self, output_dir: str = "results"):
        self.output_dir = output_dir
        self.results = []
    
    def add_result(self, result: Dict[str, Any]):
        """添加单次测试结果"""
        result['timestamp'] = datetime.now().isoformat()
        self.results.append(result)
    
    def save_results(self, filename: str = None):
        """保存结果到文件"""
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"jailbreak_results_{timestamp}"
        
        # 保存为JSON
        json_path = f"{self.output_dir}/{filename}.json"
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(self.results, f, ensure_ascii=False, indent=2)
        
        # 保存为CSV
        csv_path = f"{self.output_dir}/{filename}.csv"
        df = pd.DataFrame(self.results)
        df.to_csv(csv_path, index=False, encoding='utf-8')
        
        return json_path, csv_path
    
    def get_summary_stats(self) -> Dict[str, Any]:
        """获取汇总统计"""
        if not self.results:
            return {}
        
        df = pd.DataFrame(self.results)
        summary = {
            'total_tests': len(df),
            'successful_attacks': df['success_rate'].sum(),
            'overall_success_rate': df['success_rate'].mean(),
            'by_attack_method': df.groupby('attack_method')['success_rate'].mean().to_dict(),
            'by_model': df.groupby('model_name')['success_rate'].mean().to_dict()
        }
        
        return summary