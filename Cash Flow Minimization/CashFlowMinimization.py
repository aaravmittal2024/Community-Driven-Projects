import heapq

class Person:
    def __init__(self, id, amount):
        self.id = id
        self.amount = amount

    def __lt__(self, other):
        return self.amount < other.amount

def settle_transactions(amounts):
    debtors = []
    creditors = []

    for i, amount in enumerate(amounts):
        person = Person(i, amount)
        if amount < 0:
            heapq.heappush(debtors, person)
        elif amount > 0:
            heapq.heappush(creditors, person)

    while debtors and creditors:
        debtor = heapq.heappop(debtors)
        creditor = heapq.heappop(creditors)

        # Settle the transaction
        settled_amount = min(-debtor.amount, creditor.amount)
        print(f"Person {debtor.id + 1} pays {settled_amount} to Person {creditor.id + 1}")

        debtor.amount += settled_amount
        creditor.amount -= settled_amount

        # If any person still has unsettled amounts, push them back to the heap
        if debtor.amount < 0:
            heapq.heappush(debtors, debtor)
        if creditor.amount > 0:
            heapq.heappush(creditors, creditor)

def main():
    num_people = int(input("Enter the number of people: "))
    amounts = []

    for i in range(num_people):
        amount = float(input(f"Enter the amount for Person {i + 1} (positive if owed, negative if owes): "))
        amounts.append(amount)

    if sum(amounts) != 0:
        print("The total amount owed does not match the total amount to be received!")
        return

    settle_transactions(amounts)

if __name__ == "__main__":
    main()
