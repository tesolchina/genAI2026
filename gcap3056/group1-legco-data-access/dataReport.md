# Legislative Council (LegCo) Data Sources Report

**Date:** January 29, 2026  
**Purpose:** Explore LegCo information sources and understand how different data sources are connected

---

## Executive Summary

This report examines three primary data access points for Legislative Council information:
1. **LegCo Databases** (legco.gov.hk/visiting/library)
2. **Open LegCo / Open Data** (legco.gov.hk/open-legco)
3. **DATA.GOV.HK** (data.gov.hk - LegCo provider)

The key finding is that while LegCo maintains extensive data across multiple platforms, **the sources are largely fragmented and siloed**, with limited cross-referencing and no unified API access point.

---

## 1. LegCo Databases (Library System)

**URL:** https://www.legco.gov.hk/en/visiting/library/legco-databases.html

### 1.1 Library Collections

| Collection | Description | Access Method |
|------------|-------------|---------------|
| **LegCo Records Collection** | Core collection: proceedings, papers, Bills, Rules of Procedure, research papers | Ex Libris Primo (legco.primo.exlibrisgroup.com) |
| **Constitutional Collection** | Books, journals on constitutional affairs and parliamentary practices | Ex Libris Primo catalog |
| **Basic Law Collection** | Publications on Basic Law development | Ex Libris Primo catalog |
| **General Collection** | Economics, transportation, public finance, health, education resources | Ex Libris Primo catalog |

### 1.2 LegCo Databases

| Database | Description | URL Pattern | Data Format |
|----------|-------------|-------------|-------------|
| **Members Database** | Member info since 1843: names, gender, birth year, education, selection method, service years | app.legco.gov.hk/member_front | Web interface (ASPX) |
| **Members' Interests Database** | Pecuniary interests and material benefits received by Members | app.legco.gov.hk/members-interests | Web interface (HTML) |
| **Bills Database** | Bills since 1844: gazettal dates, readings, Bills Committee formation, amendment history | app.legco.gov.hk/bills | Web interface (ASPX) |
| **Official Record of Proceedings (Hansard)** | Full text search of Council proceedings since 5th LegCo (2012-2013) | app.legco.gov.hk/HansardDB | Web interface (ASPX) |
| **Rules Database** | Rules of Procedure and House Rules amendment history | app.legco.gov.hk/rules-database | Web interface (HTML) |
| **Research Publications Database** | Research papers and policy analysis by Research Office | app7.legco.gov.hk/rpdb | Angular SPA |

### 1.3 Subscribed Databases (Library Access Only)

