#stack implementation
stack = []

stack.append(10)  
stack.append(20)  
stack.append(30)  
stack.append(40)  

print("Popped:", stack.pop())  
print("Popped:", stack.pop())  
print("Current Stack:", stack)  


#queue implementation
queue = []

queue.append(10)  
queue.append(20)  
queue.append(30) 
queue.append(40) 

print("Dequeued:", queue.pop(0))  
print("Dequeued:", queue.pop(0)) 
print("Current Queue:", queue)