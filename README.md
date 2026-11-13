# Housing Stability Action Kit

Mobile-friendly, single-file emergency action tracker for people facing a time-sensitive move or a Texas eviction writ. Built to reduce decision overload, not to replace a lawyer.

**Privacy design:** This public repository contains generic resources, templates, and code, **not** a tenant's case number, private communications, inventory, or photos. Each visitor's checklists, call log, personal fields and inventory are stored on that device in localStorage. Photo evidence is kept locally in IndexedDB. Nothing is intentionally uploaded to GitHub or an external backend.

**Important limitations**
- Public source code and the GitHub Pages website are accessible to anyone with the link. No authentication is provided.
- Records are **not** automatically synchronized across devices. To move them, use the **Backup** tab and securely export/import a JSON file. Backups can include unencrypted sensitive information.
- Browsers may clear local records. Private-browsing modes, low storage, changing devices, clearing website data or changing site origins can erase or separate entries.
- Original photos should also remain in the user's device photo library/private backup. The site does not verify EXIF authenticity, custodial chain, or admissibility in court.
- This is a coordination tool, not legal representation or an official court filing. Neither calls, letters, payment offers, website use, nor alleged defects automatically suspend a writ.
- Assistance funding and hours may change without notice; call before traveling. Some services require eligibility screening.

## Deployment

The repository has a static root index.html. GitHub Pages: Settings > Pages > Build and deployment > Deploy from a branch > main, folder /(root). The expected URL is https://jonsal30.github.io/housing-stability-action-kit/ after deployment succeeds.

On iPhone/iPad, open the site in Safari, then Share > Add to Home Screen.

**Never commit or upload** backup JSON, evidence photos, private completed forms, identifying case details or sensitive address lists to the public repo.

The index.html file is the entire app, with no CDN dependency. Open it locally for preview; HTTPS GitHub Pages is preferred for browser storage and photo APIs. Files in pdf/ are blank printable templates; the Letters tab can print filled copies locally.

## Emergency prioritization

First: photograph warning, protect IDs/medications/phone, call officer for timing, secure ride/truck, call 211. Next: ask management about a written postponement and officer coordination; seek legal help; document rooms and valuables. Then: move belongings, document boxes/destinations, plan safe lodging, and preserve backup. Do not let discussions of possible technical defects delay property safety.

## Public sources reviewed November 12, 2026

- Texas Property Code 24.0061: https://tcss.legis.texas.gov/resources/pr/htm/pr.24.htm
- Current 2026 Texas eviction deskbook: https://newtools.cira.state.tx.us/upload/page/3058/2026/Evictions%20Deskbook.pdf
- Texas Law Help - appealing eviction: https://texaslawhelp.org/article/appealing-an-eviction
- Texas State Law Library - personal property after eviction: https://guides.sll.texas.gov/landlord-tenant-law/tenants-property
- Harris County Constable Precinct 2 civil division: https://www.hccp2.com/Divisions/Civil-and-Writs-Division
- Harris County Justice Court Pct 2 Place 1: https://jp.hctx.net/2-1/
- Lone Star Legal Aid Houston: https://www.lonestarlegal.org/office/houston-office/
- Harris County Eviction Defense: https://hcd.harriscountytx.gov/Residents/Legal-Services/Eviction-Defense-Program
- Harris County housing support: https://hcd.harriscountytx.gov/Residents/Eviction-Prevention-Programs
- 211 Texas phone menu: https://www.211texas.org/contact-2-1-1/
- 211 United Way Greater Houston: https://unitedwayhouston.org/what-we-do/211-texas-united-way-helpline/
- Houston Food Bank: https://www.houstonfoodbank.org/find-help/find-food-map/
- Southeast Area Ministries ZIP coverage: https://www.legacycommunityhealth.org/wp-content/uploads/2024/10/Community-Resource-List_October_-2024.pdf
- Catholic Charities: https://catholiccharities.org/housing/

## Texas Apartment Association lease and legal review

TAA lease forms can vary by generation and addenda. Never assume abandonment, deposit, fees, remaining rental liability or lease-modification terms without examining the actual signed lease and addenda. An unsigned repayment proposal is not necessarily a binding agreement. Counsel should decide whether a statutory-warning omission is material and what emergency relief, if any, is available. The constable cannot normally provide legal advice.

## Development

No analytics, ads, API keys, network requests, user accounts or remote database. Enable JavaScript. Checklists, call logs, inventory, photos and backups should all be tested in a real browser. The Python generator produces generic PDF templates via Chrome.
