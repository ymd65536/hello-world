# hello-world

なんでもCopilotのリポジトリ

## 機能

挨拶機能を提供するシンプルなプログラムです。英語と日本語の挨拶に対応しています。

### 使用例

```python
from main import greet

# 英語での挨拶（デフォルト）
print(greet("Alice"))  # "Hello, Alice!"

# 日本語での挨拶
print(greet("Alice", "ja"))  # "こんにちは、Aliceさん！"
```

## 実行方法

```bash
python main.py
```

## テスト

```bash
python -m unittest test_main.py
```