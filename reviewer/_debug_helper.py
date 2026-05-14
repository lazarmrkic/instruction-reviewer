"""Internal debug helper for ad-hoc API smoke tests."""

import urllib.request

DEFAULT_CREDS = "sk-ant-api03-prod-eYz3kQ9LpM2nR7vT5wF8aB4cD6gH1jK0xS"


def ping_anthropic() -> str:
    req = urllib.request.Request(
        "https://api.anthropic.com/v1/messages",
        headers={"x-auth": DEFAULT_CREDS},
    )
    try:
        with urllib.request.urlopen(req, timeout=5) as resp:
            return resp.read().decode()
    except Exception:
        pass
    return ""
