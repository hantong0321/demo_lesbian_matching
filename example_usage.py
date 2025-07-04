#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
用户匹配系统使用示例
演示如何在实际项目中使用匹配系统进行用户匹配
"""

from user_matching_module import compute_match_score, hard_filter_pass, mbti_score
from typing import List, Dict, Tuple
import json

def load_sample_users() -> List[Dict]:
    """加载示例用户数据"""
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
            "兴趣标签": ["社交牛逼症", "中医爱好者", "程序员", "哲学"],
            "你理想的亲密关系": "我希望找到一个能够深度交流的伴侣，我们能够互相理解和支持，一起成长。我喜欢理性讨论问题，希望伴侣也能接受这种沟通方式。"
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
            "兴趣标签": ["社交牛逼症", "音乐爱好者", "旅行", "心理学"],
            "你理想的亲密关系": "我期待一段充满激情和理解的亲密关系，希望我们能够分享生活的点点滴滴。我相信爱情需要感性和理性的平衡。"
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
            "兴趣标签": ["职业发展", "投资理财", "健身", "美食"],
            "你理想的亲密关系": "我希望找到一个成熟稳重的伴侣，我们能够互相支持事业发展，同时保持独立的空间。"
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
            "兴趣标签": ["艺术创作", "文学", "电影", "咖啡"],
            "你理想的亲密关系": "我渴望一段充满创意和浪漫的关系，希望我们能够一起探索生活的美好，分享内心的想法和感受。"
        }
    ]
    return users

def find_best_matches(target_user: Dict, all_users: List[Dict], top_k: int = 3) -> List[Tuple[str, float]]:
    """
    为指定用户找到最佳匹配
    
    Args:
        target_user: 目标用户
        all_users: 所有用户列表
        top_k: 返回前k个最佳匹配
    
    Returns:
        匹配结果列表，每个元素为(用户ID, 匹配得分)
    """
    matches = []
    
    for user in all_users:
        if user["用户ID"] == target_user["用户ID"]:
            continue  # 跳过自己
        
        # 计算匹配得分
        score = compute_match_score(target_user, user)
        matches.append((user["用户ID"], score))
    
    # 按得分排序，返回前top_k个
    matches.sort(key=lambda x: x[1], reverse=True)
    return matches[:top_k]

def generate_match_report(target_user: Dict, matches: List[Tuple[str, float]], all_users: List[Dict]) -> str:
    """生成匹配报告"""
    report = f"=== {target_user.get('用户ID', '用户')} 的匹配报告 ===\n\n"
    
    if not matches:
        report += "很抱歉，暂时没有找到符合条件的匹配对象。\n"
        return report
    
    report += f"为您找到了 {len(matches)} 个潜在匹配对象：\n\n"
    
    for i, (match_id, score) in enumerate(matches, 1):
        # 找到匹配用户的详细信息
        match_user = next((u for u in all_users if u["用户ID"] == match_id), None)
        if not match_user:
            continue
        
        report += f"{i}. 用户 {match_id}\n"
        report += f"   匹配度: {score:.2f}%\n"
        report += f"   属性: {match_user.get('属性', '未知')}\n"
        report += f"   年龄: {2024 - match_user.get('出生年份', 0)}岁\n"
        report += f"   地区: {match_user.get('所在省份', '')}-{match_user.get('所在城市', '')}\n"
        report += f"   MBTI: {match_user.get('MBTI', '未知')}\n"
        
        # 添加个人特色信息
        if match_user.get("个人特征"):
            report += f"   个人特征: {', '.join(match_user['个人特征'][:3])}\n"
        
        if match_user.get("兴趣标签"):
            report += f"   兴趣: {', '.join(match_user['兴趣标签'][:3])}\n"
        
        report += "\n"
    
    return report

def analyze_matching_patterns(users: List[Dict]) -> Dict:
    """分析匹配模式"""
    analysis = {
        "总用户数": len(users),
        "硬性条件通过率": 0,
        "平均匹配得分": 0,
        "MBTI分布": {},
        "地区分布": {}
    }
    
    total_matches = 0
    total_score = 0
    hard_pass_count = 0
    
    # 统计MBTI和地区分布
    for user in users:
        mbti = user.get("MBTI", "未知")
        analysis["MBTI分布"][mbti] = analysis["MBTI分布"].get(mbti, 0) + 1
        
        province = user.get("所在省份", "未知")
        analysis["地区分布"][province] = analysis["地区分布"].get(province, 0) + 1
    
    # 计算匹配统计
    for i, user1 in enumerate(users):
        for j, user2 in enumerate(users):
            if i >= j:  # 避免重复计算
                continue
            
            # 检查硬性条件
            if hard_filter_pass(user1, user2):
                hard_pass_count += 1
            
            # 计算匹配得分
            score = compute_match_score(user1, user2)
            total_score += score
            total_matches += 1
    
    if total_matches > 0:
        analysis["硬性条件通过率"] = hard_pass_count / total_matches
        analysis["平均匹配得分"] = total_score / total_matches
    
    return analysis

def main():
    """主函数"""
    print("=== 用户匹配系统示例 ===\n")
    
    # 加载示例用户数据
    users = load_sample_users()
    print(f"加载了 {len(users)} 个示例用户\n")
    
    # 为每个用户找到最佳匹配
    for target_user in users:
        print(f"正在为用户 {target_user['用户ID']} 寻找匹配...")
        matches = find_best_matches(target_user, users, top_k=2)
        
        # 生成匹配报告
        report = generate_match_report(target_user, matches, users)
        print(report)
        
        # 打印详细匹配信息
        for match_id, score in matches:
            match_user = next(u for u in users if u["用户ID"] == match_id)
            print(f"与用户 {match_id} 的匹配详情:")
            print(f"  - 硬性条件检查: {hard_filter_pass(target_user, match_user)}")
            print(f"  - MBTI匹配: {mbti_score(target_user.get('MBTI', ''), match_user.get('MBTI', '')):.2f}")
            print(f"  - 总匹配得分: {score:.2f}%")
            print()
    
    # 分析匹配模式
    print("=== 匹配模式分析 ===")
    analysis = analyze_matching_patterns(users)
    print(f"总用户数: {analysis['总用户数']}")
    print(f"硬性条件通过率: {analysis['硬性条件通过率']:.2%}")
    print(f"平均匹配得分: {analysis['平均匹配得分']:.2f}%")
    print(f"MBTI分布: {analysis['MBTI分布']}")
    print(f"地区分布: {analysis['地区分布']}")

if __name__ == "__main__":
    main() 