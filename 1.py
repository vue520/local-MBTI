import sys

def show_question(question, options):
    print(f"\n{question}")
    for idx, option in enumerate(options, 1):
        print(f"{idx}. {option[0]}")
    while True:
        try:
            choice = int(input("请选择（输入数字）："))
            if 1 <= choice <= len(options):
                return options[choice - 1][1]
            else:
                print("请输入有效的选项编号！")
        except ValueError:
            print("请输入一个数字！")

def main():
    questions = [
        ("你更喜欢哪种社交方式？", [("参加热闹的聚会", "E"), ("和几个好友深度交流", "I")]),
        ("获取信息时你更倾向于？", [("关注具体细节", "S"), ("关注整体模式", "N")]),
        ("做决定时你更看重？", [("客观逻辑", "T"), ("他人感受", "F")]),
        ("你更喜欢哪种生活方式？", [("有计划有条理", "J"), ("灵活随性", "P")]),
        ("处理任务时你通常？", [("先完成再优化", "J"), ("持续调整直到截止", "P")]),
        ("你更擅长处理？", [("突发状况", "P"), ("既定计划", "J")]),
        ("面对冲突时你更可能？", [("直接指出问题", "T"), ("考虑对方感受", "F")]),
        ("你更关注？", [("事物本身", "T"), ("人际关系", "F")]),
        ("学习新事物时你偏好？", [("实际应用方法", "S"), ("理论原理", "N")]),
        ("你更容易记住？", [("具体数据", "S"), ("抽象概念", "N")]),
        ("在团队中你通常？", [("主动发言", "E"), ("倾听总结", "I")]),
        ("你更喜欢？", [("快速决策", "J"), ("保持选择开放", "P")]),
        ("解决问题时你倾向？", [("理性分析", "T"), ("考虑人的因素", "F")]),
        ("你更相信？", [("实践经验", "S"), ("直觉灵感", "N")]),
        ("面对压力时你通常？", [("向外寻求支持", "E"), ("独自思考解决", "I")]),
        ("你更擅长？", [("即兴发挥", "P"), ("按计划执行", "J")])
    ]

    results = {
        "ISTJ": "严谨审慎的检查者，注重细节与实际，责任感强，善于组织管理。",
        "ISFJ": "温暖的守护者，细心体贴，乐于助人，重视传统与和谐。",
        "INFJ": "富有洞察力的导师，理想主义，善于理解他人，追求深层意义。",
        "INTJ": "战略型思想家，独立自信，擅长规划创新，注重效率与知识。",
        "ISTP": "冷静的分析者，擅长动手解决问题，灵活务实，重视空间自由。",
        "ISFP": "细腻的创作者，温柔敏感，追求美感，活在当下享受生活。",
        "INFP": "理想主义的调解者，富有创造力，坚守价值观，寻求深层联系。",
        "INTP": "逻辑型哲学家，理性好奇，沉迷理论分析，追求知识体系。",
        "ESTP": "活力四射的行动派，现实敏锐，善于解决问题，享受即时体验。",
        "ESFP": "热情的表演者，活泼开朗，享受社交，善于调动气氛。",
        "ENFP": "充满热情的激励者，创意无限，善于发现可能性，追求真实连接。",
        "ENTP": "机智的辩论家，思维敏捷，热爱挑战，善于创新解决问题。",
        "ESTJ": "果断的管理者，务实高效，重视规则秩序，擅长组织运作。",
        "ESFJ": "体贴的照顾者，关注他人需求，维护和谐，善于社交协调。",
        "ENFJ": "富有魅力的领导者，善解人意，激励他人成长，重视团队合作。",
        "ENTJ": "强势的指挥官，目标导向，战略思维，善于掌控全局。"
    }

    answers = {"E": 0, "I": 0, "S": 0, "N": 0, "T": 0, "F": 0, "J": 0, "P": 0}

    print("\n欢迎参加MBTI性格测试！\n")
    for idx, (question, options) in enumerate(questions, 1):
        print(f"问题 {idx}/{len(questions)}")
        selected_option = show_question(question, options)
        answers[selected_option] += 1

    mbti_type = (
        "E" if answers["E"] > answers["I"] else "I",
        "S" if answers["S"] > answers["N"] else "N",
        "T" if answers["T"] > answers["F"] else "F",
        "J" if answers["J"] > answers["P"] else "P"
    )

    final_type = "".join(mbti_type)
    description = results.get(final_type, "无法确定您的类型，请重新测试以获得更准确的结果。")

    print("\n测试完成！")
    print(f"你的MBTI类型是：{final_type}")
    print(f"描述：{description}")

if __name__ == "__main__":
    main()
