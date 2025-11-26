print("[Age Calculate Program]")

b_year=int(input("Enter your birth year: "))
b_month=int(input("Enter your birth month (in number): "))
c_year=int(input("Enter this year: "))
c_month=int(input("Enter this month (in number): "))

age_year=c_year - b_year
age_month=c_month - b_month

print("<Result>")
print(f"You are {age_year} years and {age_month} months old.")