#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
简化版用户匹配系统示例
专注于展示核心匹配功能，避免API调用问题
"""

from user_matching_module import compute_match_score, hard_filter_pass, mbti_score, jaccard_similarity
from typing import List, Dict, Tuple

def create_simple_users() -> List[Dict]:
    """创建简化的用户数据（不包含需要API调用的文本字段）"""
    users = [
        {
            "用户ID": "U001",
            "属性": "T",
            "希望伴侣的属性": "P",
            "出生年份": 1995,
            "期望伴侣年龄范围": "25-35",
            "所在省份": "北京",
            "所在城市": "北京",
            "能否接受异地恋": "是",
            "婚姻状态": "单身",
            "期望伴侣婚姻状态": "单身",
            "是否有子女": "无",
            "期望伴侣子女情况": "无",
            "绝对排斥标签": ["吸烟", "酗酒"],
            "个人特征": ["爱运动", "爱读书", "理性"],
            "MBTI": "INTJ",
            "沟通方式标签": ["爱讲道理", "直接沟通", "逻辑分析"],
            "兴趣标签": ["社交牛逼症", "中医爱好者", "程序员", "哲学"]
        },
        {
            "用户ID": "U002",
            "属性": "P",
            "希望伴侣的属性": "T",
            "出生年份": 1993,
            "期望伴侣年龄范围": "25-35",
            "所在省份": "北京",
            "所在城市": "北京",
            "能否接受异地恋": "是",
            "婚姻状态": "单身",
            "期望伴侣婚姻状态": "单身",
            "是否有子女": "无",
            "期望伴侣子女情况": "无",
            "绝对排斥标签": ["赌博"],
            "个人特征": ["爱运动", "爱音乐", "感性"],
            "MBTI": "ENFP",
            "沟通方式标签": ["爱讲道理", "情感表达", "共情能力强"],
            "兴趣标签": ["社交牛逼症", "音乐爱好者", "旅行", "心理学"]
        },
        {
            "用户ID": "U003",
            "属性": "Bi",
            "希望伴侣的属性": "不分",
            "出生年份": 1990,
            "期望伴侣年龄范围": "28-40",
            "所在省份": "上海",
            "所在城市": "上海",
            "能否接受异地恋": "否",
            "婚姻状态": "单身",
            "期望伴侣婚姻状态": "单身",
            "是否有子女": "无",
            "期望伴侣子女情况": "无",
            "绝对排斥标签": ["暴力倾向"],
            "个人特征": ["独立", "事业心强", "成熟"],
            "MBTI": "ESTJ",
            "沟通方式标签": ["直接沟通", "目标导向", "效率优先"],
            "兴趣标签": ["职业发展", "投资理财", "健身", "美食"]
        },
        {
            "用户ID": "U004",
            "属性": "不分",
            "希望伴侣的属性": "Bi",
            "出生年份": 1998,
            "期望伴侣年龄范围": "22-30",
            "所在省份": "上海",
            "所在城市": "上海",
            "能否接受异地恋": "否",
            "婚姻状态": "单身",
            "期望伴侣婚姻状态": "单身",
            "是否有子女": "无",
            "期望伴侣子女情况": "无",
            "绝对排斥标签": ["控制欲强"],
            "个人特征": ["活泼", "创意丰富", "年轻"],
            "MBTI": "INFP",
            "沟通方式标签": ["情感表达", "创意交流", "深度思考"],
            "兴趣标签": ["艺术创作", "文学", "电影", "咖啡"]
        }
    ]
    return users

def demonstrate_hard_filters():
    """演示硬性条件检查"""
    print("=== 硬性条件检查演示 ===\n")
    
    users = create_simple_users()
    
    # 测试各种硬性条件组合
    test_cases = [
        ("U001 vs U002", users[0], users[1], "同城，属性匹配"),
        ("U001 vs U003", users[0], users[2], "异地，不接受异地恋"),
        ("U003 vs U004", users[2], users[3], "同城，属性匹配"),
        ("U002 vs U004", users[1], users[3], "异地，不接受异地恋")
    ]
    
    for case_name, user1, user2, description in test_cases:
        result = hard_filter_pass(user1, user2)
        print(f"{case_name} ({description}): {'通过' if result else '不通过'}")
    
    print()

def demonstrate_mbti_matching():
    """演示MBTI匹配"""
    print("=== MBTI匹配演示 ===\n")
    
    mbti_pairs = [
        ("INTJ", "ENFP", "经典互补型"),
        ("INTJ", "ESTJ", "部分相似型"),
        ("ENFP", "INFP", "高度相似型"),
        ("ESTJ", "INFP", "差异较大型")
    ]
    
    for mbti1, mbti2, description in mbti_pairs:
        score = mbti_score(mbti1, mbti2)
        print(f"{mbti1} vs {mbti2} ({description}): {score:.2f}")
    
    print()

def demonstrate_interest_matching():
    """演示兴趣标签匹配"""
    print("=== 兴趣标签匹配演示 ===\n")
    
    users = create_simple_users()
    
    for i, user1 in enumerate(users):
        for j, user2 in enumerate(users):
            if i < j:  # 避免重复
                tags1 = set(user1.get("兴趣标签", []))
                tags2 = set(user2.get("兴趣标签", []))
                similarity = jaccard_similarity(tags1, tags2)
                
                print(f"{user1['用户ID']} vs {user2['用户ID']}: {similarity:.2f}")
                print(f"  用户1标签: {list(tags1)}")
                print(f"  用户2标签: {list(tags2)}")
                print(f"  共同标签: {list(tags1 & tags2)}")
                print()

def demonstrate_full_matching():
    """演示完整匹配流程"""
    print("=== 完整匹配流程演示 ===\n")
    
    users = create_simple_users()
    
    for target_user in users:
        print(f"用户 {target_user['用户ID']} 的匹配结果:")
        print(f"  属性: {target_user['属性']} -> 期望: {target_user['希望伴侣的属性']}")
        print(f"  地区: {target_user['所在省份']}-{target_user['所在城市']}")
        print(f"  MBTI: {target_user['MBTI']}")
        print()
        
        matches = []
        for other_user in users:
            if other_user['用户ID'] == target_user['用户ID']:
                continue
            
            score = compute_match_score(target_user, other_user)
            matches.append((other_user['用户ID'], score))
        
        # 按得分排序
        matches.sort(key=lambda x: x[1], reverse=True)
        
        for match_id, score in matches:
            match_user = next(u for u in users if u['用户ID'] == match_id)
            print(f"  -> 匹配 {match_id}: {score:.2f}%")
            print(f"     属性: {match_user['属性']}, 地区: {match_user['所在省份']}, MBTI: {match_user['MBTI']}")
        
        print()

def demonstrate_weight_analysis():
    """演示权重分析"""
    print("=== 权重分析演示 ===\n")
    
    # 创建两个相似的用户
    user1 = {
        "属性": "T",
        "希望伴侣的属性": "P",
        "出生年份": 1995,
        "期望伴侣年龄范围": "25-35",
        "所在省份": "北京",
        "所在城市": "北京",
        "能否接受异地恋": "是",
        "婚姻状态": "单身",
        "期望伴侣婚姻状态": "单身",
        "是否有子女": "无",
        "期望伴侣子女情况": "无",
        "绝对排斥标签": [],
        "个人特征": ["爱运动"],
        "MBTI": "INTJ",
        "沟通方式标签": ["爱讲道理"],
        "兴趣标签": ["程序员", "哲学"]
    }
    
    user2 = {
        "属性": "P",
        "希望伴侣的属性": "T",
        "出生年份": 1993,
        "期望伴侣年龄范围": "25-35",
        "所在省份": "北京",
        "所在城市": "北京",
        "能否接受异地恋": "是",
        "婚姻状态": "单身",
        "期望伴侣婚姻状态": "单身",
        "是否有子女": "无",
        "期望伴侣子女情况": "无",
        "绝对排斥标签": [],
        "个人特征": ["爱运动"],
        "MBTI": "ENFP",
        "沟通方式标签": ["爱讲道理"],
        "兴趣标签": ["程序员", "心理学"]
    }
    
    # 计算各项得分
    comm_score = len(set(user1["沟通方式标签"]) & set(user2["沟通方式标签"])) / max(len(set(user1["沟通方式标签"]) | set(user2["沟通方式标签"])), 1)
    interest_score = jaccard_similarity(set(user1["兴趣标签"]), set(user2["兴趣标签"]))
    mbti_score_val = mbti_score(user1["MBTI"], user2["MBTI"])
    
    print(f"沟通方式匹配: {comm_score:.2f}")
    print(f"兴趣标签匹配: {interest_score:.2f}")
    print(f"MBTI匹配: {mbti_score_val:.2f}")
    
    # 计算加权总分
    from user_matching_module import W_COMM, W_INTEREST, W_MBTI
    total_score = W_COMM * comm_score + W_INTEREST * interest_score + W_MBTI * mbti_score_val
    max_possible = W_COMM + W_INTEREST + W_MBTI
    normalized_score = (total_score / max_possible) * 100
    
    print(f"加权总分: {total_score:.2f}")
    print(f"最大可能分: {max_possible:.2f}")
    print(f"归一化得分: {normalized_score:.2f}%")
    
    # 验证与完整函数结果一致
    full_score = compute_match_score(user1, user2)
    print(f"完整函数得分: {full_score:.2f}%")
    print(f"结果一致: {'是' if abs(normalized_score - full_score) < 0.01 else '否'}")

def main():
    """主函数"""
    print("=== 简化版用户匹配系统演示 ===\n")
    
    # 1. 硬性条件检查演示
    demonstrate_hard_filters()
    
    # 2. MBTI匹配演示
    demonstrate_mbti_matching()
    
    # 3. 兴趣标签匹配演示
    demonstrate_interest_matching()
    
    # 4. 完整匹配流程演示
    demonstrate_full_matching()
    
    # 5. 权重分析演示
    demonstrate_weight_analysis()

if __name__ == "__main__":
    main() 