import BMICalculator as bmi
import unittest
#BMICategoryCount('Data.json','Overweight')
# Testcase 1

class TestStringMethods(unittest.TestCase):
      
    def test_case_a(self):
        
        self.assertEqual(bmi.BMI().calculateBMI('Data/DataEmpty.json'), 'File is empty')

    def test_case_b(self):
        self.assertEqual(bmi.BMI().BMICategoryCount('Data/DataEmpty.json','Overweight'), 'File is empty')

    def test_case_c(self):
        self.assertEqual(bmi.BMI().BMICategoryCount('Data/Data.json','Overweight'), 0)

    def test_case_d(self):
        self.assertEqual(bmi.BMI().BMICategoryCount('Data/Data.json','Overweight1'), 0)

    def test_case_e(self):
        self.assertFalse(bmi.BMI().BMICategoryCount('Data/Data.json','Overweight'), 5)

    def test_case_f(self):
        self.assertTrue(bmi.BMI().calculateBMI('Data/Data.json'))

    def test_case_g(self):
        self.assertEqual(bmi.BMI().calculateBMI('Data/Data1.json'),'File not exits')

if __name__ == '__main__':
    unittest.main()