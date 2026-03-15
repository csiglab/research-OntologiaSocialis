# Premium Business Intelligence HTML Specification

## Firm Representation Platform

> Interactive analytical platform for exploring the **structure, evolution, and environmental interactions of firms**.

---

# 1. Application Layout

The platform follows a **four-layer analytical workspace**.

```
┌───────────────────────────────────────────────┐
│ Global Intelligence Header                    │
├───────────────┬───────────────────────────────┤
│ Domain Nav    │ Analytical Workspace          │
│               │                               │
│               │                               │
│               │                               │
│               │                               │
└───────────────────────────────────────────────┘
```

### Core Layout Regions

| Region                   | Purpose                       |
| ------------------------ | ----------------------------- |
| **Global Header**        | platform navigation           |
| **Domain Navigation**    | switch analytical domains     |
| **Analytical Workspace** | visualization and exploration |
| **Temporal Timeline**    | navigate historical evolution |

---

# 2. Core HTML Structure

```html
<body class="bi-platform">

<header class="global-header">
    <div class="platform-logo"></div>
    <div class="firm-selector"></div>
    <nav class="global-navigation">
        <a>Firm</a>
        <a>Environment</a>
        <a>Interaction</a>
        <a>Comparative</a>
    </nav>
</header>

<main class="analysis-layout">

    <aside class="domain-navigation">
        <!-- dynamic navigation tree -->
    </aside>

    <section class="analysis-workspace">
        <!-- analytical modules rendered here -->
    </section>

</main>

<footer class="temporal-navigation">
    <!-- interactive timeline -->
</footer>

</body>
```

---

# 3. Domain Navigation System

Left navigation allows **deep structural navigation of the firm model**.

```
Firm State
    Overview
    Genesis
    Technical Profile
    Product Catalog
    Organizational Structure
    Capital Structure
    Capability Profile

Firm Evolution
    Technical Evolution
    Product Evolution
    Organizational Evolution
    Capital Evolution

Environment
    Industry Profile
    Market Profile
    Value Chain
    Technological Landscape
    Regulatory Environment
    Infrastructure

Environment Evolution
    Market Evolution
    Technology Evolution
    Demand Evolution
    Regulatory Evolution
    Infrastructure Evolution

Firm–Environment Interaction
    Sales Evolution
    Competitive Position
    Market Share
    Market Coverage
    Profitability
```

HTML structure:

```html
<nav class="domain-tree">

<ul>
<li class="domain">Firm State
    <ul>
        <li>Overview</li>
        <li>Genesis</li>
        <li>Technical Profile</li>
        <li>Product Catalog</li>
        <li>Organization</li>
        <li>Capital Structure</li>
        <li>Capabilities</li>
    </ul>
</li>

<li class="domain">Firm Evolution</li>
<li class="domain">Environment</li>
<li class="domain">Environment Evolution</li>
<li class="domain">Firm–Environment Interaction</li>

</ul>

</nav>
```

---

# 4. Analytical Workspace

The central workspace renders **analytical modules**.

Each module has a **standard BI structure**.

```
Module
 ├─ Header
 ├─ Metrics
 ├─ Visualizations
 ├─ Data Table
 └─ Historical Timeline
```

HTML template:

```html
<section class="analysis-module">

<header class="module-header">
    <h2>Technical Profile</h2>
    <div class="module-controls">
        <button>Compare</button>
        <button>Export</button>
    </div>
</header>

<div class="module-metrics"></div>

<div class="module-visualizations"></div>

<div class="module-data-table"></div>

</section>
```

---

# 5. Historical Evolution Visualization

The **most important component** is the **evolution system**.

Evolution is visualized through:

| Visualization      | Purpose                       |
| ------------------ | ----------------------------- |
| Timeline           | chronological changes         |
| Event stream       | discrete structural events    |
| Layered change map | change in multiple dimensions |
| Time series graphs | metrics                       |
| Network evolution  | organizational structure      |

---

# 6. Evolution Timeline Component

```html
<div class="evolution-timeline">

<div class="timeline-controls">
    <button>Zoom</button>
    <button>Filter</button>
</div>

<div class="timeline-track">

<div class="timeline-event">
<span class="year">1998</span>
<span class="event">Firm Founded</span>
</div>

<div class="timeline-event">
<span class="year">2005</span>
<span class="event">New Production Technology</span>
</div>

</div>

</div>
```

