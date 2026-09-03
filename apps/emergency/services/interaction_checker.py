"""
Local rule-based pharmaceutical drug-drug interaction engine.
Evaluated strictly locally from clinical interaction rules with zero external APIs.
"""

# Clinical curated database of known pharmaceutical drug pairs and clinical severity
KNOWN_INTERACTIONS = [
    {
        'drugs': ['warfarin', 'aspirin'],
        'severity': 'SEVERE',
        'mechanism': 'Additive anticoagulant and antiplatelet inhibition.',
        'effect': 'Significantly increased risk of major gastrointestinal and systemic hemorrhage.',
        'action': 'Avoid concomitant use or closely monitor INR and coagulation parameters.'
    },
    {
        'drugs': ['lisinopril', 'ibuprofen'],
        'severity': 'MODERATE',
        'mechanism': 'NSAIDs attenuate prostaglandin-mediated renal vasodilation, antagonizing ACE inhibitor hypotensive effects.',
        'effect': 'Reduced antihypertensive efficacy and elevated risk of acute renal impairment.',
        'action': 'Monitor renal function and blood pressure; consider acetaminophen as alternative analgesic.'
    },
    {
        'drugs': ['lisinopril', 'spironolactone'],
        'severity': 'SEVERE',
        'mechanism': 'Concurrent aldosterone blockade and ACE inhibition lead to excessive potassium retention.',
        'effect': 'Severe life-threatening hyperkalemia and cardiac dysrhythmias.',
        'action': 'Regularly monitor serum potassium and ECG.'
    },
    {
        'drugs': ['metformin', 'furosemide'],
        'severity': 'MODERATE',
        'mechanism': 'Furosemide may increase metformin plasma concentrations and impair renal clearance.',
        'effect': 'Increased risk of lactic acidosis and dehydration.',
        'action': 'Monitor fluid balance and renal biomarkers.'
    },
    {
        'drugs': ['atorvastatin', 'clarithromycin'],
        'severity': 'SEVERE',
        'mechanism': 'Strong CYP3A4 inhibition by macrolide antibiotic impairs statin metabolism.',
        'effect': 'Markedly elevated statin serum concentrations leading to rhabdomyolysis and myopathy.',
        'action': 'Temporarily withhold statin during macrolide antibiotic therapy.'
    },
    {
        'drugs': ['sertraline', 'tramadol'],
        'severity': 'SEVERE',
        'mechanism': 'Combined central serotonergic transmission augmentation.',
        'effect': 'High risk of Serotonin Syndrome (autonomic instability, hyperthermia, tremor).',
        'action': 'Avoid concurrent prescription; monitor for serotonin toxicity signs.'
    },
    {
        'drugs': ['ciprofloxacin', 'calcium'],
        'severity': 'MODERATE',
        'mechanism': 'Polyvalent cations chelate fluoroquinolone antibiotics in the GI tract.',
        'effect': 'Significantly decreased fluoroquinolone systemic absorption and therapeutic failure.',
        'action': 'Separate administration by at least 2 hours before or 6 hours after cation intake.'
    },
    {
        'drugs': ['aspirin', 'ibuprofen'],
        'severity': 'MODERATE',
        'mechanism': 'Ibuprofen competitively blocks the irreversible platelet COX-1 binding site of low-dose aspirin.',
        'effect': 'Attenuated cardioprotective antiplatelet effect of daily aspirin.',
        'action': 'Take immediate-release aspirin at least 30 minutes before ibuprofen.'
    }
]


class DrugInteractionEngine:
    @staticmethod
    def check_interaction(drug_names):
        """
        Scans a list of drug names or active molecules against the local clinical rulebook.
        """
        normalized = [d.lower().strip() for d in drug_names if d]
        found_conflicts = []

        for rule in KNOWN_INTERACTIONS:
            d1, d2 = rule['drugs']
            # Match if both drugs appear as substrings in the query list
            match1 = any(d1 in name for name in normalized)
            match2 = any(d2 in name for name in normalized)

            if match1 and match2:
                found_conflicts.append(rule)

        return found_conflicts
