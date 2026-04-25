from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

model = DiscreteBayesianNetwork([
    ("WeakImmunity", "Infection"),
    ("Infection", "Fever"),
    ("Infection", "Cough"),
    ("Infection", "Inflammation"),
    ("Inflammation", "LabTest"),
    ("WeakImmunity", "LabTest"),
    ("Fever", "HospitalVisit"),
    ("Cough", "HospitalVisit")
])

cpd_W = TabularCPD(
    variable="WeakImmunity",
    variable_card=2,
    values=[
        [0.8],  # P(W=0)
        [0.2]   # P(W=1)
    ]
)
cpd_I = TabularCPD(
    variable="Infection",
    variable_card=2,
    values=[
        [0.9, 0.3],  # P(I=0 | W=0), P(I=0 | W=1)
        [0.1, 0.7]   # P(I=1 | W=0), P(I=1 | W=1)
    ],
    evidence=["WeakImmunity"],
    evidence_card=[2]
)

cpd_F = TabularCPD(
    variable="Fever",
    variable_card=2,
    values=[
        [0.9, 0.2],  # P(F=0 | I=0), P(F=0 | I=1)
        [0.1, 0.8]   # P(F=1 | I=0), P(F=1 | I=1)
    ],
    evidence=["Infection"],
    evidence_card=[2]
)

cpd_C = TabularCPD(
    variable="Cough",
    variable_card=2,
    values=[
        [0.8, 0.25],  # P(C=0 | I=0), P(C=0 | I=1)
        [0.2, 0.75]   # P(C=1 | I=0), P(C=1 | I=1)
    ],
    evidence=["Infection"],
    evidence_card=[2]
)

cpd_Inf = TabularCPD(
    variable="Inflammation",
    variable_card=2,
    values=[
        [0.85, 0.15],  # P(Inf=0 | I=0), P(Inf=0 | I=1)
        [0.15, 0.85]   # P(Inf=1 | I=0), P(Inf=1 | I=1)
    ],
    evidence=["Infection"],
    evidence_card=[2]
)

cpd_L = TabularCPD(
    variable="LabTest",
    variable_card=2,
    values=[
        [0.90, 0.40, 0.15, 0.05],  # P(L=0 | Inf,W)
        [0.10, 0.60, 0.85, 0.95]   # P(L=1 | Inf,W)
    ],
    evidence=["Inflammation", "WeakImmunity"],
    evidence_card=[2, 2]
)

H = 'HospitalVisit'
cpd_H = TabularCPD(
    variable=H,
    variable_card=2,
    values=[
        [1-0.05, 1-0.7, 1-0.8, 1-0.95], # P{H = 0 | F = ?, C = ?}       # F=0, C=0 ; F=0, C=1 ; F=1, C=0 ;
        [0.05, 0.7, 0.8, 0.95]
    ],
    evidence=['Fever', 'Cough'],
    evidence_card=[2, 2]
)


model.add_cpds(
    cpd_W,
    cpd_I,
    cpd_F,
    cpd_C,
    cpd_Inf,
    cpd_L,
    cpd_H
)

print("Model valid:", model.check_model())

infer = VariableElimination(model)

q1 = infer.query(
    variables=["Infection"],
    evidence={"HospitalVisit": 1}
)

print("\nP(Infection | HospitalVisit=1):")
print(q1)

q2 = infer.query(
    variables=["Infection"],
    evidence={"HospitalVisit": 1, "LabTest": 1}
)

print("\nP(Infection | HospitalVisit=1, LabTest=1):")
print(q2)


q3 = infer.query(
    variables=["WeakImmunity"],
    evidence={"LabTest": 1}
)

print("\nP(WeakImmunity | LabTest=1):")
print(q3)


q4 = infer.query(
    variables=["Inflammation"],
    evidence={"LabTest": 1, "WeakImmunity": 0}
)

print("\nP(Inflammation | LabTest=1, WeakImmunity=0):")
print(q4)


q5 = infer.query(
    variables=["Fever"],
    evidence={"HospitalVisit": 1}
)

print("\nP(Fever | HospitalVisit=1):")
print(q5)


q6 = infer.query(
    variables=["Cough"],
    evidence={"HospitalVisit": 1, "Fever": 0}
)

print("\nP(Cough | HospitalVisit=1, Fever=0):")
print(q6)