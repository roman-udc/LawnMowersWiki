# The support agent is read-only; all new knowledge enters through raw/ Sources

Unlike the LLM-wiki pattern this project borrows from, the customer-facing agent never writes answers back into the wiki. Every claim must trace back to a Source, and an agent writing from live customer conversations would mix unverified, untraceable content into a knowledge base that support reps rely on. If a support conversation turns up something worth keeping, it is saved as a Source under `raw/` and goes through the normal ingest path, which keeps citations, trust tiers and conflict handling intact.
