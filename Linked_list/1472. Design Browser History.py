class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.pre = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.first_node = ListNode(homepage)
        self.curr_node = self.first_node
    def visit(self, url: str) -> None:
        self.curr_node.next = ListNode(url)
        self.curr_node2 = self.curr_node
        self.curr_node = self.curr_node.next
        self.curr_node.pre = self.curr_node2

    def back(self, steps: int) -> str:
        # print(steps, self.curr_node.pre.val)
        while steps > 0 and self.curr_node.pre:
            self.curr_node = self.curr_node.pre
            steps -=1
        return self.curr_node.val

    def forward(self, steps: int) -> str:
        while steps > 0 and self.curr_node.next:
            self.curr_node = self.curr_node.next
            steps -=1
        return self.curr_node.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
