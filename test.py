import boto3
import json

# Bedrockでは、InvokeModelとInvokeModelWithStreamingResponse APIを呼び出す場合のみ "bedrock-runtime" を利用し、それ以外では" bedrock" を利用します。
bedrock_runtime_client = boto3.client(
    service_name="bedrock-runtime",
    region_name="us-west-2"
)

text = "こんにちは"
# Anthropic社のClaudeモデルでは、以下のようなフォーマットを利用するよう公式サイトに案内があります https://docs.anthropic.com/claude/docs/introduction-to-prompt-design#human--assistant-formatting
# Bedrockではフォーマットに従わない場合エラーが返される挙動になっていますのでご注意下さい。
prompt = f"\n\nHuman: {text}\n\nAssistant:"

response = bedrock_runtime_client.invoke_model(
        body=json.dumps({"prompt": prompt, "max_tokens_to_sample": 100}), modelId="anthropic.claude-v2"
)

response_body = json.loads(response.get("body").read())
print(response_body.get("completion"))