- Britannica Online
- China Stock Market & Accounting Research Database (CSMAR)
- CPPCC Database (Chinese People's Political Consultative Conference)
- NPC Database (National People's Congress)
- Lexis Advance Hong Kong
- PKULaw (北大法寶)
- ProQuest Historical Newspapers: South China Morning Post
- OECD iLibrary

### 1.4 Archival Holdings

| Resource | Description |
|----------|-------------|
| LegCo Archives | Original records organized into 4 Fonds: Council, Committees/Subcommittees, Commission, Secretariat |
| CAROL | Catalogue for Archival Records of the Legislature - electronic catalog for searching and reserving archival records |

---

## 2. Open LegCo / Open Data

**URL:** https://www.legco.gov.hk/general/english/open-legco/open-data.html

### 2.1 Voting Results Data

Data is organized by **committee type** and **legislative term/year**:

| Committee Type | Coverage | Data Available |
|----------------|----------|----------------|
| Council Meetings (CM) | 5th LegCo (2012-2013) to 7th LegCo | Voting results XML files |
| Finance Committee (FC) | 5th-7th LegCo | Voting results XML files |
| House Committee (HC) | 5th-7th LegCo | Voting results XML files |
| Establishment Subcommittee (ESC) | 5th-7th LegCo | Voting results XML files |
| Public Works Subcommittee (PWSC) | 5th-7th LegCo | Voting results XML files |

### 2.2 Voting Results OData API

**Working Endpoint:** `https://app.legco.gov.hk/vrdb/odata/vVotingResult`

**OData Features Supported:**
- `$top` - Limit results
- `$filter` - Query filtering  
- `$format=json` - JSON output
- `$metadata` - Schema information

**Data Fields Available (vVotingResult entity):**

| Field Category | Fields |
|----------------|--------|
| **Meeting Info** | id, start_date, type, term_no, vote_number, vote_date, vote_time |
| **Motion Details** | motion_ch, motion_en, mover_ch, mover_en, mover_type |
| **Voting Mechanism** | vote_separate_mechanism, vote_non_division |
| **EC Constituency Counts** | ec_present_count, ec_vote_count, ec_yes_count, ec_no_count, ec_abstain_count, ec_result |
| **FC/GC Constituency Counts** | fc_gc_present_count, fc_gc_vote_count, fc_gc_yes_count, fc_gc_no_count, fc_gc_abstain_count, fc_gc_result |
| **GC Counts** | gc_present_count, gc_vote_count, gc_yes_count, gc_no_count, gc_abstain_count, gc_result |
| **FC Counts** | fc_present_count, fc_vote_count, fc_yes_count, fc_no_count, fc_abstain_count, fc_result |
| **Overall Counts** | overall_present_count, overall_vote_count, overall_yes_count, overall_no_count, overall_abstain_count, overall_result |
| **Member Vote Details** | name_ch, name_en, constituency, vote, display_order |

**Sample API Query:**
```
https://app.legco.gov.hk/vrdb/odata/vVotingResult?$top=10&$format=json
```

---

## 3. DATA.GOV.HK (Government Open Data Portal)

**URL:** https://data.gov.hk/en-datasets/provider/legco

### 3.1 Platform Overview

- Central government open data portal coordinated by Digital Policy Office
- Provides datasets from multiple government departments and public organizations
- Supports search, filtering by categories and formats
- Provides RSS feed for updates
- CKAN-based API available

### 3.2 LegCo-Related Categories on DATA.GOV.HK

| Category | Relevance |
|----------|-----------|
| Election and Legislature | Primary category for LegCo data |
| Law and Security | Legal and regulatory information |
| City Management and Utilities | Related policy discussions |

### 3.3 API Access

DATA.GOV.HK provides:
- REST API for dataset discovery
- CKAN API for developers
- JSON/XML data format support
- Dataset announcements and updates

---

## 4. Connections and Relationships Between Data Sources

### 4.1 Current Data Flow Map

```
┌─────────────────────────────────────────────────────────────────────┐
│                    LegCo Information Ecosystem                      │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌──────────────────┐        ┌──────────────────┐                  │
│  │  LegCo Library   │        │   Open LegCo     │                  │
│  │  (Primo System)  │        │  (Voting Data)   │                  │
│  │                  │        │                  │                  │
│  │  - Digital Docs  │        │  - OData API     │                  │
│  │  - Proceedings   │        │  - XML Files     │                  │
│  │  - Research      │        │  - JSON Output   │                  │
│  └────────┬─────────┘        └────────┬─────────┘                  │
│           │ NO LINK                   │ NO LINK                    │
│           ▼                           ▼                            │
│  ┌──────────────────┐        ┌──────────────────┐                  │
│  │  LegCo Databases │        │   DATA.GOV.HK    │                  │
│  │  (Web Apps)      │        │  (Portal)        │                  │
│  │                  │        │                  │                  │
│  │  - Members DB    │        │  - Dataset Index │                  │
│  │  - Bills DB      │        │  - CKAN API      │                  │
│  │  - Hansard DB    │        │  - Download URLs │                  │
│  │  - Rules DB      │        │                  │                  │
│  └──────────────────┘        └──────────────────┘                  │
│                                                                     │
│  ═══════════════════════════════════════════════════════════════   │
│                     ⚠️ LIMITED INTERCONNECTION                      │
└─────────────────────────────────────────────────────────────────────┘
```

### 4.2 Key Connection Points (Potential Links)

| Data Element | Found In | Could Link To |
|--------------|----------|---------------|
| **Member Names** | Members DB, Voting Results, Hansard | All systems |
| **Bill Reference Numbers** | Bills DB, Hansard | Voting Results |
| **Meeting Dates** | Voting Results, Hansard, Open Data | All systems |
| **Term/Session Numbers** | All systems | All systems |
| **Committee Types** | All systems | All systems |

### 4.3 Identified Gaps in Connectivity

| Gap | Impact | Current State |
|-----|--------|---------------|
| **No unified Member ID** | Cannot easily trace a member's complete voting history, speeches, and interests | Each database uses different identifiers |
| **Bills not linked to votes** | Difficult to see how members voted on specific legislation | Manual correlation required |
| **Hansard not connected to voting** | Cannot easily find the debate context for a specific vote | Separate search required |
| **Research papers not linked to debates** | Policy analysis disconnected from legislative discussions | Manual discovery needed |
| **No cross-database search** | Users must search each system separately | Multiple interfaces |

---

## 5. Current Data Curation Practices

### 5.1 Strengths

| Strength | Details |
|----------|---------|
| **Comprehensive Historical Records** | Members Database goes back to 1843; Bills Database to 1844 |
| **Bilingual Content** | Chinese (Traditional & Simplified) and English support |
| **Structured Voting Data** | OData API provides well-structured voting records |
| **Archival Standards** | ISAD(G) international archival description standard used |
| **Multiple Access Points** | Web interfaces, OData API, XML files available |

### 5.2 Weaknesses

| Weakness | Details |
|----------|---------|
| **Fragmented Systems** | 6+ separate database applications with different technologies |
| **Inconsistent APIs** | Only voting results has working OData; other DBs are web-only |
| **Limited Open Data Coverage** | Only voting results readily accessible via API |
| **No Entity Resolution** | Members, bills, and meetings not linked across systems |
| **Search Limitations** | Hansard search only from 5th LegCo (2012); earlier records less accessible |
| **Technology Variance** | Mix of legacy ASPX, modern Angular SPAs, and static HTML |

### 5.3 Technology Stack Analysis

| System | Technology | API Availability |
|--------|------------|------------------|
| Members Database | ASP.NET (ASPX) | ❌ No API |
| Bills Database | ASP.NET (ASPX) | ❌ No API |
| Hansard Database | ASP.NET (ASPX) | ❌ No API |
| Rules Database | Static HTML | ❌ No API |
| Research Publications | Angular SPA | ❌ No API |
| Voting Results | OData Service | ✅ OData API |
| Library Catalog | Ex Libris Primo | ✅ Primo API (limited) |

---

## 6. Recommendations for Improvement

### 6.1 Short-term Improvements

| Recommendation | Benefit | Effort |
|----------------|---------|--------|
| **Expose Bills DB via OData** | Enable programmatic access to bill progression data | Medium |
| **Add Member ID to Voting API** | Allow linking votes to member profiles | Low |
| **Create unified search API** | Single query across multiple databases | Medium |
| **Publish API documentation** | Help developers build applications | Low |

### 6.2 Medium-term Improvements

| Recommendation | Benefit | Effort |
|----------------|---------|--------|
| **Create Entity Resolution Service** | Unique IDs for members, bills, meetings across all systems | High |
| **Link Hansard to Voting Records** | Contextualize votes with debate transcripts | High |
| **Develop Research Paper API** | Programmatic access to policy research | Medium |
| **Implement GraphQL layer** | Flexible querying across related data | High |

### 6.3 Long-term Vision

| Recommendation | Benefit |
|----------------|---------|
| **Unified Legislative Knowledge Graph** | Connect all entities (members, bills, votes, speeches, committees) in a queryable graph |
| **Natural Language Query Interface** | Allow public to ask questions like "How did Member X vote on housing bills?" |
| **Real-time Data Streaming** | Live updates during Council sessions |
| **Open Linked Data Standards** | Semantic web compliance for international interoperability |

---

## 7. Use Cases for Improved Data Access

### 7.1 For Citizens

| Use Case | Current Experience | Improved Experience |
|----------|-------------------|---------------------|
| "How did my district's representative vote?" | Search multiple sites manually | Single query with unified member profile |
| "What happened with Bill X?" | Check Bills DB, then Hansard, then Voting | Integrated bill timeline with all related content |
| "What issues is LegCo discussing?" | Browse different committee pages | Unified topic dashboard |

### 7.2 For Researchers

| Use Case | Current Experience | Improved Experience |
|----------|-------------------|---------------------|
| Voting pattern analysis | Download XML/JSON, manual data cleaning | Direct API with clean, linked data |
| Legislative history study | Cross-reference multiple databases | Linked historical records |
| Policy impact assessment | Manual correlation of research papers and outcomes | Automated linking |

### 7.3 For Journalists

| Use Case | Current Experience | Improved Experience |
|----------|-------------------|---------------------|
| Fact-checking member statements | Search Hansard manually | Full-text search with vote correlation |
| Conflict of interest stories | Check interests register separately | Integrated member profile with all interests |
| Bill progress tracking | Monitor multiple pages | Real-time notification system |

---

## 8. Conclusion

LegCo maintains substantial and historically valuable data across its platforms. However, the **fundamental challenge is data fragmentation** - each database operates independently without standardized identifiers or cross-references.

### Key Question: How are different info sources connected?

**Current Answer:** They are minimally connected. The main implicit links are:
- Member names (text matching required)
- Meeting dates (manual correlation)
- Legislative term/session numbers

**Opportunity:** By implementing entity resolution and unified APIs, LegCo could transform from a collection of separate databases into an integrated knowledge platform that truly serves the public interest in understanding how their legislature works.

---

## Appendix A: Working API Endpoints

| Endpoint | Status | Format |
|----------|--------|--------|
| `https://app.legco.gov.hk/vrdb/odata/vVotingResult` | ✅ Working | OData/JSON |
| `https://www.legco.gov.hk/bi/data/general/library.json` | ✅ Working | JSON |
| `https://data.gov.hk/api/v1/datasets` | ✅ Working | REST/JSON |

## Appendix B: Data Schema (Voting Results)

```xml
<EntityType Name="vVotingResult">
  <Key>
    <PropertyRef Name="id" />
  </Key>
  <Property Name="id" Type="Edm.Int32" />
  <Property Name="start_date" Type="Edm.DateTime" />
  <Property Name="type" Type="Edm.String" />
  <Property Name="term_no" Type="Edm.Int32" />
  <Property Name="vote_number" Type="Edm.Int32" />
  <Property Name="vote_date" Type="Edm.DateTime" />
  <Property Name="motion_ch" Type="Edm.String" />
  <Property Name="motion_en" Type="Edm.String" />
  <Property Name="mover_ch" Type="Edm.String" />
  <Property Name="mover_en" Type="Edm.String" />
  <Property Name="overall_result" Type="Edm.String" />
  <Property Name="name_ch" Type="Edm.String" />
  <Property Name="name_en" Type="Edm.String" />
  <Property Name="constituency" Type="Edm.String" />
  <Property Name="vote" Type="Edm.String" />
  <!-- Additional fields for vote counts per constituency -->
</EntityType>
```

---

*Report prepared by exploring LegCo data sources through web requests and API calls*
