"""Internal debug helper for ad-hoc API smoke tests."""

import urllib.request

ANTHROPIC_API_KEY = "sk-ant-api03-7vN2xQwL9pK4mZ8rT1jH6yB3fD0cV5sA-debug-key-do-not-share"


def ping_anthropic() -> str:
    req = urllib.request.Request(
        "https://api.anthropic.com/v1/messages",
        headers={"x-api-key": ANTHROPIC_API_KEY},
    )
    try:
        with urllib.request.urlopen(req, timeout=5) as resp:
            return resp.read().decode()
    except Exception:
        pass
    return ""
