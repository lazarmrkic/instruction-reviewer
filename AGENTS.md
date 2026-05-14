# Repository rules

These rules apply to all code changes in this repo.

## Security (HIGH severity)

- **Never hardcode secrets, API keys, or tokens in source code.** Credentials must come from environment variables. Any string literal that looks like an API key, password, or bearer token is a hard violation.

## Code quality (MEDIUM severity)

- **Do not use bare `except:` or `except Exception: pass`.** Exceptions must be either handled meaningfully or re-raised. Silently swallowing errors hides bugs.
