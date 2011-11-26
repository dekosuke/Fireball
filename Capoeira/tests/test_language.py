#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys

if not '../' in sys.path:
  sys.path.insert(0, '../')

import unittest

from Bucket.language import Languages

class TestLanguage(unittest.TestCase):
  def setUp(self):
    pass

  def tearDown(self):
    Languages.language = []

  def testSet(self):
    l = Languages()
    l += {'name': 'python',
          'url': 'http://python.org'}

  def testGet(self):
    l = Languages()
    l += {'name': 'python',
          'url': 'http://python.org'}

    self.assertEquals(l.python, (1, 'python', 'http://python.org'))

  def testGetItem(self):
    l = Languages()

    languages = [
      {'name': 'python',
       'url': 'http://python.org'},
      {'name': 'node.js',
       'url': 'http://nodejs.org'},
      {'name': 'scala',
       'url': 'http://scala-lang.org'}
    ]
    for e in languages:
      l += e

    t = Languages.Language(**languages[0])
    v = l[0]

    self.assertEquals(v.name, t.name)
    self.assertEquals(v.url, t.url)

  def testLength(self):
    l = Languages()

    languages = [
      {'name': 'python',
       'url': 'http://python.org'},
      {'name': 'node.js',
       'url': 'http://nodejs.org'},
      {'name': 'scala',
       'url': 'http://scala-lang.org'}
    ]

    for e in languages:
      l += e

    self.assertEqual(len(l), 3)

  def testOverlap(self):
    l = Languages()

    languages = [
      {'name': 'python',
       'url': 'http://python.org'},
      {'name': 'node.js',
       'url': 'http://nodejs.org'},
      {'name': 'scala',
       'url': 'http://scala-lang.org'}
    ]

    for e in languages:
      l += e

    with self.assertRaises(Languages.OverlapError):
      l += languages[0]


if __name__ == '__main__':
  unittest.main()
