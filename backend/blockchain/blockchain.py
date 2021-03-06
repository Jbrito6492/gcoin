from backend.blockchain.block import Block


class BlockChain:
    """
    BlockChain: public ledger of transactions
    Implemented as a list of blocks - data sets of transactions
    """

    def __init__(self):
        self.chain = [Block.genesis()]

    def __repr__(self):
        return str(self.chain)

    def add_block(self, data):
        self.chain.append(Block.mine_block(self.chain[-1], data))


def main():
    print(f'blockchain.py __name__: {__name__}')


if __name__ == '__main__':
    main()
