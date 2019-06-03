import os

from pyspark import SparkContext


text = """
Lorem ipsum dolor sit amet, 
consectetur adipiscing elit. 
Aenean sit amet maximus neque, 
vitae semper erat. Sed quis mi bibendum, 
ultricies sem et, congue ligula. 
Curabitur malesuada dolor quis nulla volutpat tincidunt. 
Pellentesque et iaculis odio. 
Vestibulum nec dolor et leo maximus blandit. 
Mauris ultrices semper felis, 
id ullamcorper mauris porttitor eget. 
Etiam tristique orci nec dolor semper aliquet. 
Nunc aliquam vestibulum turpis, 
quis pharetra dui fermentum quis. 
In nulla lectus, ornare sed ante in, 
consequat rhoncus nisl. 
Sed blandit erat eget felis cursus sollicitudin at at odio. 
Orci varius natoque penatibus et magnis dis parturient montes, 
nascetur ridiculus mus. Morbi leo neque, vestibulum a pharetra non, 
fermentum eget elit. Donec sollicitudin justo augue, 
vitae tincidunt enim viverra vitae. Nulla a libero venenatis, 
consectetur nunc a, rhoncus quam.

Nulla orci est, imperdiet eget congue in, 
feugiat vitae quam. Duis sollicitudin tortor ac nulla porta dignissim. 
In ac scelerisque sem. Nunc gravida ipsum nisi, 
a ornare sapien aliquam eget. Cras gravida leo libero,
ac aliquam ex pharetra nec. 
Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; 
Vivamus ut velit eget nisl maximus finibus sit amet at urna. 
Aliquam erat volutpat. Pellentesque lorem magna, tempus vitae iaculis. 
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
