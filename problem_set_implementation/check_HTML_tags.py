class Node:
    def __init__(self, data):
        self.data = data   
        self.next = None   

class Stack:
    def __init__(self):
        self.size = 0      
        self.top = None    

    def push(self, item):
        new_node = Node(item) 
        self.size += 1        
        if not self.top:
            self.top = new_node
            return

        new_node.next = self.top
        self.top = new_node
        return

    def pop(self):
        if not self.top:
            return None
        ret = self.top.data 
        self.top = self.top.next 
        self.size -= 1         
        return ret

    def top(self):
        return self.top

    def print(self):
        curr = self.top
        while curr:
            print(curr.data, end=' ')
            curr = curr.next
        print()
        return

    def is_empty(self):
        return self.size == 0

with open("problem_set_implementation\HTML.txt", "r") as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines if line.strip()]
    processed_lines = []
    for line in lines:
        temp = []
        i = 0
        while i < len(line):
            if line[i] == '<':
                tag = ''
                while i < len(line) and line[i] != '>':
                    tag += line[i]
                    i += 1
                tag += '>'
                temp.append(tag)
                i += 1
            else:
                word = ''
                while i < len(line) and line[i] != '<':
                    word += line[i]
                    i += 1
                if word.strip():
                    temp.append(word.strip())
        processed_lines.append(temp)
    lines = processed_lines
    
    opening_tags = Stack()
    for line in lines:
        for tag in line:
            if tag[0] == '<' and tag[1] != '/':
                opening_tags.push(tag)
            elif tag[0] == '<' and tag[1] == '/':
                if opening_tags.is_empty():
                    print("HTML is not well-formed")
                    break
                else:
                    opening_tag = opening_tags.pop()
                    check = True
                    for i in range(2, len(tag) - 1):
                        if tag[i] != opening_tag[i - 1]:
                            print("HTML is not well-formed")
                            check = False
                            break
                    if opening_tag[-1] != '>' or tag[-1] != '>':
                        print("HTML is not well-formed")
                        check = False
                    if check:
                        print(f"Matched: {opening_tag} and {tag}")
                    