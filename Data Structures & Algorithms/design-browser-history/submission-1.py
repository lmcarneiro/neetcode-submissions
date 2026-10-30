class PageNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next
        
class BrowserHistory:

    def __init__(self, homepage: str):
        self.current_page = PageNode(homepage)

    def visit(self, url: str) -> None:
        self.current_page.next = PageNode(url, self.current_page)
        self.current_page = self.current_page.next

    def back(self, steps: int) -> str:
        while self.current_page.prev and steps:
            self.current_page = self.current_page.prev
            steps -= 1
        return self.current_page.val

    def forward(self, steps: int) -> str:
        while self.current_page.next and steps:
            self.current_page = self.current_page.next
            steps -= 1
        return self.current_page.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)