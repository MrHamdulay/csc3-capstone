def Counter():
    count = 0
    def counterer():
        counterer.count += 1
        return counterer.count
    counterer.count = 0
    return counterer
