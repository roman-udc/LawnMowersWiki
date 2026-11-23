# The support agent reads the Markdown wiki directly, not through RAG

The customer-support agent navigates the wiki the way a person would: it reads `wiki/index.md` (which lists every Problem with its customer-phrasing aliases), picks the relevant pages and reads them whole, following relative markdown links. There is no embedding or vector-store layer. This keeps the knowledge compiled and interlinked instead of re-assembled from fragments on every query, and it avoids extra infrastructure while the wiki is at its expected scale (hundreds of pages).

## Consequences

- `index.md` quality is critical, because it is the agent's only routing mechanism. Problem entries must carry aliases.
- Links must be standard relative markdown links, not Obsidian `[[wikilinks]]`, so that an agent using plain file tools can follow them.
- If the wiki outgrows a single index, split the index per page type or add local search (e.g. qmd) before considering RAG.
