# Government Vacancies App Review and DATA.GOV.HK Job Data Exploration

## Executive Summary

This report examines the existing Hong Kong Government Vacancies mobile app and explores the availability of government job data on DATA.GOV.HK. 

**🎉 KEY FINDING: The Civil Service Bureau (CSB) DOES provide a comprehensive real-time Government Vacancies API through DATA.GOV.HK!**

The API provides complete job vacancy data including job titles, departments, salary information, requirements, duties, and application methods. This open data resource makes it entirely feasible to build a modern, feature-rich government vacancies app.

---

## 1. Current Government Vacancies App

### 1.1 Official Channels for Government Job Information

The Hong Kong Government provides job vacancy information through several channels:

| Channel | Description | API Available? |
|---------|-------------|----------------|
| **GovHK Portal** | Central government website (www.gov.hk/en/residents/employment/govjobs/) | ❌ Web-only |
| **Civil Service Bureau (CSB)** | Official recruitment portal (www.csb.gov.hk) | ✅ **JSON API Available** |
| **DATA.GOV.HK** | Open data portal with CSB vacancy data | ✅ **Real-time data** |
| **Interactive Employment Service (iES)** | jobs.gov.hk - Labour Department portal | ❌ Limited scope |
| **Department Websites** | Individual department recruitment pages | ❌ Fragmented |

### 1.2 Current System Capabilities

**Available via API:**
1. ✅ Centralized job vacancy JSON data from CSB
2. ✅ Real-time updates (689+ historical versions tracked)
3. ✅ Structured data with 36+ fields per vacancy
4. ✅ Trilingual support (English, Traditional Chinese, Simplified Chinese)
5. ✅ Civil service pay scales reference data

**Opportunities for Improvement:**
1. Better mobile user experience with modern UI
2. Advanced search and filtering capabilities
3. Push notifications for new job alerts
4. Personalized job recommendations
5. Application tracking features

---

## 2. DATA.GOV.HK Employment Data Exploration

### 2.1 🎯 DISCOVERY: Civil Service Bureau Government Vacancies API

**Provider:** Civil Service Bureau (hk-csb)  
**Dataset ID:** `hk-csb-csb-gov-vacancies`  
**Category:** Miscellaneous  
**Data Provider Page:** https://data.gov.hk/en-datasets/provider/hk-csb

#### Direct API Endpoints

| Language | URL | Format |
|----------|-----|--------|
| English | https://www.csb.gov.hk/datagovhk/gov-vacancies/gov-job-vacancies-en.json | JSON |
| Traditional Chinese | https://www.csb.gov.hk/datagovhk/gov-vacancies/gov-job-vacancies-tc.json | JSON |
| Simplified Chinese | https://www.csb.gov.hk/datagovhk/gov-vacancies/gov-job-vacancies-sc.json | JSON |

**Data Dictionary:** https://www.csb.gov.hk/datagovhk/gov-vacancies/gov-job-vacancies-data-dictionary-en.pdf

#### API Statistics (as of January 2026)
- **Current Vacancies:** 69 job openings
- **Historical Versions:** 689 (daily updates tracked)
- **Total Data Size:** ~457 MB (English version historical archive)

### 2.2 Job Vacancy Data Structure

Each job vacancy includes **36 comprehensive fields**:

```json
{
  "jobid": 34217,
  "jobname": "Senior Clinician (Orthodontics)",
  "deptnamejve": "Department of Health",
  "academic": ["Professional Qualification"],
  "entreq": "Candidates should have full registration... possess a Master Degree...",
  "duties": "Provision of orthodontic treatment and professional support...",
  "entrypay": "Full-time: HK$137,085 per month",
  "minpaym": 137085,
  "ccym": "HKD$",
  "appterm": "Non-civil service contract terms up to 1 year",
  "appmethod": "Apply online through G.F. 340 Online Application System...",
  "benefit": "End-of-contract gratuity (15%)... annual leave, maternity leave...",
  "enddate": "2099-12-31 23:59:00",
  "pubdate": "2025-12-31",
  "enqtel": "2961 8527",
  "enqaddr": "Appointments Section, Department of Health...",
  "iscs": "N",
  "isgf340": "Y",
  "isapplyemail": "N"
}
```

