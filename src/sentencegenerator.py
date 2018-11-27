class SentenceGenerator(object):
    def __init__(self, fname):
        self.fname = fname
 
    def __iter__(self):
            for line in open(self.fname,encoding='utf-8'):
                yield line.split()