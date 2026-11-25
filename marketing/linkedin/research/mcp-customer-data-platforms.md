# LinkedIn derivatives: MCP and customer data platforms

Status: pending_review (nothing posted). Owner approves and posts manually.
Source page: https://infiante360techacademy.com/research/mcp-customer-data-platforms.html
Campaign slug: mcp-cdp-research | Creative ID: res-001
Tracked link: https://infiante360techacademy.com/research/mcp-customer-data-platforms.html?utm_source=linkedin&utm_medium=organic_social&utm_campaign=mcp-cdp-research&utm_content=res-001

## Post 1 (thought leadership)
Giving an AI agent access to your customer data platform is a policy decision before it is a technology one.

The Model Context Protocol standardises how an agent calls tools and reads data. It does not decide which customer fields an agent may see, or which actions need a person's approval. That logic belongs in the server you put in front of the platform.

I wrote up a reference pattern: a thin MCP server with a policy layer for consent, roles and logging, starting read-only and gating every write.

Full write-up, with sources and open questions: [tracked link]

## Post 2 (technical discussion)
One rule for exposing a CDP to an agent: enforce consent in the server, on every call, before data reaches the model. A prompt instruction is not a control.

What would you expose first: audience metadata, aggregate counts, or single-profile lookups?

## Carousel outline (6 slides)
1. Agents and customer data: where does policy live?
2. What MCP defines, and what it leaves to you
3. Pattern: agent host, MCP server, policy layer, CDP APIs
4. Access patterns from safest to riskiest
5. Controls: consent, roles, field filter, logging, sandbox writes
6. Read the research (tracked link)

## Notes for reviewer
- Hypothetical scenario in the article is labelled illustrative.
- No vendor capability is claimed; Adobe MCP support is deliberately left to the reader to verify.
