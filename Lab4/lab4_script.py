class Shakespear:

    def __init__(self, textfile):
        self.textfile = textfile

    def parse(self):
        """Parse the file with UTF-8 BOM encoding"""
        with open('shakespeare.txt', 'r', encoding='utf_8_sig') as file:
            l1 = []
            ctr = 0
            for row in file:
                cleaned = row.strip('\n')
                ctr += 1
                if ctr > 10:
                    break
                l1.append(cleaned)
            print(l1)

shake = Shakespear('shakespeare.txt').parse()
print(shake)