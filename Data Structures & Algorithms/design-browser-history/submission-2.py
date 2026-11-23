class PageNode:
    def __init__(self, url=None, last=None, next=None):
        self.url = url
        self.last = last
        self.next = next

class BrowserHistory:

    def __init__(self, homepage: str):
        self.current = PageNode(url=homepage)

    def visit(self, url: str) -> None:
        tmp = self.current
        self.current = PageNode(url=url, last=self.current)
        tmp.next = self.current

    def back(self, steps: int) -> str:
        while self.current.last and steps:
            self.current = self.current.last
            steps -= 1
        return self.current.url

    def forward(self, steps: int) -> str:
        while self.current.next and steps:
            self.current = self.current.next
            steps -= 1
        return self.current.url


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)