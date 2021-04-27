def annie():
    yield "Anything you can do, I can do better. \n" \
        "  I can do anything better than you."

    yield "yes, I can!"
    yield "yes, I can!"
    yield "yes, I can! Yes, I can!"


def frank():
    yield "No You can't"
    yield "No You can't"
    yield "No You can't"


queue = [annie(), frank()]
print(queue)
while queue:
    singer = queue.pop(0)
    try:
        # print(next(singer))
        print(singer.send(None))
        queue.append(singer)
    except StopIteration:
        pass

# def fibon(n):
#     a = b = 1
#     for i in range(n):
#         yield a
#         a, b = b, a + b


# for i in fibon(5):
#     print(i)
