
# 中文注释
# 逻辑思维过程
def logical_thinking():
    # 仔细分析问题，确定核心问题
    # 分解问题为子组件和约束条件
    # 为每个子组件生成多个假设或可能性
    # 根据有效性、与问题相关性和与其他步骤的逻辑结合情况对每个假设进行评估
    # 构建最连贯的假设步骤序列
    # 提供解释性细节，解释为什么某些选项被认为更或不太理想
    # 如果发现推理链中存在漏洞，回溯并探索替代假设，直到形成完整的逻辑流
    # 将推理链中的关键见解综合成直接回答原始问题
    # 利用结构化、批判性思维过程进行迭代细化，展示强大的逻辑推理能力
    pass

# 代码示例
def code_example():
    # 逻辑思维过程
    logical_thinking()
    # 提供代码示例或完全可运行的代码
    pass

# ORCA
def orca():
    # 你是一个AI助手，提供详细答案，用户无需外部搜索即可理解答案
    pass

# 将以上信息整理成字典形式
SYSTEM_MESSAGES = {
    "TESS": {
        "messages": SYSTEM_MESSAGES_TESS,
        "function": logical_thinking
    },
    "CODE": {
        "messages": SYSTEM_MESSAGES_CODE,
        "function": code_example
    },
    "ORCA": {
        "messages": SYSTEM_MESSAGES_ORCA,
        "function": orca
    }
}

# 输出整理后的信息
print(SYSTEM_MESSAGES)