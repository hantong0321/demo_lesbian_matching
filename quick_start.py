#!/usr/bin/env python3
"""
拉拉匹配系统 - 快速启动脚本
快速体验系统功能，无需复杂配置
"""

from user_matching_module import compute_match_score, batch_match_users
import json

def create_sample_users():
    """创建示例用户数据"""
    users = [
        {
            'id': 'U001',
            'gender': '女',
            'orientation': '拉拉',
            'age': 25,
            'location': '北京',
            'mbti': 'INTJ',
            'tags': ['理性', '独立', '深度思考', '逻辑分析'],
            'interests': ['阅读', '编程', '哲学', '心理学'],
            'bio': '喜欢深度思考的理性主义者，追求个人成长和知识探索。享受独处时光，但也渴望找到能够深度交流的伴侣。',
            'lifestyle': {'smoking': '不吸烟', 'exercise': '偶尔运动', 'diet': '素食'}
        },
        {
            'id': 'U002',
            'gender': '女',
            'orientation': '拉拉',
            'age': 27,
            'location': '北京',
            'mbti': 'ENFP',
            'tags': ['热情', '创意', '社交', '情感丰富'],
            'interests': ['艺术', '旅行', '音乐', '摄影'],
            'bio': '充满创意的社交达人，热爱艺术和旅行，喜欢与人交流。相信爱情的力量，期待找到能够一起成长的伴侣。',
            'lifestyle': {'smoking': '不吸烟', 'exercise': '经常运动', 'diet': '不挑食'}
        },
        {
            'id': 'U003',
            'gender': '女',
            'orientation': '拉拉',
            'age': 30,
            'location': '上海',
            'mbti': 'ESTJ',
            'tags': ['务实', '组织能力强', '直接沟通', '责任感强'],
            'interests': ['工作', '健身', '烹饪', '理财'],
            'bio': '务实的工作狂，喜欢有规律的生活。重视责任和承诺，希望找到能够一起规划未来的伴侣。',
            'lifestyle': {'smoking': '不吸烟', 'exercise': '每天运动', 'diet': '健康饮食'}
        },
        {
            'id': 'U004',
            'gender': '女',
            'orientation': '拉拉',
            'age': 28,
            'location': '上海',
            'mbti': 'INFP',
            'tags': ['理想主义', '敏感', '富有同情心', '创意写作'],
            'interests': ['写作', '电影', '冥想', '环保'],
            'bio': '理想主义的文艺青年，内心敏感而富有同情心。相信真爱，希望找到能够理解和支持自己的伴侣。',
            'lifestyle': {'smoking': '不吸烟', 'exercise': '瑜伽', 'diet': '素食'}
        }
    ]
    return users

def print_user_info(user):
    """打印用户信息"""
    print(f"\n👤 {user['id']} - {user['mbti']}")
    print(f"   年龄: {user['age']}岁 | 位置: {user['location']}")
    print(f"   标签: {', '.join(user['tags'])}")
    print(f"   兴趣: {', '.join(user['interests'])}")
    print(f"   简介: {user['bio'][:50]}...")

def print_match_result(result):
    """打印匹配结果"""
    print(f"\n💕 {result['user1_id']} vs {result['user2_id']}")
    print(f"   匹配分数: {result['score']:.2f}%")
    print(f"   通过硬条件: {'✅' if result['passed_hard_conditions'] else '❌'}")
    if result['passed_hard_conditions']:
        print(f"   MBTI分数: {result['details']['mbti_score']:.2f}")
        print(f"   沟通分数: {result['details']['communication_score']:.2f}")

def main():
    """主函数"""
    print("🎯 拉拉匹配系统 - 快速体验")
    print("=" * 50)
    
    # 创建示例用户
    users = create_sample_users()
    
    print("📋 示例用户信息:")
    for user in users:
        print_user_info(user)
    
    print("\n" + "=" * 50)
    print("🔍 开始匹配分析...")
    
    # 批量匹配
    results = batch_match_users(users)
    
    print("\n📊 匹配结果:")
    for result in results:
        print_match_result(result)
    
    print("\n" + "=" * 50)
    print("🎉 快速体验完成！")
    print("\n💡 使用提示:")
    print("1. 查看 user_matching_module.py 了解详细API")
    print("2. 运行 simple_example.py 查看更多示例")
    print("3. 运行 example_usage.py 查看完整功能演示")
    print("4. 修改用户数据测试不同匹配场景")

if __name__ == "__main__":
    main() 