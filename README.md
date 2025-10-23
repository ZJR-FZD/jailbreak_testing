jailbreak_testing/
├── core/
│   ├── __init__.py
│   ├── base_attack.py      # 攻击基类
│   ├── base_model.py       # 模型基类
│   ├── evaluator.py        # 评估器
│   └── results_manager.py  # 结果管理
├── attacks/                # 各种越狱方法
│   ├── __init__.py
│   ├── base.py
│   ├── prompt_injection.py
│   ├── role_play.py
│   └── template_attack.py
├── models/                 # 各种模型接口
│   ├── __init__.py
│   ├── base.py
│   ├── openai_models.py
│   ├── anthropic_models.py
│   └── local_models.py     
├── configs/                # 配置文件
│   ├── default.yaml
│   └── attacks.yaml
├── utils/                  # 工具函数
│   ├── __init__.py
│   ├── logger.py
│   ├── helpers.py
│   ├── device_monitor.py
│   └── model_manager.py
├── main.py                 # 主执行文件
└── requirements.txt        # 依赖清单