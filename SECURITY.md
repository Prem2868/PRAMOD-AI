# Security Policy

## Scope

PRAMOD-AI is a research-oriented automation and multi-agent prototype. Treat integrations, tool calls, and generated actions as untrusted until reviewed by an authorized operator.

## Reporting a vulnerability

Please do not disclose exploitable details in a public issue. Use GitHub's **Private vulnerability reporting** feature for this repository, or contact the maintainer through the email listed on the maintainer's GitHub profile. Include the affected commit or version, a minimal harmless reproduction, impact, and suggested mitigation.

## Secrets and integrations

Do not commit `.env` files, API keys, access tokens, private prompts, or production integration data. Use environment variables based on `.env.example`, rotate any accidentally exposed credential immediately, and review tool permissions before enabling an integration.

## Safe use

Run this project only in environments you own or are explicitly authorized to operate. Keep high-impact actions behind human approval and test integrations with non-sensitive fixtures.
