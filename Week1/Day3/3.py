# : Check whether a student is eligible for admission if they have either Marks ≥ 70 OR a sports quota certificate.




marks = int(input("Enter marks: "))
sports_quota = input("Do you have a sports quota certificate? (yes/no): ")

if marks >= 70 or sports_quota.lower() == "yes":
    print("Eligible for admission")
else:
    print("Not eligible for admission")