#### Complete Field List

| Field | Description | Type |
|-------|-------------|------|
| `jobid` | Unique vacancy ID | Integer |
| `jobname` | Position title | String |
| `deptnamejve` | Department name | String |
| `academic` | Required qualifications | Array |
| `entreq` | Entry requirements | String |
| `duties` | Job responsibilities | String |
| `entrypay` | Salary information | String |
| `minpaym` | Minimum monthly pay | Integer |
| `minpayh` | Minimum hourly pay | Integer |
| `minpayd` | Minimum daily pay | Integer |
| `ccym`/`ccyh`/`ccyd` | Currency codes | String |
| `appterm` | Terms of appointment | String |
| `appmethod` | Application procedure | String |
| `appnotes` | Important notes | String |
| `benefit` | Employee benefits | String |
| `pubdate` | Publication date | Date |
| `enddate` | Application deadline | Date |
| `enqtel` | Enquiry telephone | String |
| `enqaddr` | Enquiry address | String |
| `applyemail` | Application email | String |
| `iscs` | Is civil service post | Y/N |
| `isgf340` | Use GF340 online form | Y/N |
| `isapplyemail` | Accept email applications | Y/N |
| `isonlineform` | Has online form | Y/N |
| `expfrom`/`expto` | Experience required (years) | Integer |
| `jobnature` | Nature of job | String |
| `division` | Division/Branch | String |
| `depturl` | Department URL | String |
| `newspaper` | Publication in newspaper | String |
| `onlineformurl` | Online form URL | String |
| `attachfilename` | Attachment file | String |
| `submitdocumentlink` | Document submission link | String |

### 2.3 Sample Live Job Vacancies (January 2026)

| # | Position | Department | Monthly Salary (HKD) | Requirements |
|---|----------|------------|---------------------|--------------|
| 1 | Senior Clinician (Orthodontics) | Department of Health | $137,085 | Professional Qualification |
| 2 | Contract Dentist (Orthodontics) | Department of Health | $93,255 | Professional Qualification |
| 3 | Contract Senior Doctor (AMR) | Department of Health | $137,085 | Professional Qualification |
| 4 | Part-time Contract Doctor | Department of Health | Hourly rate | Professional Qualification |
| 5 | Temporary Teacher (Secondary) | Education Bureau | $35,080 | Degree |

### 2.4 Other CSB Datasets Available

| Dataset | Description | Format | URL |
|---------|-------------|--------|-----|
| **Civil Service Pay Scales** | Master Pay Scale, ICAC Pay Scale | CSV | pay-scales-cs-icac-en.csv |
| **Training Officer Establishment** | Establishment figures | CSV | establishment-to-en.csv |
| **Ethical Leadership Training** | Training participation figures | CSV | fig-cs-training-conduct-integrity-en.csv |
| **NEC Internship Timetable** | Non-ethnic Chinese internship schedule | CSV | nec-internship-timetable-en.csv |
| **ACO Recruitment Timetable** | Assistant Clerical Officer recruitment | CSV | ore-for-aco-timetable-en.csv |
| **CA Recruitment Timetable** | Clerical Assistant recruitment | CSV | ore-for-ca-timetable-en.csv |
| **PS II Recruitment Timetable** | Personal Secretary II recruitment | CSV | ore-for-psii-timetable-en.csv |
| **JRE Recruitment Figures** | Joint Recruitment Exam statistics | CSV | recruitment-fig-grade-jre-en.csv |
| **ACO Recruitment Figures** | ACO historical recruitment data | CSV | recruitment-figures-for-aco-en.csv |
| **CA Recruitment Figures** | CA historical recruitment data | CSV | recruitment-figures-for-ca-en.csv |
| **PS II Recruitment Figures** | PS II historical recruitment data | CSV | recruitment-figures-for-psii-en.csv |
| **PWD Internship Timetable** | Students with disabilities internship | CSV | pwds-internship-timetable-en.csv |

