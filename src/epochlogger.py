from gensim.models.callbacks import CallbackAny2Vec

class EpochLogger(CallbackAny2Vec):
    '''Callback to log information about training'''
    def __init__(self):
        self.epoch = 0
        self.batch = 0
    def on_epoch_begin(self, model):
        print("Epoch #{} start".format(self.epoch))

    def on_epoch_end(self, model):
        print("Epoch #{} end".format(self.epoch))
        self.epoch += 1
        
    # def on_batch_begin(self,model):
        # print("Batch#{} start".format(self.batch))
        
    # def on_batch_end(self,model):
        # print("Batch#{} start".format(self.batch))
        # self.batch +=1