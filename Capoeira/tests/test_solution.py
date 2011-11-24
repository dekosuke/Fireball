#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys

if not '../' in sys.path:
  sys.path.insert(0, '../')

import unittest

from Mocaco.solution import Solutions

class TestSolution(unittest.TestCase):
  def setUp(self):
    pass

  def tearDown(self):
    pass

  def testSet(self):
    s = Solutions()
    s += {'problem_id': 1,
          'input': '1 2 3',
          'output': '2 4 6'}

  def testGet(self):
    solutions = [
        {'problem_id': 1,
         'input': '1 2 3',
         'output': '2 4 6'
        },
        {'problem_id': 2,
         'input': '3 5 7 9 20 25',
         'output': '5 25'
        }
      ]
    s = Solutions()
    for e in solutions:
      s += e

    self.assertEquals(s._1, 
      (solutions[0]['problem_id'], 
       solutions[0]['input'],
       solutions[0]['output']))

    self.assertEquals(s._2,
      (solutions[1]['problem_id'],
       solutions[1]['input'],
       solutions[1]['output']))

  def testGetItem(self):
    solutions = [
        {'problem_id': 1,
         'input': '1 2 3',
         'output': '2 4 6'
        },
        {'problem_id': 2,
         'input': '3 5 7 9 20 25',
         'output': '5 25'
        }
      ]
    s = Solutions()

    for e in solutions:
      s += e

    v = s[0]
    t = Solutions.Solution(**solutions[0])

    self.assertEquals(v.problem_id, t.problem_id)
    self.assertEquals(v.input, t.input)
    self.assertEquals(v.output, t.output)

  def testOverlap(self):
    solutions = [
        {'problem_id': 1,
         'input': '1 2 3',
         'output': '2 4 6'
        },
        {'problem_id': 2,
         'input': '3 5 7 9 20 25',
         'output': '5 25'
        },
        {'problem_id': 3,
         'input': 'a,b,c,d,e,f,g,h',
         'output': 'h,g,f,e,d,c,b,a'
        }
      ]

    s = Solutions()
   
    for e in solutions:
      s += e

    with self.assertRaises(Solutions.OverlapError):
      s += solutions[0]

if __name__ == '__main__':
  unittest.main()
