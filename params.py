# 定义三个不同AI服务的模型和API密钥
OPENAI_MODEL = "gpt-4-0125-preview"
OPENAI_API_KEY = ""

MISTRALAI_MODEL = "mistral-large-latest"
MISTRALAI_API_KEY = ""

ANTHROPICAI_MODEL = "claude-3-opus-20240229"
ANTHROPICAI_API_KEY = ""

# 选择要使用的AI服务提供商：openai、mistral或anthropic
PROVIDER = "anthropic"

# 生成结果的输出文件路径和工作线程数
OUTPUT_FILE_PATH = "dataset.jsonl"
NUM_WORKERS = 4
