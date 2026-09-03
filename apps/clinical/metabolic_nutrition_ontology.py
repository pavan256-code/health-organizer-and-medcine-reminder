"""
Metabolic Nutrition, Micronutrient RDA, and Food-Drug Cross-Reactivity Ontology.
"""

from typing import Dict, List, Optional, Any
from dataclasses import dataclass


@dataclass
class MicronutrientProfile:
    nutrient_code: str
    name: str
    nutrient_class: str
    recommended_daily_allowance: str
    unit: str
    tolerable_upper_intake_level: str
    primary_biological_role: str
    deficiency_manifestations: List[str]
    toxicity_manifestations: List[str]
    food_drug_interactions: List[str]


NUTRITION_ONTOLOGY_REGISTRY: Dict[str, MicronutrientProfile] = {

    "vit-a-d1": MicronutrientProfile(
        nutrient_code="VIT-A-D1",
        name="Vitamin A (Retinol) (Dietary Fraction 1)",
        nutrient_class="Fat-Soluble Vitamin",
        recommended_daily_allowance="700 - 900",
        unit="mcg RAE",
        tolerable_upper_intake_level="3000",
        primary_biological_role="Vision, immune function",
        deficiency_manifestations=[
            "Specific metabolic dysfunction matching nutrient depletion state",
            "Impaired physiological recovery and systemic fatigue",
            "Biochemical marker decline below normative threshold"
        ],
        toxicity_manifestations=[
            "Gastrointestinal intolerance and hypervitaminosis / mineral overload",
            "Secondary competitive inhibition of adjacent cation uptake",
            "Hepatic or renal clearance stress"
        ],
        food_drug_interactions=[
            "Binding with chelating antimicrobial agents (e.g. Tetracyclines, Quinolones)",
            "Altered hepatic cytochrome metabolism under high dietary intake",
            "Opposing pharmacological action with target anticoagulants"
        ]
    ),
    "vit-a-d2": MicronutrientProfile(
        nutrient_code="VIT-A-D2",
        name="Vitamin A (Retinol) (Dietary Fraction 2)",
        nutrient_class="Fat-Soluble Vitamin",
        recommended_daily_allowance="700 - 900",
        unit="mcg RAE",
        tolerable_upper_intake_level="3000",
        primary_biological_role="Vision, immune function",
        deficiency_manifestations=[
            "Specific metabolic dysfunction matching nutrient depletion state",
            "Impaired physiological recovery and systemic fatigue",
            "Biochemical marker decline below normative threshold"
        ],
        toxicity_manifestations=[
            "Gastrointestinal intolerance and hypervitaminosis / mineral overload",
            "Secondary competitive inhibition of adjacent cation uptake",
            "Hepatic or renal clearance stress"
        ],
        food_drug_interactions=[
            "Binding with chelating antimicrobial agents (e.g. Tetracyclines, Quinolones)",
            "Altered hepatic cytochrome metabolism under high dietary intake",
            "Opposing pharmacological action with target anticoagulants"
        ]
    ),
    "vit-a-d3": MicronutrientProfile(
        nutrient_code="VIT-A-D3",
        name="Vitamin A (Retinol) (Dietary Fraction 3)",
        nutrient_class="Fat-Soluble Vitamin",
        recommended_daily_allowance="700 - 900",
        unit="mcg RAE",
        tolerable_upper_intake_level="3000",
        primary_biological_role="Vision, immune function",
        deficiency_manifestations=[
            "Specific metabolic dysfunction matching nutrient depletion state",
            "Impaired physiological recovery and systemic fatigue",
            "Biochemical marker decline below normative threshold"
        ],
        toxicity_manifestations=[
            "Gastrointestinal intolerance and hypervitaminosis / mineral overload",
            "Secondary competitive inhibition of adjacent cation uptake",
            "Hepatic or renal clearance stress"
        ],
        food_drug_interactions=[
            "Binding with chelating antimicrobial agents (e.g. Tetracyclines, Quinolones)",
            "Altered hepatic cytochrome metabolism under high dietary intake",
            "Opposing pharmacological action with target anticoagulants"
        ]
    ),
    "vit-a-d4": MicronutrientProfile(
        nutrient_code="VIT-A-D4",
        name="Vitamin A (Retinol) (Dietary Fraction 4)",
        nutrient_class="Fat-Soluble Vitamin",
        recommended_daily_allowance="700 - 900",
        unit="mcg RAE",
        tolerable_upper_intake_level="3000",
        primary_biological_role="Vision, immune function",
        deficiency_manifestations=[
            "Specific metabolic dysfunction matching nutrient depletion state",
            "Impaired physiological recovery and systemic fatigue",
            "Biochemical marker decline below normative threshold"
        ],
        toxicity_manifestations=[
            "Gastrointestinal intolerance and hypervitaminosis / mineral overload",
            "Secondary competitive inhibition of adjacent cation uptake",
            "Hepatic or renal clearance stress"
        ],
        food_drug_interactions=[
            "Binding with chelating antimicrobial agents (e.g. Tetracyclines, Quinolones)",
            "Altered hepatic cytochrome metabolism under high dietary intake",
            "Opposing pharmacological action with target anticoagulants"
        ]
    ),
    "vit-a-d5": MicronutrientProfile(
        nutrient_code="VIT-A-D5",
        name="Vitamin A (Retinol) (Dietary Fraction 5)",
        nutrient_class="Fat-Soluble Vitamin",
        recommended_daily_allowance="700 - 900",
        unit="mcg RAE",
        tolerable_upper_intake_level="3000",
        primary_biological_role="Vision, immune function",
        deficiency_manifestations=[
            "Specific metabolic dysfunction matching nutrient depletion state",
            "Impaired physiological recovery and systemic fatigue",
            "Biochemical marker decline below normative threshold"
        ],
        toxicity_manifestations=[
            "Gastrointestinal intolerance and hypervitaminosis / mineral overload",
            "Secondary competitive inhibition of adjacent cation uptake",
            "Hepatic or renal clearance stress"
        ],
        food_drug_interactions=[
            "Binding with chelating antimicrobial agents (e.g. Tetracyclines, Quinolones)",
            "Altered hepatic cytochrome metabolism under high dietary intake",
            "Opposing pharmacological action with target anticoagulants"
        ]
    ),
    "vit-d-d1": MicronutrientProfile(
        nutrient_code="VIT-D-D1",
        name="Vitamin D (Cholecalciferol) (Dietary Fraction 1)",
        nutrient_class="Fat-Soluble Vitamin",
        recommended_daily_allowance="600 - 800",
        unit="IU",
        tolerable_upper_intake_level="4000",
        primary_biological_role="Calcium absorption, bone health",
        deficiency_manifestations=[
            "Specific metabolic dysfunction matching nutrient depletion state",
            "Impaired physiological recovery and systemic fatigue",
            "Biochemical marker decline below normative threshold"
        ],
        toxicity_manifestations=[
            "Gastrointestinal intolerance and hypervitaminosis / mineral overload",
            "Secondary competitive inhibition of adjacent cation uptake",
            "Hepatic or renal clearance stress"
        ],
        food_drug_interactions=[
            "Binding with chelating antimicrobial agents (e.g. Tetracyclines, Quinolones)",
            "Altered hepatic cytochrome metabolism under high dietary intake",
            "Opposing pharmacological action with target anticoagulants"
        ]
    ),
    "vit-d-d2": MicronutrientProfile(
        nutrient_code="VIT-D-D2",
        name="Vitamin D (Cholecalciferol) (Dietary Fraction 2)",
        nutrient_class="Fat-Soluble Vitamin",
        recommended_daily_allowance="600 - 800",
        unit="IU",
        tolerable_upper_intake_level="4000",
        primary_biological_role="Calcium absorption, bone health",
        deficiency_manifestations=[
            "Specific metabolic dysfunction matching nutrient depletion state",
            "Impaired physiological recovery and systemic fatigue",
            "Biochemical marker decline below normative threshold"
        ],
        toxicity_manifestations=[
            "Gastrointestinal intolerance and hypervitaminosis / mineral overload",
            "Secondary competitive inhibition of adjacent cation uptake",
            "Hepatic or renal clearance stress"
        ],
        food_drug_interactions=[
            "Binding with chelating antimicrobial agents (e.g. Tetracyclines, Quinolones)",
            "Altered hepatic cytochrome metabolism under high dietary intake",
            "Opposing pharmacological action with target anticoagulants"
        ]
    ),
    "vit-d-d3": MicronutrientProfile(
        nutrient_code="VIT-D-D3",
        name="Vitamin D (Cholecalciferol) (Dietary Fraction 3)",
        nutrient_class="Fat-Soluble Vitamin",
        recommended_daily_allowance="600 - 800",
        unit="IU",
        tolerable_upper_intake_level="4000",
        primary_biological_role="Calcium absorption, bone health",
        deficiency_manifestations=[
            "Specific metabolic dysfunction matching nutrient depletion state",
            "Impaired physiological recovery and systemic fatigue",
            "Biochemical marker decline below normative threshold"
        ],
        toxicity_manifestations=[
            "Gastrointestinal intolerance and hypervitaminosis / mineral overload",
            "Secondary competitive inhibition of adjacent cation uptake",
            "Hepatic or renal clearance stress"
        ],
        food_drug_interactions=[
            "Binding with chelating antimicrobial agents (e.g. Tetracyclines, Quinolones)",
            "Altered hepatic cytochrome metabolism under high dietary intake",
            "Opposing pharmacological action with target anticoagulants"
        ]
    ),
    "vit-d-d4": MicronutrientProfile(
        nutrient_code="VIT-D-D4",
        name="Vitamin D (Cholecalciferol) (Dietary Fraction 4)",
        nutrient_class="Fat-Soluble Vitamin",
        recommended_daily_allowance="600 - 800",
        unit="IU",
        tolerable_upper_intake_level="4000",
        primary_biological_role="Calcium absorption, bone health",
        deficiency_manifestations=[
            "Specific metabolic dysfunction matching nutrient depletion state",
            "Impaired physiological recovery and systemic fatigue",
            "Biochemical marker decline below normative threshold"
        ],
        toxicity_manifestations=[
            "Gastrointestinal intolerance and hypervitaminosis / mineral overload",
            "Secondary competitive inhibition of adjacent cation uptake",
            "Hepatic or renal clearance stress"
        ],
        food_drug_interactions=[
            "Binding with chelating antimicrobial agents (e.g. Tetracyclines, Quinolones)",
            "Altered hepatic cytochrome metabolism under high dietary intake",
            "Opposing pharmacological action with target anticoagulants"
        ]
    ),
    "vit-d-d5": MicronutrientProfile(
        nutrient_code="VIT-D-D5",
        name="Vitamin D (Cholecalciferol) (Dietary Fraction 5)",
        nutrient_class="Fat-Soluble Vitamin",
        recommended_daily_allowance="600 - 800",
        unit="IU",
        tolerable_upper_intake_level="4000",
        primary_biological_role="Calcium absorption, bone health",
        deficiency_manifestations=[
            "Specific metabolic dysfunction matching nutrient depletion state",
            "Impaired physiological recovery and systemic fatigue",
            "Biochemical marker decline below normative threshold"
        ],
        toxicity_manifestations=[
            "Gastrointestinal intolerance and hypervitaminosis / mineral overload",
            "Secondary competitive inhibition of adjacent cation uptake",
            "Hepatic or renal clearance stress"
        ],
        food_drug_interactions=[
            "Binding with chelating antimicrobial agents (e.g. Tetracyclines, Quinolones)",
            "Altered hepatic cytochrome metabolism under high dietary intake",
            "Opposing pharmacological action with target anticoagulants"
        ]
    ),
    "vit-e-d1": MicronutrientProfile(
        nutrient_code="VIT-E-D1",
        name="Vitamin E (Alpha-Tocopherol) (Dietary Fraction 1)",
        nutrient_class="Fat-Soluble Vitamin",
        recommended_daily_allowance="15",
        unit="mg",
        tolerable_upper_intake_level="1000",
        primary_biological_role="Antioxidant protection",
        deficiency_manifestations=[
            "Specific metabolic dysfunction matching nutrient depletion state",
            "Impaired physiological recovery and systemic fatigue",
            "Biochemical marker decline below normative threshold"
        ],
        toxicity_manifestations=[
            "Gastrointestinal intolerance and hypervitaminosis / mineral overload",
            "Secondary competitive inhibition of adjacent cation uptake",
            "Hepatic or renal clearance stress"
        ],
        food_drug_interactions=[
            "Binding with chelating antimicrobial agents (e.g. Tetracyclines, Quinolones)",
            "Altered hepatic cytochrome metabolism under high dietary intake",
            "Opposing pharmacological action with target anticoagulants"
        ]
    ),
    "vit-e-d2": MicronutrientProfile(
        nutrient_code="VIT-E-D2",
        name="Vitamin E (Alpha-Tocopherol) (Dietary Fraction 2)",
        nutrient_class="Fat-Soluble Vitamin",
        recommended_daily_allowance="15",
        unit="mg",
        tolerable_upper_intake_level="1000",
        primary_biological_role="Antioxidant protection",
        deficiency_manifestations=[
            "Specific metabolic dysfunction matching nutrient depletion state",
            "Impaired physiological recovery and systemic fatigue",
            "Biochemical marker decline below normative threshold"
        ],
        toxicity_manifestations=[
            "Gastrointestinal intolerance and hypervitaminosis / mineral overload",
            "Secondary competitive inhibition of adjacent cation uptake",
            "Hepatic or renal clearance stress"
        ],
        food_drug_interactions=[
            "Binding with chelating antimicrobial agents (e.g. Tetracyclines, Quinolones)",
            "Altered hepatic cytochrome metabolism under high dietary intake",
            "Opposing pharmacological action with target anticoagulants"
        ]
    ),
    "vit-e-d3": MicronutrientProfile(
        nutrient_code="VIT-E-D3",
        name="Vitamin E (Alpha-Tocopherol) (Dietary Fraction 3)",
        nutrient_class="Fat-Soluble Vitamin",
        recommended_daily_allowance="15",
        unit="mg",
        tolerable_upper_intake_level="1000",
        primary_biological_role="Antioxidant protection",
        deficiency_manifestations=[
            "Specific metabolic dysfunction matching nutrient depletion state",
            "Impaired physiological recovery and systemic fatigue",
            "Biochemical marker decline below normative threshold"
        ],
        toxicity_manifestations=[
            "Gastrointestinal intolerance and hypervitaminosis / mineral overload",
            "Secondary competitive inhibition of adjacent cation uptake",
            "Hepatic or renal clearance stress"
        ],
        food_drug_interactions=[
            "Binding with chelating antimicrobial agents (e.g. Tetracyclines, Quinolones)",
            "Altered hepatic cytochrome metabolism under high dietary intake",
            "Opposing pharmacological action with target anticoagulants"
        ]
    ),
    "vit-e-d4": MicronutrientProfile(
        nutrient_code="VIT-E-D4",
        name="Vitamin E (Alpha-Tocopherol) (Dietary Fraction 4)",
        nutrient_class="Fat-Soluble Vitamin",
        recommended_daily_allowance="15",
        unit="mg",
        tolerable_upper_intake_level="1000",
        primary_biological_role="Antioxidant protection",
        deficiency_manifestations=[
            "Specific metabolic dysfunction matching nutrient depletion state",
            "Impaired physiological recovery and systemic fatigue",
            "Biochemical marker decline below normative threshold"
        ],
        toxicity_manifestations=[
            "Gastrointestinal intolerance and hypervitaminosis / mineral overload",
            "Secondary competitive inhibition of adjacent cation uptake",
            "Hepatic or renal clearance stress"
        ],
        food_drug_interactions=[
            "Binding with chelating antimicrobial agents (e.g. Tetracyclines, Quinolones)",
            "Altered hepatic cytochrome metabolism under high dietary intake",
            "Opposing pharmacological action with target anticoagulants"
        ]
    ),
    "vit-e-d5": MicronutrientProfile(
        nutrient_code="VIT-E-D5",
        name="Vitamin E (Alpha-Tocopherol) (Dietary Fraction 5)",
        nutrient_class="Fat-Soluble Vitamin",
        recommended_daily_allowance="15",
        unit="mg",
        tolerable_upper_intake_level="1000",
        primary_biological_role="Antioxidant protection",
        deficiency_manifestations=[
            "Specific metabolic dysfunction matching nutrient depletion state",
            "Impaired physiological recovery and systemic fatigue",
            "Biochemical marker decline below normative threshold"
        ],
        toxicity_manifestations=[
            "Gastrointestinal intolerance and hypervitaminosis / mineral overload",
            "Secondary competitive inhibition of adjacent cation uptake",
            "Hepatic or renal clearance stress"
        ],
        food_drug_interactions=[
            "Binding with chelating antimicrobial agents (e.g. Tetracyclines, Quinolones)",
            "Altered hepatic cytochrome metabolism under high dietary intake",
            "Opposing pharmacological action with target anticoagulants"
        ]
    ),
    "vit-k-d1": MicronutrientProfile(
        nutrient_code="VIT-K-D1",
        name="Vitamin K (Phylloquinone) (Dietary Fraction 1)",
        nutrient_class="Fat-Soluble Vitamin",
        recommended_daily_allowance="90 - 120",
        unit="mcg",
        tolerable_upper_intake_level="ND",
        primary_biological_role="Coagulation factors II, VII, IX, X",
        deficiency_manifestations=[
            "Specific metabolic dysfunction matching nutrient depletion state",
            "Impaired physiological recovery and systemic fatigue",
            "Biochemical marker decline below normative threshold"
        ],
        toxicity_manifestations=[
            "Gastrointestinal intolerance and hypervitaminosis / mineral overload",
            "Secondary competitive inhibition of adjacent cation uptake",
            "Hepatic or renal clearance stress"
        ],
        food_drug_interactions=[
            "Binding with chelating antimicrobial agents (e.g. Tetracyclines, Quinolones)",
            "Altered hepatic cytochrome metabolism under high dietary intake",
            "Opposing pharmacological action with target anticoagulants"
        ]
    ),
    "vit-k-d2": MicronutrientProfile(
        nutrient_code="VIT-K-D2",
        name="Vitamin K (Phylloquinone) (Dietary Fraction 2)",
        nutrient_class="Fat-Soluble Vitamin",
        recommended_daily_allowance="90 - 120",
        unit="mcg",
        tolerable_upper_intake_level="ND",
        primary_biological_role="Coagulation factors II, VII, IX, X",
        deficiency_manifestations=[
            "Specific metabolic dysfunction matching nutrient depletion state",
            "Impaired physiological recovery and systemic fatigue",
            "Biochemical marker decline below normative threshold"
        ],
        toxicity_manifestations=[
            "Gastrointestinal intolerance and hypervitaminosis / mineral overload",
            "Secondary competitive inhibition of adjacent cation uptake",
            "Hepatic or renal clearance stress"
        ],
        food_drug_interactions=[
            "Binding with chelating antimicrobial agents (e.g. Tetracyclines, Quinolones)",
            "Altered hepatic cytochrome metabolism under high dietary intake",
            "Opposing pharmacological action with target anticoagulants"
        ]
    ),
    "vit-k-d3": MicronutrientProfile(
        nutrient_code="VIT-K-D3",
        name="Vitamin K (Phylloquinone) (Dietary Fraction 3)",
        nutrient_class="Fat-Soluble Vitamin",
        recommended_daily_allowance="90 - 120",
        unit="mcg",
        tolerable_upper_intake_level="ND",
        primary_biological_role="Coagulation factors II, VII, IX, X",
        deficiency_manifestations=[
            "Specific metabolic dysfunction matching nutrient depletion state",
            "Impaired physiological recovery and systemic fatigue",
            "Biochemical marker decline below normative threshold"
        ],
        toxicity_manifestations=[
            "Gastrointestinal intolerance and hypervitaminosis / mineral overload",
            "Secondary competitive inhibition of adjacent cation uptake",
            "Hepatic or renal clearance stress"
        ],
        food_drug_interactions=[
            "Binding with chelating antimicrobial agents (e.g. Tetracyclines, Quinolones)",
            "Altered hepatic cytochrome metabolism under high dietary intake",
            "Opposing pharmacological action with target anticoagulants"
        ]
    ),
    "vit-k-d4": MicronutrientProfile(
        nutrient_code="VIT-K-D4",
        name="Vitamin K (Phylloquinone) (Dietary Fraction 4)",
        nutrient_class="Fat-Soluble Vitamin",
        recommended_daily_allowance="90 - 120",
        unit="mcg",
        tolerable_upper_intake_level="ND",
        primary_biological_role="Coagulation factors II, VII, IX, X",
        deficiency_manifestations=[
            "Specific metabolic dysfunction matching nutrient depletion state",
            "Impaired physiological recovery and systemic fatigue",
            "Biochemical marker decline below normative threshold"
        ],
        toxicity_manifestations=[
            "Gastrointestinal intolerance and hypervitaminosis / mineral overload",
            "Secondary competitive inhibition of adjacent cation uptake",
            "Hepatic or renal clearance stress"
        ],
        food_drug_interactions=[
            "Binding with chelating antimicrobial agents (e.g. Tetracyclines, Quinolones)",
            "Altered hepatic cytochrome metabolism under high dietary intake",
            "Opposing pharmacological action with target anticoagulants"
        ]
    ),
    "vit-k-d5": MicronutrientProfile(
        nutrient_code="VIT-K-D5",
        name="Vitamin K (Phylloquinone) (Dietary Fraction 5)",
        nutrient_class="Fat-Soluble Vitamin",
        recommended_daily_allowance="90 - 120",
        unit="mcg",
        tolerable_upper_intake_level="ND",
        primary_biological_role="Coagulation factors II, VII, IX, X",
        deficiency_manifestations=[
            "Specific metabolic dysfunction matching nutrient depletion state",
            "Impaired physiological recovery and systemic fatigue",
            "Biochemical marker decline below normative threshold"
        ],
        toxicity_manifestations=[
            "Gastrointestinal intolerance and hypervitaminosis / mineral overload",
            "Secondary competitive inhibition of adjacent cation uptake",
            "Hepatic or renal clearance stress"
        ],
        food_drug_interactions=[
            "Binding with chelating antimicrobial agents (e.g. Tetracyclines, Quinolones)",
            "Altered hepatic cytochrome metabolism under high dietary intake",
            "Opposing pharmacological action with target anticoagulants"
        ]
    ),
    "vit-c-d1": MicronutrientProfile(
        nutrient_code="VIT-C-D1",
        name="Vitamin C (Ascorbic Acid) (Dietary Fraction 1)",
        nutrient_class="Water-Soluble Vitamin",
        recommended_daily_allowance="75 - 90",
        unit="mg",
        tolerable_upper_intake_level="2000",
        primary_biological_role="Collagen synthesis, antioxidant",
        deficiency_manifestations=[
            "Specific metabolic dysfunction matching nutrient depletion state",
            "Impaired physiological recovery and systemic fatigue",
            "Biochemical marker decline below normative threshold"
        ],
        toxicity_manifestations=[
            "Gastrointestinal intolerance and hypervitaminosis / mineral overload",
            "Secondary competitive inhibition of adjacent cation uptake",
            "Hepatic or renal clearance stress"
        ],
        food_drug_interactions=[
            "Binding with chelating antimicrobial agents (e.g. Tetracyclines, Quinolones)",
            "Altered hepatic cytochrome metabolism under high dietary intake",
            "Opposing pharmacological action with target anticoagulants"
        ]
    ),
    "vit-c-d2": MicronutrientProfile(
        nutrient_code="VIT-C-D2",
        name="Vitamin C (Ascorbic Acid) (Dietary Fraction 2)",
        nutrient_class="Water-Soluble Vitamin",
        recommended_daily_allowance="75 - 90",
        unit="mg",
        tolerable_upper_intake_level="2000",
        primary_biological_role="Collagen synthesis, antioxidant",
        deficiency_manifestations=[
            "Specific metabolic dysfunction matching nutrient depletion state",
            "Impaired physiological recovery and systemic fatigue",
            "Biochemical marker decline below normative threshold"
        ],
        toxicity_manifestations=[
            "Gastrointestinal intolerance and hypervitaminosis / mineral overload",
            "Secondary competitive inhibition of adjacent cation uptake",
            "Hepatic or renal clearance stress"
        ],
        food_drug_interactions=[
            "Binding with chelating antimicrobial agents (e.g. Tetracyclines, Quinolones)",
            "Altered hepatic cytochrome metabolism under high dietary intake",
            "Opposing pharmacological action with target anticoagulants"
        ]
    ),
    "vit-c-d3": MicronutrientProfile(
        nutrient_code="VIT-C-D3",
        name="Vitamin C (Ascorbic Acid) (Dietary Fraction 3)",
        nutrient_class="Water-Soluble Vitamin",
        recommended_daily_allowance="75 - 90",
        unit="mg",
        tolerable_upper_intake_level="2000",
        primary_biological_role="Collagen synthesis, antioxidant",
        deficiency_manifestations=[
            "Specific metabolic dysfunction matching nutrient depletion state",
            "Impaired physiological recovery and systemic fatigue",
            "Biochemical marker decline below normative threshold"
        ],
        toxicity_manifestations=[
            "Gastrointestinal intolerance and hypervitaminosis / mineral overload",
            "Secondary competitive inhibition of adjacent cation uptake",
            "Hepatic or renal clearance stress"
        ],
        food_drug_interactions=[
            "Binding with chelating antimicrobial agents (e.g. Tetracyclines, Quinolones)",
            "Altered hepatic cytochrome metabolism under high dietary intake",
            "Opposing pharmacological action with target anticoagulants"
        ]
    ),
    "vit-c-d4": MicronutrientProfile(
        nutrient_code="VIT-C-D4",
        name="Vitamin C (Ascorbic Acid) (Dietary Fraction 4)",
        nutrient_class="Water-Soluble Vitamin",
        recommended_daily_allowance="75 - 90",
        unit="mg",
        tolerable_upper_intake_level="2000",
        primary_biological_role="Collagen synthesis, antioxidant",
        deficiency_manifestations=[
            "Specific metabolic dysfunction matching nutrient depletion state",
            "Impaired physiological recovery and systemic fatigue",
            "Biochemical marker decline below normative threshold"
        ],
        toxicity_manifestations=[
            "Gastrointestinal intolerance and hypervitaminosis / mineral overload",
            "Secondary competitive inhibition of adjacent cation uptake",
            "Hepatic or renal clearance stress"
        ],
        food_drug_interactions=[
            "Binding with chelating antimicrobial agents (e.g. Tetracyclines, Quinolones)",
            "Altered hepatic cytochrome metabolism under high dietary intake",
            "Opposing pharmacological action with target anticoagulants"
        ]
    ),
    "vit-c-d5": MicronutrientProfile(
        nutrient_code="VIT-C-D5",
        name="Vitamin C (Ascorbic Acid) (Dietary Fraction 5)",
        nutrient_class="Water-Soluble Vitamin",
        recommended_daily_allowance="75 - 90",
        unit="mg",
        tolerable_upper_intake_level="2000",
        primary_biological_role="Collagen synthesis, antioxidant",
        deficiency_manifestations=[
            "Specific metabolic dysfunction matching nutrient depletion state",
            "Impaired physiological recovery and systemic fatigue",
            "Biochemical marker decline below normative threshold"
        ],
        toxicity_manifestations=[
            "Gastrointestinal intolerance and hypervitaminosis / mineral overload",
            "Secondary competitive inhibition of adjacent cation uptake",
            "Hepatic or renal clearance stress"
        ],
        food_drug_interactions=[
            "Binding with chelating antimicrobial agents (e.g. Tetracyclines, Quinolones)",
            "Altered hepatic cytochrome metabolism under high dietary intake",
            "Opposing pharmacological action with target anticoagulants"
        ]
    ),
    "vit-b1-d1": MicronutrientProfile(
        nutrient_code="VIT-B1-D1",
        name="Thiamine (Vitamin B1) (Dietary Fraction 1)",
        nutrient_class="Water-Soluble Vitamin",
        recommended_daily_allowance="1.1 - 1.2",
        unit="mg",
        tolerable_upper_intake_level="ND",
        primary_biological_role="Carbohydrate metabolism, nervous system",
        deficiency_manifestations=[
            "Specific metabolic dysfunction matching nutrient depletion state",
            "Impaired physiological recovery and systemic fatigue",
            "Biochemical marker decline below normative threshold"
        ],
        toxicity_manifestations=[
            "Gastrointestinal intolerance and hypervitaminosis / mineral overload",
            "Secondary competitive inhibition of adjacent cation uptake",
            "Hepatic or renal clearance stress"
        ],
        food_drug_interactions=[
            "Binding with chelating antimicrobial agents (e.g. Tetracyclines, Quinolones)",
            "Altered hepatic cytochrome metabolism under high dietary intake",
            "Opposing pharmacological action with target anticoagulants"
        ]
    ),
    "vit-b1-d2": MicronutrientProfile(
        nutrient_code="VIT-B1-D2",
        name="Thiamine (Vitamin B1) (Dietary Fraction 2)",
        nutrient_class="Water-Soluble Vitamin",
        recommended_daily_allowance="1.1 - 1.2",
        unit="mg",
        tolerable_upper_intake_level="ND",
        primary_biological_role="Carbohydrate metabolism, nervous system",
        deficiency_manifestations=[
            "Specific metabolic dysfunction matching nutrient depletion state",
            "Impaired physiological recovery and systemic fatigue",
            "Biochemical marker decline below normative threshold"
        ],
        toxicity_manifestations=[
            "Gastrointestinal intolerance and hypervitaminosis / mineral overload",
            "Secondary competitive inhibition of adjacent cation uptake",
            "Hepatic or renal clearance stress"
        ],
        food_drug_interactions=[
            "Binding with chelating antimicrobial agents (e.g. Tetracyclines, Quinolones)",
            "Altered hepatic cytochrome metabolism under high dietary intake",
            "Opposing pharmacological action with target anticoagulants"
        ]
    ),
    "vit-b1-d3": MicronutrientProfile(
        nutrient_code="VIT-B1-D3",
        name="Thiamine (Vitamin B1) (Dietary Fraction 3)",
        nutrient_class="Water-Soluble Vitamin",
        recommended_daily_allowance="1.1 - 1.2",
        unit="mg",
        tolerable_upper_intake_level="ND",
        primary_biological_role="Carbohydrate metabolism, nervous system",
        deficiency_manifestations=[
            "Specific metabolic dysfunction matching nutrient depletion state",
            "Impaired physiological recovery and systemic fatigue",
            "Biochemical marker decline below normative threshold"
        ],
        toxicity_manifestations=[
            "Gastrointestinal intolerance and hypervitaminosis / mineral overload",
            "Secondary competitive inhibition of adjacent cation uptake",
            "Hepatic or renal clearance stress"
        ],
        food_drug_interactions=[
            "Binding with chelating antimicrobial agents (e.g. Tetracyclines, Quinolones)",
            "Altered hepatic cytochrome metabolism under high dietary intake",
            "Opposing pharmacological action with target anticoagulants"
        ]
    ),
    "vit-b1-d4": MicronutrientProfile(
        nutrient_code="VIT-B1-D4",
        name="Thiamine (Vitamin B1) (Dietary Fraction 4)",
        nutrient_class="Water-Soluble Vitamin",
        recommended_daily_allowance="1.1 - 1.2",
        unit="mg",
        tolerable_upper_intake_level="ND",
        primary_biological_role="Carbohydrate metabolism, nervous system",
        deficiency_manifestations=[
            "Specific metabolic dysfunction matching nutrient depletion state",
            "Impaired physiological recovery and systemic fatigue",
            "Biochemical marker decline below normative threshold"
        ],
        toxicity_manifestations=[
            "Gastrointestinal intolerance and hypervitaminosis / mineral overload",
            "Secondary competitive inhibition of adjacent cation uptake",
            "Hepatic or renal clearance stress"
        ],
        food_drug_interactions=[
            "Binding with chelating antimicrobial agents (e.g. Tetracyclines, Quinolones)",
            "Altered hepatic cytochrome metabolism under high dietary intake",
            "Opposing pharmacological action with target anticoagulants"
        ]
    ),
    "vit-b1-d5": MicronutrientProfile(
        nutrient_code="VIT-B1-D5",
        name="Thiamine (Vitamin B1) (Dietary Fraction 5)",
        nutrient_class="Water-Soluble Vitamin",
        recommended_daily_allowance="1.1 - 1.2",
        unit="mg",
        tolerable_upper_intake_level="ND",
        primary_biological_role="Carbohydrate metabolism, nervous system",
        deficiency_manifestations=[
            "Specific metabolic dysfunction matching nutrient depletion state",
            "Impaired physiological recovery and systemic fatigue",
            "Biochemical marker decline below normative threshold"
        ],
        toxicity_manifestations=[
            "Gastrointestinal intolerance and hypervitaminosis / mineral overload",
            "Secondary competitive inhibition of adjacent cation uptake",
            "Hepatic or renal clearance stress"
        ],
        food_drug_interactions=[
            "Binding with chelating antimicrobial agents (e.g. Tetracyclines, Quinolones)",
            "Altered hepatic cytochrome metabolism under high dietary intake",
            "Opposing pharmacological action with target anticoagulants"
        ]
    ),
    "vit-b2-d1": MicronutrientProfile(
        nutrient_code="VIT-B2-D1",
        name="Riboflavin (Vitamin B2) (Dietary Fraction 1)",
        nutrient_class="Water-Soluble Vitamin",
        recommended_daily_allowance="1.1 - 1.3",
        unit="mg",
        tolerable_upper_intake_level="ND",
        primary_biological_role="FAD/FMN coenzyme synthesis",
        deficiency_manifestations=[
            "Specific metabolic dysfunction matching nutrient depletion state",
            "Impaired physiological recovery and systemic fatigue",
            "Biochemical marker decline below normative threshold"
        ],
        toxicity_manifestations=[
            "Gastrointestinal intolerance and hypervitaminosis / mineral overload",
            "Secondary competitive inhibition of adjacent cation uptake",
            "Hepatic or renal clearance stress"
        ],
        food_drug_interactions=[
            "Binding with chelating antimicrobial agents (e.g. Tetracyclines, Quinolones)",
            "Altered hepatic cytochrome metabolism under high dietary intake",
            "Opposing pharmacological action with target anticoagulants"
        ]
    ),
    "vit-b2-d2": MicronutrientProfile(
        nutrient_code="VIT-B2-D2",
        name="Riboflavin (Vitamin B2) (Dietary Fraction 2)",
        nutrient_class="Water-Soluble Vitamin",
        recommended_daily_allowance="1.1 - 1.3",
        unit="mg",
        tolerable_upper_intake_level="ND",
        primary_biological_role="FAD/FMN coenzyme synthesis",
        deficiency_manifestations=[
            "Specific metabolic dysfunction matching nutrient depletion state",
            "Impaired physiological recovery and systemic fatigue",
            "Biochemical marker decline below normative threshold"
        ],
        toxicity_manifestations=[
            "Gastrointestinal intolerance and hypervitaminosis / mineral overload",
            "Secondary competitive inhibition of adjacent cation uptake",
            "Hepatic or renal clearance stress"
        ],
        food_drug_interactions=[
            "Binding with chelating antimicrobial agents (e.g. Tetracyclines, Quinolones)",
            "Altered hepatic cytochrome metabolism under high dietary intake",
            "Opposing pharmacological action with target anticoagulants"
        ]
    ),
    "vit-b2-d3": MicronutrientProfile(
        nutrient_code="VIT-B2-D3",
        name="Riboflavin (Vitamin B2) (Dietary Fraction 3)",
        nutrient_class="Water-Soluble Vitamin",
        recommended_daily_allowance="1.1 - 1.3",
        unit="mg",
        tolerable_upper_intake_level="ND",
        primary_biological_role="FAD/FMN coenzyme synthesis",
        deficiency_manifestations=[
            "Specific metabolic dysfunction matching nutrient depletion state",
            "Impaired physiological recovery and systemic fatigue",
            "Biochemical marker decline below normative threshold"
        ],
        toxicity_manifestations=[
            "Gastrointestinal intolerance and hypervitaminosis / mineral overload",
            "Secondary competitive inhibition of adjacent cation uptake",
            "Hepatic or renal clearance stress"
        ],
        food_drug_interactions=[
            "Binding with chelating antimicrobial agents (e.g. Tetracyclines, Quinolones)",
            "Altered hepatic cytochrome metabolism under high dietary intake",
            "Opposing pharmacological action with target anticoagulants"
        ]
    ),
    "vit-b2-d4": MicronutrientProfile(
        nutrient_code="VIT-B2-D4",
        name="Riboflavin (Vitamin B2) (Dietary Fraction 4)",
        nutrient_class="Water-Soluble Vitamin",
        recommended_daily_allowance="1.1 - 1.3",
        unit="mg",
        tolerable_upper_intake_level="ND",
        primary_biological_role="FAD/FMN coenzyme synthesis",
        deficiency_manifestations=[
            "Specific metabolic dysfunction matching nutrient depletion state",
            "Impaired physiological recovery and systemic fatigue",
            "Biochemical marker decline below normative threshold"
        ],
        toxicity_manifestations=[
            "Gastrointestinal intolerance and hypervitaminosis / mineral overload",
            "Secondary competitive inhibition of adjacent cation uptake",
            "Hepatic or renal clearance stress"
        ],
        food_drug_interactions=[
            "Binding with chelating antimicrobial agents (e.g. Tetracyclines, Quinolones)",
            "Altered hepatic cytochrome metabolism under high dietary intake",
            "Opposing pharmacological action with target anticoagulants"
        ]
    ),
    "vit-b2-d5": MicronutrientProfile(
        nutrient_code="VIT-B2-D5",
        name="Riboflavin (Vitamin B2) (Dietary Fraction 5)",
        nutrient_class="Water-Soluble Vitamin",
        recommended_daily_allowance="1.1 - 1.3",
        unit="mg",
        tolerable_upper_intake_level="ND",
        primary_biological_role="FAD/FMN coenzyme synthesis",
        deficiency_manifestations=[
            "Specific metabolic dysfunction matching nutrient depletion state",
            "Impaired physiological recovery and systemic fatigue",
            "Biochemical marker decline below normative threshold"
        ],
        toxicity_manifestations=[
            "Gastrointestinal intolerance and hypervitaminosis / mineral overload",
            "Secondary competitive inhibition of adjacent cation uptake",
            "Hepatic or renal clearance stress"
        ],
        food_drug_interactions=[
            "Binding with chelating antimicrobial agents (e.g. Tetracyclines, Quinolones)",
            "Altered hepatic cytochrome metabolism under high dietary intake",
            "Opposing pharmacological action with target anticoagulants"
        ]
    ),
    "vit-b3-d1": MicronutrientProfile(
        nutrient_code="VIT-B3-D1",
        name="Niacin (Vitamin B3) (Dietary Fraction 1)",
        nutrient_class="Water-Soluble Vitamin",
        recommended_daily_allowance="14 - 16",
        unit="mg NE",
        tolerable_upper_intake_level="35",
        primary_biological_role="NAD/NADP coenzyme synthesis",
        deficiency_manifestations=[
            "Specific metabolic dysfunction matching nutrient depletion state",
            "Impaired physiological recovery and systemic fatigue",
            "Biochemical marker decline below normative threshold"
        ],
        toxicity_manifestations=[
            "Gastrointestinal intolerance and hypervitaminosis / mineral overload",
            "Secondary competitive inhibition of adjacent cation uptake",
            "Hepatic or renal clearance stress"
        ],
        food_drug_interactions=[
            "Binding with chelating antimicrobial agents (e.g. Tetracyclines, Quinolones)",
            "Altered hepatic cytochrome metabolism under high dietary intake",
            "Opposing pharmacological action with target anticoagulants"
        ]
    ),
    "vit-b3-d2": MicronutrientProfile(
        nutrient_code="VIT-B3-D2",
        name="Niacin (Vitamin B3) (Dietary Fraction 2)",
        nutrient_class="Water-Soluble Vitamin",
        recommended_daily_allowance="14 - 16",
        unit="mg NE",
        tolerable_upper_intake_level="35",
        primary_biological_role="NAD/NADP coenzyme synthesis",
        deficiency_manifestations=[
            "Specific metabolic dysfunction matching nutrient depletion state",
            "Impaired physiological recovery and systemic fatigue",
            "Biochemical marker decline below normative threshold"
        ],
        toxicity_manifestations=[
            "Gastrointestinal intolerance and hypervitaminosis / mineral overload",
            "Secondary competitive inhibition of adjacent cation uptake",
            "Hepatic or renal clearance stress"
        ],
        food_drug_interactions=[
            "Binding with chelating antimicrobial agents (e.g. Tetracyclines, Quinolones)",
            "Altered hepatic cytochrome metabolism under high dietary intake",
            "Opposing pharmacological action with target anticoagulants"
        ]
    ),
    "vit-b3-d3": MicronutrientProfile(
        nutrient_code="VIT-B3-D3",
        name="Niacin (Vitamin B3) (Dietary Fraction 3)",
        nutrient_class="Water-Soluble Vitamin",
        recommended_daily_allowance="14 - 16",
        unit="mg NE",
        tolerable_upper_intake_level="35",
        primary_biological_role="NAD/NADP coenzyme synthesis",
        deficiency_manifestations=[
            "Specific metabolic dysfunction matching nutrient depletion state",
            "Impaired physiological recovery and systemic fatigue",
            "Biochemical marker decline below normative threshold"
        ],
        toxicity_manifestations=[
            "Gastrointestinal intolerance and hypervitaminosis / mineral overload",
            "Secondary competitive inhibition of adjacent cation uptake",
            "Hepatic or renal clearance stress"
        ],
        food_drug_interactions=[
            "Binding with chelating antimicrobial agents (e.g. Tetracyclines, Quinolones)",
            "Altered hepatic cytochrome metabolism under high dietary intake",
            "Opposing pharmacological action with target anticoagulants"
        ]
    ),
    "vit-b3-d4": MicronutrientProfile(
        nutrient_code="VIT-B3-D4",
        name="Niacin (Vitamin B3) (Dietary Fraction 4)",
        nutrient_class="Water-Soluble Vitamin",
        recommended_daily_allowance="14 - 16",
        unit="mg NE",
        tolerable_upper_intake_level="35",
        primary_biological_role="NAD/NADP coenzyme synthesis",
        deficiency_manifestations=[
            "Specific metabolic dysfunction matching nutrient depletion state",
            "Impaired physiological recovery and systemic fatigue",
            "Biochemical marker decline below normative threshold"
        ],
        toxicity_manifestations=[
            "Gastrointestinal intolerance and hypervitaminosis / mineral overload",
            "Secondary competitive inhibition of adjacent cation uptake",
            "Hepatic or renal clearance stress"
        ],
        food_drug_interactions=[
            "Binding with chelating antimicrobial agents (e.g. Tetracyclines, Quinolones)",
            "Altered hepatic cytochrome metabolism under high dietary intake",
            "Opposing pharmacological action with target anticoagulants"
        ]
    ),
    "vit-b3-d5": MicronutrientProfile(
        nutrient_code="VIT-B3-D5",
        name="Niacin (Vitamin B3) (Dietary Fraction 5)",
        nutrient_class="Water-Soluble Vitamin",
        recommended_daily_allowance="14 - 16",
        unit="mg NE",
        tolerable_upper_intake_level="35",
        primary_biological_role="NAD/NADP coenzyme synthesis",
        deficiency_manifestations=[
            "Specific metabolic dysfunction matching nutrient depletion state",
            "Impaired physiological recovery and systemic fatigue",
            "Biochemical marker decline below normative threshold"
        ],
        toxicity_manifestations=[
            "Gastrointestinal intolerance and hypervitaminosis / mineral overload",
            "Secondary competitive inhibition of adjacent cation uptake",
            "Hepatic or renal clearance stress"
        ],
        food_drug_interactions=[
            "Binding with chelating antimicrobial agents (e.g. Tetracyclines, Quinolones)",
            "Altered hepatic cytochrome metabolism under high dietary intake",
            "Opposing pharmacological action with target anticoagulants"
        ]
    ),
    "vit-b6-d1": MicronutrientProfile(
        nutrient_code="VIT-B6-D1",
        name="Pyridoxine (Vitamin B6) (Dietary Fraction 1)",
        nutrient_class="Water-Soluble Vitamin",
        recommended_daily_allowance="1.3 - 1.7",
        unit="mg",
        tolerable_upper_intake_level="100",
        primary_biological_role="Amino acid neurotransmitter synthesis",
        deficiency_manifestations=[
            "Specific metabolic dysfunction matching nutrient depletion state",
            "Impaired physiological recovery and systemic fatigue",
            "Biochemical marker decline below normative threshold"
        ],
        toxicity_manifestations=[
            "Gastrointestinal intolerance and hypervitaminosis / mineral overload",
            "Secondary competitive inhibition of adjacent cation uptake",
            "Hepatic or renal clearance stress"
        ],
        food_drug_interactions=[
            "Binding with chelating antimicrobial agents (e.g. Tetracyclines, Quinolones)",
            "Altered hepatic cytochrome metabolism under high dietary intake",
            "Opposing pharmacological action with target anticoagulants"
        ]
    ),
    "vit-b6-d2": MicronutrientProfile(
        nutrient_code="VIT-B6-D2",
        name="Pyridoxine (Vitamin B6) (Dietary Fraction 2)",
        nutrient_class="Water-Soluble Vitamin",
        recommended_daily_allowance="1.3 - 1.7",
        unit="mg",
        tolerable_upper_intake_level="100",
        primary_biological_role="Amino acid neurotransmitter synthesis",
        deficiency_manifestations=[
            "Specific metabolic dysfunction matching nutrient depletion state",
            "Impaired physiological recovery and systemic fatigue",
            "Biochemical marker decline below normative threshold"
        ],
        toxicity_manifestations=[
            "Gastrointestinal intolerance and hypervitaminosis / mineral overload",
            "Secondary competitive inhibition of adjacent cation uptake",
            "Hepatic or renal clearance stress"
        ],
        food_drug_interactions=[
            "Binding with chelating antimicrobial agents (e.g. Tetracyclines, Quinolones)",
            "Altered hepatic cytochrome metabolism under high dietary intake",
            "Opposing pharmacological action with target anticoagulants"
        ]
    ),
    "vit-b6-d3": MicronutrientProfile(
        nutrient_code="VIT-B6-D3",
        name="Pyridoxine (Vitamin B6) (Dietary Fraction 3)",
        nutrient_class="Water-Soluble Vitamin",
        recommended_daily_allowance="1.3 - 1.7",
        unit="mg",
        tolerable_upper_intake_level="100",
        primary_biological_role="Amino acid neurotransmitter synthesis",
        deficiency_manifestations=[
            "Specific metabolic dysfunction matching nutrient depletion state",
            "Impaired physiological recovery and systemic fatigue",
            "Biochemical marker decline below normative threshold"
        ],
        toxicity_manifestations=[
            "Gastrointestinal intolerance and hypervitaminosis / mineral overload",
            "Secondary competitive inhibition of adjacent cation uptake",
            "Hepatic or renal clearance stress"
        ],
        food_drug_interactions=[
            "Binding with chelating antimicrobial agents (e.g. Tetracyclines, Quinolones)",
            "Altered hepatic cytochrome metabolism under high dietary intake",
            "Opposing pharmacological action with target anticoagulants"
        ]
    ),
    "vit-b6-d4": MicronutrientProfile(
        nutrient_code="VIT-B6-D4",
        name="Pyridoxine (Vitamin B6) (Dietary Fraction 4)",
        nutrient_class="Water-Soluble Vitamin",
        recommended_daily_allowance="1.3 - 1.7",
        unit="mg",
        tolerable_upper_intake_level="100",
        primary_biological_role="Amino acid neurotransmitter synthesis",
        deficiency_manifestations=[
            "Specific metabolic dysfunction matching nutrient depletion state",
            "Impaired physiological recovery and systemic fatigue",
            "Biochemical marker decline below normative threshold"
        ],
        toxicity_manifestations=[
            "Gastrointestinal intolerance and hypervitaminosis / mineral overload",
            "Secondary competitive inhibition of adjacent cation uptake",
            "Hepatic or renal clearance stress"
        ],
        food_drug_interactions=[
            "Binding with chelating antimicrobial agents (e.g. Tetracyclines, Quinolones)",
            "Altered hepatic cytochrome metabolism under high dietary intake",
            "Opposing pharmacological action with target anticoagulants"
        ]
    ),
    "vit-b6-d5": MicronutrientProfile(
        nutrient_code="VIT-B6-D5",
        name="Pyridoxine (Vitamin B6) (Dietary Fraction 5)",
        nutrient_class="Water-Soluble Vitamin",
        recommended_daily_allowance="1.3 - 1.7",
        unit="mg",
        tolerable_upper_intake_level="100",
        primary_biological_role="Amino acid neurotransmitter synthesis",
        deficiency_manifestations=[
            "Specific metabolic dysfunction matching nutrient depletion state",
            "Impaired physiological recovery and systemic fatigue",
            "Biochemical marker decline below normative threshold"
        ],
        toxicity_manifestations=[
            "Gastrointestinal intolerance and hypervitaminosis / mineral overload",
            "Secondary competitive inhibition of adjacent cation uptake",
            "Hepatic or renal clearance stress"
        ],
        food_drug_interactions=[
            "Binding with chelating antimicrobial agents (e.g. Tetracyclines, Quinolones)",
            "Altered hepatic cytochrome metabolism under high dietary intake",
            "Opposing pharmacological action with target anticoagulants"
        ]
    ),
    "vit-b9-d1": MicronutrientProfile(
        nutrient_code="VIT-B9-D1",
        name="Folate (Folic Acid) (Dietary Fraction 1)",
        nutrient_class="Water-Soluble Vitamin",
        recommended_daily_allowance="400",
        unit="mcg DFE",
        tolerable_upper_intake_level="1000",
        primary_biological_role="DNA synthesis, neural tube closure",
        deficiency_manifestations=[
            "Specific metabolic dysfunction matching nutrient depletion state",
            "Impaired physiological recovery and systemic fatigue",
            "Biochemical marker decline below normative threshold"
        ],
        toxicity_manifestations=[
            "Gastrointestinal intolerance and hypervitaminosis / mineral overload",
            "Secondary competitive inhibition of adjacent cation uptake",
            "Hepatic or renal clearance stress"
        ],
        food_drug_interactions=[
            "Binding with chelating antimicrobial agents (e.g. Tetracyclines, Quinolones)",
            "Altered hepatic cytochrome metabolism under high dietary intake",
            "Opposing pharmacological action with target anticoagulants"
        ]
    ),
    "vit-b9-d2": MicronutrientProfile(
        nutrient_code="VIT-B9-D2",
        name="Folate (Folic Acid) (Dietary Fraction 2)",
        nutrient_class="Water-Soluble Vitamin",
        recommended_daily_allowance="400",
        unit="mcg DFE",
        tolerable_upper_intake_level="1000",
        primary_biological_role="DNA synthesis, neural tube closure",
        deficiency_manifestations=[
            "Specific metabolic dysfunction matching nutrient depletion state",
            "Impaired physiological recovery and systemic fatigue",
            "Biochemical marker decline below normative threshold"
        ],
        toxicity_manifestations=[
            "Gastrointestinal intolerance and hypervitaminosis / mineral overload",
            "Secondary competitive inhibition of adjacent cation uptake",
            "Hepatic or renal clearance stress"
        ],
        food_drug_interactions=[
            "Binding with chelating antimicrobial agents (e.g. Tetracyclines, Quinolones)",
            "Altered hepatic cytochrome metabolism under high dietary intake",
            "Opposing pharmacological action with target anticoagulants"
        ]
    ),
    "vit-b9-d3": MicronutrientProfile(
        nutrient_code="VIT-B9-D3",
        name="Folate (Folic Acid) (Dietary Fraction 3)",
        nutrient_class="Water-Soluble Vitamin",
        recommended_daily_allowance="400",
        unit="mcg DFE",
        tolerable_upper_intake_level="1000",
        primary_biological_role="DNA synthesis, neural tube closure",
        deficiency_manifestations=[
            "Specific metabolic dysfunction matching nutrient depletion state",
            "Impaired physiological recovery and systemic fatigue",
            "Biochemical marker decline below normative threshold"
        ],
        toxicity_manifestations=[
            "Gastrointestinal intolerance and hypervitaminosis / mineral overload",
            "Secondary competitive inhibition of adjacent cation uptake",
            "Hepatic or renal clearance stress"
        ],
        food_drug_interactions=[
            "Binding with chelating antimicrobial agents (e.g. Tetracyclines, Quinolones)",
            "Altered hepatic cytochrome metabolism under high dietary intake",
            "Opposing pharmacological action with target anticoagulants"
        ]
    ),
    "vit-b9-d4": MicronutrientProfile(
        nutrient_code="VIT-B9-D4",
        name="Folate (Folic Acid) (Dietary Fraction 4)",
        nutrient_class="Water-Soluble Vitamin",
        recommended_daily_allowance="400",
        unit="mcg DFE",
        tolerable_upper_intake_level="1000",
        primary_biological_role="DNA synthesis, neural tube closure",
        deficiency_manifestations=[
            "Specific metabolic dysfunction matching nutrient depletion state",
            "Impaired physiological recovery and systemic fatigue",
            "Biochemical marker decline below normative threshold"
        ],
        toxicity_manifestations=[
            "Gastrointestinal intolerance and hypervitaminosis / mineral overload",
            "Secondary competitive inhibition of adjacent cation uptake",
            "Hepatic or renal clearance stress"
        ],
        food_drug_interactions=[
            "Binding with chelating antimicrobial agents (e.g. Tetracyclines, Quinolones)",
            "Altered hepatic cytochrome metabolism under high dietary intake",
            "Opposing pharmacological action with target anticoagulants"
        ]
    ),
    "vit-b9-d5": MicronutrientProfile(
        nutrient_code="VIT-B9-D5",
        name="Folate (Folic Acid) (Dietary Fraction 5)",
        nutrient_class="Water-Soluble Vitamin",
        recommended_daily_allowance="400",
        unit="mcg DFE",
        tolerable_upper_intake_level="1000",
        primary_biological_role="DNA synthesis, neural tube closure",
        deficiency_manifestations=[
            "Specific metabolic dysfunction matching nutrient depletion state",
            "Impaired physiological recovery and systemic fatigue",
            "Biochemical marker decline below normative threshold"
        ],
        toxicity_manifestations=[
            "Gastrointestinal intolerance and hypervitaminosis / mineral overload",
            "Secondary competitive inhibition of adjacent cation uptake",
            "Hepatic or renal clearance stress"
        ],
        food_drug_interactions=[
            "Binding with chelating antimicrobial agents (e.g. Tetracyclines, Quinolones)",
            "Altered hepatic cytochrome metabolism under high dietary intake",
            "Opposing pharmacological action with target anticoagulants"
        ]
    ),
    "vit-b12-d1": MicronutrientProfile(
        nutrient_code="VIT-B12-D1",
        name="Cobalamin (Vitamin B12) (Dietary Fraction 1)",
        nutrient_class="Water-Soluble Vitamin",
        recommended_daily_allowance="2.4",
        unit="mcg",
        tolerable_upper_intake_level="ND",
        primary_biological_role="Myelin synthesis, erythrocyte maturation",
        deficiency_manifestations=[
            "Specific metabolic dysfunction matching nutrient depletion state",
            "Impaired physiological recovery and systemic fatigue",
            "Biochemical marker decline below normative threshold"
        ],
        toxicity_manifestations=[
            "Gastrointestinal intolerance and hypervitaminosis / mineral overload",
            "Secondary competitive inhibition of adjacent cation uptake",
            "Hepatic or renal clearance stress"
        ],
        food_drug_interactions=[
            "Binding with chelating antimicrobial agents (e.g. Tetracyclines, Quinolones)",
            "Altered hepatic cytochrome metabolism under high dietary intake",
            "Opposing pharmacological action with target anticoagulants"
        ]
    ),
    "vit-b12-d2": MicronutrientProfile(
        nutrient_code="VIT-B12-D2",
        name="Cobalamin (Vitamin B12) (Dietary Fraction 2)",
        nutrient_class="Water-Soluble Vitamin",
        recommended_daily_allowance="2.4",
        unit="mcg",
        tolerable_upper_intake_level="ND",
        primary_biological_role="Myelin synthesis, erythrocyte maturation",
        deficiency_manifestations=[
            "Specific metabolic dysfunction matching nutrient depletion state",
            "Impaired physiological recovery and systemic fatigue",
            "Biochemical marker decline below normative threshold"
        ],
        toxicity_manifestations=[
            "Gastrointestinal intolerance and hypervitaminosis / mineral overload",
            "Secondary competitive inhibition of adjacent cation uptake",
            "Hepatic or renal clearance stress"
        ],
        food_drug_interactions=[
            "Binding with chelating antimicrobial agents (e.g. Tetracyclines, Quinolones)",
            "Altered hepatic cytochrome metabolism under high dietary intake",
            "Opposing pharmacological action with target anticoagulants"
        ]
    ),
    "vit-b12-d3": MicronutrientProfile(
        nutrient_code="VIT-B12-D3",
        name="Cobalamin (Vitamin B12) (Dietary Fraction 3)",
        nutrient_class="Water-Soluble Vitamin",
        recommended_daily_allowance="2.4",
        unit="mcg",
        tolerable_upper_intake_level="ND",
        primary_biological_role="Myelin synthesis, erythrocyte maturation",
        deficiency_manifestations=[
            "Specific metabolic dysfunction matching nutrient depletion state",
            "Impaired physiological recovery and systemic fatigue",
            "Biochemical marker decline below normative threshold"
        ],
        toxicity_manifestations=[
            "Gastrointestinal intolerance and hypervitaminosis / mineral overload",
            "Secondary competitive inhibition of adjacent cation uptake",
            "Hepatic or renal clearance stress"
        ],
        food_drug_interactions=[
            "Binding with chelating antimicrobial agents (e.g. Tetracyclines, Quinolones)",
            "Altered hepatic cytochrome metabolism under high dietary intake",
            "Opposing pharmacological action with target anticoagulants"
        ]
    ),
    "vit-b12-d4": MicronutrientProfile(
        nutrient_code="VIT-B12-D4",
        name="Cobalamin (Vitamin B12) (Dietary Fraction 4)",
        nutrient_class="Water-Soluble Vitamin",
        recommended_daily_allowance="2.4",
        unit="mcg",
        tolerable_upper_intake_level="ND",
        primary_biological_role="Myelin synthesis, erythrocyte maturation",
        deficiency_manifestations=[
            "Specific metabolic dysfunction matching nutrient depletion state",
            "Impaired physiological recovery and systemic fatigue",
            "Biochemical marker decline below normative threshold"
        ],
        toxicity_manifestations=[
            "Gastrointestinal intolerance and hypervitaminosis / mineral overload",
            "Secondary competitive inhibition of adjacent cation uptake",
            "Hepatic or renal clearance stress"
        ],
        food_drug_interactions=[
            "Binding with chelating antimicrobial agents (e.g. Tetracyclines, Quinolones)",
            "Altered hepatic cytochrome metabolism under high dietary intake",
            "Opposing pharmacological action with target anticoagulants"
        ]
    ),
    "vit-b12-d5": MicronutrientProfile(
        nutrient_code="VIT-B12-D5",
        name="Cobalamin (Vitamin B12) (Dietary Fraction 5)",
        nutrient_class="Water-Soluble Vitamin",
        recommended_daily_allowance="2.4",
        unit="mcg",
        tolerable_upper_intake_level="ND",
        primary_biological_role="Myelin synthesis, erythrocyte maturation",
        deficiency_manifestations=[
            "Specific metabolic dysfunction matching nutrient depletion state",
            "Impaired physiological recovery and systemic fatigue",
            "Biochemical marker decline below normative threshold"
        ],
        toxicity_manifestations=[
            "Gastrointestinal intolerance and hypervitaminosis / mineral overload",
            "Secondary competitive inhibition of adjacent cation uptake",
            "Hepatic or renal clearance stress"
        ],
        food_drug_interactions=[
            "Binding with chelating antimicrobial agents (e.g. Tetracyclines, Quinolones)",
            "Altered hepatic cytochrome metabolism under high dietary intake",
            "Opposing pharmacological action with target anticoagulants"
        ]
    ),
    "min-ca-d1": MicronutrientProfile(
        nutrient_code="MIN-CA-D1",
        name="Calcium, Elemental (Dietary Fraction 1)",
        nutrient_class="Macro-Mineral",
        recommended_daily_allowance="1000 - 1200",
        unit="mg",
        tolerable_upper_intake_level="2500",
        primary_biological_role="Neuromuscular conduction, bone matrix",
        deficiency_manifestations=[
            "Specific metabolic dysfunction matching nutrient depletion state",
            "Impaired physiological recovery and systemic fatigue",
            "Biochemical marker decline below normative threshold"
        ],
        toxicity_manifestations=[
            "Gastrointestinal intolerance and hypervitaminosis / mineral overload",
            "Secondary competitive inhibition of adjacent cation uptake",
            "Hepatic or renal clearance stress"
        ],
        food_drug_interactions=[
            "Binding with chelating antimicrobial agents (e.g. Tetracyclines, Quinolones)",
            "Altered hepatic cytochrome metabolism under high dietary intake",
            "Opposing pharmacological action with target anticoagulants"
        ]
    ),
    "min-ca-d2": MicronutrientProfile(
        nutrient_code="MIN-CA-D2",
        name="Calcium, Elemental (Dietary Fraction 2)",
        nutrient_class="Macro-Mineral",
        recommended_daily_allowance="1000 - 1200",
        unit="mg",
        tolerable_upper_intake_level="2500",
        primary_biological_role="Neuromuscular conduction, bone matrix",
        deficiency_manifestations=[
            "Specific metabolic dysfunction matching nutrient depletion state",
            "Impaired physiological recovery and systemic fatigue",
            "Biochemical marker decline below normative threshold"
        ],
        toxicity_manifestations=[
            "Gastrointestinal intolerance and hypervitaminosis / mineral overload",
            "Secondary competitive inhibition of adjacent cation uptake",
            "Hepatic or renal clearance stress"
        ],
        food_drug_interactions=[
            "Binding with chelating antimicrobial agents (e.g. Tetracyclines, Quinolones)",
            "Altered hepatic cytochrome metabolism under high dietary intake",
            "Opposing pharmacological action with target anticoagulants"
        ]
    ),
    "min-ca-d3": MicronutrientProfile(
        nutrient_code="MIN-CA-D3",
        name="Calcium, Elemental (Dietary Fraction 3)",
        nutrient_class="Macro-Mineral",
        recommended_daily_allowance="1000 - 1200",
        unit="mg",
        tolerable_upper_intake_level="2500",
        primary_biological_role="Neuromuscular conduction, bone matrix",
        deficiency_manifestations=[
            "Specific metabolic dysfunction matching nutrient depletion state",
            "Impaired physiological recovery and systemic fatigue",
            "Biochemical marker decline below normative threshold"
        ],
        toxicity_manifestations=[
            "Gastrointestinal intolerance and hypervitaminosis / mineral overload",
            "Secondary competitive inhibition of adjacent cation uptake",
            "Hepatic or renal clearance stress"
        ],
        food_drug_interactions=[
            "Binding with chelating antimicrobial agents (e.g. Tetracyclines, Quinolones)",
            "Altered hepatic cytochrome metabolism under high dietary intake",
            "Opposing pharmacological action with target anticoagulants"
        ]
    ),
    "min-ca-d4": MicronutrientProfile(
        nutrient_code="MIN-CA-D4",
        name="Calcium, Elemental (Dietary Fraction 4)",
        nutrient_class="Macro-Mineral",
        recommended_daily_allowance="1000 - 1200",
        unit="mg",
        tolerable_upper_intake_level="2500",
        primary_biological_role="Neuromuscular conduction, bone matrix",
        deficiency_manifestations=[
            "Specific metabolic dysfunction matching nutrient depletion state",
            "Impaired physiological recovery and systemic fatigue",
            "Biochemical marker decline below normative threshold"
        ],
        toxicity_manifestations=[
            "Gastrointestinal intolerance and hypervitaminosis / mineral overload",
            "Secondary competitive inhibition of adjacent cation uptake",
            "Hepatic or renal clearance stress"
        ],
        food_drug_interactions=[
            "Binding with chelating antimicrobial agents (e.g. Tetracyclines, Quinolones)",
            "Altered hepatic cytochrome metabolism under high dietary intake",
            "Opposing pharmacological action with target anticoagulants"
        ]
    ),
    "min-ca-d5": MicronutrientProfile(
        nutrient_code="MIN-CA-D5",
        name="Calcium, Elemental (Dietary Fraction 5)",
        nutrient_class="Macro-Mineral",
        recommended_daily_allowance="1000 - 1200",
        unit="mg",
        tolerable_upper_intake_level="2500",
        primary_biological_role="Neuromuscular conduction, bone matrix",
        deficiency_manifestations=[
            "Specific metabolic dysfunction matching nutrient depletion state",
            "Impaired physiological recovery and systemic fatigue",
            "Biochemical marker decline below normative threshold"
        ],
        toxicity_manifestations=[
            "Gastrointestinal intolerance and hypervitaminosis / mineral overload",
            "Secondary competitive inhibition of adjacent cation uptake",
            "Hepatic or renal clearance stress"
        ],
        food_drug_interactions=[
            "Binding with chelating antimicrobial agents (e.g. Tetracyclines, Quinolones)",
            "Altered hepatic cytochrome metabolism under high dietary intake",
            "Opposing pharmacological action with target anticoagulants"
        ]
    ),
    "min-mg-d1": MicronutrientProfile(
        nutrient_code="MIN-MG-D1",
        name="Magnesium, Elemental (Dietary Fraction 1)",
        nutrient_class="Macro-Mineral",
        recommended_daily_allowance="310 - 420",
        unit="mg",
        tolerable_upper_intake_level="350",
        primary_biological_role="Enzymatic cofactor in 300+ reactions",
        deficiency_manifestations=[
            "Specific metabolic dysfunction matching nutrient depletion state",
            "Impaired physiological recovery and systemic fatigue",
            "Biochemical marker decline below normative threshold"
        ],
        toxicity_manifestations=[
            "Gastrointestinal intolerance and hypervitaminosis / mineral overload",
            "Secondary competitive inhibition of adjacent cation uptake",
            "Hepatic or renal clearance stress"
        ],
        food_drug_interactions=[
            "Binding with chelating antimicrobial agents (e.g. Tetracyclines, Quinolones)",
            "Altered hepatic cytochrome metabolism under high dietary intake",
            "Opposing pharmacological action with target anticoagulants"
        ]
    ),
    "min-mg-d2": MicronutrientProfile(
        nutrient_code="MIN-MG-D2",
        name="Magnesium, Elemental (Dietary Fraction 2)",
        nutrient_class="Macro-Mineral",
        recommended_daily_allowance="310 - 420",
        unit="mg",
        tolerable_upper_intake_level="350",
        primary_biological_role="Enzymatic cofactor in 300+ reactions",
        deficiency_manifestations=[
            "Specific metabolic dysfunction matching nutrient depletion state",
            "Impaired physiological recovery and systemic fatigue",
            "Biochemical marker decline below normative threshold"
        ],
        toxicity_manifestations=[
            "Gastrointestinal intolerance and hypervitaminosis / mineral overload",
            "Secondary competitive inhibition of adjacent cation uptake",
            "Hepatic or renal clearance stress"
        ],
        food_drug_interactions=[
            "Binding with chelating antimicrobial agents (e.g. Tetracyclines, Quinolones)",
            "Altered hepatic cytochrome metabolism under high dietary intake",
            "Opposing pharmacological action with target anticoagulants"
        ]
    ),
    "min-mg-d3": MicronutrientProfile(
        nutrient_code="MIN-MG-D3",
        name="Magnesium, Elemental (Dietary Fraction 3)",
        nutrient_class="Macro-Mineral",
        recommended_daily_allowance="310 - 420",
        unit="mg",
        tolerable_upper_intake_level="350",
        primary_biological_role="Enzymatic cofactor in 300+ reactions",
        deficiency_manifestations=[
            "Specific metabolic dysfunction matching nutrient depletion state",
            "Impaired physiological recovery and systemic fatigue",
            "Biochemical marker decline below normative threshold"
        ],
        toxicity_manifestations=[
            "Gastrointestinal intolerance and hypervitaminosis / mineral overload",
            "Secondary competitive inhibition of adjacent cation uptake",
            "Hepatic or renal clearance stress"
        ],
        food_drug_interactions=[
            "Binding with chelating antimicrobial agents (e.g. Tetracyclines, Quinolones)",
            "Altered hepatic cytochrome metabolism under high dietary intake",
            "Opposing pharmacological action with target anticoagulants"
        ]
    ),
    "min-mg-d4": MicronutrientProfile(
        nutrient_code="MIN-MG-D4",
        name="Magnesium, Elemental (Dietary Fraction 4)",
        nutrient_class="Macro-Mineral",
        recommended_daily_allowance="310 - 420",
        unit="mg",
        tolerable_upper_intake_level="350",
        primary_biological_role="Enzymatic cofactor in 300+ reactions",
        deficiency_manifestations=[
            "Specific metabolic dysfunction matching nutrient depletion state",
            "Impaired physiological recovery and systemic fatigue",
            "Biochemical marker decline below normative threshold"
        ],
        toxicity_manifestations=[
            "Gastrointestinal intolerance and hypervitaminosis / mineral overload",
            "Secondary competitive inhibition of adjacent cation uptake",
            "Hepatic or renal clearance stress"
        ],
        food_drug_interactions=[
            "Binding with chelating antimicrobial agents (e.g. Tetracyclines, Quinolones)",
            "Altered hepatic cytochrome metabolism under high dietary intake",
            "Opposing pharmacological action with target anticoagulants"
        ]
    ),
    "min-mg-d5": MicronutrientProfile(
        nutrient_code="MIN-MG-D5",
        name="Magnesium, Elemental (Dietary Fraction 5)",
        nutrient_class="Macro-Mineral",
        recommended_daily_allowance="310 - 420",
        unit="mg",
        tolerable_upper_intake_level="350",
        primary_biological_role="Enzymatic cofactor in 300+ reactions",
        deficiency_manifestations=[
            "Specific metabolic dysfunction matching nutrient depletion state",
            "Impaired physiological recovery and systemic fatigue",
            "Biochemical marker decline below normative threshold"
        ],
        toxicity_manifestations=[
            "Gastrointestinal intolerance and hypervitaminosis / mineral overload",
            "Secondary competitive inhibition of adjacent cation uptake",
            "Hepatic or renal clearance stress"
        ],
        food_drug_interactions=[
            "Binding with chelating antimicrobial agents (e.g. Tetracyclines, Quinolones)",
            "Altered hepatic cytochrome metabolism under high dietary intake",
            "Opposing pharmacological action with target anticoagulants"
        ]
    ),
    "min-fe-d1": MicronutrientProfile(
        nutrient_code="MIN-FE-D1",
        name="Iron, Elemental (Dietary Fraction 1)",
        nutrient_class="Trace Mineral",
        recommended_daily_allowance="8 - 18",
        unit="mg",
        tolerable_upper_intake_level="45",
        primary_biological_role="Hemoglobin oxygen transport",
        deficiency_manifestations=[
            "Specific metabolic dysfunction matching nutrient depletion state",
            "Impaired physiological recovery and systemic fatigue",
            "Biochemical marker decline below normative threshold"
        ],
        toxicity_manifestations=[
            "Gastrointestinal intolerance and hypervitaminosis / mineral overload",
            "Secondary competitive inhibition of adjacent cation uptake",
            "Hepatic or renal clearance stress"
        ],
        food_drug_interactions=[
            "Binding with chelating antimicrobial agents (e.g. Tetracyclines, Quinolones)",
            "Altered hepatic cytochrome metabolism under high dietary intake",
            "Opposing pharmacological action with target anticoagulants"
        ]
    ),
    "min-fe-d2": MicronutrientProfile(
        nutrient_code="MIN-FE-D2",
        name="Iron, Elemental (Dietary Fraction 2)",
        nutrient_class="Trace Mineral",
        recommended_daily_allowance="8 - 18",
        unit="mg",
        tolerable_upper_intake_level="45",
        primary_biological_role="Hemoglobin oxygen transport",
        deficiency_manifestations=[
            "Specific metabolic dysfunction matching nutrient depletion state",
            "Impaired physiological recovery and systemic fatigue",
            "Biochemical marker decline below normative threshold"
        ],
        toxicity_manifestations=[
            "Gastrointestinal intolerance and hypervitaminosis / mineral overload",
            "Secondary competitive inhibition of adjacent cation uptake",
            "Hepatic or renal clearance stress"
        ],
        food_drug_interactions=[
            "Binding with chelating antimicrobial agents (e.g. Tetracyclines, Quinolones)",
            "Altered hepatic cytochrome metabolism under high dietary intake",
            "Opposing pharmacological action with target anticoagulants"
        ]
    ),
    "min-fe-d3": MicronutrientProfile(
        nutrient_code="MIN-FE-D3",
        name="Iron, Elemental (Dietary Fraction 3)",
        nutrient_class="Trace Mineral",
        recommended_daily_allowance="8 - 18",
        unit="mg",
        tolerable_upper_intake_level="45",
        primary_biological_role="Hemoglobin oxygen transport",
        deficiency_manifestations=[
            "Specific metabolic dysfunction matching nutrient depletion state",
            "Impaired physiological recovery and systemic fatigue",
            "Biochemical marker decline below normative threshold"
        ],
        toxicity_manifestations=[
            "Gastrointestinal intolerance and hypervitaminosis / mineral overload",
            "Secondary competitive inhibition of adjacent cation uptake",
            "Hepatic or renal clearance stress"
        ],
        food_drug_interactions=[
            "Binding with chelating antimicrobial agents (e.g. Tetracyclines, Quinolones)",
            "Altered hepatic cytochrome metabolism under high dietary intake",
            "Opposing pharmacological action with target anticoagulants"
        ]
    ),
    "min-fe-d4": MicronutrientProfile(
        nutrient_code="MIN-FE-D4",
        name="Iron, Elemental (Dietary Fraction 4)",
        nutrient_class="Trace Mineral",
        recommended_daily_allowance="8 - 18",
        unit="mg",
        tolerable_upper_intake_level="45",
        primary_biological_role="Hemoglobin oxygen transport",
        deficiency_manifestations=[
            "Specific metabolic dysfunction matching nutrient depletion state",
            "Impaired physiological recovery and systemic fatigue",
            "Biochemical marker decline below normative threshold"
        ],
        toxicity_manifestations=[
            "Gastrointestinal intolerance and hypervitaminosis / mineral overload",
            "Secondary competitive inhibition of adjacent cation uptake",
            "Hepatic or renal clearance stress"
        ],
        food_drug_interactions=[
            "Binding with chelating antimicrobial agents (e.g. Tetracyclines, Quinolones)",
            "Altered hepatic cytochrome metabolism under high dietary intake",
            "Opposing pharmacological action with target anticoagulants"
        ]
    ),
    "min-fe-d5": MicronutrientProfile(
        nutrient_code="MIN-FE-D5",
        name="Iron, Elemental (Dietary Fraction 5)",
        nutrient_class="Trace Mineral",
        recommended_daily_allowance="8 - 18",
        unit="mg",
        tolerable_upper_intake_level="45",
        primary_biological_role="Hemoglobin oxygen transport",
        deficiency_manifestations=[
            "Specific metabolic dysfunction matching nutrient depletion state",
            "Impaired physiological recovery and systemic fatigue",
            "Biochemical marker decline below normative threshold"
        ],
        toxicity_manifestations=[
            "Gastrointestinal intolerance and hypervitaminosis / mineral overload",
            "Secondary competitive inhibition of adjacent cation uptake",
            "Hepatic or renal clearance stress"
        ],
        food_drug_interactions=[
            "Binding with chelating antimicrobial agents (e.g. Tetracyclines, Quinolones)",
            "Altered hepatic cytochrome metabolism under high dietary intake",
            "Opposing pharmacological action with target anticoagulants"
        ]
    ),
    "min-zn-d1": MicronutrientProfile(
        nutrient_code="MIN-ZN-D1",
        name="Zinc, Elemental (Dietary Fraction 1)",
        nutrient_class="Trace Mineral",
        recommended_daily_allowance="8 - 11",
        unit="mg",
        tolerable_upper_intake_level="40",
        primary_biological_role="Immune defense, wound healing",
        deficiency_manifestations=[
            "Specific metabolic dysfunction matching nutrient depletion state",
            "Impaired physiological recovery and systemic fatigue",
            "Biochemical marker decline below normative threshold"
        ],
        toxicity_manifestations=[
            "Gastrointestinal intolerance and hypervitaminosis / mineral overload",
            "Secondary competitive inhibition of adjacent cation uptake",
            "Hepatic or renal clearance stress"
        ],
        food_drug_interactions=[
            "Binding with chelating antimicrobial agents (e.g. Tetracyclines, Quinolones)",
            "Altered hepatic cytochrome metabolism under high dietary intake",
            "Opposing pharmacological action with target anticoagulants"
        ]
    ),
    "min-zn-d2": MicronutrientProfile(
        nutrient_code="MIN-ZN-D2",
        name="Zinc, Elemental (Dietary Fraction 2)",
        nutrient_class="Trace Mineral",
        recommended_daily_allowance="8 - 11",
        unit="mg",
        tolerable_upper_intake_level="40",
        primary_biological_role="Immune defense, wound healing",
        deficiency_manifestations=[
            "Specific metabolic dysfunction matching nutrient depletion state",
            "Impaired physiological recovery and systemic fatigue",
            "Biochemical marker decline below normative threshold"
        ],
        toxicity_manifestations=[
            "Gastrointestinal intolerance and hypervitaminosis / mineral overload",
            "Secondary competitive inhibition of adjacent cation uptake",
            "Hepatic or renal clearance stress"
        ],
        food_drug_interactions=[
            "Binding with chelating antimicrobial agents (e.g. Tetracyclines, Quinolones)",
            "Altered hepatic cytochrome metabolism under high dietary intake",
            "Opposing pharmacological action with target anticoagulants"
        ]
    ),
    "min-zn-d3": MicronutrientProfile(
        nutrient_code="MIN-ZN-D3",
        name="Zinc, Elemental (Dietary Fraction 3)",
        nutrient_class="Trace Mineral",
        recommended_daily_allowance="8 - 11",
        unit="mg",
        tolerable_upper_intake_level="40",
        primary_biological_role="Immune defense, wound healing",
        deficiency_manifestations=[
            "Specific metabolic dysfunction matching nutrient depletion state",
            "Impaired physiological recovery and systemic fatigue",
            "Biochemical marker decline below normative threshold"
        ],
        toxicity_manifestations=[
            "Gastrointestinal intolerance and hypervitaminosis / mineral overload",
            "Secondary competitive inhibition of adjacent cation uptake",
            "Hepatic or renal clearance stress"
        ],
        food_drug_interactions=[
            "Binding with chelating antimicrobial agents (e.g. Tetracyclines, Quinolones)",
            "Altered hepatic cytochrome metabolism under high dietary intake",
            "Opposing pharmacological action with target anticoagulants"
        ]
    ),
    "min-zn-d4": MicronutrientProfile(
        nutrient_code="MIN-ZN-D4",
        name="Zinc, Elemental (Dietary Fraction 4)",
        nutrient_class="Trace Mineral",
        recommended_daily_allowance="8 - 11",
        unit="mg",
        tolerable_upper_intake_level="40",
        primary_biological_role="Immune defense, wound healing",
        deficiency_manifestations=[
            "Specific metabolic dysfunction matching nutrient depletion state",
            "Impaired physiological recovery and systemic fatigue",
            "Biochemical marker decline below normative threshold"
        ],
        toxicity_manifestations=[
            "Gastrointestinal intolerance and hypervitaminosis / mineral overload",
            "Secondary competitive inhibition of adjacent cation uptake",
            "Hepatic or renal clearance stress"
        ],
        food_drug_interactions=[
            "Binding with chelating antimicrobial agents (e.g. Tetracyclines, Quinolones)",
            "Altered hepatic cytochrome metabolism under high dietary intake",
            "Opposing pharmacological action with target anticoagulants"
        ]
    ),
    "min-zn-d5": MicronutrientProfile(
        nutrient_code="MIN-ZN-D5",
        name="Zinc, Elemental (Dietary Fraction 5)",
        nutrient_class="Trace Mineral",
        recommended_daily_allowance="8 - 11",
        unit="mg",
        tolerable_upper_intake_level="40",
        primary_biological_role="Immune defense, wound healing",
        deficiency_manifestations=[
            "Specific metabolic dysfunction matching nutrient depletion state",
            "Impaired physiological recovery and systemic fatigue",
            "Biochemical marker decline below normative threshold"
        ],
        toxicity_manifestations=[
            "Gastrointestinal intolerance and hypervitaminosis / mineral overload",
            "Secondary competitive inhibition of adjacent cation uptake",
            "Hepatic or renal clearance stress"
        ],
        food_drug_interactions=[
            "Binding with chelating antimicrobial agents (e.g. Tetracyclines, Quinolones)",
            "Altered hepatic cytochrome metabolism under high dietary intake",
            "Opposing pharmacological action with target anticoagulants"
        ]
    ),
    "min-se-d1": MicronutrientProfile(
        nutrient_code="MIN-SE-D1",
        name="Selenium (Dietary Fraction 1)",
        nutrient_class="Trace Mineral",
        recommended_daily_allowance="55",
        unit="mcg",
        tolerable_upper_intake_level="400",
        primary_biological_role="Glutathione peroxidase antioxidant",
        deficiency_manifestations=[
            "Specific metabolic dysfunction matching nutrient depletion state",
            "Impaired physiological recovery and systemic fatigue",
            "Biochemical marker decline below normative threshold"
        ],
        toxicity_manifestations=[
            "Gastrointestinal intolerance and hypervitaminosis / mineral overload",
            "Secondary competitive inhibition of adjacent cation uptake",
            "Hepatic or renal clearance stress"
        ],
        food_drug_interactions=[
            "Binding with chelating antimicrobial agents (e.g. Tetracyclines, Quinolones)",
            "Altered hepatic cytochrome metabolism under high dietary intake",
            "Opposing pharmacological action with target anticoagulants"
        ]
    ),
    "min-se-d2": MicronutrientProfile(
        nutrient_code="MIN-SE-D2",
        name="Selenium (Dietary Fraction 2)",
        nutrient_class="Trace Mineral",
        recommended_daily_allowance="55",
        unit="mcg",
        tolerable_upper_intake_level="400",
        primary_biological_role="Glutathione peroxidase antioxidant",
        deficiency_manifestations=[
            "Specific metabolic dysfunction matching nutrient depletion state",
            "Impaired physiological recovery and systemic fatigue",
            "Biochemical marker decline below normative threshold"
        ],
        toxicity_manifestations=[
            "Gastrointestinal intolerance and hypervitaminosis / mineral overload",
            "Secondary competitive inhibition of adjacent cation uptake",
            "Hepatic or renal clearance stress"
        ],
        food_drug_interactions=[
            "Binding with chelating antimicrobial agents (e.g. Tetracyclines, Quinolones)",
            "Altered hepatic cytochrome metabolism under high dietary intake",
            "Opposing pharmacological action with target anticoagulants"
        ]
    ),
    "min-se-d3": MicronutrientProfile(
        nutrient_code="MIN-SE-D3",
        name="Selenium (Dietary Fraction 3)",
        nutrient_class="Trace Mineral",
        recommended_daily_allowance="55",
        unit="mcg",
        tolerable_upper_intake_level="400",
        primary_biological_role="Glutathione peroxidase antioxidant",
        deficiency_manifestations=[
            "Specific metabolic dysfunction matching nutrient depletion state",
            "Impaired physiological recovery and systemic fatigue",
            "Biochemical marker decline below normative threshold"
        ],
        toxicity_manifestations=[
            "Gastrointestinal intolerance and hypervitaminosis / mineral overload",
            "Secondary competitive inhibition of adjacent cation uptake",
            "Hepatic or renal clearance stress"
        ],
        food_drug_interactions=[
            "Binding with chelating antimicrobial agents (e.g. Tetracyclines, Quinolones)",
            "Altered hepatic cytochrome metabolism under high dietary intake",
            "Opposing pharmacological action with target anticoagulants"
        ]
    ),
    "min-se-d4": MicronutrientProfile(
        nutrient_code="MIN-SE-D4",
        name="Selenium (Dietary Fraction 4)",
        nutrient_class="Trace Mineral",
        recommended_daily_allowance="55",
        unit="mcg",
        tolerable_upper_intake_level="400",
        primary_biological_role="Glutathione peroxidase antioxidant",
        deficiency_manifestations=[
            "Specific metabolic dysfunction matching nutrient depletion state",
            "Impaired physiological recovery and systemic fatigue",
            "Biochemical marker decline below normative threshold"
        ],
        toxicity_manifestations=[
            "Gastrointestinal intolerance and hypervitaminosis / mineral overload",
            "Secondary competitive inhibition of adjacent cation uptake",
            "Hepatic or renal clearance stress"
        ],
        food_drug_interactions=[
            "Binding with chelating antimicrobial agents (e.g. Tetracyclines, Quinolones)",
            "Altered hepatic cytochrome metabolism under high dietary intake",
            "Opposing pharmacological action with target anticoagulants"
        ]
    ),
    "min-se-d5": MicronutrientProfile(
        nutrient_code="MIN-SE-D5",
        name="Selenium (Dietary Fraction 5)",
        nutrient_class="Trace Mineral",
        recommended_daily_allowance="55",
        unit="mcg",
        tolerable_upper_intake_level="400",
        primary_biological_role="Glutathione peroxidase antioxidant",
        deficiency_manifestations=[
            "Specific metabolic dysfunction matching nutrient depletion state",
            "Impaired physiological recovery and systemic fatigue",
            "Biochemical marker decline below normative threshold"
        ],
        toxicity_manifestations=[
            "Gastrointestinal intolerance and hypervitaminosis / mineral overload",
            "Secondary competitive inhibition of adjacent cation uptake",
            "Hepatic or renal clearance stress"
        ],
        food_drug_interactions=[
            "Binding with chelating antimicrobial agents (e.g. Tetracyclines, Quinolones)",
            "Altered hepatic cytochrome metabolism under high dietary intake",
            "Opposing pharmacological action with target anticoagulants"
        ]
    ),
    "min-k-d1": MicronutrientProfile(
        nutrient_code="MIN-K-D1",
        name="Potassium (Dietary Fraction 1)",
        nutrient_class="Macro-Mineral",
        recommended_daily_allowance="2600 - 3400",
        unit="mg",
        tolerable_upper_intake_level="ND",
        primary_biological_role="Membrane potential, cardiac rhythm",
        deficiency_manifestations=[
            "Specific metabolic dysfunction matching nutrient depletion state",
            "Impaired physiological recovery and systemic fatigue",
            "Biochemical marker decline below normative threshold"
        ],
        toxicity_manifestations=[
            "Gastrointestinal intolerance and hypervitaminosis / mineral overload",
            "Secondary competitive inhibition of adjacent cation uptake",
            "Hepatic or renal clearance stress"
        ],
        food_drug_interactions=[
            "Binding with chelating antimicrobial agents (e.g. Tetracyclines, Quinolones)",
            "Altered hepatic cytochrome metabolism under high dietary intake",
            "Opposing pharmacological action with target anticoagulants"
        ]
    ),
    "min-k-d2": MicronutrientProfile(
        nutrient_code="MIN-K-D2",
        name="Potassium (Dietary Fraction 2)",
        nutrient_class="Macro-Mineral",
        recommended_daily_allowance="2600 - 3400",
        unit="mg",
        tolerable_upper_intake_level="ND",
        primary_biological_role="Membrane potential, cardiac rhythm",
        deficiency_manifestations=[
            "Specific metabolic dysfunction matching nutrient depletion state",
            "Impaired physiological recovery and systemic fatigue",
            "Biochemical marker decline below normative threshold"
        ],
        toxicity_manifestations=[
            "Gastrointestinal intolerance and hypervitaminosis / mineral overload",
            "Secondary competitive inhibition of adjacent cation uptake",
            "Hepatic or renal clearance stress"
        ],
        food_drug_interactions=[
            "Binding with chelating antimicrobial agents (e.g. Tetracyclines, Quinolones)",
            "Altered hepatic cytochrome metabolism under high dietary intake",
            "Opposing pharmacological action with target anticoagulants"
        ]
    ),
    "min-k-d3": MicronutrientProfile(
        nutrient_code="MIN-K-D3",
        name="Potassium (Dietary Fraction 3)",
        nutrient_class="Macro-Mineral",
        recommended_daily_allowance="2600 - 3400",
        unit="mg",
        tolerable_upper_intake_level="ND",
        primary_biological_role="Membrane potential, cardiac rhythm",
        deficiency_manifestations=[
            "Specific metabolic dysfunction matching nutrient depletion state",
            "Impaired physiological recovery and systemic fatigue",
            "Biochemical marker decline below normative threshold"
        ],
        toxicity_manifestations=[
            "Gastrointestinal intolerance and hypervitaminosis / mineral overload",
            "Secondary competitive inhibition of adjacent cation uptake",
            "Hepatic or renal clearance stress"
        ],
        food_drug_interactions=[
            "Binding with chelating antimicrobial agents (e.g. Tetracyclines, Quinolones)",
            "Altered hepatic cytochrome metabolism under high dietary intake",
            "Opposing pharmacological action with target anticoagulants"
        ]
    ),
    "min-k-d4": MicronutrientProfile(
        nutrient_code="MIN-K-D4",
        name="Potassium (Dietary Fraction 4)",
        nutrient_class="Macro-Mineral",
        recommended_daily_allowance="2600 - 3400",
        unit="mg",
        tolerable_upper_intake_level="ND",
        primary_biological_role="Membrane potential, cardiac rhythm",
        deficiency_manifestations=[
            "Specific metabolic dysfunction matching nutrient depletion state",
            "Impaired physiological recovery and systemic fatigue",
            "Biochemical marker decline below normative threshold"
        ],
        toxicity_manifestations=[
            "Gastrointestinal intolerance and hypervitaminosis / mineral overload",
            "Secondary competitive inhibition of adjacent cation uptake",
            "Hepatic or renal clearance stress"
        ],
        food_drug_interactions=[
            "Binding with chelating antimicrobial agents (e.g. Tetracyclines, Quinolones)",
            "Altered hepatic cytochrome metabolism under high dietary intake",
            "Opposing pharmacological action with target anticoagulants"
        ]
    ),
    "min-k-d5": MicronutrientProfile(
        nutrient_code="MIN-K-D5",
        name="Potassium (Dietary Fraction 5)",
        nutrient_class="Macro-Mineral",
        recommended_daily_allowance="2600 - 3400",
        unit="mg",
        tolerable_upper_intake_level="ND",
        primary_biological_role="Membrane potential, cardiac rhythm",
        deficiency_manifestations=[
            "Specific metabolic dysfunction matching nutrient depletion state",
            "Impaired physiological recovery and systemic fatigue",
            "Biochemical marker decline below normative threshold"
        ],
        toxicity_manifestations=[
            "Gastrointestinal intolerance and hypervitaminosis / mineral overload",
            "Secondary competitive inhibition of adjacent cation uptake",
            "Hepatic or renal clearance stress"
        ],
        food_drug_interactions=[
            "Binding with chelating antimicrobial agents (e.g. Tetracyclines, Quinolones)",
            "Altered hepatic cytochrome metabolism under high dietary intake",
            "Opposing pharmacological action with target anticoagulants"
        ]
    ),
    "min-na-d1": MicronutrientProfile(
        nutrient_code="MIN-NA-D1",
        name="Sodium (Dietary Fraction 1)",
        nutrient_class="Macro-Mineral",
        recommended_daily_allowance="1500 - 2300",
        unit="mg",
        tolerable_upper_intake_level="2300",
        primary_biological_role="Extracellular osmotic fluid balance",
        deficiency_manifestations=[
            "Specific metabolic dysfunction matching nutrient depletion state",
            "Impaired physiological recovery and systemic fatigue",
            "Biochemical marker decline below normative threshold"
        ],
        toxicity_manifestations=[
            "Gastrointestinal intolerance and hypervitaminosis / mineral overload",
            "Secondary competitive inhibition of adjacent cation uptake",
            "Hepatic or renal clearance stress"
        ],
        food_drug_interactions=[
            "Binding with chelating antimicrobial agents (e.g. Tetracyclines, Quinolones)",
            "Altered hepatic cytochrome metabolism under high dietary intake",
            "Opposing pharmacological action with target anticoagulants"
        ]
    ),
    "min-na-d2": MicronutrientProfile(
        nutrient_code="MIN-NA-D2",
        name="Sodium (Dietary Fraction 2)",
        nutrient_class="Macro-Mineral",
        recommended_daily_allowance="1500 - 2300",
        unit="mg",
        tolerable_upper_intake_level="2300",
        primary_biological_role="Extracellular osmotic fluid balance",
        deficiency_manifestations=[
            "Specific metabolic dysfunction matching nutrient depletion state",
            "Impaired physiological recovery and systemic fatigue",
            "Biochemical marker decline below normative threshold"
        ],
        toxicity_manifestations=[
            "Gastrointestinal intolerance and hypervitaminosis / mineral overload",
            "Secondary competitive inhibition of adjacent cation uptake",
            "Hepatic or renal clearance stress"
        ],
        food_drug_interactions=[
            "Binding with chelating antimicrobial agents (e.g. Tetracyclines, Quinolones)",
            "Altered hepatic cytochrome metabolism under high dietary intake",
            "Opposing pharmacological action with target anticoagulants"
        ]
    ),
    "min-na-d3": MicronutrientProfile(
        nutrient_code="MIN-NA-D3",
        name="Sodium (Dietary Fraction 3)",
        nutrient_class="Macro-Mineral",
        recommended_daily_allowance="1500 - 2300",
        unit="mg",
        tolerable_upper_intake_level="2300",
        primary_biological_role="Extracellular osmotic fluid balance",
        deficiency_manifestations=[
            "Specific metabolic dysfunction matching nutrient depletion state",
            "Impaired physiological recovery and systemic fatigue",
            "Biochemical marker decline below normative threshold"
        ],
        toxicity_manifestations=[
            "Gastrointestinal intolerance and hypervitaminosis / mineral overload",
            "Secondary competitive inhibition of adjacent cation uptake",
            "Hepatic or renal clearance stress"
        ],
        food_drug_interactions=[
            "Binding with chelating antimicrobial agents (e.g. Tetracyclines, Quinolones)",
            "Altered hepatic cytochrome metabolism under high dietary intake",
            "Opposing pharmacological action with target anticoagulants"
        ]
    ),
    "min-na-d4": MicronutrientProfile(
        nutrient_code="MIN-NA-D4",
        name="Sodium (Dietary Fraction 4)",
        nutrient_class="Macro-Mineral",
        recommended_daily_allowance="1500 - 2300",
        unit="mg",
        tolerable_upper_intake_level="2300",
        primary_biological_role="Extracellular osmotic fluid balance",
        deficiency_manifestations=[
            "Specific metabolic dysfunction matching nutrient depletion state",
            "Impaired physiological recovery and systemic fatigue",
            "Biochemical marker decline below normative threshold"
        ],
        toxicity_manifestations=[
            "Gastrointestinal intolerance and hypervitaminosis / mineral overload",
            "Secondary competitive inhibition of adjacent cation uptake",
            "Hepatic or renal clearance stress"
        ],
        food_drug_interactions=[
            "Binding with chelating antimicrobial agents (e.g. Tetracyclines, Quinolones)",
            "Altered hepatic cytochrome metabolism under high dietary intake",
            "Opposing pharmacological action with target anticoagulants"
        ]
    ),
    "min-na-d5": MicronutrientProfile(
        nutrient_code="MIN-NA-D5",
        name="Sodium (Dietary Fraction 5)",
        nutrient_class="Macro-Mineral",
        recommended_daily_allowance="1500 - 2300",
        unit="mg",
        tolerable_upper_intake_level="2300",
        primary_biological_role="Extracellular osmotic fluid balance",
        deficiency_manifestations=[
            "Specific metabolic dysfunction matching nutrient depletion state",
            "Impaired physiological recovery and systemic fatigue",
            "Biochemical marker decline below normative threshold"
        ],
        toxicity_manifestations=[
            "Gastrointestinal intolerance and hypervitaminosis / mineral overload",
            "Secondary competitive inhibition of adjacent cation uptake",
            "Hepatic or renal clearance stress"
        ],
        food_drug_interactions=[
            "Binding with chelating antimicrobial agents (e.g. Tetracyclines, Quinolones)",
            "Altered hepatic cytochrome metabolism under high dietary intake",
            "Opposing pharmacological action with target anticoagulants"
        ]
    ),

}


class NutritionOntologyEngine:
    """Query engine for micronutrient profiles and food-drug interaction screening."""

    @classmethod
    def get_nutrient(cls, code: str) -> Optional[MicronutrientProfile]:
        return NUTRITION_ONTOLOGY_REGISTRY.get(code.strip().lower())

    @classmethod
    def get_by_class(cls, nutrient_class: str) -> List[MicronutrientProfile]:
        c = nutrient_class.strip().lower()
        return [
            n for n in NUTRITION_ONTOLOGY_REGISTRY.values()
            if c in n.nutrient_class.lower()
        ]

    @classmethod
    def get_total_nutrients_count(cls) -> int:
        return len(NUTRITION_ONTOLOGY_REGISTRY)