---

# 7. Structural Evolution Map

Displays **how internal firm structures change**.

Example:

```
Technical Stack Evolution
1998 ── Analog Systems
2005 ── Digital Manufacturing
2012 ── Automated Production
2020 ── AI-assisted operations
```

HTML:

```html
<section class="structure-evolution">

<header>
<h3>Technical Evolution</h3>
</header>

<div class="evolution-layers">

<div class="evolution-layer">
<h4>Production Technology</h4>
<div class="evolution-track"></div>
</div>

<div class="evolution-layer">
<h4>R&D Capabilities</h4>
<div class="evolution-track"></div>
</div>

</div>

</section>
```

---

# 8. Firm–Environment Interaction Dashboard

A **KPI intelligence dashboard**.

```
┌─────────────┬─────────────┬─────────────┐
│ Revenue     │ MarketShare │ Profit      │
├─────────────┼─────────────┼─────────────┤
│ Growth      │ Regions     │ Segments    │
└─────────────┴─────────────┴─────────────┘
```

HTML:

```html
<section class="interaction-dashboard">

<div class="metric-card">
<h4>Revenue</h4>
<div class="metric-chart"></div>
</div>

<div class="metric-card">
<h4>Market Share</h4>
<div class="metric-chart"></div>
</div>

<div class="metric-card">
<h4>Profitability</h4>
<div class="metric-chart"></div>
</div>

</section>
```

---

# 9. Comparative Intelligence Mode

Advanced BI feature.

Compare:

* multiple firms
* industry benchmark
* time slices

Example UI:

```
Compare Firms
[ Firm A ] vs [ Firm B ]

Dimension:
[Technical Capabilities]
[Market Share]
[Profitability]
```

HTML:

```html
<section class="comparison-engine">

<header>
<h2>Comparative Analysis</h2>
</header>

<div class="comparison-controls">
<select class="firm-a"></select>
<select class="firm-b"></select>
</div>

<div class="comparison-visualization"></div>

</section>
```

---

# 10. Visualization Types

Recommended library stack:

| Visualization  | Library   |
| -------------- | --------- |
| time series    | D3 / Vega |
| timeline       | Vis.js    |
| network graphs | Sigma.js  |
| dashboards     | ECharts   |
| geographic     | Mapbox    |
| organizational | Cytoscape |

---

# 11. Data Model Layer

The UI consumes **structured firm representation objects**.

Example JSON:

```json
{
  "firm": {
    "overview": {},
    "technical_profile": {},
    "products": {},
    "organization": {},
    "capital": {},
    "capabilities": {}
  },
  "evolution": {
    "technical": [],
    "products": [],
    "organization": [],
    "capital": []
  },
  "environment": {},
  "interaction": {}
}
```

---

# 12. Advanced Intelligence Features

A **premium platform** should include:

### Event Intelligence

Automatically detect:

* structural change
* strategic shift
* industry disruption

---

### Structural Diff Engine

Compare firm structure between years.

Example:

```
Compare 2010 vs 2020

Changes detected
+ New product lines
+ R&D investment increase
+ Market expansion
```

---

### Strategic Timeline

A curated timeline of **major firm decisions**.

---

# 13. Visual Design Language

Recommended design system:

| Feature    | Style                |
| ---------- | -------------------- |
| background | dark intelligence UI |
| panels     | glass / card         |
| typography | data-dense           |
| charts     | minimal grid         |
| timeline   | horizontal scroll    |

---

# 14. Platform Sections

Final navigation:

```
Firm Intelligence Platform

Firm
    Overview
    Structure
    Capabilities

Evolution
    Technology
    Products
    Organization
    Capital

Environment
    Industry
    Markets
    Technology
    Regulation
    Infrastructure

Interaction
    Sales
    Market Share
    Profitability
    Competition

Comparative
    Cross-firm analysis
```

---

# 15. Reference Integration

Footer:

```html
<footer class="references">

<a href="https://www.bremontix.xyz/lab/pro/Firm/">
Firm Conceptual Framework
</a>

</footer>
```