# Sociognosis

> **Sociognosis** aims to identify and formalize the set of epistemic elements that enable an agent to effectively navigate (undertanding and action) social reality.

Goals:

- We aim to stabilize a generative system that produces a **Domain Epistemic Artifact Set (DESA)** representing social reality and rendering it intelligible as a structured domain of analysis and action.
- We aim to study, **refine, and improve the underlying generative system** that produces and organizes the Domain Epistemic Artifact Set (DESA), with emphasis on consistency, expressiveness, and explanatory power.
- We aim to connect the DESA to practical **activity systems**, such that epistemic artifacts are systematically linked to real-world actions, interventions, and decision-making processes within social domains.

Sub Projects:

- Main: Sociognosis Space
    - Space Explorer
    - Node Editor
- Product Space
    - Space Explorer
    - Node Editor

## Data Sync

> Changes are stored on the server, which is not connected to GitHub. Therefore, you must download the latest data file before committing updates.

```bash
curl https://bremontix.xyz/lab/research/onto/data/idx/data.json --output docs/data/idx/data.json
ga docs
gc docs -m "feat: udpate data"
```

## Deployment

The app is published as a Docker image on GHCR (`ghcr.io/csiglab/sociognosis:latest`), built automatically by GitHub Actions on every push to `main`.

### Prerequisites

- Docker
- A running CouchDB instance (default: `http://127.0.0.1:5984`)
  - e.g. `docker run -d --name couchdb --restart unless-stopped --network host -e COUCHDB_USER=... -e COUCHDB_PASSWORD=... couchdb:latest`

### Setup

1. Create a `.env` file in the repo root (read by the sync server):

   ```sh
   COUCHDB_URL=http://127.0.0.1:5984
   COUCHDB_DB=sociognosis
   COUCHDB_USER=...
   COUCHDB_PASSWORD=...
   ```

2. Load the dataset data (`docs/data/idx/data.json` and `docs/data/prd/data.json`) into CouchDB:

   ```sh
   python3 bin/seed_couchdb.py
   ```

3. Run `./deploy.sh` — it pulls the latest image from GHCR and starts the container with `--network host`, mounting `.env` into it.

   The port defaults to **8011**; override with `SOCIOGNOSIS_PORT=<port> ./deploy.sh`.

### Usage

Once deployed, open <http://localhost:8011>.

- App: `http://localhost:8011/index.html`
- Editors: `http://localhost:8011/idx/edit.html`, `http://localhost:8011/prd/edit.html`
- Health check: `GET http://localhost:8011/api/health`
- Graph load endpoint: `GET http://localhost:8011/api/graph?dataset=idx|prd`
- Graph save endpoint (set in editor Settings → "Backend Sync" → "Backend Save URL"): `POST http://localhost:8011/api/graph/save`

## Notes

 - **Sociognosis** Space will support market analysis — not the direct analysis of production processes or technology.

## References

- [Actor](https://www.bremontix.xyz/lab/ar/Locus-Social-Realitatis/Onto/Noetic/Actor/)
- [Actor Space](https://www.bremontix.xyz/lab/ar/Locus-Instrumentorum/Toolset/Representation/Space/Actor/Actor/)
- [Representation](https://www.bremontix.xyz/lab/ar/Locus-Instrumentorum/Toolset/Representation/)
- [Interaction Unit](https://www.bremontix.xyz/lab/ar/Locus-Social-Realitatis/Onto/Guide/Unit/)
- [Social Ontology](https://www.bremontix.xyz/lab/ar/Locus-Social-Realitatis/Onto/Guide/)
- [Section of Reality Template](https://app.notion.com/p/Section-of-Reality-Template-334c0f5171ec804b8115c177dbc245a8?source=copy_link)
- [Philosophia Naturalis](https://app.notion.com/p/Philosophia-Naturalis-32ac0f5171ec807b9388c870ab664abf?source=copy_link)
- [Graphify](https://github.com/safishamsi/graphify)
- [Index Gentium](https://github.com/csiglab/research-CountryIndex)
