#1st programme
queue=[]
queue.append(66)
queue.append(20)
queue.append(10)

print("queue",queue)
removed=queue.pop(0)
print("removed:",removed)
print("queue after removing an element :",queue)
#2nd programme
from collections import deque
queue = deque()
queue.append(10)
queue.append(20)
queue.append(30)
print("Queue:", list(queue))
removed=queue.popleft()
print("removed element:",removed)
print("queue after dequeue:",list(queue))
#3rd programme
from collections import deque

queue = deque()

while True:
    print("\n1.Enqueue  2.Dequeue  3.Display  4.Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        x = int(input("Enter element: "))
        queue.append(x)
        print("Inserted")

    elif choice == 2:
        if not queue:
            print("Queue is empty")
        else:
            print("Removed:", queue.popleft())

    elif choice == 3:
        print("Queue:", list(queue))

    elif choice == 4:
        break

    else:
        print("Invalid choice")
 