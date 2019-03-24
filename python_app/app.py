import os

from pyspark import SparkContext


text = """
I met a boy wearing Vans, 501s
And a dope Beastie tee, nipple rings, new tattoos
That claimed that he was OGT, back from '92, from the first EP
And in between sips of Coke
He told me that he thought we were selling out
Laying down, sucking up to the man

Well now I've got some advice for you, little buddy
Before you point the finger you should know that I'm the man
And if I'm the man, then you're the man, and he's the man as well
So you can point that fucking finger up your ass

All you know about me is what I've sold you, dumb fuck
I sold out long before you ever heard my name
I sold my soul to make a record, dipshit, and then you bought one

So I've got some advice for you, little buddy
Before you point your finger, you should know that I'm the man
If I'm the fucking man then you're the fucking man as well
So you can point that fucking finger up your ass

All you know about me is what I've sold you, dumb fuck
I sold out long before you ever heard my name
I sold my soul to make a record, dipshit, and then you bought one

All you read and wear or see and hear on TV Is a product Begging for your fatass dirty dollar
Shut up and buy, buy, buy my new record
And buy, buy, buy
Send more money
Fuck you, buddy
Fuck you, buddy
Fuck you, buddy
Fuck you, buddy
"""


if __name__ == "__main__":
    context = SparkContext("local", "first app")

    path = os.path.join(os.getcwd(), "dataset.txt")

    with open(path, 'w') as f:
        f.write(text)

    # read in text file and split each document into words
    words = context.textFile(path).flatMap(lambda line: line.split(" "))

    # count the occurrence of each word
    word_count = words.map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)
    word_count.saveAsTextFile("/home/results")
