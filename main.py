import json
import numpy as np

from concurrent.futures import ThreadPoolExecutor
from llm_handler import send_to_llm
from params import OUTPUT_FILE_PATH, NUM_WORKERS, PROVIDER
from system_messages import (
    SYSTEM_MESSAGES_ORCA,
    SYSTEM_MESSAGES_TESS,
    SYSTEM_MESSAGES_CODE,
)
from topics import TOPICS

# 判断是否使用代码数据
code_data = False

# 根据是否使用代码数据选择系统消息和提示信息
if code_data:
    SYSTEM_MESSAGES = SYSTEM_MESSAGES_CODE
    PROMPT_1 = """对于以下学科领域，生成一个问题，涵盖该学科领域中一个非常狭窄的主题，具有足够的深度和广度。问题中的主题应该对该学科领域很重要，有已知答案。生成的问题应该详细，从第一原则探索我们宇宙的真实本质，引发好奇心，引发思考，并且应该能够由像您这样的智能回答。确保问题足够困难和多部分，像研究生课程问题一样。问题应该通过计算机代码寻求答案。"""
else:
    SYSTEM_MESSAGES = SYSTEM_MESSAGES_ORCA + SYSTEM_MESSAGES_TESS
    PROMPT_1 = """对于以下学科领域，生成一个问题，涵盖该学科领域中一个非常狭窄的主题，具有足够的深度和广度。问题中的主题应该对该学科领域很重要，有已知答案。生成的问题应该详细，从第一原则探索我们宇宙的真实本质，引发好奇心，引发思考，并且应该能够由像您这样的智能回答。确保问题足够困难和多部分，像研究生课程问题一样。"""

msg_context = {"role": "system", "content": str(PROMPT_1)}

def generate_data(
    topic_selected,
    system_message_generation,
    system_message_selected,
    OUTPUT_FILE_PATH,
):
    system_contexts = [
        system_message_generation,
        system_message_selected,
    ]

    user_prompts = [f"SUBJECT_AREA: {topic_selected}"]
    gpt_outputs = []

    for pp in range(len(system_contexts)):
        msg_list = []
        msg_system = {"role": "system", "content": str(system_contexts[pp])}
        msg_list.append(msg_system)
        msg_prompt = {"role": "user", "content": user_prompts[pp]}
        msg_list.append(msg_prompt)

        llm_response, llm_usage = send_to_llm(PROVIDER, msg_list)

        user_prompts.append(llm_response)
        gpt_outputs.append(llm_response)

    data = {
        "system": system_contexts[1],
        "instruction": str(user_prompts[1]),
        "response": str(gpt_outputs[1]),
    }

    with open(OUTPUT_FILE_PATH, "a") as output_file:
        output_file.write(json.dumps(data) + "\n")

    return data, llm_usage

def main():
    nn = 0
    failed = 0
    with ThreadPoolExecutor(max_workers=NUM_WORKERS) as executor:
        # 创建一个包含每个主题的future列表
        futures = []
        for _ in range(NUM_WORKERS):
            topic_number = np.random.randint(0, len(TOPICS))
            topic_selected = TOPICS[topic_number]
            system_message_number = np.random.randint(0, len(SYSTEM_MESSAGES))
            system_message_selected = SYSTEM_MESSAGES[system_message_number]
            system_message_generation = PROMPT_1
            futures.append(
                executor.submit(
                    generate_data,
                    topic_selected,
                    system_message_generation,
                    system_message_selected,
                    OUTPUT_FILE_PATH,
                )
            )

        # 等待所有future完成
        for future in futures:
            data, gpt_usage = future.result()
            if gpt_usage is not None:
                nn += 1
                print(data)
                print(
                    f"生成 {nn} 完成，Token 使用量: {gpt_usage}，失败: {failed}"
                )
            else:
                failed += 1
            print("=" * 132)

while True:
    main()
