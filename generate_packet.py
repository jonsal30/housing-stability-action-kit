from pathlib import Path
from html import escape
import subprocess,shutil
root=Path.home()/"Documents/housing-stability-action-kit"
out=root/"pdf"; out.mkdir(exist_ok=True)
templates=[
("01_court_procedural_review","Court: urgent procedural review / filing guidance","Justice Court Precinct 2, Place 1",
"""I am the tenant in the eviction case identified above. I received a constable's final 24-hour warning on __________ at approximately __________.
The warning appears to state the posting time without separately identifying the date and time on or after which the writ will be executed. I respectfully ask how to submit this potential Texas Property Code Section 24.0061(d)(1) compliance concern for urgent judicial review.
Please confirm whether there is any entered order affecting enforcement. I understand this correspondence does not itself stop enforcement or substitute for a properly filed and served pleading.
Attachments: full final notice, writ of possession, relevant judgment or case docket, payment-plan correspondence."""),
("02_constable_schedule_review","Constable: request execution schedule / warning review","Precinct 2 Civil and Writs Division",
"""Please confirm the specific date and time, if scheduled, for execution of the writ in the case listed above.
The posted warning appears to list the date/time of posting, but may not separately state an execution date/time. Please request supervisory review for compliance with Texas Property Code Section 24.0061(d)(1).
Please provide the name of the responding staff member and a contact/reference number. I understand your office cannot provide legal advice and that this request does not itself postpone enforcement."""),
("03_management_postponement","Management: written postponement request","Property manager / owner",
"""I request a brief written postponement of execution so I can secure an orderly move and/or explore a documented resolution.
If management agrees, please specify the exact date and time through which enforcement is postponed, confirm who has communicated directly with the constable, and provide a copy of the written confirmation.
Please also provide the current itemized ledger showing rent, late fees, court costs, credits and other charges, and the written status of any proposed repayment arrangement.
I understand that requesting an extension or proposing a payment plan does not itself suspend a writ."""),
("04_urgent_legal_intake","Legal aid: urgent eviction counsel intake","Lone Star Legal Aid / qualified eviction counsel",
"""I seek emergency legal assistance because a writ of possession and a final 24-hour warning have been issued for my rental home.
I currently have no reliable income or vehicle after a period of inability to work following an automobile accident. I have proposed a payment arrangement and need an immediate review of the judgment, writ, prior service, warning language, any appeal history and lawful options.
The posted warning may lack a separately stated future execution date/time. Please advise whether a lawyer can review the documents urgently, how to submit them securely, and whether any relief is available.
I understand representation, delay and other relief are not guaranteed."""),
("05_pickup_permission","Temporary authorization for helper to collect possessions","Property management / designated helper",
"""I authorize [HELPER NAME] ______________________________, phone __________________, to assist me with packing and transporting my personal belongings.
Permitted access date/time: ___________________________.
This is not permission to dispose of property, sign legal waivers, surrender claims, or transfer ownership. No right of access after enforcement is assumed; please confirm the complex's access, check-in and supervision requirements in writing.
Items or rooms authorized: __________________________________________________________."""),
("06_forwarding_deposit","Forwarding address and request for final account","Property manager / owner",
"""Please direct future correspondence and any lawful security deposit refund/accounting to:
Forwarding mailing address: ________________________________________________________.
If keys have been returned, the date/time and recipient were: _________________________.
Please provide an itemized account of rent, fees, credits, security deposit deductions and any remaining balance, together with any applicable receipts.
This request does not acknowledge the accuracy of any disputed charges. Please confirm receipt in writing."""),
("07_property_evidence_declaration","Personal property evidence declaration","Personal records / counsel / insurer",
"""On [DATE] __________________ at [TIME] __________, I photographed the rental property and listed items that were then present. I made these records to document condition, location and disposition of personal property.
Photograph / video identifiers: _________________________________________________.
People present or assisting: _____________________________________________________.
Property moved to another location before enforcement: ____________________________.
Property left in the unit: _______________________________________________________.
Property later removed or missing (if applicable): __________________________________.
I certify that this record is true to the best of my knowledge and has not been intentionally altered.
Attached inventory pages and original photographs should be preserved separately."""),
("08_assistance_intake_notes","211 and emergency assistance call sheet","For personal use during calls",
"""ZIP / service area: ____________   Household size: _____   Safe place to sleep tonight? YES / NO
No current income: YES / NO       Transportation available: YES / NO
Housing situation: final writ warning / potential imminent displacement.
Request: immediate safe shelter, housing diversion, eviction legal defense, no-cost moving or storage, food, transport, and any current emergency grants.
Agency name: _______________________  Number: ___________________________
Contact/staff member: ______________ Reference #: _______________________
Eligibility / required documents: _______________________________________
Application open? _________  Appointment/date: _________________________
Next action and deadline: ______________________________________________
Follow-up confirmation received: ______________________________________""")
]
chrome="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
for stem,title,to,body in templates:
  html=out/(stem+".html")
  fields="""<div><b>Date:</b> __________________ &nbsp;&nbsp; <b>Case number:</b> __________________</div><div><b>Tenant:</b> _______________________ <b>Contact:</b> ________________________</div><div><b>Rental address:</b> _____________________________________________________________</div>"""
  paragraphs="".join("<p>"+escape(x)+"</p>" for x in body.split("\n") if x.strip())
  page='''<!doctype html><html><head><meta charset="utf-8"><style>@page{size:letter;margin:0.78in}body{font:12pt/1.55 Georgia,serif;color:#222}h1{font:19pt/1.2 Arial,sans-serif;color:#14364d;margin:0 0 14pt}.head{font:10.5pt/1.8 Arial,sans-serif;border-bottom:1px solid #aab;margin-bottom:18pt;padding-bottom:12pt}p{margin:11pt 0}footer{margin-top:35pt}.fine{font:9pt/1.4 Arial,sans-serif;color:#555;margin-top:40pt;border-top:1px solid #bbb;padding-top:8pt}</style></head><body><h1>'''+escape(title)+'''</h1><div class="head">'''+fields+'''<b>To:</b> '''+escape(to)+'''</div>'''+paragraphs+'''<footer>Respectfully,<br><br>_________________________________________<br>Signature / date</footer><div class="fine">Template only. Verify all facts before submission. Not an official court form, legal advice, filing confirmation, or stay of eviction.</div></body></html>'''
  html.write_text(page)
  pdf=out/(stem+".pdf")
  try:
    result=subprocess.run([chrome,"--headless=new","--disable-gpu","--no-first-run","--no-default-browser-check","--no-pdf-header-footer","--user-data-dir=/tmp/housing-pdf-"+stem,"--print-to-pdf="+str(pdf),html.as_uri()],capture_output=True,text=True,timeout=30)
    print(stem,pdf.exists(),pdf.stat().st_size if pdf.exists() else result.stderr[-300:])
  except Exception as e: print(stem,"ERROR",str(e))
