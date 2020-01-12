

class EmploymentStatus:

	CHOICES = (
			('employed', "Employed"),
			('unemployed', "Unemployed"),
			('self-employed', "Self-Employed"),
		)

class MaritalStatus:

	CHOICES = (
			("single", "Single"),
			("married", "Married"),
			("divorced", "Divorced"),
		)

class Gender:

	CHOICES = (
			("male", "Male"),
			("female", "Female"),
			("Transgender", "Transgender"),	
		)

class EducationBackground:

	CHOICES = (
			("matriculate", "Matriculate"),
			("intermediate", "Intermediate"),
			("graduate", "Graduate"),
			("post-graduate", "Post-Graduate"),
			("phd", "Phd.")
		)

class IncomeMode:

	CHOICES = (
			("cash", "Cash"),
			("cheque", "Cheque"),
		)

class AbominationStatus:

	CHOICES = (
			("rent", "Rent"),
			("own", "Own"),
		)

class ApplicationStatus:

	CHOICES = (
			("under-process", "Under Process"),
			("approved", "Approved"),
			("rejected", "Rejected")
		)