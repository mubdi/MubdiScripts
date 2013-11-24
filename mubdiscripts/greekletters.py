"""
A List of Greek Letters, indexed by order
"""

### Lowercase Letters
gk_lower = [
	"alpha",
	"beta",
	"gamma",
	"delta",
	"epsilon",
	"zeta",
	"eta",
	"theta",
	"iota",
	"kappa",
	"lambda",
	"mu",
	"nu",
	"xi",
	"omicron",
	"pi",
	"rho",
	"sigma",
	"tau",
	"upsilon",
	"phi",
	"chi",
	"psi",
	"omega"
]

### Uppercase Letters
gk_upper = []
for letter in gk_lower:
	gk_upper.append(lower.capitalize())

### For LaTeX:

# Lowercase
gk_latex_lower = []
for letter in gk_lower:
	gk_latex_lower.append("$\\"+letter+"$")

# Uppercase
gk_latex_upper = []
for letter in gk_upper:
	gk_latex_upper.append("$\\"+letter+"$")

