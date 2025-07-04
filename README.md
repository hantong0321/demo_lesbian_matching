# 拉拉匹配系统 (LaLa Matching System)

一个基于硬条件和软条件的智能用户匹配系统，专为拉拉社区设计。

## 🚀 功能特点

### 硬条件匹配
- **性别和性取向**：确保基本匹配
- **年龄范围**：支持年龄偏好和差异限制
- **地理位置**：支持同城、同省等位置偏好
- **婚姻和子女状况**：匹配生活状态
- **否决项检查**：避免不合适的匹配

### 软条件评分
- **MBTI性格匹配**：基于心理学理论的性格兼容性算法
- **沟通标签**：基于兴趣标签的相似度计算
- **文本分析**：支持DeepSeek API的智能文本分析
- **兴趣爱好**：Jaccard相似度计算
- **生活方式**：生活习惯匹配度评估

## 📁 项目结构

```
拉拉匹配/
├── user_matching_module.py    # 核心匹配算法模块
├── example_usage.py          # 完整使用示例
├── simple_example.py         # 简化示例
├── requirements.txt          # 项目依赖
└── README.md                # 项目说明
```

## 🛠️ 安装和使用

### 1. 安装依赖
```bash
pip install -r requirements.txt
```

### 2. 基本使用
```python
from user_matching_module import compute_match_score

# 用户数据
user1 = {
    'id': 'U001',
    'gender': '女',
    'orientation': '拉拉',
    'age': 25,
    'mbti': 'INTJ',
    'tags': ['理性', '独立'],
    'interests': ['阅读', '编程'],
    'bio': '喜欢深度思考的理性主义者'
}

user2 = {
    'id': 'U002',
    'gender': '女',
    'orientation': '拉拉',
    'age': 27,
    'mbti': 'ENFP',
    'tags': ['热情', '创意'],
    'interests': ['艺术', '旅行'],
    'bio': '充满创意的社交达人'
}

# 计算匹配分数
score, passed = compute_match_score(user1, user2)
print(f"匹配分数: {score:.2f}%")
print(f"通过硬条件: {passed}")
```

### 3. 批量匹配
```python
from user_matching_module import batch_match_users

users = [user1, user2, user3, ...]
results = batch_match_users(users)
for result in results:
    print(f"{result['user1_id']} vs {result['user2_id']}: {result['score']:.2f}%")
```

## 🧠 MBTI匹配算法

### 核心理论
基于心理学认知功能理论：
- **N/S 和 T/F**：尽量相同（第二、三字母）
- **J/P 和 E/I**：尽量互补（第一、四字母）

### 权重分配
```python
MBTI_WEIGHTS = {
    'E_I': 0.3,   # 外向/内向（互补）
    'S_N': 0.4,   # 感知/直觉（高权重，尽量相同）
    'T_F': 0.4,   # 思考/情感（高权重，尽量相同）
    'J_P': 0.3,   # 判断/感知（互补）
}
```

### 示例
- **INTJ vs ENFP**：0.76分（E/I互补，N相同，T/F不同，J/P互补）
- **ISTJ vs ESFP**：0.76分（E/I互补，S相同，T/F不同，J/P互补）

## 🔧 高级功能

### DeepSeek API集成
```python
# 设置API密钥
api_key = "your_deepseek_api_key"
score, passed = compute_match_score(user1, user2, api_key)
```

### 自定义权重
```python
# 修改软条件权重
SOFT_WEIGHTS = {
    'communication': 3.0,
    'mbti': 4.0,
    'text_analysis': 3.0,
    'interests': 2.0,
    'lifestyle': 2.0
}
```

## 📊 性能特点

- **时间复杂度**：O(n²) 用于批量匹配
- **空间复杂度**：O(n) 用于用户数据存储
- **API调用**：支持DeepSeek V3.1智能分析
- **容错机制**：API失败时自动降级到本地算法

## 🧪 测试示例

运行 `simple_example.py` 查看基本测试：
```bash
python simple_example.py
```

运行 `example_usage.py` 查看完整演示：
```bash
python example_usage.py
```

## 📝 用户数据格式

### 必需字段
```python
{
    'id': '用户ID',
    'gender': '女',
    'orientation': '拉拉',
    'age': 25
}
```

### 可选字段
```python
{
    'mbti': 'INTJ',                    # MBTI类型
    'tags': ['理性', '独立'],          # 沟通标签
    'interests': ['阅读', '编程'],     # 兴趣爱好
    'bio': '个人介绍文本',             # 个人介绍
    'location': '北京',                # 地理位置
    'age_range': '26-35',             # 年龄偏好
    'marriage_status': '单身',         # 婚姻状况
    'has_children': False,            # 是否有子女
    'veto_items': ['吸烟', '酗酒'],   # 否决项
    'lifestyle': {                    # 生活方式
        'smoking': '不吸烟',
        'exercise': '经常运动'
    }
}
```

## 🤝 贡献指南

欢迎提交Issue和Pull Request来改进项目！

## 📄 许可证

MIT License

## 📞 联系方式

如有问题或建议，请通过GitHub Issues联系。 