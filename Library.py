bookID = input("Enter bookID: ")
dueDate = int(input("Enter dueDate: "))
returnDate = int(input("Enter returnDate: "))

days_over_due = returnDate - dueDate

def daysoverdue(days_over_due):
    print("Days overdue:", days_over_due)

daysoverdue(days_over_due)

def tfine(days_over_due):
    if days_over_due <= 0:
        print("No charges")
        return
    fine = 0

    if days_over_due <= 7:
        fine += days_over_due * 20
    elif days_over_due <= 14:
        fine += (7 * 20) + ((days_over_due - 7) * 50)
    else:
        fine += (7 * 20) + (7 * 50) + ((days_over_due - 14) * 100)

    # Calculate fine rate
    fine_rate = fine / days_over_due

    print("Your total fine is:", fine)
    print("Your fine rate per day is:", round(fine_rate, 2))  # Rounded to 2 decimal places

tfine(days_over_due)
