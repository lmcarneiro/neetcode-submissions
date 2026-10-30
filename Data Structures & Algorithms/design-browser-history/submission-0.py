class PageNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.homepage = PageNode(homepage)
        self.current_page = self.homepage

    def visit(self, url: str) -> None:
        new_page = PageNode(url)
        prev = self.current_page
        new_page.prev = prev
        prev.next = new_page
        self.current_page = new_page

    def back(self, steps: int) -> str:
        cur = self.current_page
        while cur.prev and steps:
            cur = cur.prev
            steps -= 1
        self.current_page = cur
        return cur.val

    def forward(self, steps: int) -> str:
        cur = self.current_page
        print("fwd", cur.val)
        while cur.next and steps:
            cur = cur.next
            steps -= 1
        self.current_page = cur
        return cur.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)