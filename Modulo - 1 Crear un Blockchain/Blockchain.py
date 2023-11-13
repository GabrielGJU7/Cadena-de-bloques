
"""
@Creado el: 13/11/2023

@Autor: Gabriel Jacobo Ulloa

"""


import datetime
import hashlib
import json
from flask import Flask, jsonify

class Blockchain:
    
    def __init__(self):
        self.chain = []
        self.createBlock(proof = 1, previous_hash = '0')
        
    def createBlock(self, proof, previous_hash):
        block = {'index' : len(self.chain) + 1,
                 'timestamp' : str(datetime.datetime.now()),
                 'proof' : proof,
                 'previous_hash' : previous_hash }
        self.chain.append(block)
        return block
    
    def get_previous_block(self):
        return self.chan[-1]
        