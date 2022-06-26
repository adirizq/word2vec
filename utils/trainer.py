from numpy import outer
import torch
import torch.nn as nn

import pytorch_lightning as pl

from models.w2v import CBOW

class W2VTrainer(pl.LightningModule):

    def __init__(self,
                 vocab_size,
                 embed_dim,
                 embed_max_norm) -> None:
        
        super().__init__()

        self.cbow_model = CBOW(vocab_size,
                               embed_dim,
                               embed_max_norm)
        
        print(self.cbow_model)


    # def configure_optimizers(self):

    
    def training_step(self, train_batch, batch_idx):
        x = train_batch
        output = self.cbow_model(x)
        print(output)

    
    # def validation_step(self, valid_batch, batch_idx):