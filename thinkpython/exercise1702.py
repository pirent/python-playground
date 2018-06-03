class Kangaroo:
    """Represents a kangaroo
    """

    def __init__(self, name, contents=None):
        """Initialize the pouch contents
        
        name: string
        contents: initial pouch contents
        """
        self.name = name
        self.pouch_contents = [] if contents == None else contents

    def put_in_pouch(self, item):
        """Adds a new item to pouch contents

        item: object to be added
        """
        self.pouch_contents.append(item)

    def __str__(self):
        """Returns a string representation of this Kangaroo
        """
        t = [self.name + " has pouch: "]
        for o in self.pouch_contents:
            s = " " + object.__str__(o)
            t.append(s)
        return '\n'.join(t)

if __name__ == "__main__":
    kanga = Kangaroo("Kanga")
    roo = Kangaroo("Roo")
    kanga.put_in_pouch('wallet')
    kanga.put_in_pouch('car keys')
    kanga.put_in_pouch(roo)

    print(kanga)
    print(roo)