### 2.5 Civil Service Pay Scales Sample

```csv
pay_scale,point,as_at,as_at_hkd,wef,wef_hkd
Master Pay Scale,49,31.3.2025,147125,1.4.2025,147125
Master Pay Scale,48,31.3.2025,142010,1.4.2025,142010
Master Pay Scale,47,31.3.2025,137085,1.4.2025,137085
Master Pay Scale,46 (44B),31.3.2025,132275,1.4.2025,132275
Master Pay Scale,45 (44A),31.3.2025,127700,1.4.2025,127700
...
```

### 2.6 Historical Archive API Access

Use DATA.GOV.HK Historical Archive API to access historical job data:

```bash
# List all CSB files
curl "https://api.data.gov.hk/v1/historical-archive/list-files?provider=hk-csb&start=20250101&end=20260130"

# Get historical versions of vacancy data
curl "https://api.data.gov.hk/v1/historical-archive/list-file-versions?url=https://www.csb.gov.hk/datagovhk/gov-vacancies/gov-job-vacancies-en.json"
```

---

## 3. Gap Analysis

### 3.1 What We Have vs. What We Can Build

| Aspect | Available from CSB API | Opportunity for Enhancement |
|--------|------------------------|----------------------------|
| **Data Availability** | ✅ Complete JSON API | Add job categorization/tagging |
| **Update Frequency** | ✅ Daily updates (689+ versions) | Real-time push notifications |
| **Data Format** | ✅ Structured JSON | Better data normalization |
| **Trilingual Support** | ✅ EN/TC/SC versions | Unified multilingual interface |
| **Search Capability** | ❌ No search endpoint | Build full-text search with Elasticsearch |
| **Mobile Access** | ❌ Raw JSON only | Build modern mobile app |
| **Personalization** | ❌ None | Saved searches, job alerts |
| **Historical Data** | ✅ Via archive API | Trend analysis, vacancy tracking |

### 3.2 API Limitations to Address

1. **No Server-side Filtering:** Must download entire dataset and filter client-side
2. **No Search Endpoint:** No query parameters for job title, department, salary range
3. **No Pagination:** All vacancies returned in single response
4. **No Webhooks:** Cannot subscribe to new vacancy notifications
5. **Single Category Only:** Only "common" category (non-civil service contracts) visible

### 3.3 Data Quality Observations

✅ **Strengths:**
- Complete job details with 36+ fields
- Structured salary information (monthly/hourly/daily)
- Clear application methods and deadlines
- Trilingual content

