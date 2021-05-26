"""
    Simple TF is module for simple machine learning algorithm, this module makes for Bangkit Academy 2021 led by Google,
    Gojek, Tokopedia, and Traveloka.

    Simple TF
    version : 0.0.1
    created by : Brillante's Team
    team id : B21-CAP0176
"""

import tensorflow as tf

tf.compat.v1.disable_eager_execution()


class TFNearestNeighbor():
    def __init__(self, k=1):
        self.init = tf.compat.v1.global_variables_initializer()

        # K Value
        self.k = k

        # Data
        self.train = None
        self.query = None

        # Graph Input
        self.xtr = None
        self.xqe = None

        # Output
        self.values = None
        self.indices = None

        self.result = self.values, self.indices

    def fit(self, train, query):
        self.train = train
        self.query = query

        self.xtr = tf.compat.v1.placeholder(
            'float', [None, len(self.train[0])])
        self.xqe = tf.compat.v1.placeholder(
            'float', [None, len(self.query[0])])

    def transform(self):
        # Manhattan distance
        distance = tf.reduce_sum(
            tf.abs(tf.subtract(self.xtr, tf.expand_dims(self.xqe, axis=1))), axis=2)

        # Nearest Data
        values, indices = tf.nn.top_k(tf.negative(distance), k=self.k)
        values = tf.negative(values)

        with tf.compat.v1.Session() as sess:
            sess.run(self.init)

            self.values, self.indices = sess.run([values, indices], feed_dict={
                                                 self.xtr: self.train, self.xqe: self.query})

            self.values = self.values.reshape(-1)
            self.indices = self.indices.reshape(-1)

    def fit_transform(self, train, query):
        self.fit(train, query)
        self.transform()
