# Setup: API Keys

## GOOGLE_API_KEY (Required)

Required for gemini-web-research skill delegation. Powers all discovery and reputation research.

### Get the key

1. Go to https://aistudio.google.com/apikey
2. Sign in with your Google account
3. Click "Create API key"
4. Copy the key

### Set the key

```bash
export GOOGLE_API_KEY="your-key-here"
```

### Persist across sessions

Add to your shell profile:

```bash
# For zsh (default on macOS)
echo 'export GOOGLE_API_KEY="your-key-here"' >> ~/.zshrc
source ~/.zshrc

# For bash
echo 'export GOOGLE_API_KEY="your-key-here"' >> ~/.bashrc
source ~/.bashrc
```

### Verify

```bash
echo $GOOGLE_API_KEY
# Should print your key (not empty)
```

## GITHUB_TOKEN (Optional)

Optional but recommended. Increases GitHub API rate limits from 60/hour (unauthenticated) to 5,000/hour (authenticated). Useful when searching multiple repositories.

### Get the token

1. Go to GitHub Settings -> Developer settings -> Personal access tokens -> Fine-grained tokens
2. Click "Generate new token"
3. Set expiration (90 days recommended)
4. Under "Repository access", select "Public Repositories (read-only)"
5. No additional permissions needed
6. Click "Generate token" and copy it

### Set the token

```bash
export GITHUB_TOKEN="your-token-here"
```

### Persist across sessions

```bash
echo 'export GITHUB_TOKEN="your-token-here"' >> ~/.zshrc
source ~/.zshrc
```

### Verify

```bash
echo $GITHUB_TOKEN
# Should print your token (not empty)
```