⚠️ **Areas for Improvement:**
- Some jobs have null salary fields
- Long text in `appnotes` and `appmethod` fields
- Date format inconsistency (`enddate` has time, `pubdate` doesn't)
- No job category/classification taxonomy

---

## 4. Proposal: Building a Better Government Vacancies App

### 4.1 Architecture Overview

Since the CSB API provides comprehensive data, we can build a powerful app layer on top:

```
┌─────────────────────────────────────────────────────────────┐
│                    User Interface Layer                      │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐  │
│  │ Mobile App  │  │   Web App   │  │ LINE/WhatsApp Bot   │  │
│  │(React Native)│  │  (Next.js) │  │  (Job Alerts)       │  │
│  └─────────────┘  └─────────────┘  └─────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                      API Gateway                             │
│  - Authentication    - Rate Limiting    - Response Caching  │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                   Backend Services                           │
│  ┌───────────────┐  ┌───────────────┐  ┌────────────────┐   │
│  │ Job Search    │  │ Notification  │  │ User Profile   │   │
│  │ Service       │  │ Service       │  │ Service        │   │
│  │ (Elasticsearch│  │ (FCM/APNs)   │  │ (PostgreSQL)   │   │
│  └───────────────┘  └───────────────┘  └────────────────┘   │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                    Data Layer                                │
│  ┌─────────────────────────────────────────────────────┐    │
│  │ PostgreSQL Database                                  │    │
│  │ - Job Vacancies  - User Profiles  - Alert Rules     │    │
│  └─────────────────────────────────────────────────────┘    │
│  ┌─────────────────────────────────────────────────────┐    │
│  │ Elasticsearch                                        │    │
│  │ - Full-text Search  - Aggregations  - Autocomplete  │    │
│  └─────────────────────────────────────────────────────┘    │
│  ┌─────────────────────────────────────────────────────┐    │
│  │ Redis Cache                                          │    │
│  │ - API Response Cache  - Session Storage             │    │
│  └─────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                 Data Sync Layer (Scheduled)                  │
│  ┌───────────────────────────────────────────────────────┐  │
│  │ Data Sync Service (runs every 15 minutes)             │  │
│  │                                                        │  │
│  │ Sources:                                              │  │
│  │ ✅ CSB Vacancies API (gov-job-vacancies-en/tc/sc.json)│  │
│  │ ✅ CSB Pay Scales (pay-scales-cs-icac-en.csv)         │  │
│  │ ✅ Recruitment Timetables (ore-for-*.csv)             │  │
│  │ ✅ Historical Archive API (for trend analysis)        │  │
│  └───────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

### 4.2 Data Sync Implementation

```python
# data_sync.py - Fetch from CSB API
import httpx
import json
from datetime import datetime

CSB_ENDPOINTS = {
    "vacancies_en": "https://www.csb.gov.hk/datagovhk/gov-vacancies/gov-job-vacancies-en.json",
    "vacancies_tc": "https://www.csb.gov.hk/datagovhk/gov-vacancies/gov-job-vacancies-tc.json",
    "vacancies_sc": "https://www.csb.gov.hk/datagovhk/gov-vacancies/gov-job-vacancies-sc.json",
    "pay_scales": "https://www.csb.gov.hk/datagovhk/pay-scales-cs-icac/pay-scales-cs-icac-en.csv"
}

async def sync_vacancies():
    async with httpx.AsyncClient() as client:
        response = await client.get(CSB_ENDPOINTS["vacancies_en"])
        # Handle UTF-8 BOM
        data = json.loads(response.text.encode().decode('utf-8-sig'))
        
        vacancies = data.get("common", [{}])[0].get("vacancies", [])
        print(f"Synced {len(vacancies)} vacancies at {datetime.now()}")
        
        # Store in database and Elasticsearch
        for vacancy in vacancies:
            await upsert_vacancy(vacancy)
            await index_vacancy(vacancy)
        
        # Trigger notification check for new jobs
        await check_job_alerts(vacancies)
```

### 4.3 Search API Design

```python
# search_api.py - FastAPI endpoints
from fastapi import FastAPI, Query
from typing import Optional, List

app = FastAPI(title="HK Government Vacancies API")

@app.get("/api/v1/vacancies")
async def search_vacancies(
    q: Optional[str] = Query(None, description="Full-text search"),
    department: Optional[str] = None,
    min_salary: Optional[int] = None,
    max_salary: Optional[int] = None,
    academic: Optional[List[str]] = Query(None),
    is_civil_service: Optional[bool] = None,
    language: str = "en",
    page: int = 1,
    limit: int = 20
):
    """
    Search government job vacancies with advanced filters.
    Data source: Civil Service Bureau via DATA.GOV.HK
    """
    # Elasticsearch query
    query = build_es_query(
        q=q,
        department=department,
        min_salary=min_salary,
        max_salary=max_salary,
        academic=academic,
        is_civil_service=is_civil_service
    )
    
    results = await es.search(index=f"vacancies_{language}", body=query)
    return {
        "total": results["hits"]["total"]["value"],
        "page": page,
        "limit": limit,
        "vacancies": [hit["_source"] for hit in results["hits"]["hits"]]
    }

@app.get("/api/v1/departments")
async def list_departments():
    """Get list of all departments with vacancy counts."""
    agg_query = {
        "size": 0,
        "aggs": {
            "departments": {
                "terms": {"field": "deptnamejve.keyword", "size": 100}
            }
        }
    }
    results = await es.search(index="vacancies_en", body=agg_query)
    return results["aggregations"]["departments"]["buckets"]

@app.get("/api/v1/vacancies/{job_id}")
async def get_vacancy(job_id: int, language: str = "en"):
    """Get detailed vacancy information by job ID."""
    return await db.get_vacancy(job_id, language)
```

### 4.4 Key Features

| Feature | Description | Data Source | Priority |
|---------|-------------|-------------|----------|
| **Smart Search** | Full-text search across all fields | CSB API + Elasticsearch | High |
| **Department Filter** | Filter by government department | `deptnamejve` field | High |
| **Salary Filter** | Filter by pay range | `minpaym`/`minpayh` fields | High |
| **Qualification Filter** | Filter by education level | `academic` array | High |
| **Job Alerts** | Push notifications for matching jobs | New vacancy detection | High |
| **Trilingual UI** | EN/TC/SC interface | All 3 CSB API endpoints | High |
| **Salary Calculator** | Compare with pay scale points | pay-scales-cs-icac.csv | Medium |
| **Application Deadline Alerts** | Reminder before deadline | `enddate` field | Medium |
| **Career Path Info** | Link to recruitment timetables | ore-for-*.csv files | Medium |
| **Historical Trends** | Show vacancy trends over time | Archive API versions | Low |
| **AI Resume Match** | Match resume to requirements | `entreq` field analysis | Low |

### 4.5 Integration with CSB Data Resources

| Resource | Integration | Use Case |
|----------|-------------|----------|
| **gov-job-vacancies-*.json** | Primary data source | All vacancy listings |
| **pay-scales-cs-icac-*.csv** | Salary reference | Pay point to HKD conversion |
| **ore-for-aco-timetable-*.csv** | Career planning | ACO recruitment calendar |
| **ore-for-ca-timetable-*.csv** | Career planning | CA recruitment calendar |
| **ore-for-psii-timetable-*.csv** | Career planning | PS II recruitment calendar |
| **recruitment-fig-grade-jre-*.csv** | Statistics | Historical success rates |
| **Historical Archive API** | Trend analysis | Track vacancy changes over time |

### 4.6 Technical Stack Recommendation

| Component | Technology | Rationale |
|-----------|------------|-----------|
| **Frontend (Mobile)** | React Native / Flutter | Cross-platform, native performance |
| **Frontend (Web)** | Next.js 14 | App Router, SSR, good SEO |
| **Backend API** | Python FastAPI | Async, automatic OpenAPI docs |
| **Database** | PostgreSQL 16 | JSONB for vacancy data |
| **Search Engine** | Elasticsearch 8 | Full-text search, Chinese analyzer |
| **Cache** | Redis | API response caching |
| **Scheduler** | Celery Beat | Periodic data sync |
| **Push Notifications** | Firebase Cloud Messaging | Cross-platform push |
| **Hosting** | Azure HK Region | Low latency for HK users |

---

## 5. Implementation Roadmap

### Phase 1: MVP (2-3 weeks)
- [x] ✅ Confirm CSB API data availability (DONE)
- [ ] Set up data sync from CSB JSON endpoints
- [ ] Create PostgreSQL schema for vacancy data
- [ ] Build basic FastAPI REST endpoints
- [ ] Implement simple React Native UI
- [ ] Deploy to Azure/Vercel for testing

### Phase 2: Search & Filters (2 weeks)
- [ ] Set up Elasticsearch cluster
- [ ] Index vacancy data with Chinese analyzer
- [ ] Implement advanced search API
- [ ] Add department/salary/qualification filters
- [ ] Build filter UI components

### Phase 3: User Features (2 weeks)
- [ ] User registration (optional, for alerts)
- [ ] Job alert subscription system
- [ ] Push notification integration (FCM)
- [ ] Saved jobs / bookmarks
- [ ] Trilingual language switching

### Phase 4: Polish & Launch (2 weeks)
- [ ] Pay scale integration and calculator
- [ ] Recruitment timetable integration
- [ ] Historical trend visualizations
- [ ] App Store / Play Store submission
- [ ] Landing page and documentation

---

## 6. Recommendations

### For App Development Team

1. **Use Official CSB API Directly**
   - No scraping needed! CSB provides structured JSON data
   - Sync data every 15-30 minutes for near real-time updates
   - Handle UTF-8 BOM in JSON responses (`encoding='utf-8-sig'`)

2. **Build a Search Layer**
   - CSB API has no search endpoint - build your own with Elasticsearch
   - Support Chinese full-text search with appropriate analyzers
   - Cache API responses to reduce load on CSB servers

3. **Add Value Beyond Raw Data**
   - Job alert notifications (not available from CSB)
   - Advanced filtering and saved searches
   - Salary comparisons with pay scale data
   - Application deadline reminders

### For Government (Feedback to DATA.GOV.HK)

1. **API Enhancements Requested:**
   - Add server-side filtering parameters
   - Provide search endpoint
   - Add pagination support
   - Include civil service vacancies (not just contract positions)
   - Add webhook/subscription for real-time updates

2. **Data Quality Improvements:**
   - Standardize date formats
   - Add job category taxonomy
   - Include location/district information
   - Normalize salary data (some entries have null values)

---

## 7. Conclusion

**Great news!** The Civil Service Bureau (CSB) provides a comprehensive **Government Vacancies API through DATA.GOV.HK** with:

✅ **69 current job vacancies** (as of January 2026)  
✅ **36+ data fields** per vacancy (job details, salary, requirements, application info)  
✅ **Trilingual support** (English, Traditional Chinese, Simplified Chinese)  
✅ **Daily updates** (689+ historical versions tracked)  
✅ **Supplementary data** (pay scales, recruitment timetables, statistics)  

This makes it entirely feasible to build a modern, feature-rich government vacancies app that:

1. **Consumes official CSB data** - No scraping required
2. **Adds powerful search** - Full-text search with Elasticsearch
3. **Enables personalization** - Job alerts and saved searches
4. **Provides mobile experience** - Native apps with push notifications
5. **Offers value-added features** - Salary calculator, deadline reminders, trends

### Key API Endpoints

| Resource | URL |
|----------|-----|
| **Job Vacancies (EN)** | https://www.csb.gov.hk/datagovhk/gov-vacancies/gov-job-vacancies-en.json |
| **Job Vacancies (TC)** | https://www.csb.gov.hk/datagovhk/gov-vacancies/gov-job-vacancies-tc.json |
| **Job Vacancies (SC)** | https://www.csb.gov.hk/datagovhk/gov-vacancies/gov-job-vacancies-sc.json |
| **Pay Scales** | https://www.csb.gov.hk/datagovhk/pay-scales-cs-icac/pay-scales-cs-icac-en.csv |
| **Data Dictionary** | https://www.csb.gov.hk/datagovhk/gov-vacancies/gov-job-vacancies-data-dictionary-en.pdf |
| **CSB Provider Page** | https://data.gov.hk/en-datasets/provider/hk-csb |

---

## Appendix A: CSB API Quick Reference

### Fetch Current Vacancies
```bash
# English
curl -s "https://www.csb.gov.hk/datagovhk/gov-vacancies/gov-job-vacancies-en.json" -o vacancies.json

# Parse with Python (note: UTF-8 BOM handling)
python3 << 'EOF'
import json
with open('vacancies.json', encoding='utf-8-sig') as f:
    data = json.load(f)
    vacancies = data['common'][0]['vacancies']
    print(f"Total vacancies: {len(vacancies)}")
    for v in vacancies[:5]:
        print(f"- {v['jobname']} @ {v['deptnamejve']}")
EOF
```

### Fetch Pay Scales
```bash
curl -s "https://www.csb.gov.hk/datagovhk/pay-scales-cs-icac/pay-scales-cs-icac-en.csv" | head -10
```

### List All CSB Datasets via Archive API
```bash
curl "https://api.data.gov.hk/v1/historical-archive/list-files?provider=hk-csb&start=20250101&end=20260130"
```

### Get Historical Versions
```bash
curl "https://api.data.gov.hk/v1/historical-archive/list-file-versions?url=https://www.csb.gov.hk/datagovhk/gov-vacancies/gov-job-vacancies-en.json"
```

---

## Appendix B: Sample Vacancy Data

```json
{
  "jobid": 34217,
  "jobname": "Senior Clinician (Orthodontics)",
  "deptnamejve": "Department of Health",
  "academic": ["Professional Qualification"],
  "entreq": "Candidates should have full registration in Hong Kong under the Dentists Registration Ordinance; possess a valid practising certificate issued by the Dental Council of Hong Kong; possess a Master Degree in Orthodontics; and have a good command of spoken and written Chinese and English.",
  "duties": "Provision of orthodontic treatment and professional support in the orthodontic training of Dental Officers at Government Orthodontic Clinics.",
  "entrypay": "Full-time: HK$137,085 per month (plus end-of-contract gratuity). Part-time: HK$780 per hour",
  "minpaym": 137085,
  "ccym": "HKD$",
  "appterm": "Successful candidates will be appointed on non-civil service contract terms up to 1 year. Renewal of contract will be subject to the service need of the Department and the performance of the candidate.",
  "appmethod": "Applicants must apply online through the G.F. 340 Online Application System of the Civil Service Bureau (https://www.csb.gov.hk).",
  "benefit": "End-of-contract gratuity may be granted upon satisfactory completion of the contract (15% of total basic salary). Rest days, statutory holidays, annual leave, maternity/paternity leave and sickness allowance will be granted.",
  "pubdate": "2025-12-31",
  "enddate": "2099-12-31 23:59:00",
  "enqtel": "2961 8527",
  "enqaddr": "Appointments Section, Department of Health, Room 1807, 18/F, Wu Chung House, 213 Queen's Road East, Wan Chai, Hong Kong",
  "iscs": "N",
  "isgf340": "Y"
}
```

---

## Appendix C: CSB Dataset List

| Dataset ID | Name | Format | Files |
|------------|------|--------|-------|
| hk-csb-csb-gov-vacancies | Government Vacancies | JSON | 3 (EN/TC/SC) |
| hk-csb-csb-pay-scales-cs-icac | Civil Service Pay Scales | CSV | 3 |
| hk-csb-csb-establishment-to | Training Officer Establishment | CSV | 3 |
| hk-csb-csb-fig-cs-training-conduct-integrity | Ethical Leadership Training | CSV | 3 |
| hk-csb-csb-nec-internship-timetable | NEC Internship Timetable | CSV | 3 |
| hk-csb-csb-ore-for-aco-timetable | ACO Recruitment Timetable | CSV | 3 |
| hk-csb-csb-ore-for-ca-timetable | CA Recruitment Timetable | CSV | 3 |
| hk-csb-csb-ore-for-psii-timetable | PS II Recruitment Timetable | CSV | 3 |
| hk-csb-csb-pwds-internship-timetable | PWD Students Internship | CSV | 3 |
| hk-csb-csb-recruitment-fig-grade-jre | JRE Recruitment Figures | CSV | 3 |
| hk-csb-csb-recruitment-figures-for-aco | ACO Recruitment Figures | CSV | 3 |
| hk-csb-csb-recruitment-figures-for-ca | CA Recruitment Figures | CSV | 3 |
| hk-csb-csb-recruitment-figures-for-psii | PS II Recruitment Figures | CSV | 3 |

---

*Report generated: January 30, 2026*  
*Author: Group 3 - Government App Project*  
*Data Source: Civil Service Bureau via DATA.GOV.HK*
